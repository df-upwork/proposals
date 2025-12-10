# 0.
Сегодня 2025-11-24.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021992670149716146110

## 2.2. Title
Network Specialist – Set Up Port Forwarding Workaround on T-Mobile Home Internet (IPv6 + CGNAT)

## 2.3. Description
`PD` ≔ 
```text
#
I’m looking for a networking expert who can help me set up a reliable workaround for opening incoming ports on a T-Mobile Home Internet modem, which currently blocks inbound connections due to:
- IPv6-only network
- Carrier-Grade NAT (CGNAT)

#
T-Mobile confirmed they cannot open ports, but they advised that port forwarding can be achieved using third-party solutions such as:
- SSL VPN
- WireGuard

# Scope of Work
- Recommend the best method to bypass CGNAT and enable stable inbound connections
- Set up and configure a working solution (SSL VPN, WireGuard, or another viable method)
- Optionally advise if Google Cloud, or similar cloud services, can be used as a relay, tunnel, or reverse proxy workaround
- Configure everything securely and test that external devices can connect to the required ports
- Provide instructions so I can manage it afterward

# Requirements
- Strong experience with networking, NAT traversal, and IPv6
- Experience with VPNs (WireGuard, SSL VPN, or similar)
- Familiarity with cloud networking (Google Cloud, AWS, etc.) is a plus
- Ability to explain options clearly and implement the best solution

# Deliverables
- Successfully opened / forwarded ports to my local device despite T-Mobile restrictions
- Fully working configuration (VPN tunnel, cloud relay, or other method)
- Documentation of the setup

# Additional Info
I already confirmed with T-Mobile support that they cannot open ports on their network, so this will require a workaround solution, not simple port forwarding through the modem.
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
Meriden

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
Manufacturing & Construction

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Mar 27, 2022
### 5.3.2. Hire rate (%)
100
### 5.3.3. Количество опубликованных проектов (jobs posted)
39
### 5.3.4. Total spent (USD)
21K
### 5.3.5. Количество оплаченных часов в почасовых проектах
615
### 5.3.6. Средняя почасовая ставка (USD)
29.51

# 6.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
- T-Mobile currently blocks inbound connections
- T-Mobile confirmed they cannot open ports
~~~
```

