https://gemini.google.com/share/0f9c642b1828


## **1. Введение: Архитектурная дилемма интеграции Change Data Capture**

Современные корпоративные экосистемы данных все чаще требуют реализации механизмов захвата изменений (Change Data Capture — CDC) в реальном времени, связывая разнородные системы, такие как бессерверные сервисы Google Cloud Datastream и распределенные облачные базы данных MongoDB Atlas.1

Центральной проблемой при проектировании таких гибридных каналов репликации является фундаментальный конфликт C2⊥, возникающий из противоречия между жесткими требованиями к безопасности сетевого периметра и необходимостью обеспечения высокой пропускной способности и отказоустойчивости потока данных.

В данном отчете проводится исчерпывающий сравнительный анализ двух доминирующих стратегий подключения: S⌖3, основанной на SSH-туннелировании, и S⌖4, использующей проксирование на транспортном уровне (L4 TCP Proxy) или технологии Private Service Connect.

Каждая из этих стратегий обладает уникальным набором характеристик, влияющих на задержку (latency), пропускную способность (throughput) и операционную устойчивость системы в условиях нестабильности сети и динамической топологии кластера.3

Целью данного исследования является не просто перечисление технических спецификаций, но и глубокий анализ причинно-следственных связей, приводящих к таким критическим явлениям, как «TCP meltdown» в туннелированных соединениях или ошибки рукопожатия SSL/TLS при использовании прокси-серверов без корректной обработки Server Name Indication (SNI).5

Особое внимание уделяется специфике MongoDB Atlas как источника данных, учитывая его динамическую природу, использование наборов реплик (replica sets) и строгие требования к TLS-шифрованию, которые часто вступают в конфликт с возможностями клиента CDC.7

Мы рассмотрим, как ограничения Google Cloud Datastream, такие как отсутствие поддержки цепочек сертификатов или особенности разрешения DNS в частных сетях, накладывают жесткие и неочевидные рамки на выбор архитектурного решения.9

Анализ базируется на широком спектре технических данных, включая документацию облачных провайдеров, инженерные дискуссии, результаты синтетических тестов производительности и академические исследования протоколов передачи данных.11

Итоговый вывод позволит архитекторам данных и инженерам DevOps принимать математически обоснованные решения, минимизируя риски потери данных и простоя критически важных каналов репликации в продуктивных средах.

## **2. Теоретические основы конфликта транспортных протоколов и стратегия S⌖3**

### **2.1. Феноменология и риски инкапсуляции TCP в TCP (TCP-over-TCP)**

Стратегия S⌖3 опирается на механизм инкапсуляции, при котором TCP-сегменты внутреннего соединения (база данных — Datastream) упаковываются в полезную нагрузку внешнего TCP-соединения (SSH-туннель), что создает сложную вложенную структуру.3

На первый взгляд, это решение кажется элегантным и быстрым способом обхода межсетевых экранов без изменения глобальных сетевых настроек, однако оно скрывает в себе фундаментальный архитектурный изъян, известный как проблема вложенных контуров управления перегрузкой.5

Протокол TCP разработан для обеспечения гарантированной доставки данных в ненадежных сетях, используя механизмы повторной передачи пакетов (retransmission) и адаптивного изменения окна перегрузки (congestion window) в ответ на потерю пакетов или задержки подтверждения.4

Когда один TCP-поток (внутренний) работает поверх другого (внешнего), их алгоритмы обработки ошибок начинают интерферировать, создавая нелинейную положительную обратную связь, которая дестабилизирует оба соединения.

В случае потери пакета во внешнем SSH-соединении, внешний TCP-стек приостанавливает передачу данных, ожидая подтверждения (ACK) или тайм-аута для повторной отправки, что является штатным поведением протокола.3

Внутренний TCP-стек, не зная о проблемах транспортного уровня и воспринимая туннель как идеальную трубу, интерпретирует эту задержку как перегрузку сети или потерю собственных пакетов, инициируя свои независимые процедуры повторной передачи.5

Это приводит к каскадному эффекту, когда внутренний тайм-аут (RTO) истекает раньше, чем внешний канал успевает восстановить целостность потока данных и доставить задержанные сегменты.

