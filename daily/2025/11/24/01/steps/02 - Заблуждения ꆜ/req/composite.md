# 1. `B.md`
~~~~~~markdown
# 1. `᛭MDi`
## 1.1.
Каждый отдельный (произвольный, неопределённый) документ в формате Markdown, прикреплённый мной к этому запросу, буду обозначать `᛭Di`.
## 1.2.
Имя файла `᛭Di` всегда имеет расширение `.md`.
## 1.3.
Множество всех `᛭Di` буду обозначать `᛭Ds`.

# 2. `L.md`
### 2.1.
`L.md` ∈ `᛭Ds`.
## 2.2.
`L.md` описывает полуформальный язык: `᛭L`.
## 2.3.
Большинство `᛭Di` написаны на `᛭L`.
## 2.4.
Множество всех `᛭Di`, написанных на `᛭L`, буду обозначать `᛭DLs`.
Таким образом, `᛭DLs` ⊆ `᛭Ds`. 

# 3. `O.md`
## 3.1.
`O.md` ∈ `᛭DLs`
## 3.2.
`O.md` описывает некую **онтологию** (`᛭O`)  — модель предметной области, в которой тебе предстоит решать задачу.
«An **ontology** encompasses a representation, formal naming, and definitions of the categories, properties, and relations between the concepts, data, or entities»: https://en.wikipedia.org/wiki/Ontology_(information_science)

# 4. `T.md`
## 4.1.
`T.md` ∈ `᛭DLs`
## 4.2.
`T.md` описывает задачу (`᛭T`), которую ты должен решить.

# 5. Порядок твоих действий
Действуй пошагово:
## 5.1.
Сначала внимательно и полностью прочитай `L.md`.
В точности запомни его содержание.

## 5.2.
Затем внимательно и полностью прочитай `O.md`. 
В точности запомни его содержание.

## 5.3.
Затем внимательно и полностью прочитай `T.md`. 
Выполни `᛭T`.

# 6. Требования к заголовкам в твоём ответе
## 6.1.
У твоего ответа не должно быть одного общего заголовка, потому что твой ответ будет вставлен внутрь секции 1-го уровня (`#`) другого документа Markdown.
## 6.2.
Исходя из §6.1, в качестве заголовков верхего уровня ты должен использовать заголовки 2-го уровня (`##`).
Таких заголовков должно быть несколько: тем самым ты разбиваешь свой ответ на разделы.
Если твой ответ краток, то не разбивай его на разделы вообще.
## 6.3.
Разумеется, ты также можешь использовать заголовки более нижних уровней внутри заголовков 2-го уровня: для дополнительной структуризации текста.
## 6.4.
Никогда не используй выделение жирным (`**`) в заголовках.
## 6.5.
Всегда форматируй заголовки только символами решётки (`#`), не другими способами. 

~~~~~~

# 2. `L.md`
~~~~~~markdown
# 1. `≔`
## 1.1.
- `≔` — это бинарный оператор.
## 1.2.
`A ≔ B` means that `A` **denotes** `B`.
## 1.3.
Я использую `≔` для сокращения записи.
В выражении `A ≔ B` `B` обычно — это длинный текст, а `A` — это более короткое обозначение.  
## 1.4.
~~~code
A ≔
```
B
```
~~~
равнозначно `A ≔ B` и используется, когда `B` — многострочный текст.

