https://gemini.google.com/share/48f5a4673334


## **1. Введение и контекст взаимодействия**

Настоящий отчет представляет собой исчерпывающий технический ответ на запрос клиента (Upwork ID: ꆜ), касающийся интеграции сервиса Google Cloud Datastream с кластером MongoDB Atlas с использованием механизма Private Service Connect (PSC). Целью данного документа является детальный анализ проблемы, оценка предложенных технических решений и формулирование обоснованного вердикта по выбору архитектуры подключения.

В современной облачной экосистеме задачи репликации данных в реальном времени (CDC — Change Data Capture) становятся критически важными для аналитических платформ. Однако интеграция управляемых сервисов (Managed Services) от разных провайдеров — в данном случае Google Cloud Platform (GCP) и MongoDB Atlas — часто сопряжена с нетривиальными сетевыми вызовами. Основной конфликт возникает на стыке политик безопасности, механизмов маршрутизации и протоколов прикладного уровня. В ходе предварительного исследования (файлы B.md, L.md, O.md) была выявлена фундаментальная несовместимость между механизмом разрешения имен (DNS) в приватных контурах Datastream и требованиями протокола TLS/SSL, предъявляемыми MongoDB Atlas.

Данный отчет структурирован таким образом, чтобы последовательно разобрать каждый слой проблемы: от сетевого уровня (L3/L4) до уровня приложений (L7). Мы рассмотрим ограничения, накладываемые квотами Google Cloud 1, специфику работы VPC-пиринга и Private Service Connect 2, а также особенности работы драйверов MongoDB в условиях репликационных наборов (Replica Sets).4 Итогом анализа станет детализированная архитектура решения, обеспечивающая надежность, безопасность и соответствие лучшим практикам эксплуатации облачных систем.

### **1.1 Цели и задачи анализа**

В рамках формализованной задачи перед нами стоят следующие цели:

1. **Декомпозиция проблемы подключения:** Выявить корневые причины сбоев соединения, зафиксированных в логах (L.md), связанных с ошибками SSL Handshake и невозможностью разрешения DNS-имен.  
2. **Анализ ограничений платформы:** Оценить влияние квот и лимитов Google Cloud Datastream и Cloud DNS на выбор архитектурного решения.1  
3. **Оценка стратегических опций:** Провести сравнительный анализ трех основных подходов (прямое подключение, SSH-туннелирование, проксирование) с точки зрения производительности, безопасности и эксплуатационной сложности.  
4. **Разработка целевой архитектуры:** Сформировать детальное техническое задание на реализацию рекомендованного решения, включая конфигурационные параметры и схемы потоков данных.

## **2. Технический бэкграунд и формализация проблемы (Анализ B.md)**

Для понимания сути проблемы необходимо глубоко погрузиться в архитектуру сетевого взаимодействия между Google Cloud и MongoDB Atlas. Ситуация осложняется тем, что мы имеем дело с двумя независимыми облачными средами, соединенными через приватные каналы связи, которые имеют свои строгие правила транзитивности и видимости.

### **2.1 Ландшафт подключения: Datastream и Private Service Connect**

Google Cloud Datastream — это бессерверный сервис, предназначенный для асинхронной репликации данных. Архитектурно он реализован как управляемый сервис, ресурсы которого (воркеры, осуществляющие чтение и передачу данных) разворачиваются в специальном служебном проекте Google (Service Producer Project), скрытом от пользователя. Для того чтобы эти воркеры могли получить доступ к ресурсам в пользовательской сети VPC (Consumer VPC), используется механизм "Private Connectivity".7

Этот механизм базируется на технологии VPC Network Peering. При создании конфигурации частного подключения устанавливается пиринговое соединение между сетью Service Producer и сетью пользователя. Это дает воркерам Datastream возможность отправлять IP-пакеты на внутренние адреса в сети пользователя.2

С другой стороны, MongoDB Atlas предоставляет доступ к своим кластерам через Private Service Connect (PSC). PSC позволяет представить удаленный сервис (в данном случае базу данных Atlas, работающую в собственном VPC MongoDB) как локальный IP-адрес (Endpoint) внутри пользовательской сети Google Cloud VPC.3 Это обеспечивает однонаправленный доступ к базе данных без выхода в публичный интернет, что является стандартом безопасности для корпоративных систем.4

### **2.2 Фундаментальная несовместимость: Проблема "Double Peering" и DNS**

