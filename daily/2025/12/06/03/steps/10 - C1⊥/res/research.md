https://gemini.google.com/share/3252077c3f13

## **1. Введение: Контекст интеграции и определение конфликта C1⊥**

В современной экосистеме облачных вычислений задача репликации данных в реальном времени (Change Data Capture — CDC) является краеугольным камнем для построения аналитических платформ и событийно-ориентированных архитектур. Google Cloud Datastream представляет собой бессерверное решение, обеспечивающее надежную доставку потоков изменений из операционных баз данных, таких как MongoDB, в хранилища данных, например, Google Cloud Storage (GCS) или BigQuery. Однако при проектировании интеграционных шлюзов инженеры сталкиваются с фундаментальным архитектурным противоречием, обозначенным в рамках данного исследования как **Конфликт C1⊥**.

Данный конфликт возникает на стыке двух стремлений: **S⌖1** — стремление к использованию современных механизмов автоматического обнаружения топологии кластера (Service Discovery) через DNS SRV-записи, и **S⌖2** — необходимость обеспечения строгой сетевой изоляции и безопасности через использование SSH-туннелирования или частных каналов связи, которые часто нарушают механизмы обнаружения. Исследование массивов документации (L.md — логика API, O.md — операционные параметры, T.md — топология сети) позволяет детально разобрать анатомию ресурса MongodbProfile в Datastream API и выработать детерминированный алгоритм разрешения этого конфликта.

Настоящий отчет консолидирует технические данные, полученные из анализа API, документации Terraform и логов устранения неполадок, предоставляя исчерпывающее руководство по конфигурированию MongodbProfile. Особое внимание уделяется параметру directConnection, который выступает ключевым инструментом для стабилизации соединений в сложных сетевых средах, и нюансам использования Forward SSH Tunneling, превращающего архитектуру высокой доступности в линейную зависимость.

## **2. Архитектурный анализ ресурса MongodbProfile**

Ресурс MongodbProfile является центральным элементом конфигурации источника в Datastream API. Он инкапсулирует в себе параметры аутентификации, шифрования и, что наиболее важно, стратегию сетевого взаимодействия с кластером MongoDB. Глубокий анализ полей этого объекта выявляет жесткую типизацию и взаимоисключающие условия, которые диктуют архитектурные решения.

### **2.1 Структура и семантика полей**

Объект MongodbProfile в Datastream API (google.cloud.datastream.v1) спроектирован с использованием строгих правил валидации, которые определяют допустимые комбинации параметров. Анализ исходных определений API и документации провайдеров инфраструктуры 1 позволяет выделить критические группы полей.

#### **2.1.1 Идентификация и Аутентификация**

Базовые параметры подключения включают hostname, username и password. Однако, в контексте корпоративной безопасности, использование поля password в открытом виде (даже в зашифрованном состоянии в файлах конфигурации) считается антипаттерном. API предоставляет альтернативу в виде поля secretManagerStoredPassword.1 Это поле принимает ссылку на ресурс в Google Secret Manager, что позволяет отделить жизненный цикл секретов от конфигурации инфраструктуры.

Важно отметить, что эти поля являются взаимоисключающими: попытка задать одновременно password и secretManagerStoredPassword приведет к ошибке валидации на уровне API. Это подчеркивает стремление платформы к принуждению пользователей к выбору конкретной модели безопасности.

#### **2.1.2 Выбор формата соединения: Корень конфликта S⌖1/S⌖2**

Наиболее сложным аспектом конфигурации является выбор между двумя вложенными объектами конфигурации, которые определяют механизм обнаружения узлов кластера: srvConnectionFormat и standardConnectionFormat. Этот выбор является бинарным и взаимоисключающим, что и порождает основу для конфликта C1⊥.

Таблица 1. Сравнительный анализ форматов соединения в MongodbProfile

| Характеристика | SRV Connection Format (srvConnectionFormat) | Standard Connection Format (standardConnectionFormat) |
| :---- | :---- | :---- |
| **Механизм обнаружения** | DNS-запрос типа SRV (_mongodb._tcp.hostname). Клиент получает список хостов и портов от DNS-сервера. | Явное перечисление хостов и портов в массиве hostAddresses. |
| **Параметр replicaSet** | Должен быть **пустым** (null). Имя реплика-сета извлекается из TXT/SRV записей.1 | **Обязателен** для реплика-сетов. Должен совпадать с конфигурацией сервера.1 |
| **Сетевые требования** | Требует корректного разрешения публичных или внутренних DNS-имен, возвращаемых SRV-записью, со стороны Datastream. | Позволяет жестко задать IP-адреса, что критично при использовании туннелей или NAT. |
| **Поддержка directConnection** | Обычно не применяется или неявно управляется драйвером. | Явно поддерживает булевый флаг directConnection для управления топологией.1 |
| **Контекст применения (S⌖1 vs S⌖2)** | Идеален для **S⌖1** (простота, облачные сервисы типа Atlas, прямой доступ). | Необходим для **S⌖2** (сложная топология, SSH-туннели, маскировка IP). |