# 7.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
set up a reliable workaround for opening incoming ports on a T-Mobile Home Internet modem
~~~
```

# 8. Что беспокоит `ꆜ` (Aнализ №1, выполнен Gemini Deep Research)
https://gemini.google.com/share/58f709c276d1

## **1. Введение: Фундаментальная природа проблемы сетевой доступности**

В современной телекоммуникационной экосистеме наблюдается критический сдвиг парадигмы сетевой адресации, который наиболее ярко проявляется в инфраструктуре мобильных операторов и провайдеров фиксированного беспроводного доступа (FWA). Проект P⁎, инициированный клиентом ꆜ из сектора производства и строительства, обнажает фундаментальное противоречие между потребностями бизнеса в прямом удаленном доступе к локальным ресурсам и архитектурными ограничениями современных сетей IPv6-only, используемых такими операторами, как T-Mobile US.

Задача, поставленная в T⁎ — «set up a reliable workaround for opening incoming ports on a T-Mobile Home Internet modem» — не является тривиальной проблемой конфигурации клиентского оборудования. Она представляет собой столкновение с технологическим барьером Carrier-Grade NAT (CGNAT) и механизмами трансляции 464XLAT. Анализ ситуации требует деконструкции сетевой топологии провайдера, оценки рисков для бизнес-процессов клиента и разработки многоуровневой стратегии, варьирующейся от программных туннелей до смены класса обслуживания.

В данном отчете представлен исчерпывающий анализ проблемы P†, подтверждающий невозможность традиционного проброса портов, и детально разобраны три архитектурных подхода к решению: использование промежуточных ретрансляторов (VPS Relay), внедрение оверлейных сетей (Overlay Networks) и переход на бизнес-инфраструктуру со статическим адресом.

---

## **2. Деконструкция сетевой архитектуры T-Mobile Home Internet**

Понимание глубинных причин блокировки входящих соединений требует отказа от привычной модели IPv4-интернета. Сеть T-Mobile US представляет собой одну из самых масштабных в мире реализаций архитектуры IPv6-only, где поддержка устаревшего протокола IPv4 осуществляется исключительно через механизмы трансляции.

### **2.1. Технология 464XLAT и эрозия публичной адресации**

В отличие от классических сетей Dual Stack, где абонентскому оборудованию присваиваются нативные адреса обоих протоколов, T-Mobile использует архитектуру **464XLAT**, стандартизированную в RFC 6877.1 Эта архитектура была внедрена в ответ на исчерпание адресного пространства IPv4 и необходимость снижения капитальных затрат (CAPEX) на поддержание устаревшей инфраструктуры.

Система функционирует на базе двух ключевых компонентов трансляции, взаимодействие которых делает невозможным прямое входящее соединение по IPv4:

1. **CLAT (Customer-side Translator):** Этот модуль функционирует непосредственно на абонентском устройстве (CPE) или смартфоне. Он создает виртуальный сетевой интерфейс IPv4, перехватывает пакеты от приложений, не поддерживающих IPv6, и инкапсулирует их в IPv6-пакеты для передачи через ядро сети оператора. Важно отметить, что IPv4-адрес, назначаемый интерфейсу CLAT, является сугубо локальным (обычно из диапазона 192.0.0.0/29) и не маршрутизируется в глобальной сети.1  
2. **PLAT (Provider-side Translator):** Расположенный на границе ядра сети T-Mobile и публичного интернета, этот массивный шлюз выполняет функцию NAT64. Он декапсулирует трафик абонента и транслирует его в публичный IPv4-интерфейс для взаимодействия с внешними серверами.1

**Критический вывод для проекта P⁎:** В этой схеме у абонента физически отсутствует публичный IPv4-адрес. Весь трафик тысяч пользователей агрегируется на ограниченном пуле адресов шлюза PLAT. Традиционный Port Forwarding невозможен, так как шлюз PLAT не имеет механизма статического маппинга входящего порта глобального интернета на конкретный внутренний IPv6-адрес конкретного абонента. Запрос ꆜ на открытие портов через службу поддержки T-Mobile обречен на отказ не из-за нежелания оператора, а из-за архитектурной невозможности реализации такой функции в рамках массового сегмента обслуживания.5

### **2.2. Политика фильтрации трафика и ограничения IPv6**

Теоретически, наличие глобально маршрутизируемого IPv6-адреса (Global Unicast Address - GUA), который T-Mobile предоставляет каждому абоненту (обычно префикс /64), должно решать проблему доступности. Однако на практике ситуация осложняется политикой безопасности оператора.

Технический анализ подтверждает, что T-Mobile применяет жесткую политику блокировки **«нежелательного входящего трафика» (unsolicited inbound traffic)** на уровне своей сети.7 Брандмауэр оператора (Stateful Firewall) настроен таким образом, что разрешает прохождение пакетов внутрь сети только в том случае, если они являются ответом на исходящий запрос абонента (established/related connections).

Многочисленные тесты пользователей и сетевых инженеров показывают, что попытки инициировать новое соединение извне на IPv6-адрес абонентского шлюза блокируются. В редких случаях пропускаются ICMPv6 пакеты (ping), но TCP и UDP сессии на произвольные порты отбрасываются.9 Это означает, что даже при полной поддержке IPv6 на стороне оборудования клиента ꆜ, прямой доступ к серверам или оборудованию без дополнительных средств туннелирования невозможен.

### **2.3. Влияние CGNAT на промышленные протоколы**

Для клиента из сектора «Manufacturing & Construction», который, вероятно, использует специфическое ПО для мониторинга, ERP-системы или удаленный доступ к SCADA/CAD-рабочим станциям, среда CGNAT создает дополнительные риски:

* **Разрыв долгоживущих соединений:** Таблицы трансляции на шлюзах CGNAT имеют агрессивные тайм-ауты для TCP и UDP сессий для экономии памяти. Это приводит к частым разрывам соединений SSH, RDP или VPN, если не настроены механизмы keepalive.11  
* **Блокировка протоколов без состояния:** Протоколы, не устанавливающие явного соединения или использующие сложные схемы негоциации портов (например, SIP, IPsec без NAT-T, пассивный FTP), часто некорректно обрабатываются алгоритмами трансляции 464XLAT.1

Таким образом, проблема, описанная клиентом как «T-Mobile blocks inbound connections», является абсолютно обоснованной и требует внедрения решений, способных инкапсулировать входящий трафик внутри исходящего соединения, инициированного изнутри сети.

---

## **3. Стратегия I: Организация собственного шлюза (VPN Relay на VPS)**

Наиболее надежным, контролируемым и профессиональным решением («Reliable Workaround»), соответствующим требованиям бизнеса, является создание собственной инфраструктуры ретрансляции трафика. Данный подход позволяет полностью обойти ограничения CGNAT, получив статический публичный IP-адрес, не зависящий от провайдера интернета.

### **3.1. Архитектура решения WireGuard VPS Relay**

Суть метода заключается в использовании промежуточного сервера (Virtual Private Server — VPS), расположенного в дата-центре с полноценным публичным IPv4-адресом. Между локальным сервером клиента (за CGNAT) и VPS устанавливается постоянный VPN-туннель.

Техническая реализация базируется на протоколе **WireGuard**. Выбор WireGuard обусловлен его высокой производительностью, минимальным оверхедом заголовков (что критично в сетях с 464XLAT и потенциальной фрагментацией пакетов) и способностью быстро восстанавливать соединение при смене IP-адреса мобильного модема (Roaming/IP rotation).12

Поток трафика в данной схеме выглядит следующим образом:

1. Внешний клиент подключается к :[Порт X].  
2. VPS перенаправляет трафик через интерфейс WireGuard (wg0) на локальный IP туннеля.  
3. Трафик проходит через зашифрованный туннель, пробивая CGNAT T-Mobile как «исходящее» соединение.  
4. Локальный сервер клиента принимает запрос и отправляет ответ по тому же маршруту.

### **3.2. Сравнительный анализ провайдеров облачной инфраструктуры (VPS)**

Для бизнеса ꆜ выбор провайдера VPS имеет критическое значение, так как от этого зависят задержки (latency), стоимость трафика и стабильность канала. Анализ предложений на рынке выявляет существенные различия в ценообразовании и технических лимитах.

| Провайдер | Тарифный план | Стоимость / мес. | Лимит трафика (Egress) | Особенности сети и география | Рекомендация для ꆜ |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **AWS Lightsail** | Bundle (Linux) | $3.50 - $5.00 | 1 TB - 2 TB 14 | В большинстве регионов учитывается только исходящий трафик сверх нормы. Включает статический IP. | **Высокая.** Оптимальный баланс цены и качества сети Amazon. |
| **Google Cloud (GCP)** | e2-micro (Free Tier) | Бесплатно (условно) | 200 GB (Standard Tier) 16 | Premium Tier платный. Standard Tier имеет более высокие задержки. Сложная биллинговая схема. | **Низкая.** Риск непредвиденных расходов. Лимит 200GB мал для видео/VPN. |
| **Oracle Cloud** | Always Free | Бесплатно | 10 TB (Outbound) 18 | Процессоры ARM (Ampere). Сложности с регистрацией карт и доступностью инстансов. | **Средняя.** Лучшее предложение по трафику, но возможны проблемы с созданием аккаунта. |
| **DigitalOcean / Vultr** | Basic Droplet / Cloud Compute | $4.00 - $6.00 | 500 GB - 1 TB 19 | Простая тарификация. Наличие Marketplace с готовыми образами WireGuard.20 | **Высокая.** Идеально для быстрого развертывания ("One-click"). |
| **Linode (Akamai)** | Shared CPU | ~$5.00 | 1 TB 22 | Стабильная сеть, понятная документация по WireGuard. | **Высокая.** Аналогично DigitalOcean. |

**Анализ производительности:** Использование Google Cloud Free Tier может быть заманчивым, но следует учитывать, что сетевой уровень "Standard Tier" маршрутизирует трафик через публичный интернет ("cold potato routing"), что в сочетании с высокой латентностью сотовой сети T-Mobile может сделать RDP или VoIP сессии некомфортными.23 AWS Lightsail и Vultr предоставляют более предсказуемую сетевую связность.

### **3.3. Техническая реализация и настройка маршрутизации**

Для обеспечения надежности («reliable workaround»), конфигурация должна включать механизмы защиты от разрыва соединений, характерных для сотовых сетей.

#### **3.3.1. Конфигурация ядра и iptables**

На стороне VPS необходимо активировать форвардинг пакетов и настроить правила NAT. Это критический этап, так как без корректного маскарадинга (Masquerade) ответные пакеты от клиента могут потеряться.

**Настройка sysctl (VPS & Client):**

Bash

net.ipv4.ip_forward=1

Правила iptables для проброса порта (пример для порта 443):  
Сценарий требует перенаправления входящего трафика с интерфейса eth0 VPS на интерфейс wg0 (внутренний адрес клиента, например, 10.0.0.2).

Bash

### 1. Перенаправление входящего трафика (DNAT)  
iptables -t nat -A PREROUTING -d -p tcp --dport 443 -j DNAT --to-destination 10.0.0.2:443

### 2. Маскарадинг исходящего трафика (SNAT)  
Это гарантирует, что ответный трафик пойдет обратно через VPS, а не попытается уйти через шлюз T-Mobile напрямую  
```
iptables -t nat -A POSTROUTING -s 10.0.0.2 -j SNAT --to-source
```

### 3. Разрешение форвардинга  
```
iptables -A FORWARD -i eth0 -o wg0 -p tcp --syn --dport 443 -m conntrack --ctstate NEW -j ACCEPT  
iptables -A FORWARD -i eth0 -o wg0 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT  
iptables -A FORWARD -i wg0 -o eth0 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```

Источник данных для конфигурации:.11

#### **3.3.2. Борьба с таймаутами NAT (Persistent Keepalive)**

В сетях CGNAT таблицы трансляции сбрасываются очень быстро (иногда каждые 60-120 секунд бездействия). Для поддержания туннеля в активном состоянии в конфигурации WireGuard на стороне клиента (Peer) **обязательно** должен быть указан параметр PersistentKeepalive.

Рекомендуемое значение: **25 секунд**. Это значение меньше большинства стандартных таймаутов UDP в оборудовании CGNAT, что гарантирует сохранение "дыры" в NAT открытой.26

Ini, TOML

[Peer]  
PublicKey = <Server_Public_Key>  
Endpoint = <VPS_IP>:51820  
AllowedIPs = 0.0.0.0/0  
PersistentKeepalive = 25

---

## **4. Стратегия II: Оверлейные сети (Overlay Networks) и Mesh-VPN**

Для сценариев, где требуется доступ сотрудников к внутренним ресурсам, но не требуется публичный доступ для всего интернета, использование Mesh-VPN (Tailscale, ZeroTier) является более простым и масштабируемым решением. Эти технологии строят виртуальную сеть поверх существующей инфраструктуры, абстрагируясь от физической адресации.

### **4.1. Сравнительный анализ Tailscale и ZeroTier**

| Характеристика | Tailscale | ZeroTier | Анализ применимости для ꆜ |
| :---- | :---- | :---- | :---- |
| **Протокол** | WireGuard (User-space implementation) | Собственный проприетарный протокол (VL1/VL2) | Tailscale выигрывает за счет использования стандарта WireGuard, который показывает лучшую производительность и энергоэффективность.29 |
| **NAT Traversal** | Очень сильный (STUN, DERP relays) | Сильный, но иногда требует настройки роутера | Tailscale использует глобальную сеть DERP-серверов для ретрансляции трафика, если прямой P2P невозможен (что часто случается за CGNAT T-Mobile).31 |
| **Управление доступом** | ACLs, интеграция с Identity Providers (SSO) | Network controllers | Tailscale предлагает более гибкие политики безопасности (ACL), что важно для корпоративного применения.30 |
| **Простота** | "Zero Config", MagicDNS | Требует базового понимания SDN | Tailscale значительно проще в развертывании для не-сетевых инженеров. |

### **4.2. Аппаратное обеспечение: Проблема производительности шлюзов**

Поскольку клиент ꆜ не может установить VPN-агент на каждое промышленное устройство (станки, ПЛК, IP-камеры), необходимо использовать режим **Subnet Router** (маршрутизатор подсети). Выбранное устройство будет шлюзовать трафик из виртуальной сети Tailscale в физическую локальную сеть.32

Критически важно правильно выбрать аппаратную платформу для этого шлюза, так как шифрование трафика требует вычислительных ресурсов. Исследование бенчмарков показывает значительную разницу между популярными платформами:

* **Raspberry Pi 3B+:** Ограничена портом Ethernet 300 Мбит/с (через USB 2.0 шину) и слабым CPU. Реальная пропускная способность зашифрованного трафика часто не превышает 30-40 Мбит/с, что может быть недостаточно для видеопотоков.34  
* **Raspberry Pi 4 Model B:** Значительный скачок производительности. Гигабитный Ethernet и более мощный CPU позволяют достигать скоростей до 300-400 Мбит/с в режиме WireGuard.  
* **Raspberry Pi 5:** Благодаря архитектуре Cortex-A76 и криптографическим расширениям ARMv8, показывает прирост производительности в 2-3 раза по сравнению с Pi 4.35 Бенчмарки показывают возможность утилизации гигабитного канала.  
* **Mini PC (Intel N100/N5105):** Это наиболее предпочтительный вариант для бизнеса. Архитектура x86_64 с поддержкой инструкций AES-NI позволяет обрабатывать шифрованный трафик на скоростях, близких к линейной скорости провода (wire speed), при этом стоимость устройства сравнима с комплектом Raspberry Pi 5 + аксессуары.36

**Рекомендация:** Для проекта P⁎ рекомендуется использовать **Intel N100 Mini PC** или **Raspberry Pi 5** в качестве шлюза Subnet Router для исключения "бутылочного горлышка" при передаче данных.

### **4.3. Латентность и проблема DERP-серверов**

В сети T-Mobile US, находящейся за "Hard NAT", прямое соединение между узлами (UDP Hole Punching) часто не устанавливается. В этом случае Tailscale переключается на использование **DERP (Designated Encrypted Relay for Packets)** — ретрансляторов.

Это имеет два негативных последствия:

1. **Снижение пропускной способности:** Трафик идет через публичные сервера, которые могут быть перегружены. Пользователи сообщают о падении скорости до 10-15 Мбит/с при использовании релеев.37  
2. **Увеличение задержки:** Трафик делает "крюк" до дата-центра Tailscale и обратно. Для игровых или real-time приложений (управление оборудованием) это может быть критично. Тесты показывают рост пинга с 30-40 мс (Direct) до 100-120 мс (Relay).38

**Решение:** Развертывание собственного DERP-сервера (custom DERP server) на том же VPS, о котором говорилось в разделе 3, позволяет контролировать маршрут трафика и гарантировать ресурсы.39

---

## **5. Стратегия III: Туннелирование прикладного уровня (Reverse Proxies)**

Для задач, ограниченных веб-доступом (HTTP/HTTPS) или специфическими игровыми протоколами (Minecraft), существуют специализированные решения, не требующие настройки VPN на стороне клиента.

### **5.1. Cloudflare Tunnel (Zero Trust)**

Это решение позволяет безопасно публиковать веб-сервисы без открытия портов. Агент cloudflared устанавливается в локальной сети и устанавливает исходящие соединения к Edge-сети Cloudflare.

**Преимущества:**

* Мощная защита от DDoS и WAF "из коробки".  
* Работает через стандартный порт 443, который никогда не блокируется операторами.  
* Возможность настройки политик доступа (Access Policies) для сотрудников (например, вход через Google Workspace).

Юридические и технические риски (Terms of Service):  
Важно предупредить клиента ꆜ о рисках. Пункт 2.8 условий использования Cloudflare (Self-Serve) явно запрещает использование бесплатных туннелей для передачи непропорционального объема не-HTML контента (видео, образы дисков, бинарные файлы) без использования платных продуктов Cloudflare Stream/Images.40 Для компании, занимающейся строительством и производством (передача чертежей CAD, видео с камер наблюдения), это может привести к внезапной блокировке аккаунта.

### **5.2. Playit.gg и Pinggy.io**

Эти сервисы ориентированы на обход NAT для произвольных TCP/UDP протоколов.

* **Playit.gg:** Использует глобальную сеть Anycast для туннелирования трафика. Особенно эффективен для UDP-трафика (игровые серверы, VoIP), который часто плохо работает через стандартные HTTP-туннели. Поддерживает статические IP и порты на платных тарифах, что добавляет элемент надежности.43  
* **Pinggy.io:** Позволяет поднять туннель одной командой SSH без установки агента (ssh -p 443 -R0:localhost:22 tcp@a.pinggy.io). Это идеальный инструмент для экстренного доступа или отладки, но для постоянной инфраструктуры ("Reliable workaround") он менее пригоден из-за зависимости от стабильности SSH-сессии.6

---

## **6. «Ядерное» решение: Переход на T-Mobile Business Internet**

Если вышеописанные программные методы кажутся клиенту ꆜ слишком сложными в поддержке ("костылями"), существует официальный путь решения проблемы через изменение типа контракта с оператором.

### **6.1. Статический IP: Единственный способ обойти CGNAT официально**

T-Mobile предлагает услугу **Static IP** исключительно для бизнес-клиентов. При подключении этой услуги архитектура подключения меняется: абоненту присваивается фиксированный публичный IPv4-адрес, и трафик маршрутизируется через шлюз, не использующий агрессивную фильтрацию входящих соединений и CGNAT.12

**Стоимость и условия:**

* Базовая стоимость тарифа часто идентична домашнему ($50/мес с голосовой линией), но за статический IP взимается дополнительная плата (обычно $3/мес за адрес).  
* Требуется заключение бизнес-контракта.

### **6.2. Бюрократические нюансы: SSN vs EIN**

Многие малые предприниматели (Sole Proprietors) ошибочно полагают, что не могут получить бизнес-интернет без корпоративного идентификатора (EIN). Анализ условий T-Mobile показывает, что регистрация возможна с использованием **SSN (Social Security Number)** в качестве индивидуального предпринимателя.48 T-Mobile проводит проверку кредитной истории (Personal Credit Check), но наличие зарегистрированного LLC не является блокирующим фактором.51

### **6.3. Технические ловушки: APN b2b.static и оборудование**

Переход на бизнес-тариф не решает проблему автоматически. Существует два критических нюанса, незнание которых приводит к провалу внедрения:

1. **Специфическое оборудование:** Стандартные домашние шлюзы (Sagemcom, Arcadyan, Nokia trashcan) часто имеют ограниченную прошивку, не позволяющую детально настраивать APN. Для услуги Static IP T-Mobile обычно предоставляет (или требует покупки) роутеры корпоративного класса, такие как **Inseego FX2000/FX3100** или **Cradlepoint**.52  
2. **Настройка APN (Access Point Name):** Это самая частая точка отказа. По умолчанию даже бизнес-устройства подключаются к APN fast.t-mobile.com, который находится за CGNAT. Для работы статического IP необходимо вручную переключить устройство на APN **b2b.static**. Без этого действия IP-адрес останется динамическим и серым, несмотря на оплату услуги. Поддержка первого уровня часто не знает об этом нюансе, что подтверждается многочисленными жалобами пользователей.54

**Таблица 1: Сравнение T-Mobile Home vs Business Internet для задачи T⁎**

| Функция | Home Internet | Business Internet + Static IP |
| :---- | :---- | :---- |
| **Публичный IPv4** | Нет (Shared CGNAT IP) | Да (Выделенный Static IP) |
| **Входящие порты** | Заблокированы | Открыты (User Managed Firewall) |
| **APN** | fast.t-mobile.com | b2b.static |
| **Оборудование** | Стандартный шлюз (ограничен) | Inseego / Cradlepoint (гибкий) |
| **Сложность внедрения** | Высокая (требует VPN/VPS) | Низкая (после настройки APN) |
| **Reliability** | Зависит от VPS/Overlay | Максимальная (Native routing) |

---

## **7. Синтез и стратегические рекомендации**

На основе проведенного анализа, учитывая профиль клиента ꆜ (Manufacturing & Construction, потребность в надежности) и технические ограничения T-Mobile, предлагается следующая иерархия решений.

### **7.1. Рекомендация №1: Миграция на Business Internet (Golden Standard)**

Для производственной компании надежность является приоритетом. Программные туннели добавляют точки отказа (VPS упал, процесс Tailscale завис, обновление сломало конфиг).  
Действия:

1. Переоформить контракт на Sole Proprietor Business Account (используя SSN).  
2. Заказать услугу Static IPv4 ($3/мес).  
3. Запросить роутер Inseego FX3100.  
4. При настройке жестко прописать APN b2b.static.  
   Это полностью устраняет проблему CGNAT на физическом уровне.

### **7.2. Рекомендация №2: VPS Relay на базе WireGuard (Best Workaround)**

Если миграция невозможна (например, корпоративная политика или отказ в кредите), следует развернуть собственный релей.  
Конфигурация:

* **Провайдер:** AWS Lightsail ($3.50/мес) или Vultr ($5/мес).  
* **ОС:** Ubuntu 22.04 LTS.  
* **ПО:** WireGuard (Kernel module) + iptables.  
* **Важно:** Настроить PersistentKeepalive = 25 и MTU 1280-1360 для предотвращения фрагментации в туннеле 464XLAT.

### **7.3. Рекомендация №3: Tailscale Subnet Router (Ease of Use)**

Для доступа сотрудников к общим ресурсам без публикации сервисов в интернет.  
Оборудование: Использовать Intel N100 Mini PC в качестве шлюза в локальной сети. Это обеспечит пропускную способность до 400-500 Мбит/с через VPN, что достаточно для передачи тяжелых файлов или видеопотоков, в отличие от устаревших Raspberry Pi.  
В заключение, проблема P† является не ошибкой конфигурации, а следствием современной архитектуры мобильных сетей. Решение требует либо адаптации к этой архитектуре (Overlay Networks), либо выхода за её пределы (Static IP APN). Для бизнеса ꆜ путь со статическим IP является единственным гарантирующим 100% совместимость с существующими производственными процессами.

#### **Works cited**

1. Understanding 464XLAT ALG Traffic Support | Junos OS - Juniper Networks, accessed November 24, 2025, [https://www.juniper.net/documentation/us/en/software/junos/alg/topics/concept/security-xlat-alg-traffic-support-understanding.html](https://www.juniper.net/documentation/us/en/software/junos/alg/topics/concept/security-xlat-alg-traffic-support-understanding.html)  
2. 464XLAT in mobile networks | APNIC, accessed November 24, 2025, [https://www.apnic.net/wp-content/uploads/2017/01/IPv6_Migration_Strategies_for_Mobile_Networks_Whitepaper.pdf](https://www.apnic.net/wp-content/uploads/2017/01/IPv6_Migration_Strategies_for_Mobile_Networks_Whitepaper.pdf)  
3. RFC 6877 - 464XLAT: Combination of Stateful and Stateless Translation - IETF Datatracker, accessed November 24, 2025, [https://datatracker.ietf.org/doc/rfc6877/](https://datatracker.ietf.org/doc/rfc6877/)  
4. PortFowarding T-Mobile Home Internet - Channels Community, accessed November 24, 2025, [https://community.getchannels.com/t/portfowarding-t-mobile-home-internet/32162](https://community.getchannels.com/t/portfowarding-t-mobile-home-internet/32162)  
5. T-Mobile Home Internet Port Forwarding & Bypass CGNAT - PureVPN, accessed November 24, 2025, [https://www.purevpn.com/blog/t-mobile-cgnat-port-forwarding/](https://www.purevpn.com/blog/t-mobile-cgnat-port-forwarding/)  
6. Bypassing Port Forwarding Restrictions on T-Mobile Home Internet Using Pinggy, accessed November 24, 2025, [https://dev.to/lightningdev123/bypassing-port-forwarding-restrictions-on-t-mobile-home-internet-using-pinggy-3me6](https://dev.to/lightningdev123/bypassing-port-forwarding-restrictions-on-t-mobile-home-internet-using-pinggy-3me6)  
7. T-Mobile Home Internet Port Forwarding (Getting Started) | LocalXpose Blog, accessed November 24, 2025, [https://localxpose.io/blog/t-mobile-home-internet-port-forwarding](https://localxpose.io/blog/t-mobile-home-internet-port-forwarding)  
8. Firewall | Expert settings | LTE Wi-Fi Gateway TM-RTL0102 | T-Mobile Support, accessed November 24, 2025, [https://www.t-mobile.com/support/tutorials/device/t-mobile/lte-wi-fi-gateway-tm-rtl0102/topic/expert-settings/firewall](https://www.t-mobile.com/support/tutorials/device/t-mobile/lte-wi-fi-gateway-tm-rtl0102/topic/expert-settings/firewall)  
9. Does t-mobile IPv6 actually allow for incoming connections? Home Internet specifically, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/jf34gv/does_tmobile_ipv6_actually_allow_for_incoming/](https://www.reddit.com/r/tmobile/comments/jf34gv/does_tmobile_ipv6_actually_allow_for_incoming/)  
10. IPv6 with T-Mobile 5G home Internet : r/firewalla - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/firewalla/comments/1hq4zv6/ipv6_with_tmobile_5g_home_internet/](https://www.reddit.com/r/firewalla/comments/1hq4zv6/ipv6_with_tmobile_5g_home_internet/)  
11. **ULTIMATE NOOB GUIDE** - HOW TO BYPASS CGNAT USING WIREGUARD SERVER ON A VPS - STEP BY STEP FROM START TO FINISH. : r/unRAID - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/unRAID/comments/10vx69b/ultimate_noob_guide_how_to_bypass_cgnat_using/](https://www.reddit.com/r/unRAID/comments/10vx69b/ultimate_noob_guide_how_to_bypass_cgnat_using/)  
12. WireGuard behind CGNAT 5G Connection (T-Mobile 5G Business Internet) - Firewalla, accessed November 24, 2025, [https://help.firewalla.com/hc/en-us/community/posts/38610335671443-WireGuard-behind-CGNAT-5G-Connection-T-Mobile-5G-Business-Internet](https://help.firewalla.com/hc/en-us/community/posts/38610335671443-WireGuard-behind-CGNAT-5G-Connection-T-Mobile-5G-Business-Internet)  
13. How To Set Up WireGuard on Ubuntu 20.04 - DigitalOcean, accessed November 24, 2025, [https://www.digitalocean.com/community/tutorials/how-to-set-up-wireguard-on-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/how-to-set-up-wireguard-on-ubuntu-20-04)  
14. Virtual Private Server and Web Hosting – Amazon Lightsail FAQs, accessed November 24, 2025, [https://aws.amazon.com/lightsail/faq/](https://aws.amazon.com/lightsail/faq/)  
15. Amazon Lightsail Pricing, accessed November 24, 2025, [https://aws.amazon.com/lightsail/pricing/](https://aws.amazon.com/lightsail/pricing/)  
16. Google Cloud Run Pricing in 2025: A Comprehensive Guide - Cloudchipr, accessed November 24, 2025, [https://cloudchipr.com/blog/cloud-run-pricing](https://cloudchipr.com/blog/cloud-run-pricing)  
17. Network pricing - Google Cloud, accessed November 24, 2025, [https://cloud.google.com/vpc/network-pricing](https://cloud.google.com/vpc/network-pricing)  
18. What is Oracle Cloud free storage & bandwidth limit? : r/oraclecloud - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/oraclecloud/comments/passwm/what_is_oracle_cloud_free_storage_bandwidth_limit/](https://www.reddit.com/r/oraclecloud/comments/passwm/what_is_oracle_cloud_free_storage_bandwidth_limit/)  
19. 7 Best VPS for VPN Servers (Nov 2025): Reviewed by Experts - HostAdvice, accessed November 24, 2025, [https://hostadvice.com/vps/vpn-hosting/](https://hostadvice.com/vps/vpn-hosting/)  
20. VPN Server | DigitalOcean Marketplace 1-Click App, accessed November 24, 2025, [https://marketplace.digitalocean.com/apps/vpn-server](https://marketplace.digitalocean.com/apps/vpn-server)  
21. Wireguard | Vultr Marketplace One-Click Application, accessed November 24, 2025, [https://www.vultr.com/marketplace/apps/wireguard/](https://www.vultr.com/marketplace/apps/wireguard/)  
22. VPNs: Virtual Private Networks | Linode Docs, accessed November 24, 2025, [https://www.linode.com/docs/guides/networking/vpn/](https://www.linode.com/docs/guides/networking/vpn/)  
23. Network bandwidth | Compute Engine - Google Cloud Documentation, accessed November 24, 2025, [https://docs.cloud.google.com/compute/docs/network-bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth)  
24. Quotas and limits | Virtual Private Cloud - Google Cloud Documentation, accessed November 24, 2025, [https://docs.cloud.google.com/vpc/docs/quota](https://docs.cloud.google.com/vpc/docs/quota)  
25. Help setting up WireGuard for outside-in access through CGNAT? - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/WireGuard/comments/198fqqp/help_setting_up_wireguard_for_outsidein_access/](https://www.reddit.com/r/WireGuard/comments/198fqqp/help_setting_up_wireguard_for_outsidein_access/)  
26. I'm about to give up... Using a VPS as a relay to home network behind CGNAT. - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/WireGuard/comments/1gemu05/im_about_to_give_up_using_a_vps_as_a_relay_to/](https://www.reddit.com/r/WireGuard/comments/1gemu05/im_about_to_give_up_using_a_vps_as_a_relay_to/)  
27. Use Raspberry Pi as Gateway for unsupported devices : r/Tailscale - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/Tailscale/comments/1n60eyc/use_raspberry_pi_as_gateway_for_unsupported/](https://www.reddit.com/r/Tailscale/comments/1n60eyc/use_raspberry_pi_as_gateway_for_unsupported/)  
28. Set up WireGuard VPN on Ubuntu 20.04 - Vultr Docs, accessed November 24, 2025, [https://docs.vultr.com/set-up-wireguard-vpn-on-ubuntu-20-04](https://docs.vultr.com/set-up-wireguard-vpn-on-ubuntu-20-04)  
29. Cloudflare vs. Tailscale | Compare Access and Gateway to Tailscale, accessed November 24, 2025, [https://tailscale.com/compare/cloudflare-access](https://tailscale.com/compare/cloudflare-access)  
30. Tailscale vs Zerotier vs … - Duplicacy Forum, accessed November 24, 2025, [https://forum.duplicacy.com/t/tailscale-vs-zerotier-vs/9795](https://forum.duplicacy.com/t/tailscale-vs-zerotier-vs/9795)  
31. Tailscale to turn 5G home internet into VPN - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/Tailscale/comments/13qfzko/tailscale_to_turn_5g_home_internet_into_vpn/](https://www.reddit.com/r/Tailscale/comments/13qfzko/tailscale_to_turn_5g_home_internet_into_vpn/)  
32. Configure a subnet router · Tailscale Docs, accessed November 24, 2025, [https://tailscale.com/kb/1406/quick-guide-subnets](https://tailscale.com/kb/1406/quick-guide-subnets)  
33. Subnet routers · Tailscale Docs, accessed November 24, 2025, [https://tailscale.com/kb/1019/subnets](https://tailscale.com/kb/1019/subnets)  
34. Benchmarking subnet routers : r/Tailscale - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/Tailscale/comments/1mfkwuc/benchmarking_subnet_routers/](https://www.reddit.com/r/Tailscale/comments/1mfkwuc/benchmarking_subnet_routers/)  
35. Raspberry Pi 5 vs. Pi 4 AI performance CPU Benchmark: How much leap forward? - Latest News from Seeed Studio, accessed November 24, 2025, [https://www.seeedstudio.com/blog/2023/09/28/raspberry-pi-5-vs-pi-4-ai-performance-cpu-benchmark-how-much-leap-forward/](https://www.seeedstudio.com/blog/2023/09/28/raspberry-pi-5-vs-pi-4-ai-performance-cpu-benchmark-how-much-leap-forward/)  
36. Raspberry PI 5 vs Mini PC Intel N100 - Tailscale Exit Node - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/Tailscale/comments/1cyui86/raspberry_pi_5_vs_mini_pc_intel_n100_tailscale/](https://www.reddit.com/r/Tailscale/comments/1cyui86/raspberry_pi_5_vs_mini_pc_intel_n100_tailscale/)  
37. T-Mobile Home Internet. Exit Nodes, & Derp : r/Tailscale - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/Tailscale/comments/1eplfy9/tmobile_home_internet_exit_nodes_derp/](https://www.reddit.com/r/Tailscale/comments/1eplfy9/tmobile_home_internet_exit_nodes_derp/)  
38. Is Slower Mobile Internet when using an Exit Node Expected? : r/Tailscale - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/Tailscale/comments/1gwuirg/is_slower_mobile_internet_when_using_an_exit_node/](https://www.reddit.com/r/Tailscale/comments/1gwuirg/is_slower_mobile_internet_when_using_an_exit_node/)  
39. Wireguard as a relay server - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/WireGuard/comments/1hpdogz/wireguard_as_a_relay_server/](https://www.reddit.com/r/WireGuard/comments/1hpdogz/wireguard_as_a_relay_server/)  
40. Plex against Cloudflare TOS Zero trust tunnels or not? - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/PleX/comments/196yiyf/plex_against_cloudflare_tos_zero_trust_tunnels_or/](https://www.reddit.com/r/PleX/comments/196yiyf/plex_against_cloudflare_tos_zero_trust_tunnels_or/)  
41. Plex server on Argo Tunnel - Getting Started - Cloudflare Community, accessed November 24, 2025, [https://community.cloudflare.com/t/plex-server-on-argo-tunnel/708882](https://community.cloudflare.com/t/plex-server-on-argo-tunnel/708882)  
42. Clarifying TOS - General - Cloudflare Community, accessed November 24, 2025, [https://community.cloudflare.com/t/clarifying-tos/538782](https://community.cloudflare.com/t/clarifying-tos/538782)  
43. playit.gg, accessed November 24, 2025, [https://playit.gg/](https://playit.gg/)  
44. Host a Minecraft Server Without Port Forwarding Using Playit.gg - YouTube, accessed November 24, 2025, [https://www.youtube.com/watch?v=itVVhcid2_Q](https://www.youtube.com/watch?v=itVVhcid2_Q)  
45. playit.gg - support pages, accessed November 24, 2025, [https://playit.gg/support/](https://playit.gg/support/)  
46. T-Mobile Port Forwarding - Pinggy, accessed November 24, 2025, [https://pinggy.io/blog/tmobile_port_forwarding/](https://pinggy.io/blog/tmobile_port_forwarding/)  
47. Small Business Internet Service | T-Mobile for Business, accessed November 24, 2025, [https://www.t-mobile.com/business/solutions/business-internet-services/small-business-internet](https://www.t-mobile.com/business/solutions/business-internet-services/small-business-internet)  
48. T-Mobile for Business - Credit Check, accessed November 24, 2025, [https://www.t-mobile.com/business/credit-check/check-my-credit](https://www.t-mobile.com/business/credit-check/check-my-credit)  
49. Can I get tmobile 5g business internet at my home address? : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/16rl1s3/can_i_get_tmobile_5g_business_internet_at_my_home/](https://www.reddit.com/r/tmobileisp/comments/16rl1s3/can_i_get_tmobile_5g_business_internet_at_my_home/)  
50. T-Mobile for Business. : r/tmobile - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/18lz9gt/tmobile_for_business/](https://www.reddit.com/r/tmobile/comments/18lz9gt/tmobile_for_business/)  
51. Let's run a soft credit check to approve your business. - T-Mobile, accessed November 24, 2025, [https://www.t-mobile.com/business/credit-check/business-credit-check-review](https://www.t-mobile.com/business/credit-check/business-credit-check-review)  
52. Business Internet Static IP? : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1dphkw7/business_internet_static_ip/](https://www.reddit.com/r/tmobileisp/comments/1dphkw7/business_internet_static_ip/)  
53. tmobile business static ip passthrough to Mikrotik - General, accessed November 24, 2025, [https://forum.mikrotik.com/t/tmobile-business-static-ip-passthrough-to-mikrotik/183486](https://forum.mikrotik.com/t/tmobile-business-static-ip-passthrough-to-mikrotik/183486)  
54. My experience trying to get a static IP for my business : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/11t4yau/my_experience_trying_to_get_a_static_ip_for_my/](https://www.reddit.com/r/tmobileisp/comments/11t4yau/my_experience_trying_to_get_a_static_ip_for_my/)  
55. T-Mobile data & APN settings, accessed November 24, 2025, [https://www.t-mobile.com/support/devices/not-sold-by-t-mobile/byod-t-mobile-data-and-apn-settings](https://www.t-mobile.com/support/devices/not-sold-by-t-mobile/byod-t-mobile-data-and-apn-settings)  
56. PSA: If you are using T-Mobile BYOD router or Hotspot with a static ipv4 address, you must use the APN b2b.tmobile.com or b2b.static - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/j45sgz/psa_if_you_are_using_tmobile_byod_router_or/](https://www.reddit.com/r/tmobile/comments/j45sgz/psa_if_you_are_using_tmobile_byod_router_or/)

# 9. Что беспокоит `ꆜ` (Aнализ №2, выполнен Gemini Deep Research)
https://gemini.google.com/share/73c6a0d2dfe7

## **1. Введение: Архитектурный контекст задачи**

В рамках анализа проектной задачи P⁎, инициированной клиентом ꆜ (сектор производства и строительства), рассматривается фундаментальная проблема обеспечения удаленного доступа к локальным ресурсам, размещенным за шлюзом T-Mobile Home Internet (TMHI). Задача, сформулированная как необходимость "настройки обходного пути для перенаправления портов", выходит за рамки стандартного системного администрирования и погружается в область архитектуры сетей провайдерского класса.

Клиент ꆜ столкнулся с ограничениями, которые являются не дефектом конфигурации, а следствием глобального исчерпания адресного пространства IPv4 и перехода мобильных операторов на архитектуру IPv6-only. В условиях, когда устройство клиента не имеет публичного маршрутизируемого IPv4-адреса, традиционные методы трансляции сетевых адресов (NAT) и перенаправления портов (Port Forwarding) становятся математически и топологически невозможными на стороне абонентского оборудования (CPE).

Данный отчет представляет собой исчерпывающее техническое исследование сетевой среды T-Mobile US, механизмов трансляции адресов 464XLAT, феномена Carrier-Grade NAT (CGNAT) и влияния параметров MTU (Maximum Transmission Unit) на туннелирование трафика. Цель документа — предоставить глубоко обоснованные технические решения для организации стабильного входящего канала связи, соответствующего требованиям производственной надежности.

---

## **2. Глубинный анализ сетевой топологии T-Mobile Home Internet**

Для разработки надежного решения (Reliable Workaround) необходимо детально декомпозировать сетевой стек, на котором функционирует сервис TMHI. Понимание того, как пакеты данных обрабатываются на пути от глобальной сети Интернет до модема пользователя, позволяет выявить истинные причины блокировки входящих соединений.

### **2.1. Парадигма IPv6-Only и механизм 464XLAT**

Сеть T-Mobile US является одной из первых в мире, полностью перешедших на нативную маршрутизацию IPv6. Это означает, что транспортный уровень сети оператора не оперирует протоколом IPv4. Для обеспечения совместимости с подавляющим большинством ресурсов интернета, которые все еще используют IPv4 (как, вероятно, и локальные ресурсы клиента ꆜ), применяется технология **464XLAT**, описанная в стандарте RFC 6877.1

Механизм 464XLAT представляет собой сложную систему двойной трансляции, состоящую из двух ключевых компонентов, взаимодействие которых определяет доступность сетевых узлов:

1. **CLAT (Customer-side Translator):** Данный модуль функционирует непосредственно на устройстве пользователя (в данном случае — на 5G-шлюзе Arcadyan, Nokia или Sagemcom). Его задача — перехватывать исходящие IPv4-пакеты от локальных устройств (камеры, серверы, компьютеры), инкапсулировать их или транслировать в IPv6-пакеты, пригодные для передачи через транспортную сеть провайдера.  
2. **PLAT (Provider-side Translator):** Этот компонент располагается на границе ядра сети T-Mobile и публичного интернета. Он выполняет обратную функцию — Stateful NAT64. PLAT принимает IPv6-пакеты от абонентов, деинкапсулирует их обратно в IPv4 и отправляет в глобальную сеть, подменяя адрес источника на один из своих публичных IPv4-адресов.

Критически важным аспектом для задачи P⁎ является то, что PLAT работает в режиме **Stateful NAT64**. Это означает, что трансляция адресов возможна только при условии, что соединение было инициировано изнутри сети (со стороны CLAT). При попытке внешнего узла инициировать соединение на публичный IPv4-адрес PLAT, оборудование провайдера не имеет записи в таблице состояний (state table), связывающей этот входящий пакет с конкретным абонентом из миллионов пользователей, скрытых за этим IP.1 Следовательно, пакет отбрасывается. Это объясняет, почему клиент ꆜ констатирует факт: *"T-Mobile confirmed they cannot open ports"*.1 В такой архитектуре понятие "открыть порт" на стороне клиента теряет смысл, так как клиент не контролирует точку входа трафика (PLAT).

### **2.2. Carrier-Grade NAT (CGNAT) и проблема "Жесткого NAT"**

Термин CGNAT (Carrier-Grade Network Address Translation), часто используемый в технической документации и дискуссиях сообщества 1, описывает масштаб проблемы. В отличие от домашнего NAT, где один публичный IP транслируется в несколько частных (1:N), CGNAT в сети T-Mobile подразумевает каскадирование трансляций.

Абонентское оборудование находится за многоуровневым "NAT-забором". Публичный адрес, который видит внешний мир (например, 172.56.x.x или подобный из диапазона T-Mobile), является общим для тысяч пользователей в одном географическом регионе.1 Любая попытка настроить Port Forwarding на локальном роутере (например, перенаправить порт 80 на веб-сервер) влияет только на внутреннюю сеть пользователя и не имеет никакого воздействия на маршрутизаторы провайдера, где происходит реальная блокировка входящего трафика.

Более того, реализация NAT в мобильных сетях часто классифицируется как **Symmetric NAT** или **Hard NAT**. В такой конфигурации NAT-шлюз присваивает разные внешние порты для соединений с разными целевыми IP-адресами, даже если они инициированы с одного и того же внутреннего сокета.10 Это создает значительные препятствия для протоколов, пытающихся использовать технологии NAT Traversal (обход NAT), таких как STUN (Session Traversal Utilities for NAT), поскольку предсказать внешний порт становится невозможно.

### **2.3. Политики безопасности в отношении входящего IPv6-трафика**

Логично предположить, что наличие глобально маршрутизируемого IPv6-адреса (Global Unicast Address), который T-Mobile выдает абонентам (префикс /64), могло бы решить проблему. Теоретически, это позволяет обращаться к устройству напрямую, минуя NAT. Однако, анализ источников показывает, что T-Mobile применяет жесткие политики фильтрации трафика на уровне сетевого экрана (Firewall).2

Весь **незапрошенный входящий трафик (Unsolicited Inbound Traffic)** по протоколу IPv6 блокируется на стороне инфраструктуры оператора. Это решение продиктовано исторической спецификой мобильных сетей, где защита конечных устройств (смартфонов) от сканирования портов и атак извне является приоритетом. Для домашнего интернета, который позиционируется как замена кабельному подключению, эта политика не была адаптирована. Следовательно, даже при наличии "белого" IPv6-адреса, клиент ꆜ не сможет поднять сервер, доступный извне, без использования туннелирования исходящего соединения.4

Таким образом, утверждение клиента о блокировке входящих соединений является абсолютно обоснованным и технически подтвержденным свойством архитектуры сети. Решение задачи P⁎ лежит исключительно в плоскости создания **оверлейных сетей (Overlay Networks)**, которые инициируют соединение изнутри сети наружу.

---

## **3. Скрытые угрозы: MTU, фрагментация и потери пакетов**

Одной из наиболее коварных проблем, с которой сталкиваются инженеры при настройке VPN поверх сетей 464XLAT, является несоответствие размера пакета (MTU — Maximum Transmission Unit). В описании задачи P⁎ клиент упоминает необходимость настройки "SSL VPN" или "WireGuard", но не указывает на осведомленность о проблемах фрагментации. Игнорирование этого аспекта приводит к созданию нестабильных соединений, где "ping проходит, но веб-страницы не грузятся".13

### **3.1. Математика накладных расходов (Overhead) в туннелях**

Стандартный размер кадра Ethernet составляет **1500 байт**. В традиционных сетях IPv4 VPN-протоколы обычно устанавливают MTU виртуального интерфейса на уровне 1400-1420 байт, оставляя место для заголовков VPN. Однако в сети T-Mobile происходит многоуровневая инкапсуляция, которая "съедает" полезную нагрузку пакета (Payload).

Рассмотрим структуру пакета, проходящего через туннель WireGuard в сети T-Mobile:

1. **Транспортный уровень T-Mobile (IPv6):** Базовый заголовок IPv6 имеет фиксированный размер **40 байт** (против 20 байт у IPv4).15  
2. **Инкапсуляция 464XLAT (CLAT):** Если VPN-клиент пытается отправить IPv4-трафик, модуль CLAT добавляет заголовок IPv6 для транспорта через сеть оператора, плюс сохраняет заголовок IPv4 внутри.  
3. **Заголовок протокола VPN (WireGuard/OpenVPN):**  
   * WireGuard использует UDP и добавляет собственный заголовок (8 байт UDP + минимум 16 байт WireGuard header + теги аутентификации Poly1305).  
   * OpenVPN (в режиме TCP) добавляет заголовки TCP (20 байт) и собственную структуру.

Суммарные накладные расходы приводят к тому, что реальный Path MTU (PMTU) в сети T-Mobile часто падает ниже 1400 байт. Исследования пользователей и технические эксперименты указывают на то, что "безопасный" MTU для T-Mobile находится в диапазоне **1280 – 1360 байт**.14

### **3.2. Феномен "Black Hole" и отказ PMTU Discovery**

Проблема усугубляется тем, как протокол IPv6 обрабатывает фрагментацию. В отличие от IPv4, маршрутизаторы в сети IPv6 **не фрагментируют пакеты**. Если пакет превышает MTU следующего звена сети, маршрутизатор отбрасывает его и отправляет отправителю сообщение ICMPv6 "Packet Too Big" (PTB).

Однако, в современных сетях часто встречается проблема **PMTUD Black Hole** (Path MTU Discovery Black Hole). Многие фаерволы (как на стороне серверов, так и внутри сети провайдера) блокируют ICMP-трафик из соображений безопасности. В результате:

1. VPN-клиент отправляет пакет размером 1420 байт.  
2. Пакет доходит до узла 464XLAT или шлюза провайдера, где MTU ограничен (например, 1400 байт).  
3. Пакет отбрасывается.  
4. Сообщение об ошибке (ICMPv6 PTB) блокируется фаерволом или не может быть корректно сопоставлено с сессией из-за NAT.  
5. Отправитель не узнает о проблеме и продолжает слать большие пакеты, которые исчезают в "черной дыре".13

Для клиента ꆜ это проявляется как зависание SSH-сессий, недогрузка картинок на веб-сайтах или разрыв соединения при передаче файлов.

**Рекомендация:** При настройке любого туннельного решения (WireGuard, Tailscale, OpenVPN) критически важно принудительно установить **MTU = 1280 байт** на виртуальном интерфейсе. Значение 1280 является минимально допустимым MTU для IPv6, что гарантирует прохождение пакета через любое звено сети без фрагментации.14

---

## **4. Сравнительный анализ решений (Workarounds)**

На основе требований PD ("reliable workaround", "stable inbound connections") и доступных технологий, мы проанализировали три основных подхода к решению проблемы.

### **4.1. Метод А: VPS-шлюз с обратным туннелированием (Рекомендованный)**

Этот метод представляет собой золотой стандарт для обхода CGNAT, предоставляя клиенту полный контроль над трафиком и выделенный публичный IP-адрес.

**Архитектура решения:**

1. **Внешний узел (VPS):** Арендуется виртуальный сервер (Cloud VPS) у провайдера с "чистым" интернетом (AWS, Google Cloud, DigitalOcean, Oracle Cloud, RackNerd и др.). VPS имеет статический публичный IPv4-адрес.  
2. **Туннель:** Между сервером внутри сети ꆜ (например, Raspberry Pi, NAS или PC) и VPS устанавливается VPN-туннель (предпочтительно WireGuard). Инициатором соединения выступает домашний сервер (исходящее соединение), что позволяет беспрепятственно пройти через CGNAT T-Mobile.7  
3. **Перенаправление (Port Forwarding):** На VPS настраиваются правила iptables (для Linux), которые перенаправляют входящий трафик с публичного порта VPS в туннель WireGuard к домашнему серверу.

**Преимущества:**

* **Стабильность:** WireGuard — протокол без сохранения состояния (stateless), который отлично восстанавливает соединение при смене IP-адреса на модеме T-Mobile.  
* **Прозрачность:** Для внешнего клиента доступ выглядит как обычное подключение к IP-адресу. Не требуется установка специального ПО на клиентской стороне.  
* **Контроль:** Возможен проброс любых портов TCP и UDP (http, ssh, rdp, scada-протоколы).

**Специфические настройки для T-Mobile:**

* **PersistentKeepalive:** Обязательная опция в конфигурации WireGuard на стороне клиента. Рекомендуемое значение — **20-25 секунд**. Это заставляет клиент отправлять пустые пакеты, поддерживая запись в NAT-таблице T-Mobile активной и предотвращая разрыв соединения со стороны провайдера.25  
* **MTU:** Как обсуждалось выше, установка MTU = 1280 обязательна.14

| Параметр | WireGuard over VPS |
| :---- | :---- |
| **Сложность внедрения** | Высокая (требует навыков Linux/CLI) |
| **Стоимость** | От $0 (Free Tier) до $5/мес |
| **Тип трафика** | Любой (TCP/UDP/ICMP) |
| **Зависимость от провайдера** | Минимальная |

### **4.2. Метод Б: Overlay-сети (Tailscale / ZeroTier)**

Данные решения автоматизируют процесс построения туннелей, используя технологии NAT Traversal (STUN/TURN).

Tailscale:  
Построен на базе WireGuard, но работает в пространстве пользователя (userspace). Использует координационные серверы для обмена ключами.

* **Плюсы:** Крайне простая настройка (установка агента). Поддержка "Subnet Router" позволяет дать доступ ко всей локальной сети клиента, установив агент только на одно устройство.  
* **Минусы на T-Mobile:** Из-за "Hard NAT" и блокировки входящих UDP, Tailscale часто не может установить прямое соединение (Direct Connection) и переключается на использование **DERP Relays** (промежуточных серверов Tailscale).10 Это увеличивает задержку (latency) и ограничивает пропускную способность.  
* **Решение:** Для повышения шансов на прямое соединение можно попробовать рандомизировать порт UDP на стороне Tailscale, но гарантий нет.

ZeroTier:  
Использует собственный протокол (не WireGuard).

* **Проблемы:** Многочисленные отчеты указывают на нестабильность ZeroTier в сетях T-Mobile.30 Предполагается, что механизмы шейпинга UDP-трафика или некорректная обработка фрагментированных пакетов в сети оператора приводят к периодическим потерям связи ("flapping"). Для производственных задач (Manufacturing) это решение несет высокие риски.

### **4.3. Метод В: Cloudflare Tunnel (Zero Trust)**

Использует демон cloudflared для создания исходящего туннеля к инфраструктуре Cloudflare.

**Анализ применимости:**

* **HTTP/HTTPS:** Идеально подходит для веб-сервисов. Обеспечивает защиту от DDoS и скрывает реальный IP.  
* **Non-HTTP (Arbitrary TCP):** Возможно, но с ограничениями. Для доступа к SSH, RDP или SMB через Cloudflare Tunnel требуется, чтобы на *клиентском* устройстве (том, с которого подключаются) также был установлен cloudflared или WARP-клиент.33 Это нарушает требование универсальности, если доступ нужен с произвольных устройств.  
* **Риски Terms of Service (ToS):** Ранее Cloudflare запрещала передачу не-HTML контента (видео, большие файлы) через бесплатные туннели (Section 2.8). Несмотря на недавние изменения формулировок, использование туннеля для потокового видео (например, камер наблюдения на производстве) в больших объемах без использования платных продуктов (Cloudflare Stream/Images) может привести к бану аккаунта за нарушение политики "disproportionate use".36

---

## **5. Корпоративное решение: Статический IP и Бизнес-тарифы**

В ходе анализа выявлен альтернативный путь, который устраняет корень проблемы, а не борется с симптомами. T-Mobile предлагает услугу **Static IP**, но исключительно для бизнес-клиентов.40

### **5.1. Техническая реализация Static IP**

При подключении услуги статического IP (обычно стоит около $3/мес сверх тарифа), сим-карта и модем переводятся в другой сетевой сегмент.

* **APN (Access Point Name):** Устройство переключается с общедоступного fast.t-mobile.com на специализированный b2b.static.42  
* **Маршрутизация:** В этом сегменте отсутствует CGNAT. Абоненту присваивается публичный, маршрутизируемый IPv4-адрес. Порты полностью открыты для входящих соединений.  
* **Локация:** IP-адрес привязан к конкретному PoP (Point of Presence), что решает проблемы с геолокацией, характерные для динамических IP мобильных сетей.

### **5.2. Доступность для клиента**

Для клиента из сектора "Manufacturing & Construction" переход на бизнес-аккаунт является логичным шагом. T-Mobile позволяет регистрировать бизнес-аккаунты даже индивидуальным предпринимателям (Sole Proprietor) по номеру социального страхования (SSN), без обязательного наличия EIN (хотя требования могут варьироваться в зависимости от региона и менеджера).43

**Сравнительная таблица эффективности решений:**

| Характеристика | VPN Tunnel (VPS) | Cloudflare Tunnel | Static IP (Business) |
| :---- | :---- | :---- | :---- |
| **Природа решения** | Технический обход (Workaround) | Проксирование уровня приложений | Архитектурное изменение |
| **Пропускная способность** | Ограничена CPU VPS и шифрованием | Ограничена тарифом Cloudflare | Максимальная (Native) |
| **Задержка (Latency)** | Увеличена (доп. хоп до VPS) | Увеличена (через CDN) | Минимальная |
| **Надежность** | Высокая (при правильном MTU) | Высокая (для HTTP) | **Критически высокая** |
| **Влияние на оборудование** | Требует доп. сервера в LAN | Требует доп. сервера в LAN | Работает на уровне модема |

---

## **6. Влияние оборудования (Gateway Variance) и протоколов**

При выборе стратегии необходимо учитывать гетерогенность оборудования, предоставляемого T-Mobile.

### **6.1. Специфика шлюзов (Gateways)**

На сети используются модели от разных вендоров: Nokia, Arcadyan (KVD21), Sagemcom (Fast 5688W).

* **Sagemcom Fast 5688W:** Пользователи сообщают о проблемах с реализацией VPN Passthrough (пропуск VPN-трафика) и периодических сбоях Ethernet-порта при высоких нагрузках.45 Известны случаи, когда шлюз блокировал исходящий GRE-трафик (PPTP) или IPsec ESP.  
* **Arcadyan/Nokia:** Демонстрируют большую стабильность при работе с исходящими UDP-туннелями (WireGuard).

**Рекомендация:** Если клиент столкнется с необъяснимыми разрывами туннеля на Sagemcom, целесообразно запросить замену оборудования на Arcadyan или использовать промежуточный роутер, который будет инкапсулировать трафик в стандартный HTTPS (SSL VPN), менее чувствительный к фильтрации.

### **6.2. Протоколы: TCP vs UDP в нестабильной среде**

Мобильная сеть 5G подвержена **джиттеру** (вариации задержки) и **bufferbloat** (переполнению буферов).

* **WireGuard (UDP):** Предпочтителен из-за высокой скорости и быстрого восстановления. Однако, если T-Mobile агрессивно шейпит UDP (замедлят трафик), производительность может упасть.  
* **OpenVPN (TCP):** Использование TCP внутри TCP (туннель поверх TCP-соединения) считается антипаттерном ("TCP Meltdown problem"). При потере пакетов в радиоканале оба протокола TCP (внешний и внутренний) начинают процедуру ретрансмиссии, что приводит к экспоненциальному падению скорости. Тем не менее, TCP-туннель на порт 443 (маскировка под HTTPS) является самым надежным способом пробить любой фаервол, если WireGuard блокируется.

---

## **7. Синтез и рекомендации по реализации**

На основании проведенного исследования, для клиента ꆜ предлагается следующий план действий, ранжированный по степени надежности и соответствия требованиям "Network Expert".

### **7.1. Сценарий №1: "The Professional Fix" (Миграция на Static IP)**

Это наиболее чистое инженерное решение. Клиенту рекомендуется обратиться в T-Mobile Business Sales с запросом на миграцию аккаунта на "Small Business Internet" с опцией "Static IP".

* **Обоснование:** Полное устранение CGNAT, нативная поддержка всех входящих соединений, отсутствие необходимости в поддержке сложных Linux-серверов и скриптов.  
* **Стоимость:** Незначительное увеличение ежемесячного платежа (~$3 за IP).

### **7.2. Сценарий №2: "The Expert Workaround" (VPS + WireGuard)**

Если миграция на бизнес-тариф невозможна, необходимо развернуть VPS-релей.

1. **Инфраструктура:** Развернуть VPS (Ubuntu 22.04/24.04) на облачной платформе с минимальной задержкой до локации клиента (Meriden, US).  
2. **Протокол:** WireGuard.  
3. **Конфигурация MTU:** Жестко задать MTU = 1280 в конфигах wg0 на обоих концах (Client и Server).  
4. **Keepalive:** Установить PersistentKeepalive = 20 на стороне клиента (T-Mobile).  
5. **Маршрутизация:** Настроить iptables на VPS для DNAT (Destination NAT) портов на внутренний IP туннеля.

**Пример конфигурации (фрагмент для клиента):**

Ini, TOML

#### Client Config (T-Mobile side)  
[Interface]  
PrivateKey = <Client_Private_Key>  
Address = 10.10.10.2/24  
DNS = 1.1.1.1  
MTU = 1280  <-- КРИТИЧЕСКИ ВАЖНО

[Peer]  
PublicKey = <Server_Public_Key>  
Endpoint = <VPS_Public_IP>:51820  
AllowedIPs = 0.0.0.0/0  
PersistentKeepalive = 20 <-- КРИТИЧЕСКИ ВАЖНО

### **7.3. Сценарий №3: "The Easy Path" (Tailscale)**

Для быстрого доступа без сложной настройки маршрутизации рекомендуется использовать Tailscale.

* Установить Tailscale на целевое устройство.  
* Если прямое соединение не устанавливается (статус "Relay"), проверить настройки локального фаервола, но смириться с тем, что трафик пойдет через DERP-серверы Tailscale.

## **8. Заключение**

Проблема, с которой столкнулся ꆜ, является фундаментальным ограничением архитектуры 464XLAT/CGNAT, используемой T-Mobile. Прямое "открытие портов" на модеме технически невозможно, так как публичный IP-адрес не принадлежит абоненту.

Решение задачи требует сдвига парадигмы от "ожидания входящих соединений" к "инициации исходящих туннелей". Использование VPS с правильно настроенным MTU (1280 байт) и Keepalive-механизмами обеспечивает надежный обход ограничений, превращая недостаток архитектуры провайдера в управляемую, безопасную оверлейную сеть. Однако, для бизнеса наиболее устойчивым решением в долгосрочной перспективе остается переход на статический IP в рамках бизнес-контракта.

#### **Works cited**

1. T-Mobile Home Internet Port Forwarding & Bypass CGNAT - PureVPN, accessed November 24, 2025, [https://www.purevpn.com/blog/t-mobile-cgnat-port-forwarding/](https://www.purevpn.com/blog/t-mobile-cgnat-port-forwarding/)  
2. PortFowarding T-Mobile Home Internet - Channels Community, accessed November 24, 2025, [https://community.getchannels.com/t/portfowarding-t-mobile-home-internet/32162](https://community.getchannels.com/t/portfowarding-t-mobile-home-internet/32162)  
3. Case Study: T-Mobile US Goes IPv6-only Using 464XLAT - Internet Society, accessed November 24, 2025, [https://www.internetsociety.org/deploy360/2014/case-study-t-mobile-us-goes-ipv6-only-using-464xlat/](https://www.internetsociety.org/deploy360/2014/case-study-t-mobile-us-goes-ipv6-only-using-464xlat/)  
4. TMobile ISP blocked ports and port forwarding? : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/tb20gx/tmobile_isp_blocked_ports_and_port_forwarding/](https://www.reddit.com/r/tmobileisp/comments/tb20gx/tmobile_isp_blocked_ports_and_port_forwarding/)  
5. Almost a year ago, I used to have Tmobile Home 5G. Are the bugs still there. Are there new features? : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/r25ly1/almost_a_year_ago_i_used_to_have_tmobile_home_5g/](https://www.reddit.com/r/tmobileisp/comments/r25ly1/almost_a_year_ago_i_used_to_have_tmobile_home_5g/)  
6. Tmobile home internet doesn't let you portfoward. Here's how to port forward easy - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1llhpab/tmobile_home_internet_doesnt_let_you_portfoward/](https://www.reddit.com/r/tmobileisp/comments/1llhpab/tmobile_home_internet_doesnt_let_you_portfoward/)  
7. Port forwarding with T-Mobile Home Internet :( : r/HomeNetworking - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/HomeNetworking/comments/1g0am6k/port_forwarding_with_tmobile_home_internet/](https://www.reddit.com/r/HomeNetworking/comments/1g0am6k/port_forwarding_with_tmobile_home_internet/)  
8. T-Mobile Home Internet Port Forwarding (Getting Started) | LocalXpose Blog, accessed November 24, 2025, [https://localxpose.io/blog/t-mobile-home-internet-port-forwarding](https://localxpose.io/blog/t-mobile-home-internet-port-forwarding)  
9. T-Mobile home internet won't connect to VPN- and my job demands Ethernet access : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1apf562/tmobile_home_internet_wont_connect_to_vpn_and_my/](https://www.reddit.com/r/tmobileisp/comments/1apf562/tmobile_home_internet_wont_connect_to_vpn_and_my/)  
10. Connection types · Tailscale Docs, accessed November 24, 2025, [https://tailscale.com/kb/1257/connection-types](https://tailscale.com/kb/1257/connection-types)  
11. Direct Tailscale Connection (Instead of Relay) - Networking - Level1Techs Forums, accessed November 24, 2025, [https://forum.level1techs.com/t/direct-tailscale-connection-instead-of-relay/237499](https://forum.level1techs.com/t/direct-tailscale-connection-instead-of-relay/237499)  
12. Thoughts on T-Mobile 5G Internet? | ServeTheHome Forums, accessed November 24, 2025, [https://forums.servethehome.com/index.php?threads/thoughts-on-t-mobile-5g-internet.37127/](https://forums.servethehome.com/index.php?threads/thoughts-on-t-mobile-5g-internet.37127/)  
13. T-Mobile USA IPv6-only network causes IPv4 default gateway redirection failure · Issue #1268 · schwabe/ics-openvpn - GitHub, accessed November 24, 2025, [https://github.com/schwabe/ics-openvpn/issues/1268](https://github.com/schwabe/ics-openvpn/issues/1268)  
14. WireGuard MTU fixes - Kerem Erkan, accessed November 24, 2025, [https://keremerkan.net/posts/wireguard-mtu-fixes/](https://keremerkan.net/posts/wireguard-mtu-fixes/)  
15. Wireguard's minimum MTU for IPv6-over-IPv4 tunnels | Mathias' Blog, accessed November 24, 2025, [https://blog.calenhad.com/posts/2025/01/wireguard-ipv6-mtu/](https://blog.calenhad.com/posts/2025/01/wireguard-ipv6-mtu/)  
16. iOS, T-Mobile USA and IPv6 WireGuard issues. - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/WireGuard/comments/p0jeau/ios_tmobile_usa_and_ipv6_wireguard_issues/](https://www.reddit.com/r/WireGuard/comments/p0jeau/ios_tmobile_usa_and_ipv6_wireguard_issues/)  
17. Troubleshooting guide · Tailscale Docs, accessed November 24, 2025, [https://tailscale.com/kb/1023/troubleshooting](https://tailscale.com/kb/1023/troubleshooting)  
18. T-Mobile MTU issue - AllStarLink Discussion Groups, accessed November 24, 2025, [https://community.allstarlink.org/t/t-mobile-mtu-issue/23642](https://community.allstarlink.org/t/t-mobile-mtu-issue/23642)  
19. Easy app to find the right MTU value for T-Mobile, and how to change it in Windows or using a spare router - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/mb6kr9/easy_app_to_find_the_right_mtu_value_for_tmobile/](https://www.reddit.com/r/tmobileisp/comments/mb6kr9/easy_app_to_find_the_right_mtu_value_for_tmobile/)  
20. T-Mobile LTE breaks tailscale connectivity due to CGNAT and/or IPv6-only #302 - GitHub, accessed November 24, 2025, [https://github.com/tailscale/tailscale/issues/302](https://github.com/tailscale/tailscale/issues/302)  
21. Fixing VPN and VPC Connectivity Issues with T-Mobile Home Internet - DEV Community, accessed November 24, 2025, [https://dev.to/joehoppe/fixing-vpn-and-vpc-connectivity-issues-with-t-mobile-home-internet-4gn1](https://dev.to/joehoppe/fixing-vpn-and-vpc-connectivity-issues-with-t-mobile-home-internet-4gn1)  
22. T-Mobile Port Forwarding - Pinggy, accessed November 24, 2025, [https://pinggy.io/blog/tmobile_port_forwarding/](https://pinggy.io/blog/tmobile_port_forwarding/)  
23. Bypassing Port Forwarding Restrictions on T-Mobile Home Internet Using Pinggy, accessed November 24, 2025, [https://dev.to/lightningdev123/bypassing-port-forwarding-restrictions-on-t-mobile-home-internet-using-pinggy-3me6](https://dev.to/lightningdev123/bypassing-port-forwarding-restrictions-on-t-mobile-home-internet-using-pinggy-3me6)  
24. T-Mobile home internet: port forwarding : r/tmobile - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/zzbxkv/tmobile_home_internet_port_forwarding/](https://www.reddit.com/r/tmobile/comments/zzbxkv/tmobile_home_internet_port_forwarding/)  
25. Wireguard and DDNS server on T-Mobile 5g home with GL-X3000? - VPN, DNS, Leaks, accessed November 24, 2025, [https://forum.gl-inet.com/t/wireguard-and-ddns-server-on-t-mobile-5g-home-with-gl-x3000/41403](https://forum.gl-inet.com/t/wireguard-and-ddns-server-on-t-mobile-5g-home-with-gl-x3000/41403)  
26. WireGuard connection doesn't save persistent-keepalive value - Fedora Discussion, accessed November 24, 2025, [https://discussion.fedoraproject.org/t/wireguard-connection-doesnt-save-persistent-keepalive-value/72262](https://discussion.fedoraproject.org/t/wireguard-connection-doesnt-save-persistent-keepalive-value/72262)  
27. Is PersistentKeepalive < 25s being ignored? : r/WireGuard - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/WireGuard/comments/180m3i5/is_persistentkeepalive_25s_being_ignored/](https://www.reddit.com/r/WireGuard/comments/180m3i5/is_persistentkeepalive_25s_being_ignored/)  
28. Wireguard android client requires persistent keepalive - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/WireGuard/comments/1h43n8e/wireguard_android_client_requires_persistent/](https://www.reddit.com/r/WireGuard/comments/1h43n8e/wireguard_android_client_requires_persistent/)  
29. Relay vs direct connection - Tailscale - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/Tailscale/comments/1hb39xm/relay_vs_direct_connection/](https://www.reddit.com/r/Tailscale/comments/1hb39xm/relay_vs_direct_connection/)  
30. ZeroTier broken with T-Mobile at Home ISP : r/mikrotik - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/mikrotik/comments/14797wz/zerotier_broken_with_tmobile_at_home_isp/](https://www.reddit.com/r/mikrotik/comments/14797wz/zerotier_broken_with_tmobile_at_home_isp/)  
31. Slow/Unstable TCP over Zerotier on T-Mobile Home internet (5G), accessed November 24, 2025, [https://discuss.zerotier.com/t/slow-unstable-tcp-over-zerotier-on-t-mobile-home-internet-5g/3132](https://discuss.zerotier.com/t/slow-unstable-tcp-over-zerotier-on-t-mobile-home-internet-5g/3132)  
32. Unstable connections over T-Mobile 5G Home Internet while using ZT - Linux, accessed November 24, 2025, [https://discuss.zerotier.com/t/unstable-connections-over-t-mobile-5g-home-internet-while-using-zt/19554](https://discuss.zerotier.com/t/unstable-connections-over-t-mobile-5g-home-internet-while-using-zt/19554)  
33. Arbitrary TCP · Cloudflare One docs, accessed November 24, 2025, [https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/arbitrary-tcp/](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/arbitrary-tcp/)  
34. Connect with cloudflared · Cloudflare One docs, accessed November 24, 2025, [https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/)  
35. TCP tunnel - Cloudflare Community, accessed November 24, 2025, [https://community.cloudflare.com/t/tcp-tunnel/489646](https://community.cloudflare.com/t/tcp-tunnel/489646)  
36. Terms of Use - Cloudflare, accessed November 24, 2025, [https://www.cloudflare.com/website-terms/](https://www.cloudflare.com/website-terms/)  
37. Cloudflare Self-Serve Subscription Agreement, accessed November 24, 2025, [https://www.cloudflare.com/terms/](https://www.cloudflare.com/terms/)  
38. Goodbye, section 2.8 and hello to Cloudflare's new terms of service, accessed November 24, 2025, [https://blog.cloudflare.com/updated-tos/](https://blog.cloudflare.com/updated-tos/)  
39. Can someone clarify Cloudflare Tunnel's ToS for video content? - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/CloudFlare/comments/1it2a7v/can_someone_clarify_cloudflare_tunnels_tos_for/](https://www.reddit.com/r/CloudFlare/comments/1it2a7v/can_someone_clarify_cloudflare_tunnels_tos_for/)  
40. WireGuard behind CGNAT 5G Connection (T-Mobile 5G Business Internet) - Firewalla, accessed November 24, 2025, [https://help.firewalla.com/hc/en-us/community/posts/38610335671443-WireGuard-behind-CGNAT-5G-Connection-T-Mobile-5G-Business-Internet](https://help.firewalla.com/hc/en-us/community/posts/38610335671443-WireGuard-behind-CGNAT-5G-Connection-T-Mobile-5G-Business-Internet)  
41. Connect your Devices to T-Mobile Internet | T-Mobile 5G Home Internet, accessed November 24, 2025, [https://www.t-mobile.com/support/home-internet/connect](https://www.t-mobile.com/support/home-internet/connect)  
42. My experience trying to get a static IP for my business : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/11t4yau/my_experience_trying_to_get_a_static_ip_for_my/](https://www.reddit.com/r/tmobileisp/comments/11t4yau/my_experience_trying_to_get_a_static_ip_for_my/)  
43. T-Mobile Static IP's ARE Possible : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/wq1hm3/tmobile_static_ips_are_possible/](https://www.reddit.com/r/tmobileisp/comments/wq1hm3/tmobile_static_ips_are_possible/)  
44. Small Business Internet Service | T-Mobile for Business, accessed November 24, 2025, [https://www.t-mobile.com/business/solutions/business-internet-services/small-business-internet](https://www.t-mobile.com/business/solutions/business-internet-services/small-business-internet)  
45. VPN Connectivity on Sagemcom vs Arcadyan : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/12y3lca/vpn_connectivity_on_sagemcom_vs_arcadyan/](https://www.reddit.com/r/tmobileisp/comments/12y3lca/vpn_connectivity_on_sagemcom_vs_arcadyan/)  
46. I have tested over time the 3 gateways, Nokia, Arcadyan and Sagemcom, my personal experience tells me the Sagemcom is the best of the 3, stable and fast : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/168kggu/i_have_tested_over_time_the_3_gateways_nokia/](https://www.reddit.com/r/tmobileisp/comments/168kggu/i_have_tested_over_time_the_3_gateways_nokia/)

# 10.
## 10.1.
`D𐊑⠿` ≔ ⠿~ (Заблуждения `ꆜ` относительно `P⁎`)

## 10.2.
`D𐊑ᵢ` : `D𐊑⠿`

## 10.3.
`Pⰳ(D𐊑ᵢ)` ≔
```
Правдоподобность `D𐊑ᵢ`.
Правдоподобность заблуждения `D𐊑ᵢ` означает оценку того, насколько утверждение `D𐊑ᵢ` действительно является заблуждением `ꆜ`. 
```

# 11. Анализ `D𐊑⠿` №1 (выполнен Gemini Deep Think)
https://gemini.google.com/share/9e327a4b9e0b

## 1. Множество потенциальных заблуждений `ꆜ` (`D𐊑⠿`)

Анализ описания проекта (`PD`), онтологии предметной области (`O.md`) и результатов глубинного исследования (`O.md`::§8, `O.md`::§9) позволил выявить следующие ключевые потенциальные заблуждения клиента (`ꆜ`) относительно проекта (`P⁎`).

`D𐊑⠿` ≔

```ini
- D𐊑₁: (Стратегическое заблуждение: Убеждённость в абсолютной невозможности решения проблемы на уровне оператора и игнорирование опции Static IP.)
- D𐊑₂: (Архитектурное заблуждение: Предположение, что внешняя инфраструктура (Cloud/VPS) является опциональной для реализации VPN-решения в условиях CGNAT.)
- D𐊑₃: (Техническое заблуждение: Завышенные ожидания стабильности и производительности обходного пути из-за недооценки специфических проблем сети T-Mobile (464XLAT/CGNAT).)
- D𐊑₄: (Операционное заблуждение: Недооценка сложности и необходимых навыков для долгосрочного управления и поддержки технического обходного решения.)
```

## 2. Анализ и оценка `D𐊑⠿`

### 2.1. `D𐊑₁`: Стратегическое заблуждение (Невозможность официального решения)

`D𐊑₁` ≔ (Убеждённость в абсолютной невозможности решения проблемы на уровне оператора и игнорирование опции Static IP.)

#### 2.1.1. Доводы за `Pⰳ(D𐊑₁)`

1.  **Категоричное утверждение клиента:** Клиент заявляет: «I already confirmed with T-Mobile support that they cannot open ports on their network, so this will require a workaround solution» (`O.md`::§2.3). Это формирует ложную предпосылку, исключающую любые решения, кроме технических обходов.
2.  **Существование архитектурного решения:** T-Mobile предоставляет услугу Static IP для бизнес-клиентов. Эта услуга переводит абонента на специализированный APN (`b2b.static`), минуя CGNAT и фильтрацию входящего трафика, тем самым устраняя корень проблемы (`O.md`::§8.6, `O.md`::§9.5).
3.  **Ограниченность консультации:** Клиент, вероятно, общался со службой поддержки потребительского сегмента (Home Internet), которая дала верный ответ в рамках текущего тарифа, но не проинформировала о возможностях бизнес-сегмента.
4.  **Требования к надёжности:** Клиент из сектора «Manufacturing & Construction» (`O.md`::§5.2.1). Для бизнеса нативная маршрутизация через Static IP обеспечивает максимальную надёжность («Golden Standard») по сравнению с любыми «workarounds» (`O.md`::§8.7.1). Фокус на сложных технических обходах предполагает незнание о более простом и надёжном пути.

#### 2.1.2. Доводы против `Pⰳ(D𐊑₁)`

1.  **Неуказанные ограничения:** Теоретически, клиент мог исследовать опцию Static IP и отвергнуть её по причинам, не указанным в `PD` (например, нежелание оформлять бизнес-аккаунт или административные барьеры).

#### 2.1.3. Вердикт по `D𐊑₁`

Это высоковероятное и критически важное стратегическое заблуждение. Клиент исходит из ложной предпосылки о том, что проблема нерешаема на уровне провайдера, и фокусируется на сложных способах борьбы с симптомами (обходные пути) вместо устранения причины (смена класса обслуживания).

#### 2.1.4. Оценка `Pⰳ(D𐊑₁)`

**90/100**

-----

### 2.2. `D𐊑₂`: Архитектурное заблуждение (Опциональность внешней инфраструктуры)

`D𐊑₂` ≔ (Предположение, что внешняя инфраструктура (Cloud/VPS) является опциональной для реализации VPN-решения в условиях CGNAT.)

#### 2.2.1. Доводы за `Pⰳ(D𐊑₂)`

1.  **Ключевое слово "Optionally":** В `PD` клиент пишет: «**Optionally** advise if Google Cloud, or similar cloud services, can be used as a relay...» (`O.md`::§2.3). Использование слова "Optionally" указывает на то, что клиент рассматривает облачный ретранслятор как необязательный компонент или альтернативный путь.
2.  **Архитектурная необходимость:** В среде CGNAT локальное устройство не имеет публичного IP. Для обеспечения входящего доступа с помощью VPN (WireGuard/SSL VPN) один из узлов туннеля *обязательно* должен находиться вне сети CGNAT и иметь публичный IP-адрес (т.е. VPS или облачный сервер), выступая в роли ретранслятора (`O.md`::§8.3.1, `O.md`::§9.4.1). Без этого компонента входящие соединения невозможны.
3.  **Интерпретация совета T-Mobile:** Поддержка предложила "SSL VPN" и "WireGuard" как решения. Клиент мог предположить, что достаточно настроить эти протоколы локально, не понимая, что они требуют внешнего сервера-посредника для обхода CGNAT.

#### 2.2.2. Доводы против `Pⰳ(D𐊑₂)`

1.  **Осведомлённость о технологиях:** Клиент знаком с терминами "relay, tunnel, or reverse proxy workaround", что указывает на базовое понимание необходимости посредников.

#### 2.2.3. Вердикт по `D𐊑₂`

Формулировка "Optionally" является сильным индикатором архитектурного заблуждения. Клиент, вероятно, не осознает, что внешний сервер (Cloud Relay/VPS) — это не отдельное опциональное решение, а обязательный компонент инфраструктуры для того, чтобы предложенные T-Mobile VPN-технологии сработали для входящих соединений.

#### 2.2.4. Оценка `Pⰳ(D𐊑₂)`

**85/100**

-----

### 2.3. `D𐊑₃`: Техническое заблуждение (Ожидания стабильности и производительности)

`D𐊑₃` ≔ (Завышенные ожидания стабильности и производительности обходного пути из-за недооценки специфических проблем сети T-Mobile (464XLAT/CGNAT).)

#### 2.3.1. Доводы за `Pⰳ(D𐊑₃)`

Клиент требует «reliable workaround» и «stable inbound connections» (`O.md`::§2.3), но не упоминает о специфических проблемах сети T-Mobile, которые делают достижение этой стабильности нетривиальной инженерной задачей.

1.  **Проблемы MTU в 464XLAT:** Архитектура T-Mobile (464XLAT) инкапсулирует IPv4 в IPv6, что уменьшает эффективный MTU ниже стандарта (`O.md`::§9.3.1). Стандартные настройки VPN часто приводят к потере пакетов («PMTUD Black Hole») и фатальной нестабильности (`O.md`::§9.3.2). Требуется ручная тонкая настройка MTU (обычно до 1280–1360 байт).
2.  **Агрессивные тайм-ауты CGNAT:** Оборудование CGNAT быстро сбрасывает неактивные сессии (`O.md`::§8.2.3). Для поддержания VPN-туннеля требуется обязательная настройка `PersistentKeepalive` (каждые 20-25 секунд) на стороне клиента, чтобы предотвратить разрыв соединения (`O.md`::§8.3.3.2).
3.  **Риск "TCP Meltdown":** Клиент ставит SSL VPN (часто TCP) в один ряд с WireGuard (UDP). Использование TCP-туннелей в мобильных сетях чревато феноменом "TCP Meltdown", который приводит к экспоненциальному падению производительности (`O.md`::§9.6.2).

Отсутствие упоминания этих критических параметров предполагает, что клиент ожидает стабильности от стандартной конфигурации VPN.

#### 2.3.2. Доводы против `Pⰳ(D𐊑₃)`

1.  **Делегирование экспертизы:** Клиент нанимает «Network Specialist» для решения технических проблем и обеспечения стабильности. Незнание специфических параметров является причиной найма эксперта, а не обязательно заблуждением о лёгкости достижения стабильности.

#### 2.3.3. Вердикт по `D𐊑₃`

Крайне маловероятно, что клиент осведомлён о неочевидных и специфических проблемах (MTU, Keepalive, TCP Meltdown), критичных для работы туннелей в сети T-Mobile. Он, вероятно, полагает, что стабильность будет достигнута стандартными средствами, тогда как в реальности она потребует глубокой технической оптимизации и всё равно будет ограничена природой сотовой связи.

#### 2.3.4. Оценка `Pⰳ(D𐊑₃)`

**90/100**

-----

### 2.4. `D𐊑₄`: Операционное заблуждение (Сложность управления)

`D𐊑₄` ≔ (Недооценка сложности и необходимых навыков для долгосрочного управления и поддержки технического обходного решения.)

#### 2.4.1. Доводы за `Pⰳ(D𐊑₄)`

1.  **Намерение самоуправления:** Клиент запрашивает: «Provide instructions so I can manage it afterward» (`O.md`::§2.3). Это подразумевает намерение взять на себя ответственность за поддержку решения.
2.  **Сложность оптимального решения:** Если будет реализовано наиболее контролируемое техническое решение (например, VPS Relay на базе WireGuard, как рекомендовано в `O.md`::§8.7.2, `O.md`::§9.7.2), оно потребует навыков администрирования Linux. Управление VPS включает мониторинг, обновление, обеспечение безопасности, управление сложной маршрутизацией (`iptables`, NAT) и диагностику сетевых проблем (`O.md`::§8.3.3).
3.  **Профиль клиента:** Маловероятно, что у клиента из строительного сектора есть необходимые компетенции для поддержки такой инфраструктуры.

#### 2.4.2. Доводы против `Pⰳ(D𐊑₄)`

1.  **Возможность простого решения:** Если будет выбрано решение на основе управляемых сервисов (например, Tailscale), сложность управления действительно низка (`O.md`::§8.4). В этом случае ожидания клиента реалистичны, но это может противоречить требованиям к стабильности и производительности (см. `D𐊑₃` и `O.md`::§8.4.3).

#### 2.4.3. Вердикт по `D𐊑₄`

Учитывая запрос на "best method" и "reliable workaround", оптимальное решение (VPS Relay) требует значительных усилий по поддержке. Если такое решение будет передано нетехническому клиенту с намерением самоуправления, вероятность недооценки сложности управления и рисков простоя высока.

#### 2.4.4. Оценка `Pⰳ(D𐊑₄)`

**75/100**

# 12. Анализ `D𐊑⠿` №2 (выполнен Gemini Deep Research)
https://gemini.google.com/share/20fd91f64e3c


## **1. Введение и определение проблемы: Природа заблуждения клиента (D𐊑⠿)**

### **1.1 Архитектурный диссонанс ожиданий и реальности**

Центральной осью анализируемого запроса является фундаментальное заблуждение клиента (ꆜ), инициировавшего проект P⁎ на платформе Upwork. Клиент формулирует задачу как стандартную процедуру настройки сетевого оборудования: «настроить проброс портов» (Port Forwarding) на шлюзе T-Mobile Home Internet (TMHI). Данная формулировка подразумевает наличие у клиента ментальной модели, сформированной десятилетиями использования традиционных проводных провайдеров (кабельного интернета DOCSIS или DSL), где абонентскому оборудованию (CPE) присваивается уникальный, пусть и динамический, публичный IPv4-адрес. В такой парадигме маршрутизатор выступает в роли граничного устройства, отделяющего локальную сеть (LAN) от глобальной сети Интернет (WAN), и обладает полным контролем над таблицами трансляции сетевых адресов (NAT), позволяя администратору (или пользователю) явно указывать правила перенаправления входящего трафика на внутренние хосты.1

Однако реальность архитектуры 5G Fixed Wireless Access (FWA), развернутой оператором T-Mobile, радикально отличается от этой модели. Ключевое заблуждение (D𐊑⠿) заключается в непонимании того факта, что абонентский шлюз в сети T-Mobile не является граничным устройством сети Интернет в классическом понимании. Он функционирует внутри глубоко эшелонированной частной сети оператора, находясь за несколькими слоями трансляции адресов операторского класса (Carrier-Grade NAT — CGNAT).3 Клиент воспринимает невозможность открытия портов как программную недоработку, ошибку конфигурации («нужно просто найти правильную галочку») или неисправность конкретного устройства. В действительности же мы сталкиваемся с фундаментальным ограничением топологии сети, где понятие «входящее соединение» для потребительского сегмента отсутствует как класс на уровне протокола IPv4.2

### **1.2 Масштаб проблемы и контекст задачи**

Проект P⁎, по сути, представляет собой попытку преодолеть законы физики сетевой маршрутизации с помощью настроек пользовательского интерфейса. T-Mobile использует нативную сеть IPv6, а для обеспечения доступа к ресурсам IPv4 применяет механизм перехода 464XLAT. В этой схеме IPv4-адрес, который клиент видит на сайтах проверки IP, является общим для сотен или тысяч абонентов в конкретном географическом кластере. Попытка инициировать соединение с этим адресом извне обречена на провал, так как маршрутизаторы на границе сети T-Mobile не имеют записи в таблице маршрутизации, связывающей конкретный входящий порт с конкретным шлюзом пользователя.1 Пакет просто отбрасывается, не достигая даже уровня CGNAT.

Для фрилансера, берущегося за выполнение данной задачи, критически важно переквалифицировать запрос с «настройки роутера» на «проектирование оверлейной сети» или «миграцию на бизнес-тариф». Без этого сдвига парадигмы проект обречен на провал, так как технические средства для реализации прямой адресации на потребительском оборудовании T-Mobile отсутствуют физически и логически.5 Настоящий отчет призван детально разобрать каждый слой этого технического стека, от физического уровня радиоинтерфейса до прикладного уровня VPN-туннелей, чтобы обосновать невозможность решения задачи «в лоб» и предложить единственно возможные, хотя и сложные, обходные пути.

---

## **2. Анализ сетевой топологии: CGNAT и 464XLAT как непреодолимые барьеры**

### **2.1 Механика Carrier-Grade NAT (CGNAT) в сетях 5G**

Carrier-Grade NAT (CGNAT), также известный как Large Scale NAT (LSN), является вынужденной мерой в условиях исчерпания адресного пространства IPv4. В классической сети домашнего провайдера каждому модему выдается один публичный IP-адрес. В сети T-Mobile этот публичный адрес присваивается шлюзу трансляции (Provider-Side Translator — PLAT), находящемуся глубоко в ядре сети оператора. Абонентские устройства получают адреса из специального диапазона (часто 192.0.0.0/8 или 100.64.0.0/10, зарезервированного RFC 6598), которые не маршрутизируются в глобальном интернете.3

Это создает ситуацию, известную как "Hard NAT". В отличие от "Full Cone NAT", который часто встречается в домашних роутерах и позволяет относительно легко устанавливать P2P-соединения (STUN/TURN), CGNAT T-Mobile часто ведет себя как "Symmetric NAT". Это означает, что сопоставление внутреннего IP:порта и внешнего IP:порта зависит от адреса назначения. Такой динамизм делает невозможным предсказание внешнего порта, что критически важно для работы игровых серверов, VoIP и прямых VPN-соединений без посредников.6 Исследование показывает, что CGNAT блокирует весь «незапрошенный входящий трафик» (unsolicited inbound traffic), что делает традиционный проброс портов бессмысленным: даже если открыть порт на абонентском шлюзе, пакет из интернета будет отброшен еще на входе в сеть провайдера, так как PLAT не знает, кому из тысяч абонентов переслать пакет, пришедший на порт 80 или 443 общего IP-адреса.3

### **2.2 Технология 464XLAT: Иллюзия IPv4**

Для обеспечения совместимости устройств и приложений, работающих только по протоколу IPv4, в чисто IPv6-сети (IPv6-only core), T-Mobile использует архитектуру 464XLAT (RFC 6877). Эта система состоит из двух компонентов:

1. **CLAT (Customer-Side Translator):** Модуль, работающий на стороне абонентского устройства (шлюза или смартфона). Он перехватывает исходящие IPv4-пакеты от локальных устройств (ПК, консоли) и инкапсулирует их в пакеты IPv6 для транспортировки через сеть оператора.  
2. **PLAT (Provider-Side Translator):** Модуль на границе сети оператора, который распаковывает IPv6-пакеты обратно в IPv4 и отправляет их в глобальный интернет. Обратный процесс происходит симметрично.2

Для конечного пользователя эта трансляция прозрачна, но она вносит существенные ограничения. Во-первых, это дополнительные накладные расходы на заголовок пакета, что снижает эффективный размер MTU (Maximum Transmission Unit), о чем будет подробно сказано в разделе 6. Во-вторых, CLAT на потребительских шлюзах T-Mobile (Nokia, Arcadyan, Sagemcom) жестко настроен и не поддается конфигурированию пользователем. Невозможно отключить CLAT или изменить параметры трансляции. Это подтверждается отчетами пользователей, которые отмечают, что раздел NAT Forwarding в интерфейсе шлюзов либо отсутствует, либо неактивен, так как он неприменим в контексте 464XLAT для входящих соединений.7

### **2.3 Политики фильтрации входящего трафика IPv6**

Существует гипотеза, что проблему CGNAT можно обойти, используя нативный протокол IPv6, так как T-Mobile выделяет каждому абоненту глобально маршрутизируемый префикс /64. Теоретически это позволяет каждому устройству в домашней сети иметь свой уникальный публичный адрес, доступный из любой точки мира. Однако на практике T-Mobile применяет агрессивные политики межсетевого экранирования (Stateful Firewall) на границе своей сети для потребительских тарифов.

Исследования 6 подтверждают, что T-Mobile блокирует *все* входящие инициирующие соединения к IPv6-адресам абонентов, включая ICMPv6 (Ping) и UDP/TCP-пакеты, если они не являются ответом на ранее установленное исходящее соединение. Пользователи, пытавшиеся настроить IPv6-туннели на продвинутых маршрутизаторах (pfSense, Firewalla), сообщают о полной недоступности своих устройств извне, несмотря на наличие корректных глобальных адресов. Блокировка происходит выше по течению (upstream), на оборудовании оператора, и отключение фаервола на самом абонентском шлюзе не дает результата. Это окончательно разрушает надежды на простой обход CGNAT через переход на IPv6 без использования дополнительных туннелей.7

---

## **3. Аппаратные ограничения и анализ потребительского оборудования**

### **3.1 Сравнительный анализ шлюзов**

Для полноты картины необходимо рассмотреть парк оборудования, предоставляемого T-Mobile. Клиент с вероятностью 99% использует одно из потребительских устройств, функциональность которых намеренно урезана ("dumbed down") для минимизации обращений в поддержку.

| Модель шлюза | Производитель | Чипсет | Поддержка Static IP | Режим моста (Bridge Mode) | Проброс портов (Port Forwarding) | Примечания |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **KVD21** | Arcadyan | MediaTek T750 | **Нет** | Нет | Нет | Ограниченная прошивка, скрытые меню заблокированы в последних обновлениях.8 |
| **Fast 5688W** | Sagemcom | Qualcomm SDX62 | **Нет** | Нет | Нет | Известен проблемами с перегревом и нестабильным Ethernet-портом. "Double NAT" неизбежен.8 |
| **Nokia 5G21** | Nokia | Nokia | **Нет** | Нет | Нет | Старая модель, функционал аналогичен Arcadyan. Полное отсутствие настроек WAN.8 |
| **G4AR / G4SE** | Arcadyan/Sercomm | MediaTek T830 | **Нет** | Нет | Нет | Новейшие модели с поддержкой внешних антенн, но прошивка все так же заблокирована для входящих соединений.10 |
| **FX2000 / FX3100** | Inseego | Qualcomm SDX55/62 | **Да** | IP Passthrough (частичный) | **Да** | Единственные устройства, поддерживающие профиль управления APN для статического IP. Доступны *только* для бизнес-аккаунтов.5 |

### **3.2 Невозможность режима моста и проблема двойного NAT**

В отличие от кабельных модемов, которые можно перевести в прозрачный режим моста (Bridge Mode), передав публичный IP-адрес на роутер пользователя (например, Ubiquiti Dream Machine или ASUS RT-AX88U), шлюзы T-Mobile (Arcadyan, Sagemcom) всегда работают в режиме маршрутизатора. Даже если пользователь подключает свой собственный роутер, он оказывается в ситуации двойного NAT (Double NAT): первый NAT на шлюзе T-Mobile (из LAN в CGNAT-адрес), второй NAT на собственном роутере (из своей LAN в LAN шлюза T-Mobile), и третий "NAT" на уровне оператора (CGNAT).

Такая конфигурация создает каскад проблем:

1. **Нарушение работы UPnP:** Протоколы автоматического открытия портов не могут пройти через два каскада NAT.  
2. **Сложности с VPN:** Протоколы IPSec и PPTP часто не могут установить соединение через двойной NAT из-за инкапсуляции GRE.  
3. **Недоступность DMZ:** Функция DMZ на шлюзах T-Mobile, даже если присутствует, просто перенаправляет трафик на внутренний IP, но не решает проблему блокировки трафика на уровне оператора.13

Пользователи, пытавшиеся "взломать" или найти скрытые настройки через веб-инспектор браузера или API шлюза, сообщают, что T-Mobile систематически закрывает эти возможности в обновлениях прошивки "по воздуху" (OTA updates). Следовательно, ставка на конфигурацию имеющегося у клиента оборудования — это тупиковый путь.

---

## **4. Стратегия миграции: T-Mobile Business Internet как единственное нативное решение**

### **4.1 Бюрократический аспект: Оформление бизнес-аккаунта (Sole Proprietor)**

Единственный легитимный способ получить настоящий, маршрутизируемый публичный IPv4-адрес в сети T-Mobile — это переход на тарифный план Business Internet с услугой Static IP. Вопреки распространенному мнению, для этого не требуется наличие зарегистрированной корпорации (LLC/Corp) или налогового номера работодателя (EIN). Исследование 12 подтверждает, что T-Mobile позволяет открывать бизнес-линии физическим лицам в статусе «Индивидуальный предприниматель» (Sole Proprietor), используя только номер социального страхования (SSN).

Однако здесь фрилансер сталкивается с серьезным препятствием: некомпетентность первой линии поддержки. Множественные отчеты 15 свидетельствуют о том, что рядовые сотрудники службы поддержки часто дезинформируют клиентов, заявляя, что статический IP доступен только для корпораций с EIN. Клиенту ꆜ потребуется настойчивость и, возможно, несколько звонков («Roulette support»), чтобы попасть на представителя, знающего процедуру открытия Sole Prop аккаунта.

### **4.2 Аппаратный императив: Необходимость замены шлюза на Inseego**

Критически важный нюанс: услуга Static IP технически несовместима со стандартными потребительскими шлюзами (Arcadyan/Sagemcom). Система биллинга и провижининга T-Mobile может добавить услугу статического IP ($3/мес) на аккаунт, но она *не заработает*, если у клиента нет соответствующего оборудования — роутера Inseego FX2000 или FX3100.5

Это означает, что проект P⁎ неизбежно включает в себя этап физической логистики:

1. Заказ новой линии или конвертация существующей.  
2. Запрос на отправку конкретной модели роутера (Inseego).  
3. Возврат старого оборудования.  
   Без выполнения этого условия любые манипуляции с настройками обречены на провал. Как отмечено в 18, пользователи, получившие статический IP на неправильном оборудовании, просто теряют интернет-соединение или остаются на динамическом адресе.

### **4.3 Техническая ловушка: Настройка APN b2b.static**

Даже после получения правильного роутера Inseego и активации услуги, интернет «из коробки» работать через статический IP не будет. Устройства по умолчанию настроены на APN fast.t-mobile.com или fbb.home, которые выдают динамические адреса из пула CGNAT.

Для активации статического IP необходимо вручную изменить настройки APN в административной панели роутера на b2b.static.19 Это действие часто вызывает затруднения, так как поддержка T-Mobile не всегда предоставляет эту информацию проактивно.21 Более того, интерфейс Inseego может требовать создания нового профиля подключения и назначения его активным по умолчанию, что неочевидно для рядового пользователя. Также стоит отметить, что APN b2b.static работает *только* в режиме IPv4 (или dual stack с приоритетом IPv4), и в некоторых случаях (например, в зонах 5G Standalone) может требовать принудительного переключения модема в режим NSA (Non-Standalone) или LTE, так как инфраструктура статических IP в 5G SA (Standalone) ядре T-Mobile все еще находится в стадии внедрения.23

---

## **5. Оверлейные сети и туннелирование: Программные обходные пути**

Если миграция на бизнес-аккаунт невозможна по финансовым или организационным причинам, единственной альтернативой становится создание оверлейной сети. Это программное решение, которое инициирует исходящее соединение изнутри сети (что разрешено фаерволом) к внешнему реле-серверу, через который затем маршрутизируется входящий трафик.

### **5.1 Cloudflare Tunnel (Argo): Риски и ограничения для видео**

Cloudflare Tunnel (cloudflared) — популярное решение для публикации веб-сервисов (HTTP/HTTPS). Оно не требует открытия портов и работает за любым NAT. Однако для проекта P⁎ существует критический риск, связанный с типами трафика.

Если клиент планирует использовать туннель для потокового видео (Plex, Jellyfin, Emby), использование бесплатного тарифа Cloudflare Tunnel является нарушением Условий использования (Terms of Service). Ранее это регулировалось Секцией 2.8, запрещавшей «непропорциональное количество не-HTML контента». Хотя в новой редакции ToS формулировки смягчены и перенесены в условия использования CDN, суть остается прежней: использование глобальной сети доставки контента Cloudflare для прокачки терабайтов личного видео-трафика без оплаты (через продукт Cloudflare Stream) рассматривается как злоупотребление.24 Блокировка аккаунта может произойти внезапно, что делает это решение неприемлемым для надежной долгосрочной эксплуатации («set and forget»).

### **5.2 Mesh VPN: Tailscale, ZeroTier и проблема DERP**

Tailscale и ZeroTier используют методы обхода NAT (NAT traversal) для установления прямых соединений (P2P) между устройствами. Однако в сети T-Mobile, из-за жесткого CGNAT и блокировки входящих UDP-пакетов, установка прямого соединения часто не удается.

В таких случаях Tailscale переключается на использование ретрансляторов DERP (Designated Encrypted Relay for Packets).

* **Проблема:** Трафик идет через публичные сервера Tailscale. Это вносит значительную задержку (latency) и ограничивает пропускную способность (bandwidth), так как сервера являются общим ресурсом. Пользователи сообщают о падении скорости до 1-3 Мбит/с при использовании DERP, в то время как прямое соединение могло бы выдать 50-100 Мбит/с.27  
* **Решение:** Развертывание собственного DERP-сервера (Custom DERP) на дешевом VPS, но это резко повышает сложность настройки, выходя за рамки компетенций обычного пользователя.

### **5.3 Решения на базе Reverse Proxy и SSH-туннелей**

Существуют коммерческие сервисы, такие как **Pinggy**, **LocalXpose**, **ngrok**, которые предоставляют функциональность "Port Forwarding as a Service".

* **Механизм:** Пользователь запускает клиент или выполняет команду SSH (как в случае с Pinggy: ssh -p 443 -R0:localhost:8000 qr@a.pinggy.io), которая пробрасывает локальный порт на публичный сервер сервиса.28  
* **Преимущества:** Работает мгновенно, не требует настройки роутера, обходит CGNAT.  
* **Недостатки:** Бесплатные тарифы имеют ограничения по скорости, количеству соединений и часто меняющиеся домены. Для стабильного решения требуется платная подписка ($5-10/мес), что сопоставимо со стоимостью бизнес-аккаунта T-Mobile, но менее надежно.

---

## **6. Протокольные аномалии и технические детали сбоев**

### **6.1 Проблема MTU и фрагментация пакетов**

Одной из самых коварных технических проблем при использовании VPN-туннелей (WireGuard, OpenVPN, IPSec) поверх сети T-Mobile является фрагментация пакетов, вызванная несоответствием MTU.

* **Стандарт:** Ethernet использует MTU 1500 байт.  
* **Оверхед T-Mobile:** Из-за инкапсуляции 464XLAT (IPv4 внутри IPv6) полезная нагрузка кадра уменьшается. Реальный MTU часто составляет около 1420-1440 байт, а иногда и меньше в зависимости от условий радиоканала.30  
* **Механизм сбоя:** Если VPN-клиент пытается отправить пакет размером 1500 байт (плюс заголовки VPN), пакет фрагментируется. Многие фаерволы (включая оборудование T-Mobile) настроены на отбрасывание фрагментированных пакетов (особенно UDP) для защиты от DoS-атак.  
* **Симптомы:** "SSH работает, а HTTPS виснет", "Пинг проходит, а картинки не грузятся". Это классические признаки проблемы Path MTU Discovery (PMTUD), которая часто не работает через ICMP-блокировки.  
* **Решение:** Принудительное занижение MTU (MSS Clamping) на интерфейсе туннеля. Эмпирическим путем установлено, что безопасным значением для WireGuard через T-Mobile является **1280** или **1320** байт.30 Фрилансер обязан учитывать это при настройке любого оверлея.

### **6.2 Дросселирование UDP (Throttling) и TCP Meltdown**

Многочисленные тесты пользователей 32 показывают, что T-Mobile применяет Traffic Shaping (шейпинг) к UDP-трафику, который не распознается как легитимный (например, не является известным игровым трафиком или WebRTC/QUIC). Трафик WireGuard (UDP порт 51820) часто режется до скоростей <1 Мбит/с или испытывает потерю пакетов до 50%.  
При переключении на TCP-транспорт (например, OpenVPN over TCP) скорость восстанавливается, но возникает проблема "TCP Meltdown" (инкапсуляция TCP в TCP). В условиях нестабильного сотового соединения, когда внешний TCP-пакет теряется, внутренний TCP-стек начинает повторную передачу, создавая экспоненциальный рост задержек и джиттера. Это делает TCP-туннели непригодными для чувствительных к задержкам приложений (гейминг, VoIP).  
Для обхода UDP-шейпинга продвинутые пользователи используют обфускацию (например, UDP2RAW или Shadowsocks-plugin), маскируя VPN-трафик под HTTPS/QUIC, что добавляет еще один уровень сложности в проект P⁎.

---

## **7. Сводный анализ данных и оценка осуществимости (2.2)**

### **7.1 Аргументы "ЗА" осуществимость (Pⰳ)**

1. **Существование легального пути:** Наличие бизнес-тарифов для физических лиц (Sole Proprietor) открывает прямой путь к решению проблемы через Static IP. Это документированная и поддерживаемая услуга.  
2. **Зрелость оверлейных технологий:** Инструменты вроде Tailscale и Cloudflare Tunnel достигли уровня надежности, позволяющего использовать их для большинства задач удаленного администрирования и IoT, даже в условиях жесткого NAT.

### **7.2 Аргументы "ПРОТИВ" осуществимости**

1. **Несовместимость требований:** Запрос клиента на "настройку имеющегося роутера" невыполним. Требуется замена оборудования или покупка дополнительных услуг.  
2. **Нестабильность среды:** Сотовая сеть T-Mobile имеет плавающие характеристики (лаг, джиттер, смена вышек), что делает её плохой основой для хостинга серверов, требующих высокого аптайма.  
3. **Политические риски:** Зависимость от Terms of Service сторонних провайдеров (Cloudflare) или политик шейпинга оператора делает решение хрупким.

### **7.3 Сравнительная таблица решений**

| Характеристика | Native Port Forwarding (Текущая цель) | Business Static IP (Рекомендуемая цель) | Overlay / Tailscale | VPS + WireGuard |
| :---- | :---- | :---- | :---- | :---- |
| **Оборудование** | Arcadyan/Sagemcom | **Inseego FX2000/3100** | Любое | Любое + VPS |
| **Стоимость** | $0 | +$3/мес + время | Бесплатно (базовый) | ~$5/мес |
| **Сложность** | Невозможно | Средняя (бюрократия) | Низкая | Высокая (Linux) |
| **Надежность** | 0% | 100% | 80% (зависит от реле) | 90% (зависит от MTU) |
| **Игровой хостинг** | Нет | **Да** | Нет (обычно) | Да (с трудом) |

---

## **8. Вердикт и рекомендации**

### **8.1 Количественная оценка (2.3)**

Оценка выполнимости проекта в исходной формулировке ("настроить проброс портов на домашнем шлюзе"): 15/100.  
Решение технически невозможно без изменения вводных данных.  
Оценка выполнимости проекта при смене стратегии ("обеспечить доступ извне через миграцию или оверлей"): 85/100.  
Решение гарантированно существует, но требует ресурсов.

### **8.2 Итоговый вердикт (2.4)**

Проект P⁎ в его текущем виде **технически неосуществим**. Клиент ꆜ находится в плену заблуждения D𐊑⠿, полагая, что ограничение носит программный характер, тогда как оно является фундаментальным свойством сетевой архитектуры T-Mobile (CGNAT/464XLAT).

**Стратегический план действий для эксперта:**

1. **Отказать** в попытках настроить текущий потребительский шлюз (Arcadyan/Sagemcom/Nokia). Это пустая трата времени.  
2. **Предложить выбор из двух путей:**  
   * **Путь А (Профессиональный/Игровой):** Миграция на T-Mobile Business Internet (Sole Proprietor) с требованием роутера Inseego и услуги Static IP. Настройка APN b2b.static.  
   * **Путь Б (Любительский/IoT):** Использование Tailscale (с пониманием ограничений скорости через DERP) или Cloudflare Tunnel (с запретом на видео-стриминг).  
3. **Предупредить** о проблемах с MTU (рекомендовать 1280 байт) и потенциальном шейпинге UDP, если выбран путь VPN.

Только такой подход, основанный на глубоком понимании ограничений 5G-сетей, позволит превратить заведомо провальный проект в успешно реализованное решение.

#### **Works cited**

1. T-Mobile Home Internet Port Forwarding & Bypass CGNAT - PureVPN, accessed November 24, 2025, [https://www.purevpn.com/blog/t-mobile-cgnat-port-forwarding/](https://www.purevpn.com/blog/t-mobile-cgnat-port-forwarding/)  
2. PortFowarding T-Mobile Home Internet - Channels Community, accessed November 24, 2025, [https://community.getchannels.com/t/portfowarding-t-mobile-home-internet/32162](https://community.getchannels.com/t/portfowarding-t-mobile-home-internet/32162)  
3. T-Mobile Home Internet Port Forwarding (Getting Started) | LocalXpose Blog, accessed November 24, 2025, [https://localxpose.io/blog/t-mobile-home-internet-port-forwarding](https://localxpose.io/blog/t-mobile-home-internet-port-forwarding)  
4. Tmobile home internet doesn't let you portfoward. Here's how to port forward easy - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1llhpab/tmobile_home_internet_doesnt_let_you_portfoward/](https://www.reddit.com/r/tmobileisp/comments/1llhpab/tmobile_home_internet_doesnt_let_you_portfoward/)  
5. Adding Static IP Number to T-Mobile Business Internet | Network Fixes, accessed November 24, 2025, [https://networkfixes.com/adding-static-ip-number-to-t-mobile-business-internet/](https://networkfixes.com/adding-static-ip-number-to-t-mobile-business-internet/)  
6. Tmobile Home Internet and ipv6? : r/firewalla - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/firewalla/comments/1b6fa29/tmobile_home_internet_and_ipv6/](https://www.reddit.com/r/firewalla/comments/1b6fa29/tmobile_home_internet_and_ipv6/)  
7. Does t-mobile IPv6 actually allow for incoming connections? Home Internet specifically, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/jf34gv/does_tmobile_ipv6_actually_allow_for_incoming/](https://www.reddit.com/r/tmobile/comments/jf34gv/does_tmobile_ipv6_actually_allow_for_incoming/)  
8. T-Mobile Internet Gateway Setup | T-Mobile 5G Home Internet, accessed November 24, 2025, [https://www.t-mobile.com/support/home-internet/t-mobile-gateway](https://www.t-mobile.com/support/home-internet/t-mobile-gateway)  
9. Arcadyan KVD21 Gateway | T-Mobile 5G Home Internet, accessed November 24, 2025, [https://www.t-mobile.com/support/home-internet/arcadyan-gateway](https://www.t-mobile.com/support/home-internet/arcadyan-gateway)  
10. LEAKED NEW GATEWAY! T-Mobile 5G Home Internet G5AR Launches July 2025, accessed November 24, 2025, [https://www.youtube.com/watch?v=zsBMuThbEUs](https://www.youtube.com/watch?v=zsBMuThbEUs)  
11. T-Mobile For Business 5G Internet - G4SE Compatible with IP Passthrough and Static IP?, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1cy5ys1/tmobile_for_business_5g_internet_g4se_compatible/](https://www.reddit.com/r/tmobileisp/comments/1cy5ys1/tmobile_for_business_5g_internet_g4se_compatible/)  
12. T-Mobile Business Internet Plans - Unlimited and Tiered Data Options For Routers and Data Devices, accessed November 24, 2025, [https://www.rvmobileinternet.com/t-mobile-business-internet-plans-unlimited-and-tiered-data-options-for-routers-and-data-devices/](https://www.rvmobileinternet.com/t-mobile-business-internet-plans-unlimited-and-tiered-data-options-for-routers-and-data-devices/)  
13. RESOLVED: Can't get internet to work with T-Mobile Home Internet and Inseego FX2000 router | Ubiquiti Community, accessed November 24, 2025, [https://community.ui.com/questions/RESOLVED-Cant-get-internet-to-work-with-T-Mobile-Home-Internet-and-Inseego-FX2000-router/e09d8203-f0d7-4870-a0ce-8a36550285fa](https://community.ui.com/questions/RESOLVED-Cant-get-internet-to-work-with-T-Mobile-Home-Internet-and-Inseego-FX2000-router/e09d8203-f0d7-4870-a0ce-8a36550285fa)  
14. I'm eligible for T Mobile business 5g but I am not a business I live over the business . Can I just order the business plan? I tried the availability for home and it says not available but when I put the address in on thr business Internet it is more than willing to sign me up . : r - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1obe36t/im_eligible_for_t_mobile_business_5g_but_i_am_not/](https://www.reddit.com/r/tmobileisp/comments/1obe36t/im_eligible_for_t_mobile_business_5g_but_i_am_not/)  
15. Can I get tmobile 5g business internet at my home address? : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/16rl1s3/can_i_get_tmobile_5g_business_internet_at_my_home/](https://www.reddit.com/r/tmobileisp/comments/16rl1s3/can_i_get_tmobile_5g_business_internet_at_my_home/)  
16. T-Mobile Static IP's ARE Possible : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/wq1hm3/tmobile_static_ips_are_possible/](https://www.reddit.com/r/tmobileisp/comments/wq1hm3/tmobile_static_ips_are_possible/)  
17. Can't get static IP with business account if you're the sole proprietor?? : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/185bcst/cant_get_static_ip_with_business_account_if_youre/](https://www.reddit.com/r/tmobileisp/comments/185bcst/cant_get_static_ip_with_business_account_if_youre/)  
18. Business Internet (Not small business) with static IP Question : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/14jqv60/business_internet_not_small_business_with_static/](https://www.reddit.com/r/tmobileisp/comments/14jqv60/business_internet_not_small_business_with_static/)  
19. PSA: If you are using T-Mobile BYOD router or Hotspot with a static ipv4 address, you must use the APN b2b.tmobile.com or b2b.static - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/j45sgz/psa_if_you_are_using_tmobile_byod_router_or/](https://www.reddit.com/r/tmobile/comments/j45sgz/psa_if_you_are_using_tmobile_byod_router_or/)  
20. tmobile business static ip passthrough to Mikrotik - General, accessed November 24, 2025, [https://forum.mikrotik.com/t/tmobile-business-static-ip-passthrough-to-mikrotik/183486](https://forum.mikrotik.com/t/tmobile-business-static-ip-passthrough-to-mikrotik/183486)  
21. Business static IP : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/170rqcg/business_static_ip/](https://www.reddit.com/r/tmobileisp/comments/170rqcg/business_static_ip/)  
22. My experience trying to get a static IP for my business : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/11t4yau/my_experience_trying_to_get_a_static_ip_for_my/](https://www.reddit.com/r/tmobileisp/comments/11t4yau/my_experience_trying_to_get_a_static_ip_for_my/)  
23. TMobile APN / IP Address - Pepwave MAX - Peplink Community, accessed November 24, 2025, [https://forum.peplink.com/t/tmobile-apn-ip-address/42479](https://forum.peplink.com/t/tmobile-apn-ip-address/42479)  
24. accessed November 24, 2025, [https://www.reddit.com/r/selfhosted/comments/130szje/has_cloudflare_recently_changed_their_tos_re_use/#:~:text=this%20Section%202.8.-,Use%20of%20the%20Services%20for%20serving%20video%20or%20a%20disproportionate,Terms%20for%20a%20specific%20Service.](https://www.reddit.com/r/selfhosted/comments/130szje/has_cloudflare_recently_changed_their_tos_re_use/#:~:text=this%20Section%202.8.-,Use%20of%20the%20Services%20for%20serving%20video%20or%20a%20disproportionate,Terms%20for%20a%20specific%20Service.)  
25. Cloudflare Tunnel TOS - Video now allowed? : r/selfhosted - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/selfhosted/comments/1drzgml/cloudflare_tunnel_tos_video_now_allowed/](https://www.reddit.com/r/selfhosted/comments/1drzgml/cloudflare_tunnel_tos_video_now_allowed/)  
26. Delivering Videos with Cloudflare · Cloudflare Fundamentals docs, accessed November 24, 2025, [https://developers.cloudflare.com/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/)  
27. How to use only Derp instead of direct connection? : r/Tailscale - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/Tailscale/comments/10eq453/how_to_use_only_derp_instead_of_direct_connection/](https://www.reddit.com/r/Tailscale/comments/10eq453/how_to_use_only_derp_instead_of_direct_connection/)  
28. T-Mobile Port Forwarding - Pinggy, accessed November 24, 2025, [https://pinggy.io/blog/tmobile_port_forwarding/](https://pinggy.io/blog/tmobile_port_forwarding/)  
29. Bypassing Port Forwarding Restrictions on T-Mobile Home Internet Using Pinggy, accessed November 24, 2025, [https://dev.to/lightningdev123/bypassing-port-forwarding-restrictions-on-t-mobile-home-internet-using-pinggy-3me6](https://dev.to/lightningdev123/bypassing-port-forwarding-restrictions-on-t-mobile-home-internet-using-pinggy-3me6)  
30. T-Mobile MTU issue - AllStarLink Discussion Groups, accessed November 24, 2025, [https://community.allstarlink.org/t/t-mobile-mtu-issue/23642](https://community.allstarlink.org/t/t-mobile-mtu-issue/23642)  
31. VPN failing due to UDP fragments getting dropped by TMobile/Spectrum - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/networking/comments/1n3m5r1/vpn_failing_due_to_udp_fragments_getting_dropped/](https://www.reddit.com/r/networking/comments/1n3m5r1/vpn_failing_due_to_udp_fragments_getting_dropped/)  
32. UDP is throttled to about 100 kbps on T-Mobile. Wireguard won't work and TCP bas... | Hacker News, accessed November 24, 2025, [https://news.ycombinator.com/item?id=29585541](https://news.ycombinator.com/item?id=29585541)  
33. T-mobile seems to be throttling my VPN connection, tried port 443. Alternatives? Obfuscation? - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/VPN/comments/l9p5l6/tmobile_seems_to_be_throttling_my_vpn_connection/](https://www.reddit.com/r/VPN/comments/l9p5l6/tmobile_seems_to_be_throttling_my_vpn_connection/)  
34. [RANT] WG is being throttled by ISP : r/WireGuard - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/WireGuard/comments/oanyzn/rant_wg_is_being_throttled_by_isp/](https://www.reddit.com/r/WireGuard/comments/oanyzn/rant_wg_is_being_throttled_by_isp/)  
35. Throttling of Wireguard / udp? - tmobile - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/be8l6m/throttling_of_wireguard_udp/](https://www.reddit.com/r/tmobile/comments/be8l6m/throttling_of_wireguard_udp/)

# 13. Анализ `D𐊑⠿` №3 (выполнен Gemini Deep Research)
https://gemini.google.com/share/5961dc17a37a



## **1. Введение: Эпистемологический разрыв между проводными и мобильными топологиями**

В современном телекоммуникационном ландшафте наблюдается существенный когнитивный диссонанс у потребителей, переходящих с традиционных проводных архитектур (DOCSIS, GPON, DSL) на технологии фиксированного беспроводного доступа (FWA), к которым относится продукт T-Mobile Home Internet (TMHI). Анализ запроса и профиля заблуждений клиента ꆜ (обозначенного как множество D𐊑⠿) демонстрирует классический пример экстраполяции опыта использования статических, детерминированных сетей IPv4 на динамическую, высокоуровнево виртуализированную среду мобильной сети 5G/LTE.

Данный отчет представляет собой исчерпывающую деконструкцию заблуждений клиента, базирующуюся на анализе технической документации, пользовательских отчетов, условий обслуживания и фундаментальных сетевых стандартов (RFC). Мы последовательно рассмотрим архитектурные ограничения, накладываемые технологиями трансляции адресов операторского класса (CGNAT), специфику инкапсуляции трафика в мобильных сетях, бюрократические и технические барьеры сегментации услуг, а также юридические аспекты использования сети. Целью анализа является не просто опровержение заблуждений, но и предоставление глубокого понимания причинно-следственных связей, делающих ожидания клиента ꆜ нереализуемыми в текущей конфигурации сети ᛭O.

---

## **2. Структурный анализ сетевой адресации и трансляции (Заблуждение D𐊑₁)**

Центральным элементом модели мира клиента ꆜ является убеждение в возможности управления входящим трафиком через механизм переадресации портов (Port Forwarding). Это заблуждение (D𐊑₁) фундаментально противоречит архитектуре сети T-Mobile, спроектированной в условиях исчерпания адресного пространства IPv4 и перехода на IPv6-only ядро.

### **2.1. Технология Carrier-Grade NAT (CGNAT) и эрозия публичного адреса**

В отличие от традиционных провайдеров, которые часто предоставляют абоненту уникальный, пусть и динамический, публичный IPv4-адрес, T-Mobile использует агрессивную схему Carrier-Grade NAT (CGNAT), также известную как Large Scale NAT (LSN). В этой топологии шлюз, установленный в помещении клиента (CPE — Customer Premise Equipment), получает на WAN-интерфейс адрес из зарезервированного диапазона 100.64.0.0/10 (Shared Address Space, согласно RFC 6598).1

Этот адрес не маршрутизируем в глобальной сети Интернет. Трансляция адресов происходит дважды:

1. **NAT44 (Local):** На устройстве пользователя (LAN → WAN CPE).  
2. **NAT44 (Carrier):** На пограничном маршрутизаторе оператора (PGW/UPF → Internet).

Следствием этой архитектуры является то, что один публичный IPv4-адрес на выходе из сети T-Mobile обслуживает сотни, а иногда и тысячи абонентов одновременно. Порты TCP/UDP на этом публичном адресе динамически распределяются между пользовательскими сессиями. Попытка клиента ꆜ настроить переадресацию портов на своем локальном шлюзе (например, пробросить порт 32400 для Plex или 80 для веб-сервера) технически бессмысленна, так как входящий пакет из Интернета будет отброшен на уровне пограничного шлюза оператора, не имеющего записи в таблице трансляции, связывающей этот порт с конкретным абонентом.1

### **2.2. Механизм 464XLAT и однонаправленность соединений**

Сеть T-Mobile является нативной сетью IPv6. Для обеспечения совместимости с устаревшими приложениями и ресурсами IPv4 используется механизм перехода 464XLAT (RFC 6877). Эта архитектура состоит из двух ключевых компонентов:

* **CLAT (Customer-side Translator):** Модуль на клиентском шлюзе, который транслирует исходящие IPv4-пакеты в IPv6, инкапсулируя их для передачи через ядро сети.  
* **PLAT (Provider-side Translator):** Шлюз на стороне оператора, который выполняет обратную деинкапсуляцию и трансляцию в IPv4 (Stateful NAT64) для выхода в публичный интернет.4

Эта система спроектирована исключительно для инициации соединений *изнутри* сети. PLAT хранит состояние только для сессий, инициированных абонентом. Снаружи инициировать соединение к CLAT невозможно, так как PLAT не имеет статических правил mapping'а для входящих запросов. Это делает D𐊑₁ технически нереализуемым не только на уровне настроек роутера, но и на уровне фундаментального протокола транспорта данных в сети оператора.

### **2.3. Политики фильтрации входящего IPv6 трафика**

Клиент ꆜ может аргументировать, что при наличии глобально маршрутизируемого IPv6-адреса (GUA), который T-Mobile действительно предоставляет каждому устройству в сети (часто делегируя префикс /64), необходимость в NAT отпадает, и доступ должен быть открыт. Однако здесь вступает в силу политика безопасности оператора.

Исследование показывает, что стандартные шлюзы, предоставляемые T-Mobile для домашних пользователей (Nokia FastMile, Arcadyan KVD21, Sagemcom FAST 5688W), поставляются с жестко зашитыми правилами брандмауэра (Stateful Firewall), которые блокируют *весь* входящий (unsolicited) трафик, даже по протоколу IPv6.6 В отличие от роутеров класса "Prosumer" (Ubiquiti, MikroTik) или прошивок типа OpenWrt/Merlin, интерфейс управления этих шлюзов намеренно лишен функциональности для создания разрешающих правил (Allow Rules) или отключения фаервола.6

Существуют свидетельства пользователей, пытавшихся использовать сторонние приложения (например, HINT Control) или скрипты для доступа к скрытым настройкам, однако успешность таких манипуляций низка и часто сбрасывается при обновлении прошивки, которая контролируется оператором удаленно по протоколу TR-069.9 Таким образом, даже в пространстве IPv6, где проблема NAT отсутствует, административные барьеры делают организацию входящих соединений невозможной для рядового пользователя.

| Характеристика | Традиционный ISP (IPv4) | T-Mobile Home Internet (FWA) | Влияние на D𐊑₁ |
| :---- | :---- | :---- | :---- |
| **Тип адресации** | Публичный динамический IPv4 | Private IPv4 (CGNAT) + IPv6 | Исключает прямой доступ по IPv4 |
| **NAT** | Single NAT (на роутере) | Double NAT / CGNAT (Роутер + ISP) | Делает Port Forwarding бесполезным |
| **Управление Firewall** | Полный доступ пользователя | Заблокировано / Скрыто | Блокирует входящий IPv6 |
| **Протокол транспорта** | Native IPv4 / Dual Stack | IPv6-only + 464XLAT | Усложняет туннелирование IPv4 |

---

## **3. Протокольная несовместимость и туннелирование (Заблуждение D𐊑₂)**

Заблуждение D𐊑₂ касается уверенности клиента в стабильной работе корпоративных VPN-решений. Это ожидание базируется на опыте работы с проводными каналами, где MTU (Maximum Transmission Unit) стандартизирован (1500 байт), а фрагментация пакетов обрабатывается предсказуемо. В мобильной сети T-Mobile ситуация кардинально отличается.

### **3.1. Проблема фрагментации и MTU в инкапсулированных сетях**

Сети LTE и 5G используют сложную структуру инкапсуляции для передачи пользовательских данных. Пакеты пользователя оборачиваются в GTP-U (GPRS Tunneling Protocol – User Plane), который работает поверх UDP/IP. Эти дополнительные заголовки (IP header + UDP header + GTP header) отнимают часть полезной нагрузки фрейма.

Если стандартный Ethernet-кадр имеет размер 1500 байт, то эффективный MTU внутри туннеля мобильного оператора часто снижается до 1420, 1380 или даже 1280 байт (минимальный MTU для IPv6). Клиенты IPsec VPN, настроенные по умолчанию, часто пытаются отправить пакеты размером 1500 байт с установленным флагом DF (Don't Fragment). Когда такой пакет попадает в узкое место мобильной сети, оборудование оператора должно отправить обратно ICMP-сообщение "Fragmentation Needed" (Type 3, Code 4). Однако в условиях CGNAT и агрессивной фильтрации ICMP-трафика эти сообщения часто не доходят до отправителя (Black Hole PMTUD). В результате соединение устанавливается (handshake проходит на малых пакетах), но передача данных зависает при попытке отправить большой объем информации.11

Исследование подтверждает, что пользователи массово сталкиваются с ситуацией, когда VPN подключается, но веб-страницы внутри корпоративной сети не грузятся. Решением является принудительное занижение MTU на виртуальном адаптере клиента (например, netsh interface ipv4 set subinterface "VPN" mtu=1300), что противоречит ожиданию ꆜ о работе "без настроек".11

### **3.2. Блокировка протоколов без состояния (IP Protocol 50 - ESP)**

Классический IPsec использует протокол ESP (Encapsulating Security Payload) для транспорта шифрованных данных. ESP является протоколом 3-го уровня (в терминологии OSI, хотя работает поверх IP) и не имеет концепции "портов", как TCP или UDP.

NAT-маршрутизаторы (особенно уровня Carrier-Grade) должны использовать сложные эвристики для отслеживания сессий ESP от множества клиентов за одним IP. В условиях перегрузки или некорректной реализации ALG (Application Layer Gateway) на стороне T-Mobile, пакеты ESP могут просто отбрасываться или направляться не тому клиенту. Это делает "чистый" IPsec крайне ненадежным. Протоколы, инкапсулирующие VPN-трафик в UDP (NAT-T, RFC 3947) или использующие SSL/TLS (TCP/443), работают значительно стабильнее, так как для NAT-устройства они выглядят как обычный веб-трафик или стриминг.5

### **3.3. Сравнительный анализ эффективности VPN протоколов в среде TMHI**

На основе агрегированных данных 16 можно составить матрицу совместимости протоколов с сетью T-Mobile:

| Протокол | Стабильность на TMHI | Проблемы | Вердикт для D𐊑₂ |
| :---- | :---- | :---- | :---- |
| **IPsec (IKEv2/ESP)** | **Низкая / Критическая** | Фрагментация, блокировка ESP, проблемы с MTU. Требует ручного тюнинга. | **Подтверждает заблуждение.** "Из коробки" часто не работает. |
| **L2TP/IPsec** | **Средняя** | Чувствителен к Double NAT. Часто блокируется без явных причин. | Ненадежен для критических задач. |
| **OpenVPN (TCP)** | **Высокая** | Высокий оверхед (overhead), медленная скорость из-за TCP-over-TCP meltdown. | Работает, но медленно. |
| **OpenVPN (UDP)** | **Высокая** | Может требовать настройки mssfix. | Рекомендуемый легаси-вариант. |
| **SSL VPN (AnyConnect/FortiClient)** | **Высокая** | Эмулирует HTTPS трафик, отлично проходит через CGNAT. | Лучший выбор для корпоративного доступа.11 |
| **WireGuard** | **Наивысшая** | Современный код, эффективно работает с UDP, быстрое переподключение при смене IP (roaming). | Технически оптимален, но редко используется в Enterprise.16 |

Таким образом, утверждение клиента о том, что "VPN будет работать", верно лишь частично и требует существенных оговорок о типе протокола, что для обычного пользователя равносильно неработоспособности.

---

## **4. Сегментация услуг и иллюзия статического IP (Заблуждение D𐊑₃)**

Заблуждение D𐊑₃ касается возможности получения статического IP-адреса. Клиент рассматривает это как простую опцию ("add-on"), доступную по запросу, аналогично тому, как это реализовано у многих региональных ISP. Однако в экосистеме T-Mobile это жестко регламентированный процесс, связанный с сегментацией продуктов B2B и B2C.

### **4.1. Императивная сегрегация Business vs Residential**

Согласно внутренней политике T-Mobile, статические IP-адреса доступны *исключительно* для тарифных планов "Business Internet". Для тарифных планов "Home Internet" (Residential) техническая возможность присвоения статического IP заблокирована на уровне биллинга и профилей HSS/HLR (Home Subscriber Server).23

Попытки пользователей уговорить поддержку активировать эту услугу на домашнем аккаунте неизменно заканчиваются неудачей. Оператор четко разделяет продукты:

* **Home Internet:** Динамический IP, CGNAT, медиа-потребление.  
* **Business Internet:** Возможность статики ($3/мес), поддержка VPN, телеметрия.

Хотя физическое лицо может открыть бизнес-аккаунт, используя SSN в качестве Sole Proprietor, это требует переоформления договора, прохождения кредитной проверки как юрлица и, что критично, смены оборудования.14

### **4.2. Аппаратная зависимость и проблема BYOD**

Даже при переходе на бизнес-тариф, получение статического IP сопряжено с аппаратными ограничениями. Стандартные шлюзы (Nokia, Arcadyan), выдаваемые домашним пользователям, часто не поддерживают корректную работу со статическими APN (например, b2b.static). Для реализации услуги требуется использование специфических маршрутизаторов, таких как **Inseego FX2000**, **Inseego FX3100** или **Cradlepoint**.9

Более того, использование собственного оборудования (Bring Your Own Device - BYOD) в сочетании со статическим IP накладывает ограничения на режимы работы сети. Отмечено, что при активации статического IP устройства часто теряют возможность работы в режиме 5G Standalone (SA), откатываясь на Non-Standalone (NSA) или LTE, что может снижать скорость и увеличивать задержки.25

### **4.3. Географическая маршрутизация (Tromboning effect)**

Наименее очевидный для клиента аспект D𐊑₃ — это топология маршрутизации трафика со статическим IP. T-Mobile имеет ограниченное количество шлюзов (Points of Presence - PoP), терминирующих статические адреса (упоминаются узлы в Чикаго, Филадельфии, Сиэтле).25

Если клиент физически находится в Майами, а его статический IP привязан к шлюзу в Филадельфии, весь его трафик будет проходить маршрут:  
Дом (Майами) -> Вышка -> Ядро сети -> Филадельфия (PoP) -> Интернет -> Ресурс.  
Ответный трафик пойдет обратным путем. Этот эффект ("tromboning") добавляет существенную задержку (ping), часто увеличивая её на 20-50 мс и более, что критично для интерактивных приложений.26 Клиент ꆜ, ожидая улучшения связности за счет статики, рискует получить деградировавший сервис.

---

## **5. Политики допустимого использования и ограничения хостинга (Заблуждение D𐊑₄)**

Заблуждение D𐊑₄ ("я могу хостить серверы") лежит в плоскости конфликта между техническими возможностями (которые можно расширить обходными путями) и юридическими ограничениями (Terms of Service - ToS).

### **5.1. Анализ текста "Acceptable Use Policy"**

Документы, регламентирующие использование сети T-Mobile (Terms & Conditions, Acceptable Use Policy), содержат прямые запреты на использование сервиса Home Internet для определенных видов активности. В частности, запрещены:

* "Unattended use" (использование без присмотра/участия человека).  
* "Automatic data feeds" (автоматические потоки данных).  
* "Automated machine-to-machine connections".  
* Использование устройства в качестве сервера для публичного вещания ("broadcast to multiple servers or recipients").30

Хотя термин "сервер" может трактоваться широко, контекст документов указывает на то, что постоянная генерация исходящего трафика (upload), характерная для Plex-серверов, P2P-узлов или веб-хостинга, классифицируется как нарушение, способное вызвать "disproportionate congestion" (непропорциональную перегрузку) сети.

### **5.2. Приоритезация трафика (QCI) и управление перегрузками**

Мобильная сеть — это разделяемая среда (shared medium) с ограниченным спектральным ресурсом. Для управления этой средой T-Mobile использует механизмы QoS (Quality of Service), основанные на QCI (QoS Class Identifier).

* Трафик Home Internet обычно имеет более низкий приоритет (QCI 9 или ниже) по сравнению с трафиком мобильных телефонов (QCI 6-8) на той же вышке.33

Попытка запустить сервер, потребляющий значительную полосу пропускания на отдачу (Upload), в часы пик приведет к жесткому шейпингу (throttling) или деприоритизации пакетов. В отличие от проводного интернета, где пропускная способность канала относительно фиксирована, в TMHI скорость сервера будет плавать в зависимости от нагрузки на соту со стороны соседей с мобильными телефонами. Это делает хостинг технически ненадежным, даже если бы он был разрешен юридически.

### **5.3. Практика принудительного отключения**

Существуют прецеденты и положения в договорах, позволяющие оператору ограничивать или отключать абонентов, чья активность напоминает автоматизированные системы или "always-on connections", не характерные для профиля потребления человека (например, круглосуточный upload на максимальной скорости).30 Использование хотспота или шлюза в качестве замены выделенной линии для серверов ("substitute for a dedicated home internet connection") для задач, выходящих за рамки "residential use", является основанием для терминации сервиса.

---

## **6. Архитектурные обходные пути (Workarounds) и их применимость**

Несмотря на вышеописанные ограничения, технически грамотное сообщество выработало ряд решений ("костылей"), позволяющих обойти CGNAT. Однако сложность этих решений подтверждает тезис о том, что для обычного пользователя ("клиента ꆜ") задача нерешаема "из коробки".

### **6.1. Оверлейные сети (Overlay Networks)**

Использование программно-определяемых сетей (SD-WAN) типа **Tailscale** (на базе WireGuard) или **ZeroTier**. Эти инструменты используют техники "NAT Traversal" (STUN/TURN), чтобы пробить туннель сквозь CGNAT.

* *Преимущество:* Не требуют белого IP, работают поверх любого транспорта.  
* *Недостаток:* Требуют установки агента на каждое устройство. Если клиент хочет дать доступ другу к Plex, другу тоже нужно ставить Tailscale, что неудобно.36

### **6.2. Туннелирование через VPS (Virtual Private Server)**

Аренда дешевого VPS (Oracle Free Tier, Google Cloud, AWS) с публичным IPv4 и создание туннеля (WireGuard/OpenVPN) между домашним сервером и VPS.

* *Схема:* Internet -> VPS (Public IP) -> VPN Tunnel -> TMHI Gateway -> Home Server.  
* *Сложность:* Требует навыков администрирования Linux, настройки iptables, маршрутизации. Для клиента, ожидающего "просто включить порт", это непреодолимый барьер квалификации.22  
* *Риски:* Дополнительная точка отказа, увеличение задержки.

### **6.3. Cloudflare Tunnels (Argo)**

Использование демона cloudflared для публикации внутренних веб-сервисов (HTTP/HTTPS) в сеть Cloudflare.

* *Применимость:* Отлично для Home Assistant или веб-сайтов.  
* *Ограничения:* В бесплатной версии не поддерживает произвольные TCP/UDP порты (например, игровой трафик или специфические протоколы видеонаблюдения), что ограничивает функциональность по сравнению с полноценным Port Forwarding.39

---

## **7. Выводы и заключение**

Проведенный анализ позволяет с уверенностью утверждать, что набор представлений клиента ꆜ (D𐊑⠿) представляет собой систему устойчивых заблуждений, несовместимых с технической и юридической реальностью эксплуатации сети T-Mobile Home Internet.

1. **По D𐊑₁ (Port Forwarding):** Заблуждение абсолютное. Архитектура CGNAT + 464XLAT и блокировка входящего IPv6 делают традиционный проброс портов невозможным на потребительском оборудовании.  
2. **По D𐊑₂ (VPN):** Заблуждение частичное, но критическое. Стабильность IPsec VPN скомпрометирована проблемами MTU/фрагментации. Требуется переход на SSL VPN или WireGuard, что часто не зависит от воли клиента (корпоративные стандарты).  
3. **По D𐊑₃ (Static IP):** Заблуждение процедурное. Услуга недоступна для домашних пользователей, а для бизнес-пользователей несет риски увеличения задержки (routing inefficiencies).  
4. **По D𐊑₄ (Hosting):** Заблуждение юридическое и эксплуатационное. Прямое нарушение ToS и техническая ненадежность из-за низкого приоритета трафика (QCI).

Результирующая рекомендация:  
Клиенту ꆜ необходимо либо скорректировать свои ожидания (отказ от внешнего доступа, смена протоколов VPN), либо рассмотреть альтернативные способы подключения. Если функциональность, описанная в D𐊑⠿, является критической для бизнес-процессов или образа жизни клиента, T-Mobile Home Internet в его текущей архитектурной реализации не является подходящим решением. Для реализации требуемых сценариев (серверы, стабильный IPsec, белый IP) необходим либо проводной провайдер, либо переход на специализированные бизнес-решения с полным пониманием их стоимости и архитектурных компромиссов.

#### **Works cited**

1. T-Mobile Home Internet Port Forwarding & Bypass CGNAT - PureVPN, accessed November 24, 2025, [https://www.purevpn.com/blog/t-mobile-cgnat-port-forwarding/](https://www.purevpn.com/blog/t-mobile-cgnat-port-forwarding/)  
2. TMobile Home Internet Port forwarding? - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/ssx2rw/tmobile_home_internet_port_forwarding/](https://www.reddit.com/r/tmobile/comments/ssx2rw/tmobile_home_internet_port_forwarding/)  
3. Access home network remotely without an IPv4 address available at my home. - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/HomeNetworking/comments/lpa0sh/access_home_network_remotely_without_an_ipv4/](https://www.reddit.com/r/HomeNetworking/comments/lpa0sh/access_home_network_remotely_without_an_ipv4/)  
4. Any updates on port forwarding and Bridge Mode? : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/nhbf2z/any_updates_on_port_forwarding_and_bridge_mode/](https://www.reddit.com/r/tmobileisp/comments/nhbf2z/any_updates_on_port_forwarding_and_bridge_mode/)  
5. FortiClient vs T-Mobile vs Windows : r/fortinet - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/fortinet/comments/1988hdv/forticlient_vs_tmobile_vs_windows/](https://www.reddit.com/r/fortinet/comments/1988hdv/forticlient_vs_tmobile_vs_windows/)  
6. Does t-mobile IPv6 actually allow for incoming connections? Home Internet specifically, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/jf34gv/does_tmobile_ipv6_actually_allow_for_incoming/](https://www.reddit.com/r/tmobile/comments/jf34gv/does_tmobile_ipv6_actually_allow_for_incoming/)  
7. Testing IPv6 support in Roon (for users locked out of ARC due to ISP reliance on IPv6 or CGNAT), accessed November 24, 2025, [https://community.roonlabs.com/t/testing-ipv6-support-in-roon-for-users-locked-out-of-arc-due-to-isp-reliance-on-ipv6-or-cgnat/236451?page=3](https://community.roonlabs.com/t/testing-ipv6-support-in-roon-for-users-locked-out-of-arc-due-to-isp-reliance-on-ipv6-or-cgnat/236451?page=3)  
8. T-Mobile Home Internet with Synology NAS issue : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1jq109k/tmobile_home_internet_with_synology_nas_issue/](https://www.reddit.com/r/tmobileisp/comments/1jq109k/tmobile_home_internet_with_synology_nas_issue/)  
9. Questions about home and business internet : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1avrsan/questions_about_home_and_business_internet/](https://www.reddit.com/r/tmobileisp/comments/1avrsan/questions_about_home_and_business_internet/)  
10. How do I change my NAT type on the Nokia Gateway cuz I can't play online on Elden Ring, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/vingwl/how_do_i_change_my_nat_type_on_the_nokia_gateway/](https://www.reddit.com/r/tmobile/comments/vingwl/how_do_i_change_my_nat_type_on_the_nokia_gateway/)  
11. Global Protect and T-Mobile : r/paloaltonetworks - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/paloaltonetworks/comments/1kxklt7/global_protect_and_tmobile/](https://www.reddit.com/r/paloaltonetworks/comments/1kxklt7/global_protect_and_tmobile/)  
12. VPN failing due to UDP fragments getting dropped by TMobile/Spectrum - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/networking/comments/1n3m5r1/vpn_failing_due_to_udp_fragments_getting_dropped/](https://www.reddit.com/r/networking/comments/1n3m5r1/vpn_failing_due_to_udp_fragments_getting_dropped/)  
13. PSA - Fix for IKEv2 VPN with TMobile 5g and others : r/WatchGuard - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/WatchGuard/comments/1fnlh9f/psa_fix_for_ikev2_vpn_with_tmobile_5g_and_others/](https://www.reddit.com/r/WatchGuard/comments/1fnlh9f/psa_fix_for_ikev2_vpn_with_tmobile_5g_and_others/)  
14. Switched from TMHI to Small Business Internet with static IP. Couldn't be happier. - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/118j663/switched_from_tmhi_to_small_business_internet/](https://www.reddit.com/r/tmobileisp/comments/118j663/switched_from_tmhi_to_small_business_internet/)  
15. v6ops Working Group N. Elkins Internet Draft Inside Products Intended status - IETF Datatracker, accessed November 24, 2025, [https://datatracker.ietf.org/meeting/86/agenda/v6ops-drafts.pdf](https://datatracker.ietf.org/meeting/86/agenda/v6ops-drafts.pdf)  
16. WireGuard vs. OpenVPN | What Are the Differences? - Palo Alto Networks, accessed November 24, 2025, [https://www.paloaltonetworks.com/cyberpedia/wireguard-vs-openvpn](https://www.paloaltonetworks.com/cyberpedia/wireguard-vs-openvpn)  
17. Types of VPN Explained: How Each Works and Which Is Best for You - Outbyte Official Blog, accessed November 24, 2025, [https://outbyte.com/blog/types-of-vpn-explained-how-each-works-and-which-is-best-for-you/](https://outbyte.com/blog/types-of-vpn-explained-how-each-works-and-which-is-best-for-you/)  
18. Which VPN Protocol Is Best: A Comprehensive Comparison for Optimal Security - Ukita, accessed November 24, 2025, [https://www.ukita.co.uk/which-vpn-protocol-is-best/](https://www.ukita.co.uk/which-vpn-protocol-is-best/)  
19. Which is more Secure? IPsec or OpenVPN or Wireguard : r/PFSENSE - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/PFSENSE/comments/1kcbolv/which_is_more_secure_ipsec_or_openvpn_or_wireguard/](https://www.reddit.com/r/PFSENSE/comments/1kcbolv/which_is_more_secure_ipsec_or_openvpn_or_wireguard/)  
20. Wireguard vs Tailscale vs OpenVPN? : r/homelab - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/homelab/comments/13xhbsn/wireguard_vs_tailscale_vs_openvpn/](https://www.reddit.com/r/homelab/comments/13xhbsn/wireguard_vs_tailscale_vs_openvpn/)  
21. Connecting to work VPN on TMHI : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/12kqrsf/connecting_to_work_vpn_on_tmhi/](https://www.reddit.com/r/tmobileisp/comments/12kqrsf/connecting_to_work_vpn_on_tmhi/)  
22. Yet another CGNAT VPS bypass setup : r/selfhosted - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/selfhosted/comments/m0n2te/yet_another_cgnat_vps_bypass_setup/](https://www.reddit.com/r/selfhosted/comments/m0n2te/yet_another_cgnat_vps_bypass_setup/)  
23. IPv6 on Business? : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1f91ij3/ipv6_on_business/](https://www.reddit.com/r/tmobileisp/comments/1f91ij3/ipv6_on_business/)  
24. Looking for explanation of devices : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1n3cpum/looking_for_explanation_of_devices/](https://www.reddit.com/r/tmobileisp/comments/1n3cpum/looking_for_explanation_of_devices/)  
25. T-Mobile Business Internet questions : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1gnq3wx/tmobile_business_internet_questions/](https://www.reddit.com/r/tmobileisp/comments/1gnq3wx/tmobile_business_internet_questions/)  
26. Advice on switching from Home 5G internet plan to the Buisness plan : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1mvbb3l/advice_on_switching_from_home_5g_internet_plan_to/](https://www.reddit.com/r/tmobileisp/comments/1mvbb3l/advice_on_switching_from_home_5g_internet_plan_to/)  
27. Small Business Internet Service | T-Mobile for Business, accessed November 24, 2025, [https://www.t-mobile.com/business/solutions/business-internet-services/small-business-internet](https://www.t-mobile.com/business/solutions/business-internet-services/small-business-internet)  
28. 5g gateway improvement : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1fch296/5g_gateway_improvement/](https://www.reddit.com/r/tmobileisp/comments/1fch296/5g_gateway_improvement/)  
29. Stuck in Tech Support Hell : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/1m9098r/stuck_in_tech_support_hell/](https://www.reddit.com/r/tmobileisp/comments/1m9098r/stuck_in_tech_support_hell/)  
30. Frequently Asked Questions (FAQ) | T-Mobile 5G Home Internet, accessed November 24, 2025, [https://www.t-mobile.com/home-internet/faq](https://www.t-mobile.com/home-internet/faq)  
31. Home Internet TOS : r/tmobile - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/co81z3/home_internet_tos/](https://www.reddit.com/r/tmobile/comments/co81z3/home_internet_tos/)  
32. FYI - US Mobile has an interesting developmment | The VoIP-info Forum, accessed November 24, 2025, [https://www.voip-info.org/forum/threads/us-mobile-has-an-interesting-developmment.28083/](https://www.voip-info.org/forum/threads/us-mobile-has-an-interesting-developmment.28083/)  
33. Transferring large amounts of data : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/t0h7in/transferring_large_amounts_of_data/](https://www.reddit.com/r/tmobileisp/comments/t0h7in/transferring_large_amounts_of_data/)  
34. Does T-Mobile Throttle the Internet & How to Prevent it? - PureVPN, accessed November 24, 2025, [https://www.purevpn.com/blog/does-t-mobile-throttle-the-internet/](https://www.purevpn.com/blog/does-t-mobile-throttle-the-internet/)  
35. If Net Neutrality laws were just overturned, then why is TMobile still throttling youtube and twitch on mobile internet? - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/1cf8cth/if_net_neutrality_laws_were_just_overturned_then/](https://www.reddit.com/r/tmobile/comments/1cf8cth/if_net_neutrality_laws_were_just_overturned_then/)  
36. Why should I use Pangolin, Tailscale or Cloudflare Tunnels? : r/selfhosted - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/selfhosted/comments/1o6bpzz/why_should_i_use_pangolin_tailscale_or_cloudflare/](https://www.reddit.com/r/selfhosted/comments/1o6bpzz/why_should_i_use_pangolin_tailscale_or_cloudflare/)  
37. Cheap dedicated IPv4 VPS to circumvent CGNAT restrictions? : r/tmobileisp - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobileisp/comments/kvvymk/cheap_dedicated_ipv4_vps_to_circumvent_cgnat/](https://www.reddit.com/r/tmobileisp/comments/kvvymk/cheap_dedicated_ipv4_vps_to_circumvent_cgnat/)  
38. Route my entire LAN to a tailscale exit node to bypass cgnat : r ..., accessed November 24, 2025, [https://www.reddit.com/r/Tailscale/comments/1gw6vzi/route_my_entire_lan_to_a_tailscale_exit_node_to/](https://www.reddit.com/r/Tailscale/comments/1gw6vzi/route_my_entire_lan_to_a_tailscale_exit_node_to/)  
39. PSA: Proxmox Admin Interface can be served with Cloudflare Tunnel. - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/Proxmox/comments/v73it9/psa_proxmox_admin_interface_can_be_served_with/](https://www.reddit.com/r/Proxmox/comments/v73it9/psa_proxmox_admin_interface_can_be_served_with/)  
40. Idea: PiHole on the go? - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/pihole/comments/1g7dgq2/idea_pihole_on_the_go/](https://www.reddit.com/r/pihole/comments/1g7dgq2/idea_pihole_on_the_go/)  
41. I want to set-up a VPN on a VPS, will then connect to my TPLink router, that will serve as a tunnel out of my CGNAT ISP in order to gain an Open NAT on my services. Can anyone suggest a suitable and secure guide/tutorial in order to achieve this? : r/selfhosted - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/selfhosted/comments/qehefd/i_want_to_setup_a_vpn_on_a_vps_will_then_connect/](https://www.reddit.com/r/selfhosted/comments/qehefd/i_want_to_setup_a_vpn_on_a_vps_will_then_connect/)  
42. Can I escape double-NAT? : r/tmobile - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/tmobile/comments/16dowq1/can_i_escape_doublenat/](https://www.reddit.com/r/tmobile/comments/16dowq1/can_i_escape_doublenat/)