Анализ материалов исследования (B.md) и документации выявляет критический архитектурный конфликт, который делает "наивную" реализацию подключения невозможной.

#### **2.2.1 Нарушение транзитивности маршрутизации**

В Google Cloud пиринг сетей VPC не является транзитивным.9 Это означает, что если сеть A (Datastream Producer) соединена пирингом с сетью B (User Consumer VPC), а сеть B соединена с сетью C (или сервисом через PSC), то сеть A не может автоматически отправлять трафик в сеть C через сеть B.  
Хотя Private Service Connect технически отличается от классического пиринга, маршруты к PSC Endpoints не всегда автоматически экспортируются в пиринговые соединения с сервис-провайдерами, если не используются специальные механизмы, такие как PSC Interfaces.10 В стандартной конфигурации Datastream "видит" только те диапазоны IP-адресов, которые явно анонсируются из пользовательской VPC. Если PSC Endpoint находится в подсети пользовательской VPC, Datastream может иметь техническую возможность отправить пакет на этот IP, но здесь вступает в силу следующая, более серьезная проблема.

#### **2.2.2 "Черная дыра" DNS в приватных подключениях**

Документация Datastream содержит критическое ограничение: "Datastream не поддерживает разрешение доменных имен (DNS) в частных подключениях".7 Это ограничение продиктовано архитектурой изоляции. Воркеры Datastream работают в полностью управляемой среде и используют собственные DNS-резолверы Google. Они не имеют доступа к зонам Cloud DNS, настроенным в пользовательской VPC (Private Zones), так как механизмы DNS Peering между Managed Services и User VPC в данном контексте не реализованы.11

Это означает, что даже если пользователь настроит в своей сети Cloud DNS Private Zone, которая разрешает имя cluster0-shard-00.mongodb.net в IP-адрес PSC Endpoint (например, 10.128.0.5), Datastream не сможет воспользоваться этим разрешением. Сервис требует ввода IP-адреса, а не хостнейма, для установления соединения.

#### **2.2.3 Зависимость MongoDB от хостнеймов**

Протокол MongoDB и архитектура Replica Set жестко завязаны на использование доменных имен.

1. **SSL/TLS Verification:** Кластеры MongoDB Atlas защищены TLS-сертификатами, выписанными на их публичные доменные имена (например, *.mongodb.net). Если клиент (Datastream) подключается к серверу по IP-адресу (10.128.0.5), сервер все равно предъявляет сертификат для *.mongodb.net. Клиент, ожидающий соединения с IP-адресом, обнаруживает несоответствие имени в сертификате (Subject Alternative Name mismatch) и разрывает соединение, если не отключена проверка хостнейма.12  
2. **Topology Discovery:** Даже если удастся установить первичное соединение с одной нодой, драйвер MongoDB запрашивает конфигурацию реплика-сета (команда isMaster или hello). Сервер возвращает список участников кластера. В MongoDB Atlas этот список всегда содержит FQDN-имена нод, а не их IP-адреса.4 Получив этот список, Datastream пытается установить новые соединения с полученными хостнеймами. Поскольку DNS-разрешение отсутствует 7, эти попытки обречены на провал, что приводит к невозможности работы CDC.

Таким образом, мы имеем замкнутый круг: Datastream требует IP-адреса из-за отсутствия DNS, а MongoDB Atlas требует использования хостнеймов для корректной работы SSL и топологии кластера.

## **3. Глубокий анализ ограничений и данных логов (Анализ L.md)**

В данном разделе мы детально разберем конкретные технические ограничения и ошибки, подтверждающие выводы, сделанные на этапе формализации проблемы. Анализ логов (L.md) и сниппетов документации позволяет точно диагностировать причины сбоев.

### **3.1 Ошибка SSL Handshake: Hostname Mismatch**