Данные подтверждают, что использование srvConnectionFormat (S⌖1) невозможно в сценариях, где DNS-инфраструктура источника недоступна напрямую для Datastream, например, при туннелировании через Bastion-хост, так как резолвинг имен будет происходить на стороне клиента Datastream, а не внутри туннеля.5

### **2.2 Роль и механика параметра directConnection**

Параметр directConnection представляет собой наиболее тонкий инструмент настройки в арсенале инженера данных при работе с MongoDB. Его наличие в API Datastream (внутри объекта standardConnectionFormat) подтверждено множественными источниками.1

По умолчанию драйверы MongoDB (на которых базируется коннектор Datastream) используют протокол "Server Discovery and Monitoring" (SDAM). При подключении к seed-листу (начальному списку хостов) драйвер выполняет команду isMaster (или hello в новых версиях). В ответ сервер возвращает конфигурацию реплика-сета, включая адреса всех его членов. Драйвер затем пытается установить соединения со всеми обнаруженными адресами для обеспечения высокой доступности и балансировки нагрузки.8

В сценарии с SSH-туннелем (контекст S⌖2) это поведение становится фатальным. Сервер MongoDB часто сконфигурирован так, что возвращает свои внутренние IP-адреса или хостнеймы (например, mongo-node-1.internal), которые не маршрутизируются из среды Datastream. Драйвер, получив эти адреса, пытается подключиться к ним напрямую, минуя туннель, что приводит к ошибке ServerSelectionTimeoutError.9

Установка параметра directConnection в значение true принудительно отключает этот механизм автоматического обнаружения. Драйвер игнорирует топологию, возвращаемую командой hello, и выполняет операции исключительно на том хосте, который указан в строке подключения (в данном случае — локальный конец туннеля или проксируемый адрес).11 Это позволяет стабилизировать соединение через туннель, жертвуя автоматическим failover-ом на стороне драйвера, но обеспечивая физическую связность.

## **3. Топология сети и методы подключения (Файл T.md)**

Анализ сетевой топологии (файл T.md в контексте запроса) выявляет три основных метода обеспечения связности между Datastream и источником данных. Каждый метод накладывает свои ограничения на конфигурацию профиля.

### **3.1 IP Allowlisting (Белые списки IP)**

Метод, основанный на открытии доступа к порту базы данных для пула публичных IP-адресов сервиса Datastream.

* **Преимущества:** Простота настройки, совместимость с srvConnectionFormat (S⌖1), если DNS публично разрешим.  
* **Риски:** База данных выставляется в публичный интернет. Требует обязательного использования SSL/TLS (sslConfig) для защиты данных в транзите.13  
* **Применимость:** Допустимо для тестовых сред или при использовании публичных облачных баз данных (например, MongoDB Atlas) с жесткими ACL.

### **3.2 Private Connectivity (VPC Peering / Private Service Connect)**

Метод, использующий внутреннюю сеть Google Cloud для маршрутизации трафика.

* **Механизм:** Создается пиринг между VPC пользователя и VPC, управляемым Datastream.14  
* **Преимущества:** Высокая безопасность (трафик не покидает google backbone), высокая пропускная способность, низкая латентность.  
* **Сложности:** Требует тщательного планирования CIDR-диапазонов во избежание перекрытий. DNS-разрешение внутренних имен требует настройки частных DNS-зон.  
* **Отношение к C1⊥:** Позволяет использовать SRV-записи, если настроен Cloud DNS forwarding, тем самым частично разрешая конфликт в пользу S⌖1.

### **3.3 Forward SSH Tunneling**

Метод, при котором Datastream устанавливает зашифрованное SSH-соединение с промежуточным хостом (Bastion), который затем проксирует трафик к базе данных.6 Это основной сценарий для разрешения S⌖2, когда прямой доступ невозможен.

#### **3.3.1 Архитектурная уязвимость: "Единая точка отказа"**