# 2. `→`
~~~code
A → B
~~~
denotes a material conditional (https://en.wikipedia.org/wiki/Material_conditional)

# 3. `⊢`
~~~code
A ⊢ B
~~~
denotes a logical consequence (https://en.wikipedia.org/wiki/Logical_consequence)

# 4. `⊤`
## 4.1.
~~~code
⊤ B
~~~
means that `B` is true (is a fact).

## 4.2.
~~~code
⊤⟦Rs⟧ B
~~~
means:
```
(⊤ `B`) AND (`Rs` are the reasons why `B` is true)
```

## 4.3.
~~~code
A ≔⊤
```
B
```
~~~
means:
```code
(`A` ≔ `B`) AND (⊤ `B`).
```

## 4.4.
~~~code
A ≔⊤⟦Rs⟧
```
B
```
~~~
means:
```code
(`A` ≔ `B`) AND (⊤⟦Rs⟧ B).
```

# 5. `≔!`
## 5.1.
~~~code
A ≔! B
~~~
means:
```code
(`A` ≔⊤ `B`) AND (`B` is surprising).
```

## 5.2.
~~~code
A ≔!⟦Rs⟧ B
~~~
means:
```code
(`A` ≔⊤⟦Rs⟧ `B`) AND (`B` is surprising).
```

# 6. `?`
## 6.1.
~~~code
? B
~~~
means that `B` is a hypothesis.

## 6.2.
~~~code
?⟦Rs⟧ B
~~~
means:
```code
(? `B`) AND (`Rs` are the reasons for the hypothesis)
```

## 6.3.
~~~code
A ≔? B
~~~
means:
```code
(? `B`) AND (`A` ≔ `B`)
```

## 6.4.
~~~code
A ≔?⟦Rs⟧ B
~~~
means:
```code
(?⟦Rs⟧ `B`) AND (`A` ≔ `B`)
```

# 7.
## 7.1.
~~~code
A : S ≔ B
~~~
means:
```code
(`A` ≔ `B`) AND (`A` ∈ `S`).
```

## 7.2.
~~~code
A : S
~~~
means:
```code
`A` : `S` ≔ (an arbitrary element of `S`)
```

# 8. `⠿{…}`
## 8.1. `⠿{I₁, I₂, …, Iₙ}`
`⠿{I₁, I₂, …, Iₙ}` обозначает множество, заданное точным перечислением всех его элементов: {`I₁`, `I₂`, …, `Iₙ`}.

## 8.2. `⠿{I₁-Iₙ}` 
`⠿{I₁-Iₙ}` обозначает множество, заданное интервалом (диапазоном) его значений.
Это множество, в числе прочего, включает границы указанного интервала: `I₁` и `Iₙ`.

# 9. `⠿~`
## 9.1. `⠿~ (D)`
`⠿~ (D)` обозначает множество, заданное неформальным (словесным) описанием его элементов (`D`).

## 9.2.
~~~code
⠿~
```
D
```	
~~~
равнозначно `⠿~ (D)` и используется, когда `D` — многострочный текст.

## 9.3.
~~~code
S ≔ ⠿~ (D)
```yaml
- I₁
- I₂
- …
- Iₙ
```	
~~~
означает: (`S ≔ ⠿~ (D)`) AND (⠿{`I₁`, `I₂`, …, `Iₙ`} ⊆ `S`) .

# 10.
## 10.1.
`᛭DLi` : `᛭DLs`
## 10.2.
### 10.2.1.
`᛭Dc` — это обозначение `᛭DLi` самого себя.
Другими словами, если текст `᛭DLi` содержит упоминание `᛭Dс` — это значит, что `᛭Di` упоминает сам себя. 
### 10.2.2.
Например: если имя файла `᛭Di` — `sample.md`, и текст `sample.md` использует обозначение `᛭Dc`, это значит, что `᛭Dc` в данном случае обозначает документ `sample.md`.  

# 11. `§`
## 11.1.
~~~code
§P
~~~
означает ссылку на пункт `P` `᛭Dc`.
Например, §8.2.2 означает ссылку на пункт 8.2.2 `᛭Dc`.
## 11.2.
~~~code
`᛭DLi`::§P
~~~
означает ссылку на пункт `P` `᛭DLi`.
  
# 12. Local Definitions
## 12.1.
~~~code
A[§P] ≔ B
~~~
Означает:
- Для понятия `B` я **временно**, **только в рамках** §`P`, использую обозначение `A`.
- Вне §`P` это правило не применяется: в частности, если до §`P` обозначение `A` имело другой смысл, то после §`P` обозначение `A` снова будет иметь этот смысл.
- По сути, `A[§P] ≔ B` объявляет **локальную переменную** `A` с **областью действия** §`P`.
- В отличие от `A[§P] ≔ B`, `A ≔ B` объявляет **глобальную переменную** `A`.

## 12.2.
~~~code
A[§P₁, §P₂, …, §Pₙ] ≔ B
~~~
Означает, что обозначение `A` имеет значение `B` в контексте ⠿{§`P₁`, §`P₂`, …, §`Pₙ`}.
По сути, это правило аналогично §12.1, но область действия локальной переменной `A` ограничивается не одним пунктом, а множеством пунктов.

## 12.3.
~~~code
A[§P₁-§Pₙ] ≔ B
~~~
Означает, что обозначение `A` имеет значение `B` в контексте ⠿{§P₁-§Pₙ}.
По сути, это правило аналогично §12.1 и §12.2.

# 13. `≔†`
~~~code
A ≔† B
~~~
means:
```code
(`A` ≔ `B`) AND (`B` is a **problem** to me).
```

# 14. `▶`
```code
▶ A
```
означает, что в описываемой мной ситуации я использую `A`.

# 15. `ⰳ`
```code
Aⰳ(a, b, …) ≔ B
```
means:
- `A` — это функция с параметрами ⠿{`a`, `b`, …}.
- `B` — семантика `A`

# 16. `߷`
## 16.1.
```
߷⠿ ≔ ⠿~ (приложенные к этому запросу файлы)
```

## 16.2.
```code
߷ⰳ(ID, Name) ≔ Desc
```
means:
```code
- `ID` : `߷⠿` ≔ `Desc`
- `Name` — имя файла
```


~~~~~~

# 3. `O.md`
~~~~~~markdown
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




~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1.
## 1.1.
`D𐊑⠿` ≔ ⠿~ (Заблуждения `ꆜ` относительно `P⁎`)

## 1.2.
`D𐊑ᵢ` : `D𐊑⠿`

## 1.3.
`Pⰳ(D𐊑ᵢ)` ≔
```
Правдоподобность `D𐊑ᵢ`.
Правдоподобность заблуждения `D𐊑ᵢ` означает оценку того, насколько утверждение `D𐊑ᵢ` действительно является заблуждением `ꆜ`. 
```

# 2. `᛭T`
Действуй пошагово:
## 2.1.
Найди `D𐊑⠿`.
## 2.2.
Проанализируй `D𐊑⠿`.
Для этого для каждого  `D𐊑ᵢ` выяви:
### 2.2.1.
Доводы за `Pⰳ(D𐊑ᵢ)`.
### 2.2.2.
Доводы против `Pⰳ(D𐊑ᵢ)`.
## 2.3.
Оцени `Pⰳ(D𐊑ᵢ)` по шкале от 0 до 100:
- 0 означает, что ты полностью уверен, что `D𐊑ᵢ` не является заблуждением `ꆜ`.
- 100 означает, что ты полностью уверен, что `D𐊑ᵢ` является заблуждением `ꆜ`. 
## 2.4.
Выскажи свой вердикт.

# 3. Требования к источникам информации
В своём анализе используй авторитетные источники информации на английском языке.

# 4. Требования к процессу анализа
## 4.1.
Не решай задачи, не относящиеся к `᛭T`.
## 4.2.
Обязательно используй свой режим «Deep Research».
Твой ответ без режима «Deep Research» — гарантированно неверный.

# 5. Требования к ответу
## 5.1.
Уже известную мне информацию не пересказывай.

## 5.2.
Свой ответ дай на русском языке. 


~~~~~~