В результате внутренний стек генерирует новые пакеты-дубликаты, которые еще сильнее нагружают и без того нестабильный внешний канал, приводя к резкому падению пропускной способности и увеличению очередей на интерфейсах.

В предельном случае этот процесс приводит к полной остановке передачи полезных данных, известной как «TCP meltdown», когда канал занят исключительно повторными передачами пакетов, которые не могут быть доставлены.5

Исследования и практический опыт показывают, что даже незначительный процент потери пакетов (менее 1-2%) во внешнем канале может привести к катастрофическому снижению производительности вложенного соединения на несколько порядков, делая его практически непригодным для высоконагруженных потоков CDC.13

Существуют методы смягчения этого эффекта, такие как принудительное увеличение тайм-аутов внутреннего соединения или изменение алгоритмов конгестии, однако они лишь маскируют проблему, увеличивая общую латентность системы и снижая реактивность на реальные сбои.4

Альтернативой является использование протоколов на базе UDP (например, WireGuard или QUIC), которые не имеют встроенного механизма гарантированной доставки на транспортном уровне и не создают конфликта таймеров, но SSH исторически и технически жестко привязан к TCP.5

Таким образом, использование SSH-туннелирования для Datastream создает неустранимый риск производительности и стабильности, который невозможно полностью нивелировать настройками конфигурации, особенно в сетях с переменным качеством обслуживания.

### **2.2. Эксплуатационные ограничения SSH в контексте пропускной способности**

Помимо проблем с надежностью протокола, SSH-туннелирование накладывает жесткие ограничения на максимальную пропускную способность канала репликации из-за особенностей реализации шифрования в OpenSSH.15

Процесс шифрования и дешифрования данных в стандартных реализациях SSH часто выполняется в одном потоке процессора, что создает узкое место (bottleneck) на стороне бастион-хоста или клиента, особенно при использовании алгоритмов с высокими накладными расходами.11

В сценариях CDC, где объем передаваемых данных может достигать гигабайтов в час, производительность одного ядра CPU становится лимитирующим фактором, не позволяющим утилизировать всю доступную ширину сетевого канала.16

Тесты производительности показывают, что даже на мощных серверах пропускная способность SSH-туннеля может быть ограничена значениями в районе 300-500 Мбит/с, что может быть недостаточно для первоначальной синхронизации (backfill) больших баз данных MongoDB.11

Использование более быстрых шифров, таких как ChaCha20-Poly1305 или AES-GCM с аппаратным ускорением, может частично смягчить проблему, но не устраняет архитектурное ограничение однопоточной обработки соединения в рамках одной сессии.11

Более того, управление ключами SSH и доступом к бастион-хостам создает дополнительные операционные накладные расходы, требуя регулярной ротации ключей и аудита безопасности, что усложняет эксплуатацию системы.18

В контексте Datastream, который является полностью управляемым сервисом, возможности по тонкой настройке параметров SSH-клиента на стороне Google Cloud ограничены, что делает пользователя заложником стандартных настроек тайм-аутов и алгоритмов шифрования.19

## **3. Анализ стратегии S⌖4: L4 TCP-проксирование и Private Service Connect**

### **3.1. Архитектурные преимущества разрыва TCP-соединения**

Стратегия S⌖4 подразумевает использование специализированного программного обеспечения (Nginx, HAProxy) или облачных сервисов (Google Private Service Connect, AWS PrivateLink) для перенаправления TCP-трафика от Datastream к MongoDB Atlas.20

В отличие от SSH-туннелирования, L4 прокси работает на транспортном уровне, не инкапсулируя пакеты в дополнительный TCP-слой, а терминируя входящее соединение и открывая новое исходящее, что исключает проблему «TCP meltdown».22

Прокси-сервер принимает TCP-соединение от Datastream, подтверждает получение пакетов и независимо устанавливает отдельное TCP-соединение с MongoDB Atlas, пересылая байты данных между этими двумя независимыми сессиями.23

Это позволяет буферизировать данные на промежуточном узле, управлять таймаутами для каждого плеча соединения отдельно и, что наиболее важно, осуществлять интеллектуальную маршрутизацию трафика на основе состояния бэкендов.

Разделение контуров управления перегрузкой означает, что потеря пакетов на участке "Datastream — Прокси" не вызывает немедленных повторных передач на участке "Прокси — Atlas", и наоборот, что стабилизирует общую производительность системы.