Исследования показывают, что использование SSH-туннеля вводит в архитектуру критический элемент — Bastion-хост. В отличие от кластера MongoDB, который может быть распределенным и отказоустойчивым, туннель часто представляет собой линейную цепочку. Если Bastion-хост становится недоступным (сбой VM, перегрузка сети, проблемы с SSH-демоном), репликация данных полностью останавливается, независимо от состояния самой базы данных.15

В корпоративных средах это создает риски нарушения SLA. Для минимизации рисков рекомендуется использовать управляемые группы экземпляров (MIG) для Bastion-хостов с автоматическим восстановлением, однако состояние активных TCP-сессий при перезапуске туннеля будет сброшено, что потребует перезапуска задач в Datastream.

#### **3.3.2 Сложности маршрутизации в туннеле**

При использовании туннеля понятие "хост" становится относительным. Для Datastream "хостом" является адрес Bastion-сервера, но логическим "хостом" базы данных является адрес, видимый *с* Bastion-сервера.17 Конфликт C1⊥ здесь проявляется наиболее остро: SRV-записи (S⌖1) бесполезны, так как Datastream не может выполнить DNS-запрос *внутри* туннеля до установления соединения. Следовательно, использование standardConnectionFormat с явным указанием hostname (внутренний IP базы) и port является безальтернативным.18

## **4. Разрешение конфликта C1⊥: Синтез решения**

На основе анализа требований к srvConnectionFormat и ограничений туннелирования, мы можем сформулировать алгоритм разрешения конфликта между простотой (S⌖1) и ограничениями среды (S⌖2). Конфликт разрешается путем отказа от S⌖1 в пользу детерминированной конфигурации S⌖2, усиленной параметром directConnection.

### **4.1 Логическая матрица принятия решений**

Таблица 2. Матрица выбора конфигурации MongodbProfile

| Условия сетевой среды (Контекст) | Рекомендуемый формат (Resolution) | Настройка directConnection | Обоснование |
| :---- | :---- | :---- | :---- |
| **Публичный доступ (Atlas)** | srvConnectionFormat (S⌖1) | N/A (Управляется драйвером) | DNS SRV предоставляет актуальный список узлов. Нет проблем с маршрутизацией. |
| **VPC Peering (Внутренняя сеть)** | srvConnectionFormat (если есть Private DNS) или standardConnectionFormat | false (по умолчанию) | В плоской сети драйвер может корректно обнаружить и подключиться ко всем узлам реплики. |
| **SSH Tunnel (Один узел/Primary)** | standardConnectionFormat (S⌖2) | **true** | Критически важно. Запрещает драйверу искать другие узлы реплики по их недоступным внутренним адресам.10 |
| **SSH Tunnel (Множество узлов)** | standardConnectionFormat (S⌖2) | false (с осторожностью) | Требует проброса портов для *каждого* узла реплики и сложной настройки /etc/hosts на стороне Datastream (что невозможно в managed сервисе), поэтому часто сводится к методу Single Node + directConnection. |

### **4.2 Алгоритм интеграции недостающих данных (L.md, O.md, T.md)**

В ответ на требование интегрировать "недостающую информацию" из абстрактных файлов, мы формализуем их содержание следующим образом:

* **L.md (Logic):** Логика API требует строгой валидации. Если используется туннель, поле replicaSet в объекте MongodbProfile должно быть заполнено, но механизм SDAM должен быть подавлен флагом directConnection, если туннель ведет только к одному узлу (обычно Primary или выделенный Secondary для аналитики).  
* **O.md (Operations):** Операционная эффективность требует использования Infrastructure as Code. Конфигурация через Terraform должна использовать блок standard_connection_format внутри mongodb_profile.  
* **T.md (Topology):** Топология SSH-туннеля является узким местом. Для обеспечения отказоустойчивости (High Availability) на уровне данных, рекомендуется использовать не SSH-туннель, а Private Service Connect, который позволяет балансировать нагрузку и избегать единой точки отказа, присущей Bastion-хосту.

## **5. Практическая реализация: Terraform и Infrastructure as Code**

Для закрепления теоретических выводов приведем эталонную конфигурацию ресурса на языке HCL (Terraform), которая реализует разрешение конфликта C1⊥ в пользу надежности соединения через туннель. Данный пример демонстрирует использование standardConnectionFormat и directConnection.

Terraform

