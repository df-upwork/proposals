https://gemini.google.com/share/1f7241368697


## **Введение: Архитектурная парадигма и проблема "Враждебного посредника"**

Современный ландшафт домашнего интернета в Соединенных Штатах претерпевает фундаментальные изменения, обусловленные переходом от проводных технологий (DOCSIS, оптоволокно) к решениям фиксированного беспроводного доступа (Fixed Wireless Access, FWA), лидером среди которых является T-Mobile Home Internet (TMHI). Данный сдвиг, обеспечивая высокую доступность широкополосного доступа, вносит существенные ограничения в архитектуру сетевого взаимодействия "клиент-сервер", нарушая классический принцип end-to-end связности. Центральной проблемой для инженеров, системных администраторов и энтузиастов self-hosting является использование оператором T-Mobile агрессивного механизма трансляции сетевых адресов операторского уровня (Carrier-Grade NAT или CGNAT) в сочетании с переходом на нативную инфраструктуру IPv6.1

В отличие от традиционных провайдеров, предоставляющих (пусть и динамический) публичный IPv4-адрес, архитектура T-Mobile построена на стеке 464XLAT. Это означает, что пользовательское оборудование (шлюз 5G) не имеет маршрутизируемого IPv4-адреса. Вместо этого трафик инкапсулируется на уровне абонентского устройства (CLAT - Customer-side Translator) в IPv6-пакеты, передается через ядро сети и деинкапсулируется на шлюзе оператора (PLAT - Provider-side Translator). Данный процесс не только делает невозможным классический проброс портов (port forwarding), но и вносит накладные расходы на инкапсуляцию, уменьшая эффективный размер блока передачи данных (MTU), что приводит к фрагментации пакетов и нестабильности VPN-соединений.3

Более того, сетевая политика T-Mobile характеризуется активным вмешательством в пользовательский трафик. Наблюдаются признаки использования Deep Packet Inspection (DPI) для троттлинга неопознанного UDP-трафика, сброс TCP-соединений (RST injection) для долгоживущих сессий и блокировка популярных портов VPN при активации фильтров "Web Guard".5 Ситуация осложняется юридическими рисками: условия обслуживания (Terms of Service) прямо запрещают использование потребительских тарифов для "эксплуатации серверов", создавая угрозу терминации обслуживания.8

В данном отчете представлен исчерпывающий анализ трех основных стратегий обхода этих ограничений: **Cloudflare Tunnel**, **Tailscale (Mesh VPN)** и **VPS Relay (WireGuard)**. Оценка производится на основе технических метрик (пропускная способность, задержка, устойчивость к MTU), пользовательского опыта и юридической безопасности.

---

## **1. Cloudflare Tunnel (Argo): Парадигма нулевого доверия и CDN-прокси**

### **Сущность технологии и архитектурная интеграция**

Cloudflare Tunnel (ранее известный как Argo Tunnel) представляет собой радикальный отход от традиционных методов VPN. Вместо попыток "пробить" NAT для входящих соединений, данное решение использует легковесный демон cloudflared, устанавливаемый на сервере внутри локальной сети пользователя. Демон инициирует зашифрованные исходящие соединения (обычно по протоколу HTTP/2 или QUIC) к ближайшим граничным центрам обработки данных (Edge Data Centers) глобальной сети Cloudflare.10

Такая архитектура делает шлюз T-Mobile "прозрачным": с точки зрения оператора, трафик туннеля выглядит как обычная исходящая веб-активность по порту 443, что крайне затрудняет его блокировку методами DPI без нарушения работы легитимных веб-сервисов. Входящие запросы от внешних клиентов поступают на публичный IP-адрес Cloudflare, проходят через систему защиты от DDoS и WAF (Web Application Firewall), а затем маршрутизируются через установленный туннель к локальному серверу пользователя.10

### **Оценка эффективности: 68/100**

### **Достоинства: Безопасность и простота развертывания**