В контексте Google Cloud, использование Private Service Connect (PSC) можно рассматривать как высокоуровневую, полностью управляемую реализацию этой стратегии, где роль прокси выполняет глобальная SDN-инфраструктура Google Andromeda.24

PSC обеспечивает однонаправленное соединение от потребителя (Datastream) к производителю (MongoDB Atlas), сохраняя границы безопасности VPC и исключая необходимость в публичных IP-адресах, что является значительным преимуществом перед SSH-бастионами.26

Этот подход позволяет использовать внутренние IP-адреса для доступа к сервисам, находящимся в других VPC или даже других организациях, обеспечивая сетевую изоляцию и снижая поверхность атаки.

### **3.2. Роль прокси в управлении TLS и SNI для MongoDB Atlas**

Для успешного и безопасного подключения к кластерам MongoDB Atlas через промежуточный узел критически важно корректно обрабатывать расширение TLS Server Name Indication (SNI), так как Atlas обслуживает множество кластеров на одних и тех же IP-адресах балансировщиков.27

Nginx с модулем ngx_stream_proxy_module предоставляет возможность использовать директиву proxy_ssl_server_name on, которая принудительно передает имя хоста бэкенда в TLS-рукопожатии, даже если клиент подключился к IP-адресу прокси.27

Это решает проблему несоответствия сертификатов: Datastream устанавливает соединение с прокси, который может иметь собственный сертификат (или не использовать TLS на этом участке, если это внутри доверенной зоны), а прокси устанавливает валидное TLS-соединение с Atlas.29

В архитектуре Private Service Connect (PSC) эндпоинт представляется IP-адресом внутри VPC пользователя, но сертификат сервера MongoDB выдан на доменное имя вида *.mongodb.net.30

Для обеспечения корректной валидации сертификата на стороне клиента (Datastream) необходимо использовать механизмы Split Horizon DNS, чтобы доменные имена Atlas разрешались во внутренние IP-адреса PSC-эндпоинтов, а не в публичные IP.31

Однако Datastream имеет ограниченные возможности по настройке DNS и файла /etc/hosts, что делает использование PSC в чистом виде (без промежуточного DNS-резолвинга или прокси) нетривиальной задачей.32

Использование промежуточного L4 прокси (Nginx) перед PSC позволяет решить эту проблему: прокси разрешает имена через внутренний DNS или локальную конфигурацию, а Datastream подключается к прокси по статическому IP или внутреннему имени.10

Такая конфигурация также позволяет реализовать "Man-in-the-Middle" для адаптации цепочек сертификатов, если Datastream не поддерживает полные цепочки, используемые Atlas, путем перешифрования трафика собственным доверенным сертификатом.9

## **4. Специфика MongoDB Atlas: Репликация и отказоустойчивость**

### **4.1. Динамическая топология Replica Set и проблемы статической адресации**

MongoDB Atlas представляет собой распределенную систему баз данных, где узлы кластера объединены в наборы реплик (replica sets) и могут динамически менять свои роли (Primary/Secondary) и IP-адреса в процессе работы или обслуживания.33

В стандартной конфигурации приложение подключается к кластеру, используя Connection String с перечислением хостов или SRV-запись DNS, которая возвращает актуальный список доступных узлов.35

Драйвер клиента (в данном случае коннектор Datastream) должен уметь корректно обрабатывать топологию кластера, автоматически определяя текущий Primary-узел для операций захвата изменений (Oplog tailing).36

Однако при использовании SSH-туннелирования (S⌖3) конфигурация часто сводится к жесткой привязке туннеля к конкретному IP-адресу или хосту бастиона, который пробрасывает трафик на один фиксированный узел базы данных.9

Это создает критический риск при автоматическом переключении ролей (failover) в Atlas: если IP-адрес, к которому привязан туннель, переходит от Primary к Secondary, поток записи или специфичного чтения Oplog может прерваться.37

Datastream, ожидая подключения к мастеру для получения консистентного потока изменений, может столкнуться с ошибкой, если узел перешел в состояние RECOVERING или стал вторичным с задержкой репликации.7