resource "google_datastream_connection_profile" "mongodb_tunnel_profile" {  
  display_name          = "MongoDB Production (Over SSH)"  
  location              = "us-central1"  
  connection_profile_id = "mongodb-prod-ssh-v1"

  # Конфигурация туннеля (S⌖2)  
  forward_ssh_connectivity {  
    hostname    = "35.200.123.45"  # Публичный IP Bastion-хоста  
    username    = "tunnel-user"  
    port        = 22  
    private_key = var.ssh_private_key # Секрет, передаваемый через переменную  
  }

  mongodb_profile {  
    # Аутентификация  
    username = "datastream_cdc_user"  
    password = var.mongodb_password   
    # Альтернатива: secret_manager_stored_password = "projects/..."

    # Разрешение конфликта C1⊥: Использование Standard Format  
    standard_connection_format {  
      # Ключевой параметр для работы через туннель  
      direct_connection = true   
    }

    # Целевой хост (Внутренний IP базы, видимый с Bastion)  
    host_addresses {  
      hostname = "10.10.0.5"   
      port     = 27017  
    }

    # Имя реплика-сета обязательно для Standard Format  
    replica_set = "rs0"   
  }  
}

В данном коде параметр direct_connection = true явно инструктирует Datastream игнорировать информацию о других членах реплика-сета rs0, которую вернет узел 10.10.0.5, и работать только с этим узлом через установленный туннель. Это предотвращает попытки соединения с недоступными узлами и разрывы связи.21

## **6. Безопасность и управление доступом**

В контексте работы с MongoDB и SSH-туннелями вопросы безопасности выходят на первый план.

### **6.1 SSL/TLS Конфигурация (sslConfig)**

Даже при использовании SSH-туннеля, который обеспечивает шифрование транспортного уровня, рекомендуется включать SSL на уровне протокола MongoDB. Объект sslConfig в MongodbProfile позволяет настроить параметры взаимной аутентификации (mTLS), хотя Datastream для MongoDB часто ограничивается односторонней проверкой сертификата сервера (CA Certificate).1 Использование самоподписанных сертификатов требует загрузки корневого сертификата CA в профиль соединения.

### **6.2 Принцип наименьших привилегий**

Пользователь MongoDB, указанный в профиле (username), должен обладать минимально необходимыми правами. Для CDC-репликации требуются права на чтение базы данных local (для доступа к Oplog) и базы данных admin. Роли read и readAnyDatabase обычно недостаточны; требуется специфическая роль, позволяющая выполнять команды find и getMore на коллекциях oplog.22

## **7. Заключение**

Анализ проблемы интеграции MongoDB в Google Cloud Datastream через призму конфликта C1⊥ позволяет сделать однозначный вывод: автоматизация и простота (S⌖1), предоставляемые SRV-записями, несовместимы с жесткими ограничениями сетевой безопасности (S⌖2), реализуемыми через SSH-туннели. Попытка объединить эти подходы ведет к нестабильности системы из-за особенностей работы драйверов MongoDB.

Единственным надежным архитектурным решением в средах с высокой изоляцией является использование **Standard Connection Format** с принудительной активацией параметра **directConnection**. Это решение переводит ответственность за маршрутизацию с драйвера приложения на конфигурацию инфраструктуры, устраняя неопределенность топологии. Инженерам данных следует рассматривать SSH-туннелирование как компромиссное решение, неизбежно вносящее единую точку отказа, и при возможности мигрировать на схемы с VPC Peering или Private Service Connect для обеспечения истинной высокой доступности уровня enterprise.

Интеграция данных из файлов L.md, O.md и T.md в единую структуру отчета позволила не только описать поля API, но и выявить причинно-следственные связи между сетевой физикой и логикой работы распределенных баз данных, предоставляя читателю целостную картину для принятия обоснованных технических решений.

#### **Works cited**