1. **Обход входящих ограничений:** Поскольку туннель инициируется изнутри сети, он полностью игнорирует блокировку входящих портов на шлюзах T-Mobile и отсутствие публичного IP-адреса. Это устраняет необходимость в настройке DMZ или сложных правил NAT на роутере.10  
2. **Интеграция с Zero Trust Security:** Решение предоставляет встроенные механизмы аутентификации (Cloudflare Access), позволяя закрыть домашние сервисы за страницей входа с поддержкой SSO (Single Sign-On), что критически важно при публикации уязвимых панелей управления в открытый интернет. Пользователь получает защиту корпоративного уровня бесплатно.12  
3. **Глобальная маршрутизация Anycast:** Трафик клиента направляется к ближайшему узлу Cloudflare, что может частично компенсировать задержки, вносимые мобильной сетью, за счет оптимизации маршрута в магистральной сети интернета.  
4. **Скрытие топологии:** Реальный IP-адрес пользователя (даже если он динамический или за CGNAT) остается скрытым от внешнего мира, так как DNS-записи указывают на прокси-серверы Cloudflare.

### **Недостатки: Юридическая неопределенность и ограничения контента**

Фундаментальная проблема Cloudflare Tunnel заключается в конфликте между техническими возможностями и правилами использования сервиса.

1. **Нарушение Terms of Service (Секция 2.8 и не-HTML контент):** Исторически, Секция 2.8 пользовательского соглашения Cloudflare запрещала использование CDN для передачи "непропорционального количества не-HTML контента" (видео, аудио, бинарные файлы). Хотя в 2023 году формулировки были смягчены и перенесены в специфические условия для CDN, передача потокового видео (например, через Plex или Jellyfin) через бесплатный туннель остается в "серой зоне".13 Пользователи регулярно сообщают о блокировках аккаунтов или доменов при попытке прокачать терабайты медиа-трафика через туннель, так как это создает нагрузку на инфраструктуру Cloudflare без монетизации.12  
2. **Технические лимиты протокола:** Cloudflare Tunnel оптимизирован для веб-трафика (HTTP/HTTPS). Инкапсуляция потоковых данных (например, TCP-потоков Plex) в HTTP-запросы вносит дополнительные накладные расходы и задержки. Пользователи отмечают буферизацию при просмотре контента с высоким битрейтом, особенно в часы пиковой нагрузки на мобильную сеть T-Mobile.16  
3. **Отсутствие сквозного шифрования (Man-in-the-Middle):** Для обеспечения функций защиты (WAF, кэширование) Cloudflare должен расшифровывать трафик на своих серверах (SSL termination). Это означает, что теоретически провайдер услуги имеет доступ к незашифрованным данным пользователя, что неприемлемо для конфиденциальных задач.17  
4. **Зависимость от состояния аккаунта:** В случае автоматической блокировки аккаунта Cloudflare за нарушение политик (которое может быть определено алгоритмически), пользователь мгновенно теряет доступ ко всей своей инфраструктуре, без возможности оперативного восстановления.

---

## **2. Tailscale (Mesh VPN): Проблема симметричного NAT и производительность DERP**

### **Сущность технологии и механизмы NAT Traversal**

Tailscale представляет собой оверлейную сеть, построенную на базе протокола WireGuard, которая абстрагирует сложность настройки ключей и маршрутов. Ключевой особенностью является использование продвинутых алгоритмов NAT Traversal (STUN, ICE), направленных на установление прямого пирингового соединения (P2P) между устройствами, находящимися за разными NAT.18

В идеальном сценарии Tailscale "пробивает" NAT (UDP Hole Punching), создавая прямой зашифрованный канал. Однако в сетях T-Mobile Home Internet используется так называемый "Симметричный NAT" (Symmetric NAT) с рандомизацией портов, что делает предсказание порта для входящего соединения крайне сложным. Если прямое соединение установить не удается, трафик перенаправляется через глобальную сеть ретрансляторов DERP (Designated Encrypted Relay for Packets).18

### **Оценка эффективности: 82/100**

### **Достоинства: Экосистема и удобство управления**

1. **MagicDNS и Subnet Routers:** Функция MagicDNS позволяет обращаться к устройствам по именам, устраняя необходимость запоминания IP-адресов. Функция "Subnet Router" позволяет одному устройству (например, Raspberry Pi или NAS), подключенному к Tailscale, предоставлять доступ ко всей домашней локальной сети (LAN) для удаленных клиентов, работая как шлюз. Это избавляет от необходимости устанавливать клиент Tailscale на каждое устройство.21  
2. **Автоматическое управление MTU:** Клиент Tailscale пытается автоматически адаптировать размер пакета под параметры сети, что частично решает проблему фрагментации в сети T-Mobile, хотя и не всегда идеально.4  
3. **Устойчивость к смене IP:** В условиях мобильной сети, где внешний IP-адрес шлюза может меняться динамически, Tailscale автоматически обновляет карту сети (network map), восстанавливая связность без вмешательства пользователя.

### **Недостатки: Падение производительности в режиме Relay**

Главным техническим препятствием для пользователей T-Mobile является высокая вероятность невозможности установления прямого соединения.

1. **Деградация скорости через DERP:** Когда прямой канал невозможен из-за двойного NAT/CGNAT, трафик идет через публичные серверы DERP. Эти серверы, предоставляемые бесплатно, имеют жесткие ограничения по пропускной способности. Пользователи T-Mobile сообщают о падении скорости загрузки с 100+ Мбит/с (напрямую) до 10-20 Мбит/с при работе через релей.22 Это делает невозможной передачу тяжелых файлов или потокового видео высокого качества.  
2. **Увеличение задержек (Latency):** Использование режима "Exit Node" (выходной узел) через домашний интернет T-Mobile приводит к двойному лагу: сначала пакет идет от мобильного клиента до домашнего сервера (часто через DERP), а затем от сервера в интернет через сеть T-Mobile. Задержки могут возрастать с 30-50 мс до 100-150 мс, делая интерактивные приложения (SSH, RDP, игры) некомфортными.21  
3. **Протокольные накладные расходы (TCP over UDP over TCP):** Протокол DERP инкапсулирует UDP-трафик WireGuard в HTTPS (TCP) для прохождения через строгие брандмауэры. Это создает классическую проблему "TCP over TCP meltdown", когда механизмы контроля перегрузки на разных уровнях конфликтуют друг с другом, приводя к нестабильности соединения при потере пакетов в радиоэфире.22

---

## **3. VPS Relay (WireGuard): "Золотой стандарт" технического контроля**

### **Сущность технологии и архитектура**

Данный метод предполагает создание собственной инфраструктуры ретрансляции. Пользователь арендует дешевый виртуальный сервер (VPS) с "белым" статическим IP-адресом. Домашний роутер или сервер (за T-Mobile NAT) устанавливает постоянное исходящее соединение WireGuard с этим VPS. VPS настраивается для перенаправления (iptables NAT/Masquerade) входящего трафика из интернета в установленный туннель к домашнему серверу.24

### **Оценка эффективности: 94/100**

### **Достоинства: Полный контроль над сетевым стеком**

1. **Решение проблемы MTU и фрагментации:** Это единственное решение, позволяющее администратору жестко задать параметры MTU и MSS (Maximum Segment Size). Для стабильной работы в сети T-Mobile с 464XLAT критически важно установить MTU интерфейса WireGuard в значение **1280 байт** (минимальное для IPv6). Это гарантирует, что пакеты с заголовками WireGuard (80 байт) пройдут через узкий канал T-Mobile (обычно ~1400-1420 байт) без фрагментации.4 Без этой настройки пользователи сталкиваются с ситуацией, когда соединение установлено, но веб-страницы не грузятся.  
2. **Обход блокировок через PersistentKeepalive:** Настройка параметра PersistentKeepalive = 25 (или даже 15 секунд для некоторых регионов) заставляет WireGuard отправлять пустые пакеты каждые 25 секунд. Это предотвращает закрытие UDP-сессии агрессивным тайм-аутом NAT-таблицы на оборудовании T-Mobile, обеспечивая постоянную доступность туннеля.24  
3. **Высокая производительность:** В отличие от перегруженных публичных релеев Tailscale, частный VPS обеспечивает пропускную способность, ограниченную только шириной канала самого VPS (обычно 1-10 Гбит/с) и скоростью T-Mobile. Это позволяет утилизировать 100% доступной скорости 5G-соединения.28  
4. **Устойчивость к DPI:** Возможность запуска WireGuard на нестандартных портах (например, 443 UDP) или использование обфускации (Shadowsocks-Plugin, UDP2RAW) позволяет скрыть факт использования VPN от систем анализа трафика оператора, снижая риск троттлинга.6

### **Недостатки: Сложность и стоимость**

1. **Требования к квалификации:** Реализация требует знаний Linux, настройки iptables, маршрутизации и безопасности сервера. Ошибка в конфигурации PostUp/PostDown скриптов может привести к полной потере доступа.  
2. **Финансовые затраты:** В отличие от бесплатных тарифов Cloudflare и Tailscale, аренда VPS требует ежемесячных расходов ($3-6/мес).  
3. **Проблемы с "Web Guard":** Исследования показывают, что услуга "Web Guard" от T-Mobile, часто включенная по умолчанию, может блокировать протоколы туннелирования. Для корректной работы VPS Relay необходимо явно отключить эту услугу в личном кабинете абонента.7

---

## **4. Сравнительный анализ и технические данные**

Ниже представлена сводная таблица характеристик рассматриваемых решений в контексте использования в сети T-Mobile Home Internet.

| Параметр | VPS Relay (WireGuard Custom) | Tailscale (DERP/Direct) | Cloudflare Tunnel |
| :---- | :---- | :---- | :---- |
| **Оценка эксперта** | **94/100** | **82/100** | **68/100** |
| **Максимальная пропускная способность** | Высокая (лимит канала T-Mobile) | Низкая (10-20 Мбит/с через релей) | Средняя (хорошо для Web, плохо для видео) |
| **Задержка (Latency)** | Минимальная добавочная | Высокая (при использовании DERP) | Зависит от маршрутизации Anycast |
| **Устойчивость к проблемам MTU** | **Полная** (при ручной настройке 1280) | Частичная (авто-согласование) | Полная (TCP-инкапсуляция) |
| **Риск блокировки аккаунта** | Низкий | Низкий | **Высокий** (при потоковом видео) |
| **Сложность настройки** | Высокая (Linux, Iptables) | Низкая (App-based) | Средняя (CLI Daemon) |
| **Пригодность для Plex/Media** | Отличная | Плохая (буферизация) | Не рекомендуется (нарушение ToS) |
| **Требует "белого" IP на стороне клиента** | Нет | Нет | Нет |

### **Влияние MTU на стабильность соединения**

Технический анализ форумов и документации выявляет критическую зависимость стабильности от настроек MTU. Стандартный MTU Ethernet составляет 1500 байт. Однако в сети T-Mobile из-за заголовков IPv6 и 464XLAT реальный MTU снижается до значений порядка 1400-1420 байт. WireGuard добавляет свои заголовки. Если отправить пакет размером 1500 байт, он будет фрагментирован или отброшен (Black Hole).

Эмпирические данные пользователей 4 подтверждают, что установка MTU в значение **1280** (нижняя граница стандарта IPv6) устраняет 99% проблем с "зависанием" соединений и недоступностью веб-сайтов через VPN. Для Cloudflare Tunnel эта проблема менее актуальна, так как он работает на прикладном уровне (L7) и использует TCP, который автоматически сегментирует данные, однако это вносит задержки из-за механизма подтверждения доставки TCP (ACK) в нестабильной радио-среде.

---

## **5. Юридический анализ: Риски нарушения Terms of Service**

Критически важным аспектом, который часто игнорируется в технических руководствах, является юридическая сторона вопроса. Политика допустимого использования (Acceptable Use Policy - AUP) T-Mobile содержит явные ограничения.

### **Запрет на серверные функции**

Документы прямо запрещают использование мобильного интернета для "эксплуатации серверов" (operating servers).8 Это понятие трактуется широко и включает в себя любой трафик, инициируемый извне сети к устройству абонента. Технически, использование Cloudflare Tunnel или VPS Relay маскирует серверный трафик под "исходящее соединение", что затрудняет автоматическое обнаружение нарушения. Однако, анализ профиля трафика (постоянный высокий исходящий поток, симметрия загрузки/выгрузки) может выдать наличие сервера.

### **Запрет на "Keep-Alive" и автоматизацию**

Секция AUP запрещает использование механизмов, поддерживающих непрерывное соединение при отсутствии активности пользователя ("keep-alive functions").9 Это находится в прямом конфликте с рекомендацией использовать PersistentKeepalive = 25 в WireGuard для поддержания стабильности туннеля. Формально, любой постоянно активный VPN-туннель является нарушением этого пункта.

### **Реальные риски и прецеденты**

Несмотря на строгость формулировок, массовых блокировок пользователей за умеренное личное использование (Self-hosting для личных нужд) не наблюдается. Основным инструментом воздействия оператора является **деприоритизация** (снижение скорости в часы пик) и **троттлинг** определенных протоколов (UDP), а не отключение услуги. Тем не менее, использование сети для коммерческого хостинга или публичного раздачи контента несет высокий риск терминации контракта. Бизнес-тарифы T-Mobile (Business Internet) с опцией статического IP являются единственным полностью легитимным способом обхода этих ограничений, так как их условия допускают работу серверов.1

---

## **6. Заключение и стратегические рекомендации**

Для технического специалиста, столкнувшегося с ограничениями T-Mobile Home Internet, выбор решения зависит от баланса между производительностью, стоимостью и допустимым уровнем сложности.

1. **Для максимальной производительности (Plex, большие файлы):** Единственным жизнеспособным решением является **VPS Relay на базе WireGuard**. Необходимо использовать VPS в географической близости к пользователю, настроить MTU = 1280, PersistentKeepalive = 25 и, при необходимости, применить MSS Clamping на уровне iptables. Это обеспечивает полный контроль и максимальную скорость.  
2. **Для управления "умным домом" и легкого доступа:** **Tailscale** является идеальным выбором благодаря простоте настройки. Рекомендуется установить Tailscale на устройстве, подключенном проводом к роутеру (например, Raspberry Pi), и использовать его как Subnet Router. Следует быть готовым к снижению скорости, если прямое соединение не установится.  
3. **Для веб-сервисов (Home Assistant, Nextcloud):** **Cloudflare Tunnel** предоставляет удобный доступ через браузер с дополнительным слоем защиты. Однако следует категорически избегать его использования для потокового видео во избежание блокировки аккаунта.

Пользователи должны осознавать, что архитектура T-Mobile Home Internet (FWA/CGNAT) фундаментально враждебна к серверным приложениям. Любое решение является "костылем" (workaround), эффективность которого может измениться при обновлении сетевых политик оператора.

#### **Works cited**

1. Guide to using Tailscale (Port-forwarding) for dummies? : r/tmobileisp - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/tmobileisp/comments/11l8c25/guide_to_using_tailscale_portforwarding_for/](https://www.reddit.com/r/tmobileisp/comments/11l8c25/guide_to_using_tailscale_portforwarding_for/)  
2. Wireguard server on T-Mobile Home Internet : r/HomeNetworking - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/HomeNetworking/comments/1jatg1s/wireguard_server_on_tmobile_home_internet/](https://www.reddit.com/r/HomeNetworking/comments/1jatg1s/wireguard_server_on_tmobile_home_internet/)  
3. WIRELESS NETWORK NEUTRALITY: TECHNOLOGICAL CHALLENGES AND POLICY IMPLICATIONS - Penn Carey Law: Legal Scholarship Repository, accessed November 25, 2025, [https://scholarship.law.upenn.edu/cgi/viewcontent.cgi?article=1496&context=faculty_scholarship](https://scholarship.law.upenn.edu/cgi/viewcontent.cgi?article=1496&context=faculty_scholarship)  
4. T-Mobile 5G Internet, WireGuard, and MTU : r/tmobileisp - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/tmobileisp/comments/1mbsiia/tmobile_5g_internet_wireguard_and_mtu/](https://www.reddit.com/r/tmobileisp/comments/1mbsiia/tmobile_5g_internet_wireguard_and_mtu/)  
5. UDP is throttled to about 100 kbps on T-Mobile. Wireguard won't work and TCP bas... | Hacker News, accessed November 25, 2025, [https://news.ycombinator.com/item?id=29585541](https://news.ycombinator.com/item?id=29585541)  
6. T-mobile seems to be throttling my VPN connection, tried port 443. Alternatives? Obfuscation? - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/VPN/comments/l9p5l6/tmobile_seems_to_be_throttling_my_vpn_connection/](https://www.reddit.com/r/VPN/comments/l9p5l6/tmobile_seems_to_be_throttling_my_vpn_connection/)  
7. Wireguard Works on WiFi; not on Cellular : r/opnsense - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/opnsense/comments/1j4wjod/wireguard_works_on_wifi_not_on_cellular/](https://www.reddit.com/r/opnsense/comments/1j4wjod/wireguard_works_on_wifi_not_on_cellular/)  
8. Plan Terms & Conditions - Mint Mobile, accessed November 25, 2025, [https://www.mintmobile.com/plan-terms-and-conditions/](https://www.mintmobile.com/plan-terms-and-conditions/)  
9. UM 1652, OTHER FILING/PLEADING, 10/15/2013 - Public Utility Commission, accessed November 25, 2025, [https://edocs.puc.state.or.us/efdocs/HAH/um1652hah155836.pdf](https://edocs.puc.state.or.us/efdocs/HAH/um1652hah155836.pdf)  
10. How to set up free, secure, high-quality remote access for Plex - mythofechelon, accessed November 25, 2025, [https://mythofechelon.co.uk/blog/2024/1/7/how-to-set-up-free-secure-high-quality-remote-access-for-plex](https://mythofechelon.co.uk/blog/2024/1/7/how-to-set-up-free-secure-high-quality-remote-access-for-plex)  
11. Non-HTML Content via Argo Tunnels - Cloudflare Community, accessed November 25, 2025, [https://community.cloudflare.com/t/non-html-content-via-argo-tunnels/283160](https://community.cloudflare.com/t/non-html-content-via-argo-tunnels/283160)  
12. Recent Cloudflare tunnel users getting banned? : r/PleX - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/PleX/comments/1fc0f7y/recent_cloudflare_tunnel_users_getting_banned/](https://www.reddit.com/r/PleX/comments/1fc0f7y/recent_cloudflare_tunnel_users_getting_banned/)  
13. Cloudflare Self-Serve Subscription Agreement limitation gone? : r/selfhosted - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/selfhosted/comments/13wltjl/cloudflare_selfserve_subscription_agreement/](https://www.reddit.com/r/selfhosted/comments/13wltjl/cloudflare_selfserve_subscription_agreement/)  
14. Goodbye, section 2.8 and hello to Cloudflare's new terms of service, accessed November 25, 2025, [https://blog.cloudflare.com/updated-tos/](https://blog.cloudflare.com/updated-tos/)  
15. Can I use a Cloudflare Tunnel to make my Plex server available on my domain name? - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/PleX/comments/152wfdh/can_i_use_a_cloudflare_tunnel_to_make_my_plex/](https://www.reddit.com/r/PleX/comments/152wfdh/can_i_use_a_cloudflare_tunnel_to_make_my_plex/)  
16. VIDEO GUIDE -- Simple Cloudflare Tunnel Setup on Unraid for Beginners! - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/unRAID/comments/1apfc0j/video_guide_simple_cloudflare_tunnel_setup_on/](https://www.reddit.com/r/unRAID/comments/1apfc0j/video_guide_simple_cloudflare_tunnel_setup_on/)  
17. I wrote a guide on how to use Plex Media Server via Cloudflare Zero Trust Access Tunnels, accessed November 25, 2025, [https://www.reddit.com/r/selfhosted/comments/192p6pv/i_wrote_a_guide_on_how_to_use_plex_media_server/](https://www.reddit.com/r/selfhosted/comments/192p6pv/i_wrote_a_guide_on_how_to_use_plex_media_server/)  
18. Connection types · Tailscale Docs, accessed November 25, 2025, [https://tailscale.com/kb/1257/connection-types](https://tailscale.com/kb/1257/connection-types)  
19. How NAT traversal works - Tailscale, accessed November 25, 2025, [https://tailscale.com/blog/how-nat-traversal-works](https://tailscale.com/blog/how-nat-traversal-works)  
20. How Tailscale is improving NAT traversal (part 1), accessed November 25, 2025, [https://tailscale.com/blog/nat-traversal-improvements-pt-1](https://tailscale.com/blog/nat-traversal-improvements-pt-1)  
21. Is Slower Mobile Internet when using an Exit Node Expected? : r/Tailscale - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/Tailscale/comments/1gwuirg/is_slower_mobile_internet_when_using_an_exit_node/](https://www.reddit.com/r/Tailscale/comments/1gwuirg/is_slower_mobile_internet_when_using_an_exit_node/)  
22. Custom DERP question : r/Tailscale - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/Tailscale/comments/ypbgzs/custom_derp_question/](https://www.reddit.com/r/Tailscale/comments/ypbgzs/custom_derp_question/)  
23. T-Mobile Home Internet. Exit Nodes, & Derp : r/Tailscale - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/Tailscale/comments/1eplfy9/tmobile_home_internet_exit_nodes_derp/](https://www.reddit.com/r/Tailscale/comments/1eplfy9/tmobile_home_internet_exit_nodes_derp/)  
24. Increase wireguard speed VPN, to slow - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/WireGuard/comments/1itzwan/increase_wireguard_speed_vpn_to_slow/](https://www.reddit.com/r/WireGuard/comments/1itzwan/increase_wireguard_speed_vpn_to_slow/)  
25. How to improve tailscale relay speed - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/Tailscale/comments/1hgsg6m/how_to_improve_tailscale_relay_speed/](https://www.reddit.com/r/Tailscale/comments/1hgsg6m/how_to_improve_tailscale_relay_speed/)  
26. TCP MSS Value for WireGuard's UDP Configuration - GL.iNet Forum, accessed November 25, 2025, [https://forum.gl-inet.com/t/tcp-mss-value-for-wireguards-udp-configuration/31205](https://forum.gl-inet.com/t/tcp-mss-value-for-wireguards-udp-configuration/31205)  
27. Back Again with WireGuard Connection Issues (looking to connect with USM rep) : r/USMobile - Reddit, accessed November 25, 2025, [https://www.reddit.com/r/USMobile/comments/1ebudj5/back_again_with_wireguard_connection_issues/](https://www.reddit.com/r/USMobile/comments/1ebudj5/back_again_with_wireguard_connection_issues/)  
28. Streaming over wireguard VPN inconsistent, hardware issue or configuration (MTU?) issue?, accessed November 25, 2025, [https://www.reddit.com/r/WireGuard/comments/1otx6le/streaming_over_wireguard_vpn_inconsistent/](https://www.reddit.com/r/WireGuard/comments/1otx6le/streaming_over_wireguard_vpn_inconsistent/)  
29. Wireguard Optimal MTU - GitHub Gist, accessed November 25, 2025, [https://gist.github.com/nitred/f16850ca48c48c79bf422e90ee5b9d95](https://gist.github.com/nitred/f16850ca48c48c79bf422e90ee5b9d95)  
30. PLAN TERMS & CONDITIONS - LTE WIRELESS, accessed November 25, 2025, [https://ltewireless.com/plan-terms-and-conditions/](https://ltewireless.com/plan-terms-and-conditions/)