В отличие от драйверов приложений, SSH-клиент не обладает логикой понимания протокола MongoDB и не может автоматически переключить туннель на новый Primary-узел.3

Для обеспечения отказоустойчивости в стратегии S⌖3 потребовалось бы создание скриптов автоматизации, которые мониторят состояние кластера и переконфигурируют туннели, что значительно усложняет эксплуатацию.18

### **4.2. Преимущества S⌖4 в обработке Failover**

Стратегия S⌖4 с использованием интеллектуального прокси или PSC обеспечивает более надежную обработку изменений топологии кластера.21

Private Service Connect от Google и MongoDB Atlas интегрированы таким образом, что за одним IP-адресом PSC-эндпоинта скрывается балансировщик нагрузки (Network Load Balancer) на стороне Atlas.30

Этот балансировщик автоматически отслеживает состояние узлов и маршрутизирует трафик, однако для протокола MongoDB важно не просто TCP-подключение, а именно подключение к правильному узлу в зависимости от Read Preference.34

В конфигурации Atlas с PSC обычно создается отдельный эндпоинт для каждого узла или используется механизм, где драйвер получает список всех доступных приватных эндпоинтов через DNS SRV запись, адаптированную для приватного доступа.31

Если используется Nginx (как часть S⌖4), его можно настроить с несколькими upstream серверами и активными проверками (health checks), которые будут опрашивать узлы MongoDB на предмет их роли (команда isMaster или hello).29

Это позволяет прокси-серверу самостоятельно определять актуальный Primary-узел и прозрачно перенаправлять на него трафик от Datastream, даже если Datastream настроен на один статический IP-адрес прокси.

Такой подход полностью изолирует Datastream от сложностей внутренней топологии Atlas, предоставляя стабильную точку входа (Virtual IP), которая всегда ведет к активному мастеру.22

Это критически важно для минимизации времени простоя (RTO) при аварийных переключениях или плановом обновлении версий базы данных в облаке.

## **5. Сравнительный анализ производительности и безопасности (C2⊥)**

### **5.1. Таблица сравнения характеристик стратегий**

Ниже приведена сводная таблица, демонстрирующая ключевые различия между стратегиями по критическим параметрам, выявленным в ходе исследования.

| Характеристика | Стратегия S⌖3 (SSH-туннель) | Стратегия S⌖4 (L4 Прокси / PSC) | Влияние на Datastream |
| :---- | :---- | :---- | :---- |
| **Транспортный уровень** | TCP-over-TCP (инкапсуляция) | Раздельные TCP соединения | S⌖3 вызывает риск "TCP Meltdown" и нестабильности потока. |
| **Обработка Failover** | Статическая привязка к узлу | Динамическая (через LB или Health Checks) | S⌖4 обеспечивает автоматическое восстановление при смене Primary. |
| **Производительность** | Ограничена 1 ядром CPU (шифрование) | Линейное масштабирование (Multi-thread) | S⌖4 позволяет обрабатывать гигабитные потоки данных без задержек. |
| **Безопасность (TLS/SNI)** | Сложности с передачей SNI и Cert Chains | Полная поддержка SNI rewrite и Custom CA | S⌖4 решает проблему несовместимости сертификатов Datastream и Atlas. |
| **Сложность настройки** | Низкая (одна команда/профиль) | Средняя/Высокая (инфраструктура) | S⌖3 быстрее для PoC, S⌖4 необходима для Production. |
| **Отказоустойчивость** | Единая точка отказа (Bastion) | Высокая (HA Cluster / Managed Service) | S⌖4 соответствует требованиям SLA корпоративного уровня. |

### **5.2. Анализ безопасности: Доверие и шифрование**

SSH-туннели (S⌖3) исторически считаются безопасным средством административного доступа, но их использование в качестве постоянного транспорта данных вызывает вопросы с точки зрения Zero Trust архитектуры.5

Открытый SSH-порт на бастионе, доступный из публичной сети (даже с ограничением по IP), представляет собой поверхность атаки, подверженную брутфорсу и эксплойтам уязвимостей демона SSH.38

Кроме того, SSH-туннель предоставляет доступ не только к конкретному порту базы данных, но и потенциально к оболочке сервера (shell), если конфигурация не ограничена директивами no-pty, no-X11-forwarding, PermitOpen.18