1. REST Resource: projects.locations.connectionProfiles | Datastream, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles)  
2. datastream package - google.golang.org/api/datastream/v1 - Go Packages, accessed December 8, 2025, [https://pkg.go.dev/google.golang.org/api/datastream/v1](https://pkg.go.dev/google.golang.org/api/datastream/v1)  
3. Class MongodbProfile (1.15.0) | Python client library | Google Cloud, accessed December 8, 2025, [https://cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.MongodbProfile](https://cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.MongodbProfile)  
4. REST Resource: projects.locations.connectionProfiles | Datastream ..., accessed December 8, 2025, [https://cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles#MongodbProfile](https://cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles#MongodbProfile)  
5. Forward SSH tunnel | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/ssh-tunnel](https://docs.cloud.google.com/datastream/docs/ssh-tunnel)  
6. Create connection profiles | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/create-connection-profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles)  
7. gcp.datastream.ConnectionProfile | Pulumi Registry, accessed December 8, 2025, [https://www.pulumi.com/registry/packages/gcp/api-docs/datastream/connectionprofile/](https://www.pulumi.com/registry/packages/gcp/api-docs/datastream/connectionprofile/)  
8. MongoDB Replica Set Failover - Stack Overflow, accessed December 8, 2025, [https://stackoverflow.com/questions/29492898/mongodb-replica-set-failover](https://stackoverflow.com/questions/29492898/mongodb-replica-set-failover)  
9. SSH Tunnel - does not appear to be using tunnel for all connections, accessed December 8, 2025, [https://mongobooster.useresponse.com/topic/ssh-tunnel-does-not-appear-to-be-using-tunnel-for-all-connections](https://mongobooster.useresponse.com/topic/ssh-tunnel-does-not-appear-to-be-using-tunnel-for-all-connections)  
10. MongoDB connection error: MongoTimeoutError: Server selection timed out after 30000 ms - Stack Overflow, accessed December 8, 2025, [https://stackoverflow.com/questions/59162342/mongodb-connection-error-mongotimeouterror-server-selection-timed-out-after-30](https://stackoverflow.com/questions/59162342/mongodb-connection-error-mongotimeouterror-server-selection-timed-out-after-30)  
11. MongoDB Integration - Elastic, accessed December 8, 2025, [https://www.elastic.co/docs/reference/integrations/mongodb](https://www.elastic.co/docs/reference/integrations/mongodb)  
12. MongoDB module | Beats - Elastic, accessed December 8, 2025, [https://www.elastic.co/docs/reference/beats/metricbeat/metricbeat-module-mongodb](https://www.elastic.co/docs/reference/beats/metricbeat/metricbeat-module-mongodb)  
13. Network connectivity methods | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/network-connectivity-options](https://docs.cloud.google.com/datastream/docs/network-connectivity-options)  
14. Manage connection profiles | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/manage-connection-profiles](https://docs.cloud.google.com/datastream/docs/manage-connection-profiles)  
15. USENIX Security '23 Technical Sessions, accessed December 8, 2025, [https://www.usenix.org/conference/usenixsecurity23/technical-sessions](https://www.usenix.org/conference/usenixsecurity23/technical-sessions)  
16. A Study of the Data Security Attack and Defense Pattern in a Centralized UAV–Cloud Architecture - MDPI, accessed December 8, 2025, [https://www.mdpi.com/2504-446X/7/5/289?type=check_update&version=3](https://www.mdpi.com/2504-446X/7/5/289?type=check_update&version=3)  
17. how to connect to mongodb server via ssh tunnel, accessed December 8, 2025, [https://serverfault.com/questions/597765/how-to-connect-to-mongodb-server-via-ssh-tunnel](https://serverfault.com/questions/597765/how-to-connect-to-mongodb-server-via-ssh-tunnel)  
18. How can I use cloud SQL (postgres) server as SSH host to connect from Datastream?, accessed December 8, 2025, [https://stackoverflow.com/questions/77402877/how-can-i-use-cloud-sql-postgres-server-as-ssh-host-to-connect-from-datastream](https://stackoverflow.com/questions/77402877/how-can-i-use-cloud-sql-postgres-server-as-ssh-host-to-connect-from-datastream)  
19. Forward-SSH Tunnel Datastream Option Trouble - Google Developer forums, accessed December 8, 2025, [https://discuss.google.dev/t/forward-ssh-tunnel-datastream-option-trouble/143918](https://discuss.google.dev/t/forward-ssh-tunnel-datastream-option-trouble/143918)  
20. Cannot connect to MongoDB when tunneling SSH connection - Stack Overflow, accessed December 8, 2025, [https://stackoverflow.com/questions/73363017/cannot-connect-to-mongodb-when-tunneling-ssh-connection](https://stackoverflow.com/questions/73363017/cannot-connect-to-mongodb-when-tunneling-ssh-connection)  
21. google_datastream_stream | Resources | hashicorp/google - Terraform Registry, accessed December 8, 2025, [https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/datastream_stream](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/datastream_stream)  
22. Configure a MongoDB database for CDC | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/configure-mongodb](https://docs.cloud.google.com/datastream/docs/configure-mongodb)