В предоставленных материалах 13 описывается типичная ошибка: SSLHandshakeFailed: The server certificate does not match the host name.  
Когда Datastream инициирует TLS-соединение, он отправляет пакет ClientHello. Если в конфигурации профиля указан IP-адрес (что неизбежно из-за ограничений DNS), поле SNI (Server Name Indication) в ClientHello либо отсутствует, либо содержит IP-адрес.  
Сервер MongoDB Atlas, получая такой запрос, возвращает свой стандартный сертификат, выданный на доменное имя. Библиотека OpenSSL на стороне Datastream сверяет запрошенный адрес (IP) с именем в сертификате (DNS) и фиксирует ошибку валидации.  
Некоторые пользователи пытаются обойти это, загружая корневые сертификаты (CA) или используя самоподписанные сертификаты. Однако Datastream, как управляемый сервис, имеет ограниченные возможности по настройке параметров верификации. В частности, в API Datastream (v1) параметры ssl_config позволяют загрузить клиентский сертификат и CA, но не предоставляют явного флага tlsAllowInvalidHostnames, который доступен в стандартных драйверах MongoDB.14 Хотя некоторые источники упоминают возможность отключения валидации (verify_server_certificate=false или аналоги), для управляемых сервисов Google эта функциональность часто ограничена политиками безопасности, запрещающими MITM-уязвимые конфигурации.

### **3.2 Ограничения квот и масштабируемость**

При проектировании решения необходимо учитывать жесткие квоты Google Cloud, приведенные в 1 и.6

* **Лимит конфигураций частного подключения:** "Each Google Cloud project can have a maximum of 5 private connectivity configurations".1 Это критически важное ограничение. Оно означает, что мы не можем создавать отдельную сетевую конфигурацию для каждого потока данных, если их планируется много. Архитектура должна быть централизованной: одна конфигурация подключения должна обслуживать множество источников и приемников.  
* **Пропускная способность DNS:** Хотя лимиты на DNS-запросы высоки (100,000 запросов за 10 секунд на зону 6), они касаются Cloud DNS внутри пользовательской VPC. Поскольку Datastream не использует этот DNS, эти лимиты косвенно влияют только на проксирующие решения, которые мы будем рассматривать далее.  
* **Транзитивность пиринга:** Ограничения VPC Peering 2 подтверждают, что прямая маршрутизация трафика "Datastream -> Consumer VPC -> Peered Network" невозможна без промежуточного звена (NAT-шлюза или Прокси).

### **3.3 Специфика MongoDB Atlas Private Endpoint**

Согласно 16 и 4, соединения через Private Endpoint являются однонаправленными: Atlas не может инициировать соединения обратно в VPC клиента. Это упрощает модель угроз (нам не нужно беспокоиться о защите VPC от вредоносного трафика из базы данных), но накладывает ограничения на использование некоторых схем репликации, где инициатором выступает база данных. В случае Datastream инициатором всегда выступает стриминговый сервис (Datastream), поэтому данное ограничение не блокирует работу, но подтверждает необходимость корректной настройки Firewall Rules на входящий трафик в Atlas (через Security Groups в консоли Atlas).

## **4. Оценка стратегических опций (Анализ O.md)**

На основе проведенного анализа и материалов (O.md), мы рассматриваем три основных архитектурных подхода к решению проблемы. Каждый подход оценивается по критериям функциональности, безопасности, производительности и сложности поддержки.

### **4.1 Опция A: Прямое подключение к PSC Endpoint (Direct Connection)**

* **Концепция:** Настроить профиль подключения Datastream, указав IP-адрес PSC Endpoint в качестве хоста.  
* **Анализ:**  
  * *DNS:* Не работает. Datastream не может разрешить имена нод, возвращаемые командой hello.  
  * *SSL:* Не работает. Ошибка Hostname mismatch.  
  * *Workaround:* Теоретически можно попытаться использовать режим "Direct Connection" (подключение к одной ноде, минуя discovery) и отключить SSL-валидацию. Однако, как отмечалось выше, Datastream не позволяет гибко управлять флагами SSL-валидации (в частности, игнорировать hostname mismatch) через стандартный UI/API безопасным образом для управляемых источников.17 Более того, прямое подключение к одной ноде лишает систему отказоустойчивости (High Availability): если Primary-нода сменится, поток данных остановится.  
* **Вердикт:** **Непригодно для промышленной эксплуатации.** Решение слишком хрупкое и нарушает принципы безопасности.

### **4.2 Опция B: SSH-туннелирование через Bastion (Forward SSH Tunnel)**

* **Концепция:** Использовать встроенную функцию Datastream "Forward SSH tunnel".18 Разворачивается промежуточная виртуальная машина (Bastion Host) в Consumer VPC. Datastream устанавливает SSH-соединение с бастионом и пробрасывает через него трафик к MongoDB.  
* **Анализ:**  
  * *DNS:* SSH-туннель (port forwarding) работает на уровне TCP. Обычно клиент (Datastream) сам разрешает DNS-имя перед открытием туннеля. Однако в конфигурации Datastream мы указываем *локальный* порт и хост туннеля. Если Datastream подключается к туннелю, он "думает", что работает с локальным ресурсом. Проблема возникает, когда драйвер MongoDB внутри Datastream получает список хостов реплика-сета. Он попытается открыть *новые* соединения к этим хостам. SSH-туннель в режиме local forwarding (-L) пробрасывает только один конкретный порт на один конкретный хост. Он не обеспечивает прозрачного доступа ко всему кластеру динамически.  
  * *SOCKS Proxy:* Для работы с динамическим набором хостов (реплика-сетом) требуется динамический туннель (SOCKS). Документация Datastream не указывает явной поддержки SOCKS-проксирования для всего трафика драйвера MongoDB, а описывает лишь "Forward SSH tunnel" к конкретному хосту.18  
  * *Производительность:* Инкапсуляция TCP в TCP (туннелирование базы данных через SSH) известна проблемой "TCP Meltdown" при высоких нагрузках и потерях пакетов. Это создает значительные риски для стабильности CDC-потока.  
  * *Безопасность:* Требует управления SSH-ключами и администрирования ОС бастиона.  
* **Вердикт:** **Условно пригодно для простых сценариев (Single Node), но рискованно для Replica Set.** Высокая сложность настройки маршрутизации для всех членов кластера и проблемы с производительностью делают этот вариант нежелательным для высоконагруженных систем.

### **4.3 Опция C: Промежуточный TCP-прокси (Рекомендованное решение)**

* **Концепция:** Развернуть в Consumer VPC группу виртуальных машин с ПО для проксирования TCP-трафика (например, Nginx или HAProxy) за внутренним балансировщиком нагрузки (Internal Load Balancer - ILB).  
* **Механизм работы:**  
  1. Datastream подключается к IP-адресу Прокси (через Private Connectivity).  
  2. Прокси терминирует TCP-соединение.  
  3. Прокси открывает новое соединение к PSC Endpoint (или напрямую к хостнеймам Atlas, используя Cloud DNS пользовательской VPC).  
  4. Прокси передает данные между Datastream и Atlas.  
* **Решение проблемы DNS:** Прокси находится в Consumer VPC и имеет полный доступ к Cloud DNS. Он может разрешать имена *.mongodb.net в IP-адреса PSC.  
* **Решение проблемы SSL:** Nginx поддерживает директиву proxy_ssl_server_name on;.19 Это заставляет Nginx использовать SNI при подключении к Atlas, передавая правильное доменное имя. Таким образом, Atlas видит корректный запрос и возвращает валидный сертификат, который Nginx успешно проверяет.  
  * Со стороны Datastream прокси может выглядеть как конечная точка. Мы можем настроить Nginx на использование собственного сертификата (Self-Signed или от корпоративного CA) для шифрования канала "Datastream -> Proxy". Datastream будет доверять этому CA (загруженному в профиль подключения) и подключаться по IP-адресу прокси без ошибок SNI (так как сертификат прокси можно выписать на IP-адрес или Datastream будет просто доверять CA).  
* **Вердикт:** **Оптимальное архитектурное решение.** Оно полностью устраняет проблемы DNS и SSL, обеспечивает высокую производительность и масштабируемость.

## **5. Детальный анализ рекомендаций (R⬆⠿)**

В данном разделе мы формализуем выбранную стратегию (Опция C) и отбрасываем альтернативы с обоснованием, формируя итоговые рекомендации для клиента.

### **5.1 Отклоненная рекомендация: NAT/Masquerading на шлюзе**

* **Суть:** Настройка iptables NAT на промежуточной VM для перенаправления пакетов.  
* **Причина отказа:** NAT работает на уровне L3/L4 (сетевой/транспортный). Он может решить проблему маршрутизации пакетов, но он абсолютно прозрачен для протоколов SSL и MongoDB. При NAT-инге ClientHello от Datastream останется неизменным (без SNI или с неверным SNI), и SSL-хендшейк с Atlas все равно упадет. NAT не решает проблему прикладного уровня.

### **5.2 Отклоненная рекомендация: DNS Peering с Service Producer**

* **Суть:** Попытка настроить пиринг DNS между проектом Datastream и проектом клиента.  
* **Причина отказа:** Согласно документации Cloud DNS 11, функционал DNS Peering предназначен для пользовательских VPC. Google не предоставляет интерфейса для настройки DNS-пиринга "внутрь" управляемых сервисов типа Datastream (Black Box). Мы не можем повлиять на настройки резолверов внутри воркеров Datastream.

### **5.3 Принятая рекомендация: "Proxy Bridge" с перешифрованием (Re-encryption)**

Это единственное решение, которое покрывает все технические разрывы.

#### **5.3.1 Архитектурная топология**

* **Зона A (Datastream Producer Project):** Воркеры Datastream.  
* **Связь:** VPC Network Peering.  
* **Зона B (Customer Consumer VPC):**  
  * **Компонент:** Internal TCP Proxy (Nginx).  
  * **Роль:** Посредник, "переводчик" протоколов.  
  * **Сетевой доступ:** Имеет доступ к Cloud DNS Private Zone для mongodb.net.  
* **Зона C (MongoDB Atlas VPC):**  
  * **Компонент:** MongoDB Cluster.  
  * **Связь:** Private Service Connect (PSC Endpoint в Зоне B).

#### **5.3.2 Механизм решения проблем**

1. **DNS:** Datastream обращается к Прокси по статическому внутреннему IP (например, 10.128.0.50). DNS-разрешение на стороне Datastream не требуется.  
2. **SSL Identity (Datastream -> Proxy):** Прокси использует самоподписанный сертификат, созданный для IP-адреса 10.128.0.50 (или просто валидный сертификат, которому доверяет Datastream через загруженный Root CA). Это обеспечивает шифрование первого плеча и успешный хендшейк.  
3. **SSL Identity (Proxy -> Atlas):** Прокси инициирует новое TLS-соединение к Atlas. Nginx конфигурируется с proxy_ssl_server_name on, что подставляет правильное имя хоста (например, cluster0-shard-00.mongodb.net) в SNI. Хендшейк с Atlas проходит успешно, так как имя совпадает с сертификатом Atlas.  
4. **Топология кластера:** В конфигурации Nginx upstream мы можем прописать адрес PSC Endpoint. Для обеспечения работы со всеми шардами/репликами может потребоваться несколько блоков server в Nginx, слушающих на разных портах, каждый из которых мапится на соответствующую ноду Atlas (если требуется прямой доступ к конкретным нодам), либо (что предпочтительнее для CDC) использование Connection String, указывающего на прокси как на единую точку входа, при условии, что драйвер Datastream сможет корректно интерпретировать это в контексте CDC.  
   * *Важное уточнение по CDC:* Datastream часто использует протокол репликации MongoDB, читая Oplog. Ему нужен доступ к Primary или Secondary нодам. Если драйвер Datastream получит от Прокси (который перенаправляет трафик от Atlas) список реальных хостнеймов реплик (shard-00.mongodb.net), он снова попытается к ним подключиться и упадет.  
   * *Решение для Discovery:* Самый надежный способ — использовать **Direct Connection** (Single Node) в настройках Datastream, указав IP прокси. Прокси же настраивается на пересылку трафика на *текущий Primary* (через использование SRV-записи в конфигурации Nginx или через механизм Health Checks, который будет определять Primary ноду). Однако Nginx (версия Open Source) имеет ограниченные возможности по активному мониторингу протокола MongoDB.  
   * *Альтернатива:* Использовать stream модуль Nginx для проксирования всего трафика на адрес PSC Endpoint (который обычно является Load Balancer-ом на стороне Atlas или адресом одной из нод). Но наиболее стабильным вариантом является использование режима **"Direct Connection"** в Datastream и указание IP-адреса прокси. Это заставляет Datastream игнорировать топологию кластера и просто читать поток с того хоста, который мы ему подсовываем.

## **6. Безопасность и соответствие стандартам (Security & Compliance)**

Реализация схемы с проксированием вводит дополнительный элемент в цепочку доверия. Критически важно обеспечить, чтобы этот элемент не стал "слабым звеном".

### **6.1 Цепочка доверия SSL (Chain of Trust)**

Схема реализует классическую атаку Man-in-the-Middle (MITM), но в конструктивном, управляемом русле (TLS Termination Proxy).

* **Сегмент 1 (Datastream -> Proxy):** Защищен TLS. Мы генерируем свой CA и сертификат сервера для Прокси. Публичная часть CA загружается в профиль подключения Datastream в поле ca_certificate.17 Это гарантирует, что Datastream "доверяет" Прокси.  
* **Сегмент 2 (Proxy -> Atlas):** Защищен TLS. Прокси использует системное хранилище корневых сертификатов (Root CA store) ОС (Debian/RHEL) для валидации сертификатов Atlas (которые подписаны публичными CA, например Let's Encrypt или DigiCert). Директива proxy_ssl_verify on; в Nginx обязательна для предотвращения реальных MITM-атак на этом участке.

### **6.2 Аутентификация и контроль доступа**

* **Аутентификация в БД:** Прокси работает на уровне TCP (L4) и прозрачно передает пакеты аутентификации MongoDB (SCRAM-SHA-1/256). Учетные данные хранятся только в Datastream и Atlas; на Прокси они не оседают в открытом виде (трафик внутри прокси расшифровывается в памяти, но не логируется).  
* **Сетевой экран (Firewall):**  
  * *Ingress (Proxy):* Разрешить входящий трафик на порт 27017 только из диапазона IP-адресов Datastream Private Connection (отображается в консоли GCP после создания конфигурации).  
  * *Egress (Proxy):* Разрешить исходящий трафик на порт 27017 только в подсеть PSC Endpoint.

## **7. Операционный вердикт и дорожная карта внедрения (Implementation Roadmap)**

### **7.1 Итоговый Вердикт**

На основании всестороннего анализа, мы приходим к заключению, что прямое подключение Google Cloud Datastream к MongoDB Atlas через Private Service Connect технически невозможно без использования промежуточного слоя адаптации.  
Причиной является отсутствие поддержки DNS и механизмов подмены SNI в сервисе Datastream.  
**Рекомендованное решение:** Внедрение архитектуры **"Transparent TCP Proxy Bridge"** на базе Nginx в Consumer VPC. Это решение обеспечивает необходимую гибкость для преодоления ограничений протоколов, сохраняя высокий уровень безопасности и производительности.

### **7.2 План реализации (Technical Specification)**

Ниже представлен пошаговый план настройки, который должен быть выполнен инженерами клиента.

#### **Фаза 1: Подготовка инфраструктуры (Infrastructure Preparation)**

1. **Настройка PSC:** Убедиться, что в проекте GCP (Consumer VPC) создан Private Service Connect Endpoint для сервиса MongoDB Atlas.8 Зафиксировать его IP-адрес (например, 10.0.0.100).  
2. **Настройка DNS:** В Cloud DNS создать Private Zone mongodb.net (или соответствующую зону вашего кластера), настроить A-записи для перенаправления имен нод Atlas на IP-адрес PSC Endpoint. Это необходимо для того, чтобы Прокси мог разрешать имена. Проверить работу DNS с тестовой VM: dig +short cluster0-shard-00.mongodb.net должно возвращать IP PSC.

#### **Фаза 2: Развертывание Прокси (Proxy Deployment)**

1. **Provisioning:** Развернуть VM (e2-medium или выше, в зависимости от нагрузки) в той же VPC и регионе, что и Datastream Connectivity.  
2. **Генерация сертификатов:**  
   Bash  
   # Создать CA  
   openssl req -x509 -sha256 -newkey rsa:2048 -keyout ca.key -out ca.crt -days 3650 -nodes -subj '/CN=MyProxyCA'  
   # Создать сертификат сервера (для IP прокси)  
   openssl req -new -newkey rsa:2048 -keyout proxy.key -out proxy.csr -nodes -subj '/CN=10.128.0.50'  
   openssl x509 -req -CA ca.crt -CAkey ca.key -in proxy.csr -out proxy.crt -days 365 -CAcreateserial

3. Конфигурация Nginx (/etc/nginx/nginx.conf):  
   Использовать модуль stream для TCP-проксирования.  
   Nginx  
   stream {  
       server {  
           listen 27017 ssl; # Слушаем SSL от Datastream  
           proxy_pass atlas_backend;

           # Сертификаты для Datastream  
           ssl_certificate /etc/nginx/certs/proxy.crt;  
           ssl_certificate_key /etc/nginx/certs/proxy.key;

           # Настройки подключения к Atlas (SSL Re-encryption)  
           proxy_ssl on;  
           proxy_ssl_server_name on; # Включает SNI!   
           proxy_ssl_verify on;  
           proxy_ssl_trusted_certificate /etc/ssl/certs/ca-certificates.crt; # Системные руты

           # Опционально: принудительно задать имя для верификации  
           # proxy_ssl_name cluster0-shard-00.mongodb.net;   
       }

       upstream atlas_backend {  
           # Здесь используем DNS-имя Atlas. Nginx разрешит его в IP PSC через системный резолвер.  
           server cluster0-shard-00.mongodb.net:27017;  
       }  
   }

#### **Фаза 3: Настройка Datastream (Configuration)**

1. **Connection Profile:** Создать новый профиль MongoDB.  
   * **Hostname:** Внутренний IP-адрес Прокси VM (например, 10.128.0.50).  
   * **Port:** 27017.  
   * **Connectivity Method:** Private Connectivity.  
   * **Encryption:** Выбрать опцию "Server verification" (или аналогичную). Загрузить файл ca.crt (публичный ключ вашего CA), созданный на Фазе 2. Это критически важно для доверия самоподписанному сертификату прокси.17  
2. **Тестирование:** Запустить проверку соединения. Datastream должен успешно подключиться к Прокси, установить TLS-туннель, а Прокси перенаправит трафик в Atlas.

#### **Фаза 4: Отказоустойчивость (High Availability)**

Для Production-среды одиночная VM является точкой отказа.

* **Рекомендация:** Создать Instance Template с настроенным Nginx.  
* Развернуть Managed Instance Group (MIG) с автоскейлингом (мин. 2 реплики).  
* Создать Internal TCP Load Balancer (L4 ILB) перед группой.  
* В Datastream указывать IP-адрес Load Balancer-а.

### **7.3 Риски и ограничения**

1. **Ротация сертификатов:** Необходимо наладить процесс обновления сертификатов на Прокси и в профиле Datastream до истечения их срока действия.  
2. **Изменение топологии Atlas:** Если в Atlas добавляются новые шарды или меняются доменные имена, может потребоваться обновление конфигурации Nginx (если имена захардкожены) или DNS-зон. Использование динамического DNS-резолвинга в Nginx (resolver 169.254.169.254;) минимизирует этот риск.  
3. **Split-Horizon DNS:** Важно следить, чтобы приватная зона DNS не перекрывала публичную зону mongodb.net таким образом, чтобы нарушить доступ других сервисов, которым нужен публичный доступ (если таковые есть).

## **8. Заключение**

Предложенное архитектурное решение трансформирует несовместимые требования двух облачных платформ в надежную, управляемую систему. Использование TCP-прокси с функцией SNI Injection и перешифрованием трафика полностью устраняет блокирующие факторы (отсутствие DNS, SSL Hostname Mismatch), при этом оставаясь в рамках политик безопасности (все каналы шифруются). Данный подход является стандартом де-факто для интеграции legacy-систем или систем с жесткими сетевыми ограничениями, к классу которых относится текущая реализация приватных подключений в Google Cloud Datastream.

### ---

**Таблицы и Структурированные Данные**

#### **Таблица 1: Сравнительный анализ архитектурных решений**

| Характеристика | Direct PSC (Напрямую) | SSH Tunnel (Бастион) | TCP Proxy (Nginx) |
| :---- | :---- | :---- | :---- |
| **Тип подключения** | Private IP | Инкапсулированный туннель | Private IP (через посредника) |
| **Разрешение DNS** | **Провал** (Datastream не умеет) | Частично (Зависит от клиента) | **Успех** (Прокси разрешает) |
| **Обработка SSL/SNI** | **Провал** (Mismatch) | **Провал** (Туннель прозрачен) | **Успех** (Прокси инжектирует SNI) |
| **Производительность** | Высокая (Теоретически) | Низкая (Оверхед TCP-over-TCP) | Высокая (Потоковое проксирование) |
| **Сложность внедрения** | Низкая | Средняя | Средняя |
| **Безопасность** | Высокая | Высокая | Высокая (Re-encryption) |
| **Вердикт** | **Блокирует работу** | **Не рекомендуется** | **Рекомендуется к внедрению** |

#### **Таблица 2: Влияние квот Google Cloud на решение**

1

| Ресурс / Квота | Лимит | Влияние на архитектуру |
| :---- | :---- | :---- |
| **Max Private Connectivity Configs** | 5 на проект | Необходимо использовать архитектуру "Hub-and-Spoke" или Shared VPC, проксируя несколько стримов через один канал. |
| **Streams per Region** | 50 | Прокси-группа (MIG) должна масштабироваться для обработки параллельных соединений от 50 стримов. |
| **DNS Queries per Zone** | 100,000 / 10s | Настройки кэширования DNS в Nginx критичны для предотвращения троттлинга запросов к Cloud DNS. |
| **Packet Mirroring** | Не поддерживается на PSC | Отладка сети на стыке PSC затруднена; необходимо полагаться на подробные access/error логи Nginx. |

---

*Конец отчета.*

#### **Works cited**

1. Quotas and limits | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/quotas](https://docs.cloud.google.com/datastream/docs/quotas)  
2. Private services access - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/vpc/docs/private-services-access](https://docs.cloud.google.com/vpc/docs/private-services-access)  
3. Private Service Connect - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/vpc/docs/private-service-connect](https://docs.cloud.google.com/vpc/docs/private-service-connect)  
4. Announcing Google Private Service Connect (PSC) Integration for MongoDB Atlas, accessed December 7, 2025, [https://www.mongodb.com/company/blog/product-release-announcements/announcing-google-private-service-connect-psc-integration-mongodb-atlas](https://www.mongodb.com/company/blog/product-release-announcements/announcing-google-private-service-connect-psc-integration-mongodb-atlas)  
5. Configure a MongoDB database for CDC | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/configure-mongodb](https://docs.cloud.google.com/datastream/docs/configure-mongodb)  
6. Quotas and limits | Cloud DNS - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/dns/quotas](https://docs.cloud.google.com/dns/quotas)  
7. Create a private connectivity configuration | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration)  
8. Example: Private connectivity for a MongoDB Atlas cluster | Integration Connectors, accessed December 7, 2025, [https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb)  
9. VPC Network Peering | Virtual Private Cloud, accessed December 7, 2025, [https://docs.cloud.google.com/vpc/docs/vpc-peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)  
10. Configure Private Service Connect interfaces | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/psc-interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces)  
11. Google Cloud networking in-depth: What's new with Cloud DNS, accessed December 7, 2025, [https://cloud.google.com/blog/products/networking/google-cloud-networking-in-depth-whats-new-with-cloud-dns](https://cloud.google.com/blog/products/networking/google-cloud-networking-in-depth-whats-new-with-cloud-dns)  
12. Mongodb SSL connection failing when using SSL certificate issued by Let's encrypt suddenly even though the certificate is not expired - Stack Overflow, accessed December 7, 2025, [https://stackoverflow.com/questions/69481148/mongodb-ssl-connection-failing-when-using-ssl-certificate-issued-by-lets-encryp](https://stackoverflow.com/questions/69481148/mongodb-ssl-connection-failing-when-using-ssl-certificate-issued-by-lets-encryp)  
13. Atlas MongoDB SSH Tunnel hostname mismatch - Stack Overflow, accessed December 7, 2025, [https://stackoverflow.com/questions/73958306/atlas-mongodb-ssh-tunnel-hostname-mismatch](https://stackoverflow.com/questions/73958306/atlas-mongodb-ssh-tunnel-hostname-mismatch)  
14. google_datastream_connection_, accessed December 7, 2025, [https://registry.terraform.io/providers/hashicorp/google/6.11.0/docs/resources/datastream_connection_profile](https://registry.terraform.io/providers/hashicorp/google/6.11.0/docs/resources/datastream_connection_profile)  
15. Elastic MongoDB connector reference, accessed December 7, 2025, [https://www.elastic.co/docs/reference/search-connectors/es-connectors-mongodb](https://www.elastic.co/docs/reference/search-connectors/es-connectors-mongodb)  
16. Learn About Private Endpoints in Atlas - Atlas - MongoDB Docs, accessed December 7, 2025, [https://www.mongodb.com/docs/atlas/security-private-endpoint/](https://www.mongodb.com/docs/atlas/security-private-endpoint/)  
17. API Reference — google_api_datastream v0.10.0 - HexDocs, accessed December 7, 2025, [https://hexdocs.pm/google_api_datastream/](https://hexdocs.pm/google_api_datastream/)  
18. Forward SSH tunnel | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/ssh-tunnel](https://docs.cloud.google.com/datastream/docs/ssh-tunnel)  
19. Proxy RUM data to Frontend Observability | Grafana Cloud documentation, accessed December 7, 2025, [https://grafana.com/docs/grafana-cloud/monitor-applications/frontend-observability/instrument/data-proxy/](https://grafana.com/docs/grafana-cloud/monitor-applications/frontend-observability/instrument/data-proxy/)