В отличие от этого, Private Service Connect (S⌖4) обеспечивает изоляцию трафика, который никогда не покидает магистральную сеть Google и не выходит в публичный интернет, что исключает перехват и снижает риски DDoS-атак.26

Использование L4 прокси также позволяет реализовать терминирование SSL/TLS на контролируемом узле, что дает возможность инспектировать трафик (при необходимости) или адаптировать параметры шифрования под требования устаревших клиентов.39

Критическим преимуществом S⌖4 является возможность управления цепочками доверия (Chain of Trust): Datastream имеет жесткие ограничения на формат сертификатов (только leaf, без chain), что конфликтует с публичными сертификатами Atlas.9

Прокси может выступать посредником, предоставляя Datastream упрощенный сертификат, подписанный внутренним CA, и устанавливая полноценное защищенное соединение с Atlas, используя его публичные сертификаты.40

### **5.3. Экономическая эффективность и масштабируемость**

Хотя S⌖3 кажется дешевле на старте (одна маленькая VM), скрытые расходы на администрирование и риски простоя могут значительно превысить экономию.12

Ограниченная производительность SSH требует вертикального масштабирования бастиона для повышения пропускной способности, но однопоточная природа sshd быстро делает это экономически нецелесообразным.16

Стратегия S⌖4, особенно в варианте с PSC, имеет тарификацию, основанную на объеме трафика и количестве эндпоинтов, что позволяет платить только за реальное потребление.41

Nginx или HAProxy, развернутые на GCE, могут эффективно утилизировать многоядерные инстансы, обрабатывая десятки тысяч соединений одновременно благодаря асинхронной архитектуре ввода-вывода (event-driven architecture).21

Для масштабных проектов, где объемы репликации исчисляются терабайтами, S⌖4 является единственным экономически и технически оправданным решением, обеспечивающим предсказуемую стоимость владения.

## **6. Детальные рекомендации по реализации S⌖4**

### **6.1. Конфигурация Nginx как адаптера протоколов**

Для успешной реализации стратегии S⌖4 с использованием Nginx необходимо учитывать специфику протокола MongoDB и требования Datastream.

Рекомендуется использовать модуль stream в Nginx для TCP-проксирования, настроив блок upstream с перечислением узлов кластера Atlas.23

Критически важным является включение директивы proxy_ssl on и proxy_ssl_server_name on для корректной передачи SNI имени хоста Atlas при установлении соединения от прокси к базе данных.27

Для решения проблемы с сертификатами в Datastream, Nginx должен быть настроен с сертификатом, выданным локальным CA, который затем загружается в профиль соединения Datastream как доверенный.42

Пример конфигурации должен включать параметры proxy_connect_timeout и proxy_timeout с увеличенными значениями, чтобы предотвратить разрыв длинных соединений CDC в периоды простоя.20

Также рекомендуется настроить TCP keepalive (so_keepalive=on), чтобы поддерживать таблицу соединений в сетевом оборудовании активной и быстро обнаруживать обрывы связи.43

### **6.2. Интеграция с Private Service Connect**

При использовании PSC важно понимать, что Google Cloud создает эндпоинт (Forwarding Rule) в VPC потребителя, который перенаправляет трафик на Service Attachment производителя.25

Для MongoDB Atlas необходимо создать Private Endpoint в консоли Atlas и связать его с проектом Google Cloud, после чего выполнить скрипт настройки на стороне GCP для создания правил переадресации.44

Поскольку Datastream не находится в пользовательском VPC (он работает в управляемом VPC Google), необходимо настроить Private Connectivity Configuration в Datastream, которая устанавливает VPC Peering между сетью Datastream и пользовательским VPC, где находятся PSC эндпоинты.10

Это создает цепочку: Datastream -> VPC Peering -> User VPC -> PSC Endpoint -> MongoDB Atlas.

Для корректного разрешения имен в этой схеме может потребоваться настройка Cloud DNS с частными зонами, которые мапят доменные имена Atlas (полученные из SRV записи) на внутренние IP-адреса PSC эндпоинтов.41

Если настройка DNS невозможна или слишком сложна, использование промежуточного прокси-сервера (Nginx) внутри пользовательского VPC становится идеальным связующим звеном, упрощая схему адресации для Datastream до одного IP-адреса прокси.

## **7. Заключение**

Интеграция Datastream и MongoDB Atlas требует отказа от устаревших парадигм администрирования, таких как SSH-туннели (S⌖3), в пользу облачно-нативных паттернов проектирования сети (S⌖4).

Несмотря на кажущуюся сложность настройки проксирующих узлов или Private Service Connect, эти инвестиции времени многократно окупаются предсказуемостью поведения системы, безопасностью данных и возможностью линейного масштабирования.

Риски возникновения «TCP meltdown», проблемы с TLS-сертификатами и невозможность корректной обработки смены мастера в кластере делают стратегию S⌖3 непригодной для критически важных промышленных нагрузок.

Рекомендуется использовать стратегию S⌖4 как стандарт де-факто для продуктивных сред, комбинируя возможности Private Service Connect для сетевой изоляции и L4 проксирование (Nginx) для адаптации протоколов и управления сертификатами.

Такой подход обеспечивает надежный фундамент для построения аналитических платформ реального времени, минимизируя технический долг и операционные риски.

#### **Works cited**

1. Diagnose issues | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/diagnose-issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues)  
2. What is Datastream? | Google Cloud Blog, accessed December 8, 2025, [https://cloud.google.com/blog/topics/developers-practitioners/all-you-need-know-about-datastream](https://cloud.google.com/blog/topics/developers-practitioners/all-you-need-know-about-datastream)  
3. Are there disadvantages in SSH tunneling? - Unix & Linux Stack Exchange, accessed December 8, 2025, [https://unix.stackexchange.com/questions/34499/are-there-disadvantages-in-ssh-tunneling](https://unix.stackexchange.com/questions/34499/are-there-disadvantages-in-ssh-tunneling)  
4. What is TCP-over-TCP and how does OpenVPN under TCP mode avoid the issue? - Server Fault, accessed December 8, 2025, [https://serverfault.com/questions/1045786/what-is-tcp-over-tcp-and-how-does-openvpn-under-tcp-mode-avoid-the-issue](https://serverfault.com/questions/1045786/what-is-tcp-over-tcp-and-how-does-openvpn-under-tcp-mode-avoid-the-issue)  
5. Power of SSH Tunneling : r/programming - Reddit, accessed December 8, 2025, [https://www.reddit.com/r/programming/comments/bb73jo/power_of_ssh_tunneling/](https://www.reddit.com/r/programming/comments/bb73jo/power_of_ssh_tunneling/)  
6. Connecting to MongoDB Atlas cluster using nginx proxy, accessed December 8, 2025, [https://www.mongodb.com/community/forums/t/connecting-to-mongodb-atlas-cluster-using-nginx-proxy/303998](https://www.mongodb.com/community/forums/t/connecting-to-mongodb-atlas-cluster-using-nginx-proxy/303998)  
7. Connection String Options - Database Manual - MongoDB Docs, accessed December 8, 2025, [https://www.mongodb.com/docs/manual/reference/connection-string-options/](https://www.mongodb.com/docs/manual/reference/connection-string-options/)  
8. Configure a MongoDB database for CDC | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/configure-mongodb](https://docs.cloud.google.com/datastream/docs/configure-mongodb)  
9. Create connection profiles | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/create-connection-profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles)  
10. Create a private connectivity configuration | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration)  
11. Enabling High Performance Bulk Data Transfers With SSH - Pittsburgh Supercomputing Center, accessed December 8, 2025, [https://www.psc.edu/wp-content/uploads/2020/12/MG08-rapier-bennett.pdf](https://www.psc.edu/wp-content/uploads/2020/12/MG08-rapier-bennett.pdf)  
12. FAQ | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/faq](https://docs.cloud.google.com/datastream/docs/faq)  
13. Why TCP over TCP is a bad idea (2001) - Hacker News, accessed December 8, 2025, [https://news.ycombinator.com/item?id=25080693](https://news.ycombinator.com/item?id=25080693)  
14. Implementation and Performance Evaluation of TCP over QUIC Tunnels - arXiv, accessed December 8, 2025, [https://arxiv.org/html/2504.10054v2](https://arxiv.org/html/2504.10054v2)  
15. SSH File Transfer Protocol (SFTP) performance considerations in Azure Blob storage, accessed December 8, 2025, [https://learn.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-performance](https://learn.microsoft.com/en-us/azure/storage/blobs/secure-file-transfer-protocol-performance)  
16. Optimizing SSH for High-Volume Environments - DEV Community, accessed December 8, 2025, [https://dev.to/sebos/optimizing-ssh-for-high-volume-environments-5hfh](https://dev.to/sebos/optimizing-ssh-for-high-volume-environments-5hfh)  
17. DATASTREAM MYSQL HIGH LATENCY - Data Analytics - Google Developer forums, accessed December 8, 2025, [https://discuss.google.dev/t/datastream-mysql-high-latency/157499](https://discuss.google.dev/t/datastream-mysql-high-latency/157499)  
18. SSH to remote hosts through a proxy or bastion with ProxyJump - Red Hat, accessed December 8, 2025, [https://www.redhat.com/en/blog/ssh-proxy-bastion-proxyjump](https://www.redhat.com/en/blog/ssh-proxy-bastion-proxyjump)  
19. Forward SSH tunnel | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/ssh-tunnel](https://docs.cloud.google.com/datastream/docs/ssh-tunnel)  
20. Module ngx_stream_proxy_module - nginx, accessed December 8, 2025, [https://nginx.org/en/docs/stream/ngx_stream_proxy_module.html](https://nginx.org/en/docs/stream/ngx_stream_proxy_module.html)  
21. NGINX vs. HAProxy: Comparing Features and Use Cases | OpenLogic, accessed December 8, 2025, [https://www.openlogic.com/blog/nginx-vs-haproxy](https://www.openlogic.com/blog/nginx-vs-haproxy)  
22. HAProxy vs NGINX | How to Choose the Best One in 2025? | by Ecosmob Technologies, accessed December 8, 2025, [https://medium.com/@ecosmobtechnologies/haproxy-vs-nginx-how-to-choose-the-best-one-in-2025-c055a80de0ab](https://medium.com/@ecosmobtechnologies/haproxy-vs-nginx-how-to-choose-the-best-one-in-2025-c055a80de0ab)  
23. How to setup MongoDB behind Nginx Reverse Proxy [closed] - Stack Overflow, accessed December 8, 2025, [https://stackoverflow.com/questions/31853755/how-to-setup-mongodb-behind-nginx-reverse-proxy](https://stackoverflow.com/questions/31853755/how-to-setup-mongodb-behind-nginx-reverse-proxy)  
24. Announcing Google Private Service Connect (PSC) Integration for MongoDB Atlas, accessed December 8, 2025, [https://www.mongodb.com/blog/post/announcing-google-private-service-connect-psc-integration-mongodb-atlas?hmsr=joyk.com&utm_source=joyk.com&utm_medium=referral](https://www.mongodb.com/blog/post/announcing-google-private-service-connect-psc-integration-mongodb-atlas?hmsr=joyk.com&utm_source=joyk.com&utm_medium=referral)  
25. Private Service Connect Features and Benefits | Google Cloud, accessed December 8, 2025, [https://cloud.google.com/private-service-connect](https://cloud.google.com/private-service-connect)  
26. Announcing Google Private Service Connect (PSC) Integration for MongoDB Atlas, accessed December 8, 2025, [https://www.mongodb.com/company/blog/product-release-announcements/announcing-google-private-service-connect-psc-integration-mongodb-atlas](https://www.mongodb.com/company/blog/product-release-announcements/announcing-google-private-service-connect-psc-integration-mongodb-atlas)  
27. Module ngx_http_proxy_module - nginx, accessed December 8, 2025, [https://nginx.org/en/docs/http/ngx_http_proxy_module.html](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)  
28. nginx as reverse proxy with upstream SSL - Server Fault, accessed December 8, 2025, [https://serverfault.com/questions/341023/nginx-as-reverse-proxy-with-upstream-ssl](https://serverfault.com/questions/341023/nginx-as-reverse-proxy-with-upstream-ssl)  
29. MongoDB behind Nginx Reverse Proxy Manager : r/selfhosted - Reddit, accessed December 8, 2025, [https://www.reddit.com/r/selfhosted/comments/1ctr6zx/mongodb_behind_nginx_reverse_proxy_manager/](https://www.reddit.com/r/selfhosted/comments/1ctr6zx/mongodb_behind_nginx_reverse_proxy_manager/)  
30. Learn About Private Endpoints in Atlas - Atlas - MongoDB Docs, accessed December 8, 2025, [https://www.mongodb.com/docs/atlas/security-private-endpoint/](https://www.mongodb.com/docs/atlas/security-private-endpoint/)  
31. Guidance for Atlas Network Security - Atlas Architecture Center - MongoDB Docs, accessed December 8, 2025, [https://www.mongodb.com/docs/atlas/architecture/current/network-security/](https://www.mongodb.com/docs/atlas/architecture/current/network-security/)  
32. Network connectivity methods | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/network-connectivity-options](https://docs.cloud.google.com/datastream/docs/network-connectivity-options)  
33. Amazon DocumentDB: how it works, accessed December 8, 2025, [https://docs.aws.amazon.com/documentdb/latest/developerguide/how-it-works.html](https://docs.aws.amazon.com/documentdb/latest/developerguide/how-it-works.html)  
34. Guidance for Atlas High Availability - Atlas Architecture Center - MongoDB Docs, accessed December 8, 2025, [https://www.mongodb.com/docs/atlas/architecture/current/high-availability/](https://www.mongodb.com/docs/atlas/architecture/current/high-availability/)  
35. Stream data from MongoDB databases | Datastream - Google Cloud Documentation, accessed December 8, 2025, [https://docs.cloud.google.com/datastream/docs/sources-mongodb](https://docs.cloud.google.com/datastream/docs/sources-mongodb)  
36. Change Streams - Database Manual - MongoDB Docs, accessed December 8, 2025, [https://www.mongodb.com/docs/manual/changestreams/](https://www.mongodb.com/docs/manual/changestreams/)  
37. Test Primary Failover - Atlas - MongoDB Docs, accessed December 8, 2025, [https://www.mongodb.com/docs/atlas/tutorial/test-resilience/test-primary-failover/](https://www.mongodb.com/docs/atlas/tutorial/test-resilience/test-primary-failover/)  
38. How to Build and Deploy a Security-Hardened SSH Bastion Host - Reddit, accessed December 8, 2025, [https://www.reddit.com/r/linuxadmin/comments/s36hfh/ssh_bastion_host_best_practices_how_to_build_and/](https://www.reddit.com/r/linuxadmin/comments/s36hfh/ssh_bastion_host_best_practices_how_to_build_and/)  
39. Set up and troubleshoot AWS IoT Greengrass with client devices, accessed December 8, 2025, [https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-and-troubleshoot-aws-iot-greengrass-with-client-devices.html)  
40. Stream logs to a custom HTTPS endpoint - Akamai TechDocs, accessed December 8, 2025, [https://techdocs.akamai.com/datastream2/docs/stream-custom-https](https://techdocs.akamai.com/datastream2/docs/stream-custom-https)  
41. Atlas Mongo <-> GCP private connectivity using PSC, is this the best option?, accessed December 8, 2025, [https://discuss.google.dev/t/atlas-mongo-gcp-private-connectivity-using-psc-is-this-the-best-option/188902](https://discuss.google.dev/t/atlas-mongo-gcp-private-connectivity-using-psc-is-this-the-best-option/188902)  
42. ESP32 - ESP-IDF Programming Guide - Technical Documents, accessed December 8, 2025, [https://docs.espressif.com/projects/esp-idf/en/v5.1.1/esp32/esp-idf-en-v5.1.1-esp32.pdf](https://docs.espressif.com/projects/esp-idf/en/v5.1.1/esp32/esp-idf-en-v5.1.1-esp32.pdf)  
43. TLS/SSL server authentication - Progress Documentation, accessed December 8, 2025, [https://docs.progress.com/bundle/datadirect-microsoft-sql-server-odbc-80/page/TLSSSL-server-authentication_2.html](https://docs.progress.com/bundle/datadirect-microsoft-sql-server-odbc-80/page/TLSSSL-server-authentication_2.html)  
44. Example: Private connectivity for a MongoDB Atlas cluster | Integration Connectors, accessed December 8, 2025, [https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb)