https://gemini.google.com/share/deae4f0355ee

## **1. Введение и контекст исследования**

Настоящий отчет представляет собой исчерпывающий технический анализ инцидента, связанного с невозможностью установления приватного сетевого соединения между сервисом Google Cloud Datastream (Change Data Capture — CDC) и кластером MongoDB Atlas, развернутым с использованием технологии Private Service Connect (PSC). Документ подготовлен в ответ на запрос клиента (ꆜ) и направлен на детальную валидацию выявленных проблем, диагностику корневых причин сбоя на уровне архитектуры облачной сети, а также разработку детерминированных стратегий их устранения.

В современной облачной инженерии задача интеграции управляемых сервисов (Managed Services), таких как Datastream, с базами данных, размещенными в сторонних SaaS-средах (MongoDB Atlas), является критически важной для построения конвейеров данных реального времени. Однако, как показывает практика и текущий инцидент P⁎, данная интеграция сопряжена со значительными архитектурными сложностями, возникающими на стыке технологий виртуализации сетей (SDN), управления доменными именами (DNS) и политик безопасности.

Целью данного документа является не только решение локальной задачи T⁎ (установление соединения), но и предоставление глубокого понимания механики взаимодействия компонентов Google Cloud Networking. Анализ базируется на предоставленных данных об инфраструктуре (O.md), логах ошибок и авторитетной технической документации.

### **1.1. Обзор проблематики проекта P⁎**

Проект P⁎ нацелен на реализацию защищенного канала передачи данных между Google Cloud Datastream и MongoDB Atlas. Ключевым требованием является полное исключение прохождения трафика через публичный интернет ("avoid public internet traversal"). Для реализации этой задачи была выбрана архитектура, включающая:

* **VPC Peering** (через Private Services Access) для связи Datastream с пользовательской сетью (datastream-net).  
* **Private Service Connect (PSC)** для связи пользовательской сети с MongoDB Atlas.  
* **Cloud DNS Private Zone** для разрешения имен хостов Atlas во внутренние IP-адреса.

Несмотря на кажущуюся корректность дизайна, система не функционирует. Сервис Datastream демонстрирует симптомы, указывающие на попытки соединения через публичные IP-адреса, игнорируя настроенную частную зону DNS. Клиент диагностировал проблему как "Split-Horizon DNS Failure", однако, как покажет дальнейший анализ, ситуация осложняется фундаментальными ограничениями транзитивной маршрутизации в Google Cloud, которые не были учтены в исходном дизайне.

### **1.2. Методология анализа**

Анализ проводится методом декомпозиции сетевого стека взаимодействия. Мы последовательно рассмотрим:

1. Уровень DNS: Механизмы разрешения имен в управляемых VPC Google и их ограничения при пиринге.  
2. Уровень IP-маршрутизации: Топологию VPC Peering и правила транзитивности трафика к PSC Endpoint.  
3. Уровень Приложения (Application Layer): Специфику протокола MongoDB, механизмы обнаружения топологии (Service Discovery) и требования TLS/SSL.

Каждая выявленная клиентом проблема (P1†, P2†, P3†) будет подвергнута строгой технической валидации на основе официальной спецификации сервисов.

## **2. Детальный аудит инфраструктуры и валидация симптомов**

Прежде чем переходить к архитектурным решениям, необходимо зафиксировать текущее состояние системы и подтвердить корректность наблюдений, сделанных инженерной командой клиента.

### **2.1. Топология сети и компоненты**

Согласно описанию инфраструктуры, мы имеем следующую цепочку взаимодействия компонентов:

| Компонент | Роль | Сетевой сегмент | Примечание |
| :---- | :---- | :---- | :---- |
| **Datastream Service** | Источник данных (CDC) | Google Managed VPC | Управляется Google, скрыт от пользователя. |
| **PSA Connection** | Канал связи | VPC Peering | Соединяет Managed VPC и datastream-net. |
| **VPC datastream-net** | Транзитная сеть | Project: internal-resources-corp | Контролируется пользователем. |
| **PSC Endpoint** | Точка входа | IP в datastream-net | Forwarding Rule, указывающее на Service Attachment Atlas. |
| **Cloud DNS** | Разрешение имен | Zone: mongo-psc-isolated | Привязана к datastream-net. A-записи ведут на IP PSC. |
| **MongoDB Atlas** | Целевая система | Atlas VPC | Доступ через PSC Service Attachment. |

### **2.2. Анализ диагностированных проблем (P†)**

Клиент выделил три ключевых аспекта проблемы. Проведем их экспертную оценку.

#### **Проблема P1†: Соединение с публичными IP**

*Описание:* "The error logs show Datastream attempting to connect to Atlas Public IPs instead of the PSC Private IPs".

Валидация: Абсолютно подтверждено.  
Логи Datastream, фиксирующие попытки соединения с публичными адресами, являются неопровержимым доказательством того, что разрешение DNS-имен происходит некорректно. MongoDB Atlas, даже при настроенном Private Endpoint, сохраняет публичные DNS-записи для своих кластеров (обычно вида *.mongodb.net). Эти записи являются глобально разрешимыми и указывают на публичные IP-адреса шлюзов Atlas.1 Если клиент (в данном случае Datastream) не видит частную зону DNS, он обращается к публичным рекурсивным резолверам Google (8.8.8.8), которые возвращают публичные адреса.  
Поскольку в инфраструктуре клиента, вероятно, отсутствуют маршруты в интернет для Datastream (или настроены строгие правила Egress), либо IP Access List в Atlas закрыт для публичных IP Datastream, соединение завершается ошибкой Connection Refused или Timeout.

#### **Проблема P2†: Игнорирование Private DNS Zone**

*Описание:* "Datastream is ignoring the Private DNS Zone in the peered VPC and falling back to Public DNS".

Валидация: Абсолютно подтверждено (Архитектурное ограничение).  
Это наблюдение является точным описанием поведения сервиса, однако термин "ignoring" (игнорирует) может создать ложное впечатление, что это ошибка конфигурации или баг. В действительности, это задокументированное ограничение архитектуры Google Cloud Datastream при использовании метода подключения "Private Connectivity" (через VPC Peering).  
Документация Google Cloud прямо утверждает: "Datastream doesn't support Domain Name System (DNS) resolution in private connections".2  
Механизм VPC Peering объединяет пространства IP-адресов двух сетей, но не объединяет пространства имен DNS автоматически. Резолверы, работающие внутри управляемой сети Datastream, не имеют доступа к конфигурации Cloud DNS в пользовательском проекте. Они не знают о существовании зоны mongo-psc-isolated, привязанной к datastream-net, и следовательно, выполняют стандартную рекурсию через публичные корни.

#### **Проблема P3†: Ложноположительный результат верификации**

*Описание:* "Datastream Test fails... Configuring a dummy hostname proves it resolves to Public IPs... VM DNS Test succeeds".

Валидация: Критически важно.  
Клиент провел тестирование с использованием "DNS Verifier VM", размещенной внутри сети datastream-net. Успех этого теста (nslookup вернул частный IP, mongosh подключился) создал ложную уверенность в исправности инфраструктуры.  
Ошибка в рассуждениях заключается в экстраполяции прав доступа VM на сервис Datastream.

* **VM** находится *внутри* datastream-net. Она использует metadata server этой сети для DNS (169.254.169.254) и видит все зоны, привязанные к этой сети.  
* Datastream находится снаружи (в пиринговой сети). Он находится в другой зоне безопасности и административного домена.  
  Успех VM доказывает лишь то, что зона настроена корректно, но не то, что она доступна для пиров.

### **2.3. Скрытая проблема: Транзитивность маршрутизации (The Hidden Blocker)**

Помимо проблем с DNS, выявленных клиентом, анализ инфраструктуры указывает на наличие второго, еще более фундаментального блокирующего фактора, который клиент пока не диагностировал явно, но который неизбежно проявится даже при решении проблемы с именами.

Речь идет о транзитивной маршрутизации к эндпоинтам Private Service Connect.  
Согласно топологии:

1. Datastream (Network A) соединен пирингом с datastream-net (Network B).  
2. PSC Endpoint находится в datastream-net (Network B).

Документация Google Cloud по VPC Peering гласит: "The VPC Network Peering connection... doesn't let Datastream connect to: Private Service Connect endpoints located in your VPC network".3  
Это ограничение обусловлено тем, как реализованы правила пересылки (Forwarding Rules) в SDN Google. Трафик, приходящий из пиринговой сети, не может быть направлен в эндпоинт PSC, если не используются специальные конструкции (например, PSC Interface в той же сети или промежуточный прокси).  
Таким образом, даже если мы "заставим" Datastream разрешить имя в частный IP-адрес PSC (например, 10.0.0.5), пакеты от Datastream, адресованные на 10.0.0.5, будут отброшены на границе пиринга или внутри сети datastream-net из-за невозможности маршрутизации к сервисному эндпоинту.

## **3. Глубокий анализ корневых причин (Root Cause Analysis)**

В этом разделе мы подробно разберем физику процессов, приводящих к сбою, опираясь на теорию облачных сетей.

### **3.1. Механика сбоя DNS Resolution (Split-Horizon)**

Концепция Split-Horizon DNS подразумевает, что ответ на DNS-запрос зависит от источника запроса. В данном сценарии мы имеем две "вселенные":

1. **Public Internet Scope:** Здесь cluster.mongodb.net разрешается в публичные IP AWS/GCP/Azure (где хостится Atlas).  
2. **Private VPC Scope (datastream-net):** Здесь настроена Private Zone, перекрывающая публичную, где cluster.mongodb.net разрешается в локальные IP PSC.

Сервис Datastream, будучи развернутым в тенанте Google, использует свои локальные DNS-серверы. При установлении Private Connectivity через PSA (Private Services Access), Google прокладывает маршруты для трафика данных (Data Plane), но **не синхронизирует** Control Plane, отвечающий за разрешение имен.

Существует механизм "DNS Peering" (не путать с VPC Peering), который позволяет одной VPC пересылать DNS-запросы в другую.4 Однако, этот механизм требует настройки на *обеих* сторонах. Пользователь может настроить DNS Peering в своей сети, но он не имеет административного доступа к сети Datastream, чтобы настроить пересылку запросов *оттуда* в свою сеть. Datastream не предоставляет API для настройки DNS Peering со своей стороны.

Именно поэтому Datastream жестко ограничен использованием IP-адресов при приватном подключении, либо требует наличия механизмов, работающих на уровнях L3/L4, которые не зависят от DNS (что невозможно для MongoDB из-за SSL, о чем ниже).

### **3.2. Несовместимость Peering и PSC (The Transitivity Problem)**

В Google Cloud существует жесткое правило: Peering is non-transitive (Пиринг не транзитивен).  
Обычно это означает, что если Сеть А соединена с Сетью Б, а Сеть Б с Сетью В, то А не может говорить с В.  
В случае с PSC ситуация еще специфичнее. PSC Endpoint — это не просто виртуальная машина с сетевым интерфейсом. Это абстракция Software Defined Network, представляющая собой правило переадресации (Forwarding Rule), которое инкапсулирует трафик и отправляет его через Google Backbone к производителю сервиса (MongoDB Atlas).  
Когда пакет приходит из пиринговой сети (Datastream VPC), маршрутизатор VPC проверяет таблицу маршрутизации. Для обычных VM маршруты распространяются через BGP при включении флагов export-custom-routes / import-custom-routes (что клиент и сделал). Однако PSC Endpoints не являются стандартными подсетями. Они публикуются внутри VPC особым образом.  
До недавнего времени доступ к PSC Endpoint из пиринговой сети был технически невозможен. Хотя Google внедряет улучшения (например, PSC Interface), в классической схеме "PSA Peering -> Customer VPC -> PSC Endpoint" этот путь заблокирован.3  
Это означает, что архитектура клиента, подразумевающая "прозрачный проброс" соединения от Datastream через его VPC к Atlas, нереализуема в текущем виде без посредников.

## **4. Специфика протокола MongoDB и вызовы безопасности**

Понимание того, как работает драйвер MongoDB, критически важно для выбора правильной стратегии исправления. MongoDB — это не просто TCP-сокет (как PostgreSQL или MySQL). Это сложная распределенная система.

### **4.1. Обнаружение топологии (Service Discovery)**

При подключении к кластеру (Replica Set или Sharded Cluster) клиент MongoDB выполняет процедуру "Initial Handshake":

1. Клиент подключается к "Seed List" (адресам, указанным в строке подключения).  
2. Клиент отправляет команду isMaster (или hello в новых версиях).  
3. Сервер отвечает документом, содержащим конфигурацию реплика-сета, включая поле hosts, где перечислены адреса всех членов кластера (Primary и Secondaries).  
4. Клиент **обрывает** текущее соединение и переподключается к адресам, полученным в ответе isMaster, чтобы работать с конкретными нодами напрямую (балансировка чтения, запись в Primary).

Проблема: Сервер MongoDB Atlas сконфигурирован так, что он "знает" о себе только свои канонические публичные DNS-имена (например, atlas-shard-00-00.mongodb.net). В ответе на isMaster он вернет именно их.  
Даже если мы обманем Datastream на первом шаге (через /etc/hosts или прокси), драйвер Datastream получит список публичных имен и на втором шаге попытается соединиться с ними. Это вернет нас к Проблеме P1† (Public IP access).  
**Решение:** Необходимо принудительно заставить драйвер Datastream работать в режиме **Direct Connection**, игнорируя топологию. Параметр directConnection=true в строке подключения (Connection String) указывает драйверу выполнять операции непосредственно на том хосте, к которому он подключился изначально, не пытаясь обнаружить других участников.6

### **4.2. TLS/SSL и SNI (Server Name Indication)**

MongoDB Atlas требует обязательного использования TLS. Сертификаты, выдаваемые Atlas, являются валидными для доменов *.mongodb.net.  
Если Datastream подключается к прокси-серверу по IP-адресу (например, 10.10.10.10), но ожидает защищенного соединения, произойдет сбой валидации сертификата (Hostname Mismatch), так как сертификат сервера выдан на DNS-имя, а не на IP.  
Существует два пути решения:

1. **Отключение валидации:** Использование флагов типа tlsAllowInvalidHostnames или tlsInsecure. Однако, Datastream — это управляемый сервис, и его UI/API не всегда предоставляет гранулярный контроль над опциями TLS драйвера, часто требуя загрузки CA-сертификатов, но не давая кнопки "Ignore Hostname".8  
2. **Прозрачное туннелирование:** Использование механизмов, где "клиент" (Datastream) думает, что подключается к локальному хосту (туннель), или использование корректного DNS-разрешения на стороне проксирующего агента.

## **5. Стратегии решения (Remediation Strategies)**

На основе проведенного анализа мы предлагаем три стратегии решения проблемы, ранжированные по надежности, производительности и сложности реализации.

### **5.1. Стратегия А: Проксирование через VM (Рекомендуемая)**

Это наиболее надежное и архитектурно корректное решение, устраняющее как проблему DNS, так и проблему транзитивности PSC.

Суть решения:  
Внедрение промежуточного звена (Proxy VM) внутри пользовательской сети datastream-net. Datastream подключается к этой VM, а VM пересылает трафик на PSC Endpoint.  
**Архитектура:**

1. **Proxy VM:** Развертывается в VPC datastream-net (зоне доступности, близкой к Datastream). Тип машины: e2-micro или e2-small (достаточно для TCP streaming).  
2. **ПО:** Используется Nginx (модуль stream) или HAProxy.  
3. **Маршрутизация:**  
   * Datastream -> (Peering) -> Proxy VM (Private IP).  
   * Proxy VM -> (Local Network Resolution) -> PSC Endpoint DNS Name -> PSC IP.  
   * Proxy VM -> (Local Network Routing) -> PSC Endpoint.

**Конфигурация (Пример для Nginx):**

| Параметр | Значение | Обоснование |
| :---- | :---- | :---- |
| **Resolver** | 169.254.169.254 | Использование Cloud DNS метадата-сервера для разрешения приватных зон. |
| **Upstream** | atlas-endpoint-address.mongodb.net:27017 | Прокси должен обращаться по имени, чтобы сработал Private DNS. |
| **Proxy Protocol** | TCP (Layer 4) | Nginx не должен расшифровывать SSL (Passthrough), чтобы не управлять сертификатами. |

Решение проблемы MongoDB Discovery:  
В профиле Datastream необходимо:

1. Указать **IP-адрес Proxy VM** в качестве хоста.  
2. Использовать "Standard connection string".  
3. Добавить параметр directConnection=true (если поддерживается полем UI или через API/Terraform в поле аргументов).10  
4. Если Datastream строго требует валидации TLS хостнейма, может потребоваться использование собственного CA или самоподписанного сертификата на прокси, либо использование опции "Skip verification" (если доступна). В некоторых случаях, Nginx настраивается на переписывание SNI, но это сложно в реализации с mTLS Atlas.

### **5.2. Стратегия Б: Datastream Forward SSH Tunnel (Альтернативная)**

Datastream предоставляет встроенный механизм "Forward SSH tunnel".5 Это решение позволяет избежать установки и настройки Nginx, перекладывая задачу проксирования на SSH-демон.

Суть решения:  
Datastream устанавливает SSH-соединение с Bastion Host (VM в datastream-net) и пробрасывает порт до MongoDB.  
**Преимущества:**

* **Решение проблемы DNS:** Когда SSH-клиент (Datastream) просит пробросить порт на hostname:27017, разрешение этого имени выполняет **SSH-сервер** (Bastion) на своей стороне.13 Поскольку Bastion находится в datastream-net, он видит Private DNS зону и разрешает имя в IP PSC.  
* **Безопасность:** Весь трафик между Datastream и VPC шифруется SSH.  
* **Простота:** Не нужно настраивать балансировщики нагрузки или сложные конфиги Nginx. Достаточно Linux VM с публичным ключом Datastream.

**Конфигурация в Datastream:**

1. **Connectivity Method:** Forward SSH tunnel.  
2. **SSH Bastion:** IP-адрес VM в datastream-net.  
3. **Hostname (DB):** Каноническое DNS-имя Atlas (напр. cluster0-pl-0.mongodb.net).  
4. **Port:** 27017.

**Почему это работает:** SSH-туннель делает Bastion Host точкой входа. С точки зрения сети, соединение к Atlas инициирует сама VM, у которой нет проблем с маршрутизацией к PSC.

**Ограничения:**

* Производительность SSH-туннелирования ("TCP over TCP") может быть ниже, чем у чистого TCP-прокси, что критично для высоконагруженных потоков CDC.15  
* Необходимость управления SSH-ключами.

### **5.3. Стратегия В: Использование Private Service Connect Interfaces (Перспективная)**

Недавно Google представил возможность создавать PSC Interface непосредственно для Datastream.2 Это отличается от PSA (Peering).  
В этом сценарии Datastream создает сетевой интерфейс (NIC) внутри пользовательской VPC.  
Анализ:  
Если Datastream имеет "ногу" (интерфейс) в datastream-net, он технически становится локальным ресурсом сети.

* **Плюс:** Исчезает проблема транзитивности пиринга (так как нет пиринга, есть присутствие в сети).  
* **Минус:** Проблема DNS может сохраняться. Документация 2 все еще предупреждает: *"You need to provide the private IP addresses... because Datastream doesn't support DNS resolution"*. Даже имея интерфейс в подсети, Datastream может не использовать Cloud DNS резолвер этой подсети, а продолжать использовать свои внутренние.  
* **Вывод:** Этот метод решает проблему маршрутизации, но, вероятно, все еще потребует использования IP-адресов, что возвращает нас к проблеме TLS сертификатов MongoDB. Поэтому стратегии А и Б остаются предпочтительными для MongoDB.

## **6. План действий (Action Plan)**

Для скорейшего решения инцидента и разблокирования проекта P⁎, рекомендуется выполнить следующие шаги. Мы выбираем **Стратегию Б (SSH Tunnel)** как наиболее быструю для проверки (PoC) и **Стратегию А (Proxy VM)** как целевую для продакшна (из-за производительности).

### **Шаг 1: Подготовка Bastion/Proxy VM**

1. В проекте internal-resources-corp в сети datastream-net создать VM (e.g., datastream-gateway).  
2. Убедиться, что на VM разрешен входящий трафик от диапазонов IP Datastream (или конкретного пиринга).  
3. Проверить, что VM может резолвить имена Atlas в приватные IP: nslookup atlas-xxx.mongodb.net.  
4. Проверить связность с Atlas: telnet atlas-xxx.mongodb.net 27017 или mongosh....

### **Шаг 2: Настройка Datastream (Вариант SSH Tunnel)**

1. В Google Cloud Console перейти в Datastream -> Connection Profiles.  
2. Создать новый профиль MongoDB.  
3. Выбрать метод подключения: **Forward SSH tunnel**.  
4. Ввести детали SSH Bastion (IP, User, загрузить приватный ключ, публичный добавить на VM в ~/.ssh/authorized_keys).  
5. В качестве **Hostname** базы данных указать **DNS-имя Atlas** (не IP!).  
   * *Примечание:* Datastream попросит бастион разрешить это имя. Бастион вернет IP PSC. Соединение пойдет через туннель к PSC.  
6. Ввести учетные данные MongoDB пользователя.  
7. Запустить валидацию.

### **Шаг 3: Настройка Datastream (Вариант Proxy - если SSH не подходит)**

1. Настроить Nginx stream proxy на VM (как описано в п. 5.1).  
2. В профиле Datastream выбрать **Private connectivity (VPC peering)**.  
3. В качестве **Hostname** указать **Internal IP** прокси-VM.  
4. **Критически важно:** Если валидация падает на SSL Handshake (из-за несовпадения IP и имени в сертификате), необходимо рассмотреть возможность использования directConnection=true и, если возможно, загрузки корневого сертификата, либо перехода на SSH Tunnel, который прозрачнее работает с именами.

## **7. Заключение**

Анализ подтвердил, что текущая конфигурация клиента ꆜ является неработоспособной из-за фундаментальных ограничений платформы Google Cloud: отсутствия поддержки DNS-разрешения частных зон в Datastream и отсутствия транзитивной маршрутизации к PSC эндпоинтам через VPC Peering. Диагноз "Split-Horizon DNS Failure" верен, но является лишь частью проблемы.

Решение задачи требует изменения архитектуры подключения. Прямое соединение "Datastream -> Peering -> PSC" невозможно. Необходимо внедрение промежуточного узла в пользовательской VPC, который возьмет на себя функции разрешения имен и маршрутизации трафика. Использование **SSH-туннелирования** через бастион-хост является наиболее рекомендуемым способом, так как оно нативно поддерживается Datastream и элегантно обходит обе выявленные проблемы без сложной настройки прокси-серверов.

---

**Таблица: Сравнительный анализ методов подключения**

| Метод | Решает проблему DNS? | Решает проблему PSC Routing? | Сложность настройки | Примечание |
| :---- | :---- | :---- | :---- | :---- |
| **Direct Peering (Текущий)** | ❌ Нет | ❌ Нет | Низкая | **Неработоспособен** для PSC |
| **Proxy VM (Nginx)** | ✅ Да | ✅ Да | Средняя | Требует управления конфигами Nginx |
| **SSH Tunnel** | ✅ Да (через Remote Resolve) | ✅ Да | Низкая | Встроен в Datastream, рекомендуем |
| **PSC Interface** | ❌ Нет (требует IP) | ✅ Да | Высокая | Новая фича, возможны проблемы с TLS |

### ---

**Библиография и источники данных**

В отчете использованы данные из официальной документации Google Cloud и MongoDB, а также анализ предоставленных сниппетов:

* 2: Ограничения DNS в Datastream Private Connectivity.  
* 3: Ограничения транзитивности VPC Peering для PSC.  
* 5: Механика работы SSH-туннелей и удаленного разрешения DNS.  
* 6: Параметры подключения MongoDB (directConnection).  
* 1: Публичная доступность DNS-записей Atlas.

#### **Works cited**

1. Announcing Google Private Service Connect (PSC) Integration for MongoDB Atlas, accessed December 6, 2025, [https://www.mongodb.com/company/blog/product-release-announcements/announcing-google-private-service-connect-psc-integration-mongodb-atlas](https://www.mongodb.com/company/blog/product-release-announcements/announcing-google-private-service-connect-psc-integration-mongodb-atlas)  
2. Create a private connectivity configuration | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration)  
3. Configure VPC peering | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/vpc-peering](https://docs.cloud.google.com/datastream/docs/vpc-peering)  
4. How to use Cloud DNS peering in a Shared VPC environment | Google Cloud Blog, accessed December 6, 2025, [https://cloud.google.com/blog/products/networking/how-to-use-cloud-dns-peering-in-a-shared-vpc-environment/](https://cloud.google.com/blog/products/networking/how-to-use-cloud-dns-peering-in-a-shared-vpc-environment/)  
5. Create connection profiles | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/create-connection-profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles)  
6. MongoDB Integration - Elastic, accessed December 6, 2025, [https://www.elastic.co/docs/reference/integrations/mongodb](https://www.elastic.co/docs/reference/integrations/mongodb)  
7. Connection String Options - Database Manual - MongoDB Docs, accessed December 6, 2025, [https://www.mongodb.com/docs/manual/reference/connection-string-options/](https://www.mongodb.com/docs/manual/reference/connection-string-options/)  
8. Diagnose issues | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/diagnose-issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues)  
9. TLS/SSL Configuration for Clients - Database Manual - MongoDB Docs, accessed December 6, 2025, [https://www.mongodb.com/docs/manual/tutorial/configure-ssl-clients/](https://www.mongodb.com/docs/manual/tutorial/configure-ssl-clients/)  
10. Manage connection profiles | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/manage-connection-profiles](https://docs.cloud.google.com/datastream/docs/manage-connection-profiles)  
11. REST Resource: projects.locations.connectionProfiles | Datastream, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles)  
12. Forward SSH tunnel | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/ssh-tunnel](https://docs.cloud.google.com/datastream/docs/ssh-tunnel)  
13. When using an SSH tunnel does the server resolve domain names or is it still done via the ISP/DNS server on the router? - Information Security Stack Exchange, accessed December 6, 2025, [https://security.stackexchange.com/questions/144297/when-using-an-ssh-tunnel-does-the-server-resolve-domain-names-or-is-it-still-don](https://security.stackexchange.com/questions/144297/when-using-an-ssh-tunnel-does-the-server-resolve-domain-names-or-is-it-still-don)  
14. How to SSH tunnel to a destination host resolved via internal DNS on the bastion host, accessed December 6, 2025, [https://unix.stackexchange.com/questions/598819/how-to-ssh-tunnel-to-a-destination-host-resolved-via-internal-dns-on-the-bastion](https://unix.stackexchange.com/questions/598819/how-to-ssh-tunnel-to-a-destination-host-resolved-via-internal-dns-on-the-bastion)  
15. Network connectivity methods | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/network-connectivity-options](https://docs.cloud.google.com/datastream/docs/network-connectivity-options)  
16. Configure Private Service Connect interfaces | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/psc-interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces)