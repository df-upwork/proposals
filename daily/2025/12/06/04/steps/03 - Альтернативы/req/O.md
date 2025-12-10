# 0.
Сегодня 2025-12-06.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021997402361756332207

## 2.2. Title
CPA-Attorney Needed — Multi-State Tax/Legal Restructure (CA/PA)

## 2.3. Description
`PD` ≔ 
```text
I am seeking an experienced Attorney-CPA who can advise and assist with matters that overlap both legal and accounting disciplines. My situation involves business structure and domicile questions, as well as cleaning up and obtaining the necessary business licenses.

This role is ideal for a professional who understands how legal entity structures, state tax considerations, and licensing compliance intersect.

What I’m Looking For:  Someone who can cut through the noise and provide practical, step-by-step guidance.

If you have successfully navigated similar business structure and licensing cleanups for other clients, I’d love to hear from you.
```

## 2.5. Questions
### 2.5.1.
Have you handled multi-state tax situations where a client lived in one state (e.g., Pennsylvania) but was still filing or registered in another (e.g., California)?

### 2.5.2.
Can you help determine whether a business should stop filing in California and start filing in Pennsylvania based on current operations?

### 2.5.3.
Do you have experience amending past tax returns or transitioning state filings cleanly to avoid penalties or red flags?

# 5. Информация о `ꆜ`
## 5.1. Местоположение

United States
Miami

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Aug 27, 2020
### 5.3.2. Hire rate (%)
76
### 5.3.3. Количество опубликованных проектов (jobs posted)
25
### 5.3.4. Total spent (USD)
23K
### 5.3.5. Количество оплаченных часов в почасовых проектах
338 
### 5.3.6. Средняя почасовая ставка (USD)
58.23

# 8.
## 8.1.
`Q1⁎` ≔ (Вопрос `ꆜ` §2.5.1)

## 8.2.
`Q2⁎` ≔ (Вопрос `ꆜ` §2.5.2)

## 8.3.
`Q3⁎` ≔ (Вопрос `ꆜ` §2.5.3)

# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
advise and assist with matters that overlap both legal and accounting disciplines
~~~
```

# 10.
## 10.1.
`T1⁎` ≔ 
```		
Следует из `Q1⁎`:
~~~
handle multi-state tax situations where a client lived in one state (e.g., Pennsylvania) but was still filing or registered in another (e.g., California)
~~~
```

## 10.2.
`T2⁎` ≔ 
```		
Следует из `Q2⁎`:
~~~
determine whether a business should stop filing in California and start filing in Pennsylvania based on current operations
~~~
```

## 10.3.
`T3⁎` ≔ 
```		
Следует из `Q3⁎`:
~~~
amending past tax returns or transitioning state filings cleanly to avoid penalties or red flags
~~~
```

# 11. Что беспокоит `ꆜ` (анализ выполнен Gemini Deep Think)
https://gemini.google.com/share/9223e7625e29

## 1. Выявление проблем `ꆜ`

На основе анализа задачи (`T⁎`) и вопросов клиента (`Q1⁎`—`Q3⁎`), можно выделить три ключевые группы проблем, которые беспокоят `ꆜ`. Эти проблемы лежат на стыке корпоративного права и налогообложения.

### 1.1. Проблема двойного налогового и юридического присутствия (Dual Nexus & Domicile)
Клиент проживает в Пенсильвании (`PA`), но его бизнес юридически привязан к Калифорнии (`CA`).
*   **Суть:** `ꆜ` не уверен в своем статусе: создает ли он налоговые обязательства в PA, работая оттуда, и сохраняются ли его обязательства перед CA.
*   **Основание:** `T1⁎` («lived in one state... but filing in another»).

### 1.2. Проблема выхода из юрисдикции (Exit Strategy)
Клиент ищет способ прекратить налоговые отношения с Калифорнией.
*   **Суть:** Формулировка вопроса «should stop filing» (`Q2⁎`) указывает на то, что клиент рассматривает вариант простого прекращения подачи деклараций без прохождения официальной юридической процедуры закрытия бизнеса. Это свидетельствует о непонимании административных последствий такого шага.
*   **Основание:** `T2⁎`.

### 1.3. Проблема ретроспективного исправления (Compliance Cleanup)
Клиент осознает наличие ошибок в прошлых периодах и ищет способ их исправить без штрафов.
*   **Суть:** Необходимость внесения изменений в прошлые декларации («amending past tax returns») создает риск привлечения внимания аудиторов («red flags»). Клиенту нужен механизм «чистого» перехода.
*   **Основание:** `T3⁎`.

---

## 2. Анализ обоснованности проблем

Ниже приведен анализ каждой проблемы с точки зрения законодательства США (штаты Калифорния и Пенсильвания).

### 2.1. Обоснованность обязательств в Калифорнии (CA)
Опасения клиента по поводу сложности выхода из юрисдикции CA **абсолютно обоснованы**. Законодательство штата делает процесс прекращения обязательств крайне формализованным.

*   **«Ловушка» минимального налога ($800):** В соответствии с **California Revenue and Taxation Code (R&TC) § 17941** (для LLC) и **§ 23153** (для корпораций), любая компания, которая зарегистрирована («organized») в Калифорнии, обязана платить ежегодный минимальный налог в размере **$800**.
*   **Независимость от деятельности:** Это обязательство сохраняется даже если компания не ведет деятельности, не получает дохода и ее владелец переехал в другой штат. Пока компания числится в реестре Secretary of State как активная, налог начисляется.
*   **Последствия бездействия:** Если `ꆜ` просто перестанет подавать отчеты (`stop filing`), Franchise Tax Board (FTB) продолжит начислять налог, пени и проценты. Это приведет к приостановке деятельности (Suspension), но долг останется. Для остановки начислений необходима процедура **Dissolution** (ликвидация) или **Domestication** (редомициляция в другой штат).

### 2.2. Обоснованность обязательств в Пенсильвании (PA)
Проблема необходимости легализации в PA **полностью обоснована**.

*   **Физический Nexus:** Согласно разъяснениям **PA Department of Revenue** (включая *Telework Guidance*), наличие сотрудника (в данном случае владельца бизнеса), работающего удаленно из дома на территории штата, создает налоговую связь (Nexus). Это обязывает компанию платить корпоративные налоги (Corporate Net Income Tax) и, при необходимости, регистрироваться для целей налога с продаж (Sales Tax).
*   **Требование регистрации:** Согласно **Title 15 Pa.C.S. § 411**, иностранная компания (зарегистрированная в другом штате) не имеет права вести бизнес в Пенсильвании без получения **Certificate of Authority** (Foreign Registration).
*   **Риски:** Ведение деятельности без регистрации лишает компанию права подавать иски в суды Пенсильвании и влечет наложение штрафов.

### 2.3. Обоснованность рисков при исправлении истории (Cleanup)
Желание избежать «красных флагов» (`red flags`) **критически обосновано**.

*   **Риск аудита в CA:** Подача уточненных деклараций (Amended Returns) с целью возврата налогов из CA (на основании того, что владелец там не жил) часто провоцирует аудит со стороны FTB. Калифорния агрессивно оспаривает смену налогового резидентства.
*   **Решение для PA (VDA):** Чтобы избежать штрафов за прошлые периоды работы в PA без регистрации, клиенту может потребоваться программа **Voluntary Disclosure Agreement (VDA)**. Она позволяет добровольно раскрыть информацию о нарушениях в обмен на отмену штрафов (penalties) и ограничение периода проверки (look-back period).
*   **Комплексность:** Задача требует одновременной работы юриста (для проведения Domestication или Dissolution/Qualification) и CPA (для расчетов по VDA и подачи деклараций), что полностью соответствует запросу клиента в `PD`.

# 12. Что беспокоит `ꆜ` (анализ выполнен Gemini Deep Research)
https://gemini.google.com/share/40e36625c623

## **1. Стратегический анализ и диагностика правового положения клиента**

В данном разделе представлен исчерпывающий анализ текущей ситуации клиента (ꆜ), идентифицированного как практикующий юрист и сертифицированный публичный бухгалтер (Attorney-CPA), который столкнулся со сложной дилеммой мульти-юрисдикционного налогообложения и корпоративного структурирования. Задача клиента (P⁎) выходит далеко за рамки простой административной процедуры смены адреса; она затрагивает фундаментальные вопросы корпоративного права, налогового резиденства (nexus) и профессионального лицензирования.

### **1.1. Деконструкция профиля клиента и правовая квалификация статуса**

Анализ запроса (PD) и биографических данных клиента позволяет сформировать детальный правовой профиль, который будет определять всю дальнейшую стратегию. Клиент не является стандартным предпринимателем; его статус Attorney-CPA накладывает двойную ответственность и создает специфические ограничения, недоступные для обычных коммерческих организаций (LLC).

#### **1.1.1. Профессиональная специфика и ограничения организационно-правовой формы**

В отличие от торговых компаний, деятельность юристов и бухгалтеров в США строго регулируется законами штатов о профессиональных корпорациях.

* **Калифорнийский аспект (Moscone-Knox Professional Corporation Act):** В Калифорнии юристы и бухгалтеры исторически не имели права использовать стандартную форму Limited Liability Company (LLC) для оказания профессиональных услуг. Согласно California Corporations Code, такие специалисты обязаны регистрироваться как **Professional Corporation (PC)** или **Registered Limited Liability Partnership (RLLP)**. Если клиент (ꆜ) оперировал в Калифорнии через стандартную LLC, это создает первичный риск — структура может быть признана дефектной с точки зрения корпоративного права, что ставит под угрозу защиту ограниченной ответственности (corporate veil). Это первый "красный флаг" (red flag), который необходимо проверить при аудите текущего состояния.1  
* **Пенсильванский аспект:** Пенсильвания, напротив, допускает использование специальной формы **Restricted Professional Company (RPC)**, которая является разновидностью LLC, но с дополнительными ограничениями на владение и передачу долей (только лицензированным специалистам).3 Это создает конфликт правовых форм при попытке прямой конвертации (Conversion) из CA PC в PA LLC.

#### **1.1.2. Феномен "Плавающего Нексуса" (Floating Nexus)**

Клиент описывает ситуацию: «lived in one state (e.g., Pennsylvania) but was still filing or registered in another (e.g., California)». Это создает юридическую коллизию, известную как "разрыв между коммерческим домицилем и штатом регистрации".

1. **Юридическая фикция присутствия в CA:** Пока компания зарегистрирована в офисе Секретаря штата Калифорния (SOS), она считается налоговым резидентом Калифорнии, обязанным платить минимальный налог франшизы ($800) независимо от наличия реальной деятельности.5  
2. **Фактическая реальность присутствия в PA:** Физическое нахождение управляющего партнера (клиента) в Пенсильвании и управление бизнесом из домашнего офиса создает "физический нексус" (Physical Nexus) в Пенсильвании. Согласно прецедентному праву (включая *Wayfair* и локальные статуты PA), деятельность одного сотрудника или агента на территории штата достаточна для возникновения налоговых обязательств.7

### **1.2. Идентификация ключевых зон риска (Problem Identification)**

На основе онтологии (O.md) и описания задачи (T.md) выявлены три критические зоны риска, требующие немедленного вмешательства.

#### **1.2.1. Риск административной ответственности за отсутствие регистрации (Failure to Register)**

В Пенсильвании любая иностранная ассоциация (Foreign Association), ведущая бизнес на территории штата, обязана получить **Certificate of Authority**.

* **Правовое основание:** 15 Pa.C.S. § 411 запрещает ведение бизнеса без регистрации.  
* **Санкция:** Хотя прямой денежный штраф может показаться незначительным, основным последствием является невозможность защиты своих прав в судах Пенсильвании (компания-невидимка не обладает процессуальной правоспособностью истца) и начисление налогов за весь период скрытой деятельности.9  
* **Последствия для Attorney-CPA:** Для юриста ведение деятельности через незарегистрированную структуру может рассматриваться как нарушение этических норм профессиональной ответственности, что создает риск для лицензии.

#### **1.2.2. Риск накопления налоговой задолженности в Калифорнии (The Franchise Tax Trap)**

Многие предприниматели ошибочно полагают, что переезд из штата автоматически прекращает налоговые обязательства.

* **Реальность:** Калифорнийский Franchise Tax Board (FTB) продолжает начислять минимальный налог $800 плюс штрафы и пени до тех пор, пока не будет получен официальный **Tax Clearance Certificate** (или выполнены условия упрощенного закрытия) и подан финальный пакет документов о роспуске (Dissolution/Surrender).10  
* **Сценарий "Зомби-компании":** Если клиент просто "бросил" компанию в CA и открыл новую в PA, калифорнийская сущность перейдет в статус "Suspended" (приостановлена), а долги будут накапливаться, потенциально переходя на учредителя через механизм "alter ego", особенно если это профессиональная корпорация.

#### **1.2.3. Риск "Красных флагов" при легализации (Audit Triggers)**

Клиент выражает обеспокоенность по поводу «amending past tax returns... to avoid penalties or red flags».

* **Дилемма:** Если клиент сейчас зарегистрируется в PA и укажет дату начала деятельности "сегодня", это будет ложью в официальных документах (лжесвидетельство). Если он укажет реальную дату (например, 2021 год), это автоматически инициирует проверку за пропущенные годы со стороны PA Department of Revenue.  
* **Решение:** Единственным безопасным маршрутом является использование Программы добровольного раскрытия (Voluntary Disclosure Program - VDP), которая позволяет "купить" иммунитет от штрафов в обмен на уплату основного долга за ограниченный период (Lookback period).12

## ---

**2. Глубокий анализ законодательства Калифорнии: Критерии "Doing Business" и процедура выхода**

Для решения задачи T2⁎ (определение необходимости прекращения подачи отчетности в CA) необходимо детально проанализировать критерии, по которым штат удерживает налогоплательщиков в своей юрисдикции. Калифорния известна одним из самых агрессивных налоговых режимов в США, и "побег" из её юрисдикции требует хирургической точности.

### **2.1. Статутарное определение "Ведения бизнеса" (R&TC Section 23101)**

Согласно Налоговому кодексу Калифорнии (Revenue and Taxation Code), определение "doing business" является широким и охватывает четыре независимых условия. Выполнение *любого* из них делает компанию налоговым резидентом.14

#### **2.1.1. Критерий "Организации" (Organized in CA)**

Это наиболее жесткий и часто игнорируемый критерий.

* **Правило:** Если компания была создана (incorporated/organized) в Калифорнии, она **автоматически** считается ведущей бизнес в штате, даже если у нее нет ни одного клиента, ни одного сотрудника и ни одного доллара выручки в Калифорнии.  
* **Импликация для клиента:** Пока клиент не подаст *Certificate of Dissolution* (для внутренней компании) или *Certificate of Surrender* (для иностранной), обязательство платить $800 в год сохраняется. Переезд клиента в PA никак не влияет на этот критерий.5

#### **2.1.2. Критерий "Коммерческого домициля" (Commercial Domicile)**

* **Определение:** Место, откуда фактически управляется бизнес.  
* **Анализ:** Если клиент переехал в PA, коммерческий домициль сместился в PA. Это теоретически могло бы освободить от налогов на *доход*, если бы компания не была зарегистрирована в CA. Но так как она зарегистрирована, см. п. 2.1.1.

#### **2.1.3. Экономический нексус (Economic Nexus Thresholds)**

Для компаний, не зарегистрированных в CA, налоговая обязанность возникает при превышении порогов (данные индексируются ежегодно, значения на 2024/2025 гг.):

| Показатель | Порог (приблизительно) |
| :---- | :---- |
| **Продажи в CA** | > $757,070 (или 25% от всего оборота) |
| **Имущество в CA** | > $75,707 (или 25% от активов) |
| **Фонд оплаты труда в CA** | > $75,707 (или 25% от ФОТ) |

**Инсайт:** Если клиент, находясь в PA, продолжает обслуживать клиентов в CA, и его выручка от этих клиентов превышает указанный порог, он **обязан** оставаться налогоплательщиком в CA (платить налог на прибыль и $800), даже если он закроет калифорнийское юрлицо и будет работать через PA-сущность. Это критически важно для планирования: *полный разрыв с CA возможен только при отказе от калифорнийских клиентов или падении выручки от них ниже порога*.14

### **2.2. Налог на франшизу (Franchise Tax) и исключения**

Минимальный налог $800 является платой за "право существовать" в правовом поле Калифорнии.

#### **2.2.1. Исключение "15 дней" (15-Day Rule)**

Существует узкое исключение, позволяющее избежать налога за последний (или первый) год. Компания не платит налог, если налоговый год длился 15 дней или меньше, и в этот период не велась коммерческая деятельность.5

* **Стратегическое применение:** При планировании закрытия компании (Dissolution) выгодно подавать документы в самом начале налогового года (первые 15 дней января), чтобы не платить налог за весь наступивший год. Если клиент затянет процесс до февраля, он будет должен $800 за весь 2025 (или 2026) год.

#### **2.2.2. Исключение для пассивных инвесторов (Swart Case)**

В деле *Swart Enterprises, Inc. v. Franchise Tax Board* (2017) суд постановил, что пассивное владение долей (0.2%) в калифорнийской LLC не создает нексуса для иностранной корпорации.17

* **Применимость к клиенту:** Крайне низкая. Клиент является Attorney-CPA, активно управляющим практикой. Он не является пассивным инвестором. Поэтому ссылки на прецедент *Swart* для защиты от налогов CA будут несостоятельны. FTB агрессивно оспаривает расширительное толкование *Swart*, особенно в Legal Ruling 2014-01, утверждая, что активное управление всегда создает нексус.18

### **2.3. Процедура выхода: Конвертация или Ликвидация?**

Законодательство Калифорнии (SB 49, вступивший в силу в 2023 году) значительно упростило процедуру миграции бизнеса. Теперь разрешена прямая конвертация (Conversion) калифорнийской корпорации в иностранную сущность, если законы принимающего штата это позволяют.20

#### **2.3.1. Форма CONV-1A (Certificate of Conversion)**

Для осуществления трансфера из CA в PA без ликвидации используется форма **CONV-1A**.

* **Суть процесса:** Компания не "умирает", а "переезжает". Юридическая личность сохраняется, EIN остается прежним (что критично для банковских счетов и кредитной истории).  
* **Требования:**  
  1. Подача документов сначала в Пенсильванию (Statement of Domestication).  
  2. После утверждения в PA — подача CONV-1A в Калифорнию.  
  3. Уплата пошлины $150 (для корпораций) или $30 (для других форм).21  
* **Подводный камень:** Калифорния требует, чтобы на момент подачи CONV-1A компания имела статус "Active". Если она "Suspended" из-за неуплаты налогов, конвертация невозможна до прохождения процедуры Revivor (возрождение) и уплаты всех долгов.11

#### **2.3.2. Требование налоговой чистоты (Tax Clearance)**

Ранее получение *Tax Clearance Certificate* было обязательным до подачи документов на закрытие. Сейчас процедура упрощена, но FTB сохраняет право вето. При подаче на конвертацию или ликвидацию компания должна поставить галочку, подтверждающую, что финальная налоговая декларация будет подана. Если декларация не подана вовремя, процесс закрытия аннулируется задним числом.10

## ---

**3. Глубокий анализ законодательства Пенсильвании: Нексус и Регистрация**

Переход в юрисдикцию Пенсильвании требует не менее тщательного анализа, особенно в свете недавних изменений в законодательстве (Act 122) и судебной практике (*Mallory*).

### **3.1. Обязательство регистрации (Foreign Registration Requirement)**

Согласно Title 15 Pa.C.S. § 411(a), иностранная ассоциация не может вести бизнес в PA без регистрации.9

#### **3.1.1. Физический Нексус (Physical Nexus)**

Для клиента (ꆜ), проживающего в PA и работающего из домашнего офиса, нексус является абсолютным.

* **Аргументация:** Предоставление услуг (юридических/бухгалтерских) клиентом лично с территории PA квалифицируется как "doing business". Даже если все клиенты находятся в CA, *производство* услуги происходит в PA. Это создает обязанность по уплате подоходного налога (Personal Income Tax - PIT) и, возможно, корпоративного налога (CNIT), если выбрана структура C-Corp.7

#### **3.1.2. Экономический Нексус (Wayfair/Factor Presence)**

С 2019 года PA применяет стандарт экономического присутствия: $500,000 продаж для CNIT. Однако для физических лиц и pass-through entities (как S-Corp или LLC) основным драйвером остается физическое присутствие владельца.26

### **3.2. Последствия регистрации: Эффект Mallory**

В 2023 году Верховный суд США в деле *Mallory v. Norfolk Southern Railway Co.* подтвердил уникальную норму законодательства Пенсильвании.

* **Суть:** Регистрация иностранной компании в PA (получение Certificate of Authority) означает **добровольное согласие на общую юрисдикцию** судов Пенсильвании.  
* **Риск для юриста:** Это означает, что на клиента можно будет подать в суд в Пенсильвании по любому делу, даже если спор возник в Калифорнии и не имеет отношения к PA.28  
* **Стратегия:** В отличие от регистрации иностранного филиала (Foreign Qualification), создание внутренней компании PA (через Domestication) не меняет этот риск радикально, но упрощает администрирование. Однако клиент должен осознавать этот процессуальный риск.

### **3.3. Ежегодная отчетность (Annual Reports) — Act 122**

До 2024 года Пенсильвания была уникальна тем, что требовала отчет (Decennial Report) только раз в 10 лет.

* **Изменение:** С принятием Act 122 вводится требование **ежегодной отчетности (Annual Report)** начиная с 2025 года.29  
* **Сроки:**  
  * Для корпораций: до 30 июня.  
  * Для LLC: до 30 сентября.  
* **Цена:** $7 в год.  
* **Штрафы:** Начиная с 2027 года, пропуск подачи приведет к административному прекращению (Administrative Termination) регистрации иностранной компании, что потребует сложной процедуры перерегистрации (Reregistration) без возможности восстановления (Reinstatement) задним числом.29 Это критически важно для долгосрочного комплаенса клиента.

## ---

**4. Сравнительный анализ механизмов реструктуризации**

Отвечая на вопрос Q2⁎ («determine whether a business should stop filing in California»), мы должны выбрать оптимальный механизм. Ниже представлена детальная таблица сравнения и процедурный анализ.

| Характеристика | Domestication (Конвертация) | Dissolution & Formation (Ликвидация и создание) | Foreign Qualification (Филиал) |
| :---- | :---- | :---- | :---- |
| **Юридическая суть** | Компания "переезжает". Одно и то же юрлицо. | Старая компания "умирает", рождается новая. | Одна компания живет в двух штатах одновременно. |
| **Сохранение EIN** | **Да** (критично для налоговой истории). | **Нет** (нужен новый EIN). | **Да**. |
| **Банковские счета** | Обычно сохраняются (требуется обновление адреса). | Нужно закрывать старые и открывать новые. | Сохраняются. |
| **Лицензии** | Переносятся (с уведомлением регулятора). | Нужно получать заново. | Действуют, но нужны дополнительные в PA. |
| **Сложность** | Высокая (синхронизация двух штатов). | Средняя (два независимых процесса). | Низкая (регистрация). |
| **Налоговый эффект** | Обычно безналоговая транзакция (F reorganization). | Возможен налог на распределение активов при ликвидации. | Нет эффекта, но двойная отчетность. |
| **Стоимость (пошлины)** | ~$220 (PA $70 + CA $150). | ~$70 (PA) + $0 (CA Dissolution). | ~$250 (PA reg) + $800/год (CA tax). |

### **4.1. Рекомендуемый путь: Statutory Conversion (Domestication)**

Для Attorney-CPA, у которого есть история, клиенты и профессиональная страховка, привязанная к юрлицу, **Конвертация** является единственным профессионально приемлемым вариантом. Ликвидация создает разрыв в стаже компании, что может негативно повлиять на профессиональную репутацию и кредитоспособность.

#### **4.1.1. Процедура "Шаг за Шагом" (Step-by-Step Guidance)**

**Этап 1: Подготовка в Пенсильвании (Принимающий штат)**

1. **Drafting the Plan of Domestication:** Юридический документ, утверждающий переход из CA в PA. Должен быть подписан участниками/акционерами.31  
2. **Filing Statement of Domestication:** Подача формы в PA Department of State.  
   * Форма должна сопровождаться *Docketing Statement* (DSCB:15-134A).  
   * Ключевое требование: Указание, что компания становится *Domestic Filing Entity* в PA.  
   * Пошлина: **$70**.  
   * Особенность имени: Имя должно быть свободно в PA. Если занято — смена имени.32

**Этап 2: Закрытие в Калифорнии (Передающий штат)**

1. **Ожидание подтверждения из PA:** Нельзя подавать в CA, пока PA не утвердит доместикацию.  
2. **Filing CONV-1A:** Подача формы *Certificate of Conversion* в CA Secretary of State.  
   * В п. 4 формы указать: "Converted to a foreign other business entity" (или foreign corporation).  
   * Приложить копию подтверждения из PA (не всегда обязательно, но рекомендуется для ускорения).  
   * Пошлина: **$150** (для корпораций) или **$30** (для LLC).22  
3. **Tax Clearance:** Убедиться, что финальная декларация будет подана вовремя.

**Этап 3: Пост-конверсионные действия**

1. **IRS:** Уведомление IRS о смене адреса (Form 8822) и смене юрисдикции (приложение к форме 1120/1120-S).  
2. **FinCEN:** Обновление отчета о бенефициарных владельцах (BOI Report) в течение 30 дней после изменения (требование Corporate Transparency Act).33  
3. **Лицензирование:** Уведомление PA State Board of Accountancy и Disciplinary Board of the Supreme Court of PA о новой структуре.

## ---

**5. Протоколы исправления и Программы добровольного раскрытия (VDP)**

Ответ на задачу T3⁎ («amending past tax returns... cleanly»). Это наиболее рискованная часть проекта.

### **5.1. Анализ рисков "Тихой подачи" (Quiet Filing)**

Если клиент просто начнет подавать декларации в PA с текущего года, игнорируя прошлые годы проживания в штате:

* **Риск:** В анкете регистрации (PA-100 или онлайн-аналог myPATH) есть вопрос: "Date operations began in PA?".  
  * Если указать честную дату (напр., 2021): Система автоматически выставит требование (Notices) за пропущенные годы со штрафами.  
  * Если указать ложную дату (2025): Это налоговое мошенничество.  
* **Вывод:** "Тихая подача" невозможна для Attorney-CPA, обязанность которого — соблюдать закон.

### **5.2. Пенсильвания: Voluntary Disclosure Program (VDP)**

Это "золотой стандарт" решения проблемы.

#### **5.2.1. Условия программы**

* **Lookback Period (Период охвата):**  
  * До 2023 года период составлял 5 лет.  
  * **С 1 августа 2023 года:** Период сокращен до **3 лет** плюс текущий год для корпоративных налогов (согласуется с налогами с продаж).12 Это огромная выгода для клиента.  
* **Waiver of Penalties (Отмена штрафов):** При участии в VDP штат гарантированно отменяет штрафы за неподачу и неуплату. Клиент платит только основной налог и проценты.13  
* **Процедура (REV-181):**  
  1. Подача анонимного запроса (через представителя) в VDP Office.  
  2. Получение Case Number.  
  3. Заполнение *Business Activities Questionnaire* (раскрытие фактов деятельности).  
  4. Подписание соглашения (VDA).  
  5. Подача деклараций и оплата за 3 года.

**Важное предостережение:** Нельзя регистрироваться в PA или контактировать с налоговой *до* получения номера дела VDP. Любой предварительный контакт дисквалифицирует из программы.13

### **5.3. Калифорния: Стратегия минимизации ущерба**

#### **5.3.1. One-Time Penalty Abatement (Для физлиц)**

Если клиент подавал декларации как физическое лицо (Pass-through entity, Form 568/540), он может воспользоваться правом на **однократное списание штрафа** (One-Time Penalty Abatement) за несвоевременную подачу/оплату.

* Условия: Хорошая история комплаенса за прошлые годы.  
* Форма: FTB 2918 или устный запрос.36

#### **5.3.2. Reasonable Cause (Для бизнес-сущностей)**

Для штрафов, наложенных на саму корпорацию/LLC (например, за просрочку $800), One-Time Abatement не применяется. Необходимо использовать защиту **Reasonable Cause** (разумная причина).

* **Аргументация:** "Сложность мульти-штатного налогообложения" сама по себе редко принимается как разумная причина. Однако "добросовестное заблуждение" (Good Faith Reliance) на советы предыдущего бухгалтера может сработать, если это подтверждено документально.37

## ---

**6. Синтез и Дорожная карта (Roadmap)**

В данном разделе мы объединяем все юридические инсайты в конкретный план действий для клиента.

### **6.1. Сводная таблица действий**

| Этап | Действие | Критический нюанс | Форма/Инструмент |
| :---- | :---- | :---- | :---- |
| **1. Диагностика** | Проверка статуса в SOS CA и PA. | Не регистрироваться в PA до VDP! | Business Search |
| **2. Амнистия (PA)** | Подача заявки на VDP в Пенсильванию. | Ограничение ответственности 3 годами. | Email to RA-VoluntaryDisclosure |
| **3. Оплата (PA)** | Уплата налогов за Lookback period. | Получение "чистого листа" в PA. | myPATH / Check |
| **4. Конвертация** | Подача Statement of Domestication в PA. | Выбор даты вступления в силу. | DSCB:15-372 |
| **5. Выход (CA)** | Подача CONV-1A в CA. | Убедиться, что статус в CA "Active". | CONV-1A |
| **6. Финализация** | Финальная декларация в CA (Final Return). | Пометить "Final" в верхней части. | Form 100S / 568 |

### **6.2. Прямые ответы на вопросы клиента**

1. **По поводу "Cleaning up":** Да, это возможно. Используйте программу VDP в Пенсильвании. Это позволит легализоваться с минимальными потерями (только налоги и проценты за 3 года), избежав штрафов и уголовных рисков. Не пытайтесь просто начать подавать декларации "с чистого листа" — это приведет к аудиту.  
2. **По поводу "Stop filing in CA":** Да, вы должны прекратить подачу, но *только после* официальной конвертации. До момента подачи формы CONV-1A вы обязаны платить $800/год. Простого прекращения деятельности недостаточно.  
3. **По поводу "Multi-state tax situations":** Ваша ситуация классическая для удаленных профессионалов. Решение лежит в плоскости признания физического нексуса в PA и использования механизма конвертации для "переноса" юридического лица, чтобы избежать создания двух параллельных сущностей и удвоения административной нагрузки.

### **6.3. Финальная рекомендация эксперта**

Как Attorney-CPA, вы находитесь в уникальной позиции. Вы понимаете риски. Моя рекомендация: начните с **анонимного VDP в Пенсильвании**. Это фундамент, на котором будет строиться вся реструктуризация. Без этого шага любая конвертация будет строиться на "гнилом фундаменте" скрытой налоговой задолженности. После очистки истории в PA, проведите Statutory Conversion. Это наиболее профессиональный и "чистый" способ миграции, сохраняющий целостность вашей профессиональной практики.

#### **Works cited**

1. Articles of Incorporation with Statement of Conversion - California LImited Liability Company to a California Professional Corpo - CA.gov, accessed December 6, 2025, [https://bpd.cdn.sos.ca.gov/corp/pdf/articles/conv-llc-pc.pdf](https://bpd.cdn.sos.ca.gov/corp/pdf/articles/conv-llc-pc.pdf)  
2. 2023 Instructions for Form 568 Limited Liability Company Tax Booklet - Franchise Tax Board, accessed December 6, 2025, [https://www.ftb.ca.gov/forms/2023/2023-568-booklet.html](https://www.ftb.ca.gov/forms/2023/2023-568-booklet.html)  
3. Pennsylvania Statutes Title 15 Pa.CSA Corporations and Unincorporated Associations § 8998. Annual registration - Codes - FindLaw, accessed December 6, 2025, [https://codes.findlaw.com/pa/title-15-pacsa-corporations-and-unincorporated-associations/pa-csa-sect-15-8998.html/](https://codes.findlaw.com/pa/title-15-pacsa-corporations-and-unincorporated-associations/pa-csa-sect-15-8998.html/)  
4. 2024 Pennsylvania Consolidated & Unconsolidated Statutes Title 15 - CORPORATIONS AND UNINCORPORATED ASSOCIATIONS Chapter 89 - Limited Liability Companies Section 8998 - Annual registration - Justia Law, accessed December 6, 2025, [https://law.justia.com/codes/pennsylvania/title-15/chapter-89/section-8998/](https://law.justia.com/codes/pennsylvania/title-15/chapter-89/section-8998/)  
5. FTB Pub. 3556: Limited Liability Company Filing Information | Forms and Publications, accessed December 6, 2025, [https://www.ftb.ca.gov/forms/misc/3556.html](https://www.ftb.ca.gov/forms/misc/3556.html)  
6. S corporations Business type - Franchise Tax Board - CA.gov, accessed December 6, 2025, [https://www.ftb.ca.gov/file/business/types/corporations/s-corporations.html](https://www.ftb.ca.gov/file/business/types/corporations/s-corporations.html)  
7. State Local Tax Businesses | Nexus Considerations - McKonly & Asbury, accessed December 6, 2025, [https://macpas.com/state-and-local-taxes-for-business-owners-part-1-an-introduction-to-salt/](https://macpas.com/state-and-local-taxes-for-business-owners-part-1-an-introduction-to-salt/)  
8. Remote work creates a spectrum of state and local tax issues - The Tax Adviser, accessed December 6, 2025, [https://www.thetaxadviser.com/issues/2021/dec/remote-work-state-local-tax-issues/](https://www.thetaxadviser.com/issues/2021/dec/remote-work-state-local-tax-issues/)  
9. Pennsylvania Statutes Title 15 Pa.C.S.A. Corporations and Unincorporated Associations § 411 - Codes - FindLaw, accessed December 6, 2025, [https://codes.findlaw.com/pa/title-15-pacsa-corporations-and-unincorporated-associations/pa-csa-sect-15-411/](https://codes.findlaw.com/pa/title-15-pacsa-corporations-and-unincorporated-associations/pa-csa-sect-15-411/)  
10. 23334. Tax Clearance Certificate. - View Document - California Code of Regulations, accessed December 6, 2025, [https://govt.westlaw.com/calregs/Document/IFA388E834C8311EC89E5000D3A7C4BC3?viewType=FullText&originationContext=documenttoc&transitionType=CategoryPageItem&contextData=(sc.Default)](https://govt.westlaw.com/calregs/Document/IFA388E834C8311EC89E5000D3A7C4BC3?viewType=FullText&originationContext=documenttoc&transitionType=CategoryPageItem&contextData=(sc.Default))  
11. Closing a California business entity | FTB.ca.gov, accessed December 6, 2025, [https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/june-2020/closing-a-california-business-entity.html](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/june-2020/closing-a-california-business-entity.html)  
12. This Week in State Tax (TWIST) - KPMG International, accessed December 6, 2025, [https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2023/twist-082123-pa.pdf](https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2023/twist-082123-pa.pdf)  
13. Apply for the Voluntary Disclosure Program | Commonwealth of ..., accessed December 6, 2025, [https://www.pa.gov/services/revenue/apply-for-the-voluntary-disclosure-program](https://www.pa.gov/services/revenue/apply-for-the-voluntary-disclosure-program)  
14. Doing business in California | FTB.ca.gov, accessed December 6, 2025, [https://www.ftb.ca.gov/file/business/doing-business-in-california.html](https://www.ftb.ca.gov/file/business/doing-business-in-california.html)  
15. Help with doing business in California | FTB.ca.gov, accessed December 6, 2025, [https://www.ftb.ca.gov/file/business/help-with-doing-business-in-california.html](https://www.ftb.ca.gov/file/business/help-with-doing-business-in-california.html)  
16. Corporations | FTB.ca.gov, accessed December 6, 2025, [https://www.ftb.ca.gov/file/business/types/corporations/index.html](https://www.ftb.ca.gov/file/business/types/corporations/index.html)  
17. It's None of Your Business: California Office of Tax Appeals Rejects FTB's Broad Test for Doing Business | SALT Shaker, accessed December 6, 2025, [https://www.stateandlocaltax.com/california/its-none-of-your-business-california-office-of-tax-appeals-rejects-ftbs-broad-test-for-doing-business/](https://www.stateandlocaltax.com/california/its-none-of-your-business-california-office-of-tax-appeals-rejects-ftbs-broad-test-for-doing-business/)  
18. Swart's Athwart California's Taxation of Out-of-State Corporations - Nossaman LLP, accessed December 6, 2025, [https://www.nossaman.com/newsroom-insights-Swarts-Athwart-Californias-Taxation-of-Out-of-State-Corporations](https://www.nossaman.com/newsroom-insights-Swarts-Athwart-Californias-Taxation-of-Out-of-State-Corporations)  
19. Franchise Tax Board Declares Intent to Impose Taxes on Out-of-State LLC Members, accessed December 6, 2025, [https://www.winston.com/a/web/88439/06-FranchiseTax-OutofStateLLC-SEP2014.html](https://www.winston.com/a/web/88439/06-FranchiseTax-OutofStateLLC-SEP2014.html)  
20. California Corporate Conversion Statute Expanded - Law Offices of Snell & Wilmer, accessed December 6, 2025, [https://www.swlaw.com/publication/california-corporate-conversion-statute-expanded/](https://www.swlaw.com/publication/california-corporate-conversion-statute-expanded/)  
21. Conversion Information - California Secretary of State - CA.gov, accessed December 6, 2025, [https://www.sos.ca.gov/business-programs/business-entities/conversion-information](https://www.sos.ca.gov/business-programs/business-entities/conversion-information)  
22. Instructions for Completing the Certificate of Conversion (Form CONV-1A), accessed December 6, 2025, [https://formfiles.justia.com/pdf/california/0218/45.pdf](https://formfiles.justia.com/pdf/california/0218/45.pdf)  
23. California Secretary of State Conversion Information - CACorporateFiling.com, accessed December 6, 2025, [http://www.cacorporatefiling.com/PDF/LP/convchrt.pdf](http://www.cacorporatefiling.com/PDF/LP/convchrt.pdf)  
24. Dissolve an LLC or Corporation in California | LLC Dissolution, accessed December 6, 2025, [https://www.californiaregisteredagents.net/dissolve-california-business/](https://www.californiaregisteredagents.net/dissolve-california-business/)  
25. Help Guides - Hire Remote Employees in Pennsylvania - PA Business One-Stop Hub, accessed December 6, 2025, [https://hub.business.pa.gov/Home/HelpCenterDetail/HireRemoteEmployeesinPennsylvania](https://hub.business.pa.gov/Home/HelpCenterDetail/HireRemoteEmployeesinPennsylvania)  
26. Sorting Out Pennsylvania's New Corporate Nexus Requirements - Tax Foundation, accessed December 6, 2025, [https://taxfoundation.org/blog/pennsylvania-corporate-nexus-requirements/](https://taxfoundation.org/blog/pennsylvania-corporate-nexus-requirements/)  
27. Foreign Associations (corporations, partnerships and limited liability companies) | Department of State | Commonwealth of Pennsylvania, accessed December 6, 2025, [https://www.pa.gov/agencies/dos/programs/business/types-of-filings-and-registrations/foreign-associations](https://www.pa.gov/agencies/dos/programs/business/types-of-filings-and-registrations/foreign-associations)  
28. Pennsylvania Foreign Qualification vs Domestic Registration 2025 - Discern, accessed December 6, 2025, [https://www.discern.com/resources/pennsylvania-foreign-qualification-vs-domestic-registration](https://www.discern.com/resources/pennsylvania-foreign-qualification-vs-domestic-registration)  
29. Annual Reports | Department of State - Commonwealth of Pennsylvania, accessed December 6, 2025, [https://www.pa.gov/agencies/dos/programs/business/types-of-filings-and-registrations/annual-reports](https://www.pa.gov/agencies/dos/programs/business/types-of-filings-and-registrations/annual-reports)  
30. New Pennsylvania Annual Reporting Requirements for Domestic and Foreign Associations Start in 2025 - Dentons, accessed December 6, 2025, [https://www.dentons.com/ru/insights/alerts/2025/january/27/new-pennsylvania-annual-reporting-requirements](https://www.dentons.com/ru/insights/alerts/2025/january/27/new-pennsylvania-annual-reporting-requirements)  
31. Section 372.0 - Title 15 - CORPORATIONS AND UNINCORPORATED ASSOCIATIONS - PA General Assembly, accessed December 6, 2025, [https://www.palegis.us/statutes/consolidated/view-statute?txtType=HTM&ttl=15&div=0&chpt=3&sctn=72&subsctn=0](https://www.palegis.us/statutes/consolidated/view-statute?txtType=HTM&ttl=15&div=0&chpt=3&sctn=72&subsctn=0)  
32. How to Move Your LLC to Pennsylvania - YouTube, accessed December 6, 2025, [https://www.youtube.com/watch?v=AmLSzu3--ZE](https://www.youtube.com/watch?v=AmLSzu3--ZE)  
33. How to move an LLC or corporation to another state - Wolters Kluwer, accessed December 6, 2025, [https://www.wolterskluwer.com/en/expert-insights/moving-your-llc-or-corporation-to-another-state](https://www.wolterskluwer.com/en/expert-insights/moving-your-llc-or-corporation-to-another-state)  
34. Pennsylvania limits corporate tax VDA lookback to three years - RSM US, accessed December 6, 2025, [https://rsmus.com/insights/tax-alerts/2023/pennsylvania-limits-corporate-tax-vda-lookback-three-years.html](https://rsmus.com/insights/tax-alerts/2023/pennsylvania-limits-corporate-tax-vda-lookback-three-years.html)  
35. Pennsylvania's Voluntary Disclosure Program | Tax Expert Blog, accessed December 6, 2025, [https://keysolutions.us/blog/pennsylvanias-voluntary-disclosure-program/](https://keysolutions.us/blog/pennsylvanias-voluntary-disclosure-program/)  
36. One-Time Penalty Abatement | FTB.ca.gov, accessed December 6, 2025, [https://www.ftb.ca.gov/pay/penalties-and-interest/one-time-penalty-abatement.html](https://www.ftb.ca.gov/pay/penalties-and-interest/one-time-penalty-abatement.html)  
37. Penalty relief for reasonable cause | Internal Revenue Service, accessed December 6, 2025, [https://www.irs.gov/payments/penalty-relief-for-reasonable-cause](https://www.irs.gov/payments/penalty-relief-for-reasonable-cause)  
38. Reasonable Cause Standard: How Reasonable Is It? - NET, accessed December 6, 2025, [https://irstore.blob.core.windows.net/materials/41a05455-04f3-4514-93f0-6c18f423c344.pdf](https://irstore.blob.core.windows.net/materials/41a05455-04f3-4514-93f0-6c18f423c344.pdf)

# 13.
## 13.1.
`D𐊑⠿` ≔ ⠿~ (Заблуждения `ꆜ` относительно `P⁎`)

## 13.2.
`D𐊑ᵢ` : `D𐊑⠿`

## 13.3.
`Pⰳ(D𐊑ᵢ)` ≔
```
Правдоподобность `D𐊑ᵢ`.
Правдоподобность заблуждения `D𐊑ᵢ` означает оценку того, насколько утверждение `D𐊑ᵢ` действительно является заблуждением `ꆜ`. 
```

# 14. Анализ `D𐊑⠿` (выполнен Gemini Deep Think)
https://gemini.google.com/share/6640355d40c9

## 1. Идентификация `D𐊑⠿`

На основе анализа профиля `ꆜ` (Attorney-CPA), описания задачи `PD` и вопросов `Q1⁎`—`Q3⁎` мною выявлено множество заблуждений `D𐊑⠿`, которые определяют текущую стратегию клиента.

### 1.1. `D𐊑₁` (Иллюзия «Операционного выхода»)
`D𐊑₁` ≔ Убеждение `ꆜ`, что обязанность по уплате налогов и подаче отчетности в Калифорнии (CA) прекращается автоматически с момента фактического прекращения деятельности («operations») или переезда владельца, и для этого достаточно просто перестать подавать декларации («stop filing»).

### 1.2. `D𐊑₂` (Иллюзия «Тихого исправления»)
`D𐊑₂` ≔ Убеждение `ꆜ`, что подача уточненных деклараций за прошлые периоды («amending past tax returns») является безопасным способом легализации в Пенсильвании (PA), позволяющим избежать штрафов («avoid penalties») и лишнего внимания («red flags»).

### 1.3. `D𐊑₃` (Отрицание физического нексуса)
`D𐊑₃` ≔ Убеждение `ꆜ`, что проживание и работа владельца в Пенсильвании при наличии регистрации бизнеса в другом штате (CA) создают правовую неопределенность, где налоговые обязательства являются предметом выбора («determine whether»), а не безусловным фактом.

### 1.4. `D𐊑₄` (Иллюзия «Структурной простоты»)
`D𐊑₄` ≔ Убеждение `ꆜ`, что перенос юридической практики между штатами — это стандартная административная процедура, игнорирующая конфликт корпоративных форм: требование Калифорнии использовать *Professional Corporation* (PC) и специфику Пенсильвании (*Restricted Professional Company* — RPC).

## 2. Анализ `D𐊑₁`: Иллюзия «Операционного выхода»

### 2.1. Доводы за `Pⰳ(D𐊑₁)` (Почему `ꆜ` заблуждается)
В вопросе `Q2⁎` клиент формулирует задачу как «determine whether a business should stop filing... based on current operations». Это противоречит фундаментальному принципу **Franchise Tax** в Калифорнии.
Согласно **California Revenue and Taxation Code (R&TC) § 23153**, обязанность уплаты минимального налога ($800) привязана к **статусу регистрации**. Пока компания числится в реестре *Secretary of State* как активная, налог начисляется независимо от наличия деятельности или места проживания владельца. «Stop filing» без процедур *Dissolution* или *Surrender* ведет не к закрытию, а к статусу «Suspended» и накоплению долгов.

### 2.2. Доводы против `Pⰳ(D𐊑₁)` (Возможная правота `ꆜ`)
Если бы `ꆜ` вел бизнес как индивидуальный предприниматель (Sole Proprietor), его логика была бы верна: нет деятельности в штате — нет налога. Однако использование термина «business filing» и контекст корпоративного юриста подразумевают наличие зарегистрированного юрлица (Entity).

### 2.3. Оценка `Pⰳ(D𐊑₁)`
**95 / 100**. (Почти полная уверенность. Клиент пытается решить юридическую задачу административным бездействием).

## 3. Анализ `D𐊑₂`: Иллюзия «Тихого исправления»

### 3.1. Доводы за `Pⰳ(D𐊑₂)` (Почему `ꆜ` заблуждается)
В `Q3⁎` клиент ищет способ «avoid penalties» через «amending past tax returns». Это взаимоисключающие действия.
Подача просроченных деклараций в обычном порядке («Quiet Filing») автоматически влечет начисление штрафов за просрочку подачи и уплаты. Единственный легальный механизм списания штрафов в Пенсильвании — программа **Voluntary Disclosure Program (VDA)**.
Критическая ошибка `ꆜ`: подача уточненных деклараций *вне* рамок VDA дисквалифицирует налогоплательщика из программы амнистии. С 1 августа 2023 года PA VDA предлагает сокращенный период проверки (**3 года** look-back), что делает «тихое исправление» финансово невыгодным и опасным.

### 3.2. Доводы против `Pⰳ(D𐊑₂)`
Если сумма задолженности ничтожна, штрафы могут быть меньше стоимости услуг по сопровождению VDA. Но для Attorney-CPA риск профессиональной репутации и лицензии перевешивает экономию.

### 3.3. Оценка `Pⰳ(D𐊑₂)`
**90 / 100**. (Клиент выбирает инструмент, который гарантирует то, чего он хочет избежать — штрафы и внимание аудиторов).

## 4. Анализ `D𐊑₃`: Отрицание физического нексуса

### 4.1. Доводы за `Pⰳ(D𐊑₃)` (Почему `ꆜ` заблуждается)
В `Q1⁎` клиент противопоставляет проживание («lived in one state») регистрации («filing in another»), надеясь на отсутствие обязательств.
В штате Пенсильвания наличие удаленного сотрудника (тем более владельца, управляющего бизнесом из дома) создает безусловный **Physical Nexus** (связь). Согласно руководству PA Department of Revenue, это создает обязательства по *Corporate Net Income Tax* и регистрации иностранной компании. Это факт, не требующий «определения» («determine»).

### 4.2. Доводы против `Pⰳ(D𐊑₃)`
Нет. Для поставщика услуг, физически находящегося в штате, аргументов против Нексуса практически не существует.

### 4.3. Оценка `Pⰳ(D𐊑₃)`
**85 / 100**. (Клиент пытается найти лазейку в однозначной норме права).

## 5. Анализ `D𐊑₄`: Иллюзия «Структурной простоты»

### 5.1. Доводы за `Pⰳ(D𐊑₄)` (Почему `ꆜ` заблуждается)
Клиент запрашивает «structure questions», не упоминая конфликт профессиональных форм.
1.  **Калифорния:** Юристы обязаны использовать *Professional Corporation* (PC). LLC запрещены (Moscone-Knox Act).
2.  **Пенсильвания:** Юристы могут использовать *Restricted Professional Company* (RPC) или PC. Стандартная LLC для юристов недоступна.
Прямая конвертация CA PC → PA Standard LLC юридически невозможна или приведет к созданию нелегитимной структуры. Необходима сложная процедура конвертации в RPC.

### 5.2. Доводы против `Pⰳ(D𐊑₄)`
Возможно, клиент понимает это и именно поэтому ищет специалиста. Но формулировка задачи как общего «clean up» намекает на недооценку сложности.

### 5.3. Оценка `Pⰳ(D𐊑₄)`
**80 / 100**. (Высокая вероятность недооценки корпоративной специфики).

## 6. Вердикт

Клиент `ꆜ` находится в зоне высокого риска «профессиональной слепоты». Будучи экспертом в смежных областях, он экстраполирует бытовую логику на жестко регулируемые процедуры межштатового комплаенса.

Его текущий план действий, реконструируемый из вопросов, ведет к катастрофическим последствиям:
1.  **«Stop filing in CA»** (`D𐊑₁`) → Приведет к бесконечному накоплению долгов, статусу «Suspended» и невозможности легально закрыть юрлицо в будущем.
2.  **«Amend returns in PA»** (`D𐊑₂`) → Приведет к потере права на амнистию (VDA), штрафам и открытию периода проверки за все прошлые годы вместо льготных трех лет.

**Рекомендация для решения `᛭T`:** Стратегия должна строиться на категорическом отказе от интуитивных решений клиента. Единственный безопасный путь:
1.  **VDA в Пенсильвании** (анонимная подача до раскрытия личности).
2.  **Statutory Conversion (Domestication)** из CA PC в PA RPC (или PC).
3.  **Формальное закрытие (Dissolution)** в CA только после подтверждения переезда.

# 15. Анализ `D𐊑⠿` (выполнен Gemini Deep Research)
https://gemini.google.com/share/068d23f437a1


## **1. Введение: Архитектура риска в профессиональной деятельности**

Настоящий отчет представляет собой исчерпывающий анализ правового, налогового и процессуального ландшафта, в котором оперирует клиент ꆜ, обладающий двойной профессиональной квалификацией (Attorney-CPA). Задача данного документа — выполнить директиву ᛭T: выявить, категоризировать и подвергнуть критическому анализу заблуждения (D𐊑⠿), выявленные в ходе предварительной оценки ситуации клиента. Учитывая статус клиента как лицензированного специалиста в области права и бухгалтерского учета, к его действиям применяются повышенные стандарты осмотрительности, а ошибки в интерпретации законодательства несут не только финансовые, но и дисциплинарные риски.

Мульти-штатная практика, охватывающая Калифорнию (CA) и Пенсильванию (PA), представляет собой одну из наиболее агрессивных регуляторных комбинаций в США. Калифорния известна своим экспансивным определением «ведения бизнеса» и жестким администрированием франчайзингового налога, в то время как Пенсильвания обладает уникальным статутом о регистрации иностранных юридических лиц, который, в свете недавних решений Верховного суда США, создает беспрецедентные риски для общей юрисдикции. Дополнительный слой сложности вносит локальное налогообложение Филадельфии, претерпевающее радикальные изменения в 2025 году.

В отчете последовательно деконструируются заблуждения клиента относительно пассивного статуса в Калифорнии, последствий регистрации в Пенсильвании и процедур легализации налоговой истории. Анализ опирается на статутное право (R&TC, Title 15 Pa.C.S.), судебные прецеденты (*Swart*, *Jali*, *Mallory*) и административные регламенты, обеспечивая глубокое понимание механики рисков.

## ---

**2. Калифорнийский вектор: Деконструкция мифа о «пассивности» и процедурные ловушки выхода**

Одним из фундаментальных заблуждений клиента ꆜ является предположение, что минимизация физического присутствия или прекращение активных операций в Калифорнии автоматически освобождает его от обязательств по уплате франчайзингового налога. Данная позиция, вероятно, основана на неверной интерпретации прецедентного права, касающегося пассивных инвесторов, и игнорировании жестких административных процедур Налогового совета Калифорнии (Franchise Tax Board — FTB).

### **2.1. Доктрина «Ведения бизнеса» (Doing Business) и Экономический Нексус**

Согласно разделу 23101 Налогового кодекса Калифорнии (R&TC), определение «ведения бизнеса» выходит далеко за рамки физического наличия офиса или сотрудников. Законодатель закрепил широкие критерии, любой из которых достаточен для возникновения налоговых обязательств. Для Attorney-CPA, чья деятельность связана с оказанием высокостоимостных услуг, критическим фактором становится не физическое, а экономическое присутствие.

Калифорния применяет пороги «экономического нексуса» (Economic Nexus), которые ежегодно индексируются. Если профессиональная деятельность клиента генерирует выручку от источников в Калифорнии, превышающую установленные лимиты, он считается «ведущим бизнес» в штате де-юре, даже если физически находится в Пенсильвании.

| Налоговый год | Порог продаж (Sales Threshold) | Порог имущества/зарплат | Обоснование |
| :---- | :---- | :---- | :---- |
| **2023** | $711,538 | $71,154 | 1 |
| **2024** | $735,019 | $73,502 | 1 |
| **2025** | $757,070 | $75,707 | 1 |

**Анализ заблуждения:** Клиент может полагать, что отсутствие офиса в Калифорнии защищает его. Однако, согласно R&TC 23101(b), компания считается ведущей бизнес, если она «активно участвует в любой транзакции с целью финансовой выгоды» в штате.1 Для юриста или CPA даже единичная консультация клиента из Калифорнии или наличие лицензии, используемой для представления интересов в судах CA, может трактоваться как активная транзакция. Более того, превышение порога продаж (например, $735,019 в 2024 году) или наличие 25% от общих продаж в Калифорнии автоматически создает обязательство по подаче декларации и уплате налога.1

### **2.2. Прецеденты *Swart* и *Jali*: Опасная иллюзия защиты**

Центральным элементом защиты, на который часто ссылаются налогоплательщики, пытающиеся избежать минимального налога в $800, является решение Апелляционного суда по делу *Swart Enterprises, Inc. v. Franchise Tax Board* (2017). Клиент ꆜ может ошибочно полагать, что его ситуация аналогична данному кейсу.

В деле *Swart* суд постановил, что иностранная корпорация, владеющая миноритарной долей (0.2%) в калифорнийской LLC, управляемой менеджером (manager-managed), не считается «ведущей бизнес» в штате только на основании этого владения.2 Суд провел аналогию с пассивным партнером с ограниченной ответственностью (limited partner), у которого нет прав на управление и контроль.4

Однако, последующая практика, в частности решение Офиса налоговых апелляций (OTA) по делу *Jali LLC* (2019), существенно сузила и уточнила применение *Swart*. В деле *Jali* было установлено, что процент владения не является единственным критерием. Ключевым фактором является наличие **права управления**.3

**Применение к Attorney-CPA (ꆜ):**

1. **Фактор контроля:** Профессиональные компании (Professional Corporations) или LLC, созданные для практики юриста или бухгалтера, по своей природе управляются самим профессионалом. Даже если структура формально является Manager-Managed, если ꆜ выступает в роли менеджера или имеет право участвовать в управлении, защита *Swart* полностью аннулируется. OTA в деле *Jali* подтвердило, что требуется «фактоемкий анализ» (fact-intensive inquiry), и наличие управленческих полномочий неизбежно приводит к признанию деятельности активной.3  
2. **Активный характер услуг:** В отличие от пассивного инвестирования в оборудование (как в *Swart*), юридическая и бухгалтерская практика требует активного личного участия. Доход генерируется не от пассивного владения капиталом, а от оказания услуг. Следовательно, концепция пассивного инвестора здесь неприменима фундаментально.

Таким образом, опора на *Swart* для Attorney-CPA является стратегической ошибкой с высокой вероятностью опротестования со стороны FTB.

### **2.3. «Зомби-компании»: Риски незавершенной ликвидации**

Третье заблуждение в калифорнийском векторе касается процедуры выхода из юрисдикции. Клиент может считать, что прекращение подачи деклараций («stop filing») или простая отправка финальной декларации достаточны для закрытия обязательств. Это одно из самых распространенных и дорогостоящих заблуждений.

Калифорнийская система требует синхронных действий двух ведомств: Секретаря штата (SOS) и Налогового совета (FTB). Пока юридическое лицо официально не ликвидировано (Dissolved/Surrendered/Cancelled) в реестре SOS, оно продолжает накапливать обязательства по минимальному налогу ($800 в год), даже если деятельность не ведется.6

**Механика процесса и точки отказа:**

1. **Финальная декларация:** Необходимо подать декларацию (Form 100/100S/568) за текущий год, отметив поле «Final Return». Однако одного этого действия недостаточно.6  
2. **Временное окно 12 месяцев:** После подачи финальной декларации у налогоплательщика есть ровно 12 месяцев для подачи документов о ликвидации (Form DISS, SURR или CAN) в SOS.6 Пропуск этого срока аннулирует статус «финальной» декларации, и налог начинает начисляться снова.  
3. **Статус Good Standing:** Критически важно, что компания не может быть ликвидирована, если она находится в статусе *Suspended* (Приостановлена) или *Forfeited* (Аннулирована) за неуплату налогов или неподачу отчетов.9 Если клиент ꆜ просто перестал подавать отчеты в прошлом, его компания, вероятно, уже *Suspended*. Для ликвидации ему сначала придется пройти процедуру *Revivor* (Возрождение): подать все пропущенные декларации, уплатить все налоги, пени и проценты, и только после восстановления статуса подать на ликвидацию.6

Игнорирование этой процедуры приводит к созданию «зомби-компании», которая продолжает генерировать задолженность перед штатом, персональную ответственность за которую в определенных случаях могут попытаться переложить на владельцев-операторов, особенно в профессиональных структурах.

## ---

**3. Пенсильванский вектор: Конституционные риски и профессиональная специфика**

Перемещение или расширение деятельности в Пенсильванию открывает для клиента ꆜ совершенно иной спектр правовых угроз. Если в Калифорнии риски преимущественно фискальные, то в Пенсильвании они носят экзистенциальный процессуальный характер из-за уникальной трактовки юрисдикции над иностранными компаниями.

### **3.1. Феномен *Mallory*: Регистрация как согласие на «ядерную» подсудность**

Самым критическим и наименее очевидным риском для клиента является регистрация иностранной компании (Foreign Registration) в Пенсильвании. В 2023 году Верховный суд США в деле *Mallory v. Norfolk Southern Railway Co.* подтвердил конституционность статута Пенсильвании (42 Pa. Cons. Stat. § 5301), который устанавливает, что регистрация иностранной корпорации для ведения бизнеса в штате означает **автоматическое согласие на общую персональную юрисдикцию (general personal jurisdiction)** судов Пенсильвании.10

Суть проблемы:  
В большинстве штатов (согласно прецеденту Daimler AG v. Bauman) компания может быть судима по любым вопросам (общая юрисдикция) только там, где она «дома» (at home) — то есть в месте инкорпорации или основного места ведения бизнеса. Пенсильвания является исключением. Простая подача формы регистрации (Foreign Registration Statement) юридически приравнивается к добровольному согласию отвечать по любым искам в судах PA, независимо от того, где произошел инцидент.10  
Сценарий риска для Attorney-CPA:  
Предположим, клиент ꆜ регистрирует свою калифорнийскую Professional Corporation в Пенсильвании как иностранную компанию. Впоследствии бывший клиент из Калифорнии подает иск о профессиональной халатности (malpractice). Благодаря прецеденту Mallory, истец может подать этот иск в суд Пенсильвании (известный своими про-истцовыми жюри, особенно в Филадельфии), и ꆜ не сможет ходатайствовать о прекращении дела из-за отсутствия юрисдикции. Регистрация в PA сама по себе создала эту юрисдикцию.12  
Это превращает Пенсильванию в глобальный форум для исков против зарегистрированных компаний, создавая феномен «судебного туризма» (litigation tourism).11 Для профессионала, чья ответственность часто носит личный характер, это колоссальный риск.

### **3.2. Статус «Ограниченной Профессиональной Компании» (RPC)**

Вторым слоем сложности в Пенсильвании является корпоративная классификация. Клиент ꆜ не может оперировать как стандартная LLC или Корпорация из-за своей профессиональной лицензии. Законодательство Пенсильвании (Title 15, Chapter 89, Subchapter L) предусматривает специальную форму: **Restricted Professional Company (RPC)**.14

**Императивные требования:**

1. **Ограничение деятельности:** RPC может предоставлять только специфические виды услуг. Для Attorney-CPA это юридические услуги (law) и услуги публичного бухгалтерского учета (public accounting). Смешивание их с коммерческой деятельностью (например, продажей товаров) запрещено.15  
2. **Квалификация участников:** Все участники (members) RPC должны быть лицензированными специалистами. Это критично при структурировании владения.15  
3. **Ежегодная перерегистрация (Annual Registration):** В отличие от стандартных компаний, RPC обязаны ежегодно подавать *Certificate of Annual Registration* (Form DSCB:15-8998) до 15 апреля.  
4. **Финансовая нагрузка:** Сбор за ежегодную регистрацию рассчитывается как базовые $300, умноженные на количество лицензированных участников.15 Для соло-практика это минимум $300 ежегодно сверх обычных налогов.

**Риск заблуждения:** Если клиент подаст стандартную форму регистрации иностранной LLC (Form DSCB:15-412) и не отметит статус «Restricted Professional Limited Liability Company» в пункте 8, это будет считаться дефектом регистрации.17 Такой дефект может привести к тому, что его деятельность будет признана неавторизованной, а корпоративная вуаль (corporate veil) может быть легко пробита в суде, так как сущность не соответствует требованиям профессионального регулирования.

### **3.3. Реформа отчетности 2025 года: Введение Annual Report**

С 2025 года Пенсильвания переходит на новую систему корпоративной отчетности, отменяя архаичную систему «Decennial Report» (отчет раз в 10 лет) и вводя обязательный **Ежегодный отчет (Annual Report)** для всех зарегистрированных ассоциаций.18

**Параметры нового требования:**

* **Начало действия:** 1 января 2025 года.  
* **Сроки подачи:** Для корпораций — до 30 июня; для LLC — до 30 сентября; для остальных форм — до 31 декабря.19  
* **Последствия:** Неподача отчета приведет к административному роспуску (administrative dissolution) или прекращению регистрации иностранного лица.

Для клиента ꆜ, привыкшего к старым правилам PA (где ежегодная отчетность отсутствовала для большинства форм, кроме RPC), это нововведение требует пересмотра календаря комплаенса.

## ---

**4. Филадельфия: Агрессивный локальный налоговый режим**

На уровне города Филадельфия клиент сталкивается с одним из самых сложных локальных налоговых режимов в стране — Business Income and Receipts Tax (BIRT). Заблуждения относительно локализации дохода и исключений здесь могут привести к мгновенным штрафам.

### **4.1. Нексус удаленного работника (Post-Covid Nexus)**

В период пандемии Филадельфия временно ослабляла требования к нексусу для удаленных работников. Однако с 1 июля 2021 года город вернулся к жестким стандартам. Согласно официальной позиции Департамента доходов Филадельфии, наличие хотя бы одного сотрудника (включая владельца бизнеса), работающего из дома в черте города, создает достаточный нексус для обложения налогом BIRT всего бизнеса.20

Если клиент ꆜ проживает в Филадельфии и работает из дома (даже частично), он подпадает под действие BIRT. Аргумент о том, что «клиенты находятся в Калифорнии», не освобождает от налога на чистую прибыль (Net Income portion), хотя может помочь при аллокации валовой выручки (Gross Receipts portion).21

### **4.2. Критическое изменение 2025 года: Отмена исключения $100,000**

До налогового года 2024 включительно в Филадельфии действовало правило, освобождающее бизнесы с валовой выручкой менее $100,000 от подачи декларации и уплаты BIRT. Это служило «зонтиком» для многих мелких практиков и фрилансеров.

Однако, согласно Законопроекту № 250199 (Bill No. 250199), подписанному в июне 2025 года, **данное исключение отменяется начиная с налогового года 2025** (декларации, подаваемые в апреле 2026 года).23

Последствия для ꆜ:  
Начиная с 2025 года, каждый доллар выручки становится объектом отчетности. Если клиент планировал стратегию, опираясь на низкие обороты в PA для избежания локальных налогов, эта стратегия более нежизнеспособна. Одновременно с этим происходит снижение ставок (Net Income rate снижается до 5.71%, Gross Receipts rate до 1.410 mills), но расширение базы за счет отмены порога $100k является более существенным фактором для малого бизнеса.23

## ---

**5. Стратегия легализации: VDP против Amended Returns**

Столкнувшись с необходимостью урегулировать прошлые обязательства (если они есть), клиент ꆜ может рассматривать вариант «тихого» исправления через подачу уточненных деклараций (Amended Returns). Анализ показывает, что для профессионала с лицензией это крайне рискованный путь.

### **5.1. Анализ рисков подачи Amended Returns**

Департамент доходов Пенсильвании (PA DOR) четко указывает, что подача уточненной декларации или первичной декларации за прошлые периоды (late original return) не является защищенным механизмом.26

1. **Неограниченный период проверки:** Подача декларации за, например, 2018 год открывает этот год для полного аудита. Если налоговый орган обнаружит системные нарушения, он может инициировать проверку всех предыдущих лет без ограничений сроков давности (так как декларации не были поданы вовремя).  
2. **Полные штрафы:** При обычной подаче просроченных деклараций автоматически начисляются штрафы за неподачу (failure to file) и неуплату (failure to pay), которые могут достигать 25-50% от суммы налога, плюс проценты.  
3. **Репутационный риск:** Для Attorney-CPA наличие налоговых взысканий может стать предметом интереса лицензирующих органов.

### **5.2. Преимущества Программы добровольного раскрытия (VDP)**

Программа добровольного раскрытия (Voluntary Disclosure Program), предлагаемая PA DOR, является наиболее рациональным путем для легализации.27

**Ключевые параметры VDP в Пенсильвании:**

| Параметр | Условия VDP | Условия при Amended Return |
| :---- | :---- | :---- |
| **Период проверки (Lookback Period)** | Ограничен: 3 года + текущий год | Неограничен (все годы деятельности) |
| **Штрафы (Penalties)** | Полностью списываются (Waived) | Начисляются в полном объеме |
| **Проценты (Interest)** | Подлежат уплате | Подлежат уплате |
| **Анонимность** | Возможно анонимное обращение через представителя | Невозможна |
| **Условие участия** | Налогоплательщик не должен быть зарегистрирован или находиться под следствием | N/A |

**Рекомендация:** Для клиента ꆜ критически важно подать заявку на VDP *до* любой регистрации в штате. Как только он подаст форму регистрации иностранной компании (Foreign Registration Statement), он потеряет право на участие в VDP, так как станет «зарегистрированным налогоплательщиком».27 Это создает узкое процедурное окно: сначала VDP (для очистки прошлого), затем — официальная регистрация (для будущего).

## ---

**6. Таблица оценки заблуждений (D𐊑⠿)**

На основе проведенного анализа, ниже представлена сводная оценка выявленных заблуждений клиента.

| Заблуждение (Hypothesis) | Оценка Правдоподобности | Правовая реальность и последствия |
| :---- | :---- | :---- |
| **"Мое владение в CA пассивное (Swart), налог $800 платить не нужно"** | **Критически низкая (Опасно)** | Статус Attorney-CPA подразумевает управление. Дело *Jali* 3 подтверждает, что при наличии прав управления защита *Swart* не работает. Налог обязателен. |
| **"Я просто перестану подавать отчеты в CA, и компания закроется сама"** | **Нулевая** | FTB продолжит начислять налоги. Компания перейдет в статус *Suspended*, что блокирует легальную ликвидацию.9 Требуется формальный *Dissolution*. |
| **"Регистрация в PA — это формальность, не влияющая на суды"** | **Критически низкая** | Решение *Mallory* 10 делает регистрацию в PA согласием на общую юрисдикцию. Это открывает клиента для исков со всей страны в судах PA. |
| **"Я могу использовать обычную LLC для своей практики в PA"** | **Низкая** | Профессиональная этика и закон требуют использования *Restricted Professional Company* (RPC).14 Обычная LLC может быть признана нелегитимной для практики права. |
| **"Филадельфия не увидит меня, пока у меня меньше $100k выручки"** | **Устаревшая (Нулевая с 2025)** | Исключение $100k отменяется с 2025 года.23 Нексус возникает от работы из дома. Риск локальных штрафов высок. |
| **"Лучше тихо подать уточненки, чем связываться с бюрократией VDP"** | **Ошибочная** | VDP гарантирует списание штрафов и ограничение периода 3 годами. Уточненки открывают все прошлые годы для аудита и штрафов.27 |

## ---

**7. Синтез и стратегические рекомендации**

Ситуация клиента ꆜ характеризуется высоким уровнем риска, обусловленного сочетанием агрессивных налоговых юрисдикций и спецификой профессиональной деятельности. Статус Attorney-CPA не является защитным щитом; напротив, он служит отягчающим обстоятельством, так как предполагает знание закона и не позволяет ссылаться на неосведомленность.

### **7.1. Коррекция калифорнийского статуса**

Необходимо немедленно провести аудит статуса калифорнийской сущности. Если она находится в статусе *Suspended*, первоочередной задачей является процедура *Revivor* с полной уплатой задолженности. Попытка просто бросить компанию приведет к накоплению персональной ответственности. После восстановления необходимо синхронно подать финальную декларацию в FTB и документы о ликвидации в SOS.

### **7.2. Структурирование в Пенсильвании**

В свете решения *Mallory*, клиенту следует рассмотреть целесообразность регистрации калифорнийской компании как иностранной в PA. Альтернативной стратегией может быть создание новой, независимой сущности (Domestic RPC) в Пенсильвании для ведения местной практики, сохраняя калифорнийскую сущность изолированной (если деятельность в CA продолжается). Это может помочь минимизировать риски общей юрисдикции для калифорнийских активов, хотя и не устранит их полностью без тщательного корпоративного планирования.

В любом случае, сущность в PA должна быть зарегистрирована как **Restricted Professional Company**, с соблюдением требований по ежегодной перерегистрации (Annual Registration) и новому отчету (Annual Report) с 2025 года.

### **7.3. Управление филадельфийским риском**

Клиент должен подготовиться к полному налогообложению в Филадельфии с 2025 года. Необходимо настроить учет для четкого разделения валовой выручки (Gross Receipts) по источникам, чтобы минимизировать налоговую базу, но налог на чистую прибыль (Net Income) будет неизбежен при работе из дома.

### **7.4. Финальный алгоритм действий**

1. **Подать заявку на VDP в PA** (анонимно) для урегулирования любых прошлых активностей до момента официальной регистрации.  
2. **Зарегистрировать RPC в PA** (или Domestic, или Foreign, с учетом рисков *Mallory*), указав правильный профессиональный статус.  
3. **Инициировать формальный Dissolution в CA**, предварительно погасив все долги и восстановив статус, если он был утрачен.  
4. **Настроить календарь комплаенса** с учетом новых требований 2025 года (PA Annual Report, Philadelphia BIRT без льгот).

Данный подход переводит клиента из зоны высокой неопределенности и риска в поле контролируемого правового и налогового администрирования.

#### **Works cited**

1. Doing business in California | FTB.ca.gov, accessed December 7, 2025, [https://www.ftb.ca.gov/file/business/doing-business-in-california.html](https://www.ftb.ca.gov/file/business/doing-business-in-california.html)  
2. Swart Enterprises v. Franchise Tax Bd. - Justia Law, accessed December 7, 2025, [https://law.justia.com/cases/california/court-of-appeal/2017/f070922.html](https://law.justia.com/cases/california/court-of-appeal/2017/f070922.html)  
3. California OTA Rules That Member with 50-Percent Interest in a California LLC is "Doing Business" in California - BDO USA, accessed December 7, 2025, [https://www.bdo.com/insights/tax/california-ota-rules-that-member-with-50-percent-interest-in-a-california-llc-is-doing-business-in](https://www.bdo.com/insights/tax/california-ota-rules-that-member-with-50-percent-interest-in-a-california-llc-is-doing-business-in)  
4. Small Iowa corporation successfully challenges California's $800 franchise tax, accessed December 7, 2025, [https://www.thetaxadviser.com/issues/2017/aug/iowa-corporation-successfully-challenges-franchise-tax/](https://www.thetaxadviser.com/issues/2017/aug/iowa-corporation-successfully-challenges-franchise-tax/)  
5. Deciphering California's Tangled Nexus Standards | Alston & Bird, accessed December 7, 2025, [https://www.alston.com/ja/insights/publications/2020/05/deciphering-ca-tangled-nexus-standards](https://www.alston.com/ja/insights/publications/2020/05/deciphering-ca-tangled-nexus-standards)  
6. Business entities | FTB.ca.gov, accessed December 7, 2025, [https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/march-2022/business-entities.html](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/march-2022/business-entities.html)  
7. Corporations | FTB.ca.gov, accessed December 7, 2025, [https://www.ftb.ca.gov/file/business/types/corporations/index.html](https://www.ftb.ca.gov/file/business/types/corporations/index.html)  
8. California Revenue and Taxation Code § 23153 (2024) - Justia Law, accessed December 7, 2025, [https://law.justia.com/codes/california/code-rtc/division-2/part-11/chapter-2/article-2/section-23153/](https://law.justia.com/codes/california/code-rtc/division-2/part-11/chapter-2/article-2/section-23153/)  
9. Closing a California Business Entity | FTB.ca.gov, accessed December 7, 2025, [https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/june-2021/closing-a-ca-business-entity.html](https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/june-2021/closing-a-ca-business-entity.html)  
10. Mallory v. Norfolk Southern Railway Co. | 600 U.S. ___ (2023), accessed December 7, 2025, [https://supreme.justia.com/cases/federal/us/600/21-1168/](https://supreme.justia.com/cases/federal/us/600/21-1168/)  
11. Mallory v. Norfolk Southern Railway Co.: A New 'Third Rail' for Litigation Tourism or a Short-Lived Detour from the At Home Rule? - Greenberg Traurig, LLP, accessed December 7, 2025, [https://www.gtlaw.com/en/insights/2023/6/mallory-v-norfolk-southern-railway-co-a-new-third-rail-for-litigation-tourism-or-a-short-lived-detour-from-the-at-home-rule](https://www.gtlaw.com/en/insights/2023/6/mallory-v-norfolk-southern-railway-co-a-new-third-rail-for-litigation-tourism-or-a-short-lived-detour-from-the-at-home-rule)  
12. Mallory v. Norfolk Southern Railway Co. - Harvard Law Review, accessed December 7, 2025, [https://harvardlawreview.org/print/vol-137/mallory-v-norfolk-southern-railway-co/](https://harvardlawreview.org/print/vol-137/mallory-v-norfolk-southern-railway-co/)  
13. US Supreme Court Holds Business Registration Subjects Out-of-State Companies to General Personal Jurisdiction - K&L Gates, accessed December 7, 2025, [https://www.klgates.com/US-Supreme-Court-Holds-Business-Registration-Subjects-Out-of-State-Companies-to-General-Personal-Jurisdiction-6-30-2023](https://www.klgates.com/US-Supreme-Court-Holds-Business-Registration-Subjects-Out-of-State-Companies-to-General-Personal-Jurisdiction-6-30-2023)  
14. Pennsylvania Limited Liability Company | Department of State, accessed December 7, 2025, [https://www.pa.gov/agencies/dos/programs/business/types-of-filings-and-registrations/pennsylvania-limited-liability-company](https://www.pa.gov/agencies/dos/programs/business/types-of-filings-and-registrations/pennsylvania-limited-liability-company)  
15. Chapter 89. - Title 15 - CORPORATIONS AND UNINCORPORATED ASSOCIATIONS - PA General Assembly, accessed December 7, 2025, [https://www.palegis.us/statutes/consolidated/view-statute?iFrame=true&txtType=HTM&ttl=15&div=0&chpt=89](https://www.palegis.us/statutes/consolidated/view-statute?iFrame=true&txtType=HTM&ttl=15&div=0&chpt=89)  
16. Pennsylvania Statutes Title 15 Pa.CSA Corporations and Unincorporated Associations § 8998. Annual registration - Codes - FindLaw, accessed December 7, 2025, [https://codes.findlaw.com/pa/title-15-pacsa-corporations-and-unincorporated-associations/pa-csa-sect-15-8998/](https://codes.findlaw.com/pa/title-15-pacsa-corporations-and-unincorporated-associations/pa-csa-sect-15-8998/)  
17. 15 412 Foreign Registration Statement - PENNSYLVANIA DEPARTMENT OF STATE BUREAU OF CORPORATIONS AND CHARITABLE ORGANIZATIONS, accessed December 7, 2025, [https://www.pa.gov/content/dam/copapwp-pagov/en/dos/programs/business/forms/offsite-forms/15-412-Foreign-Registration-Statement.pdf](https://www.pa.gov/content/dam/copapwp-pagov/en/dos/programs/business/forms/offsite-forms/15-412-Foreign-Registration-Statement.pdf)  
18. Annual Reports | Department of State - Commonwealth of Pennsylvania, accessed December 7, 2025, [https://www.pa.gov/agencies/dos/programs/business/types-of-filings-and-registrations/annual-reports](https://www.pa.gov/agencies/dos/programs/business/types-of-filings-and-registrations/annual-reports)  
19. 2025 Pennsylvania Business Filing Requirements - Holsinger, accessed December 7, 2025, [https://www.holsinger.cpa/articles-events/2025-pennsylvania-business-filing-requirements](https://www.holsinger.cpa/articles-events/2025-pennsylvania-business-filing-requirements)  
20. Frequently Asked Questions Regarding the Expiration of Philadelphia's Temporary Nexus Waiver, accessed December 7, 2025, [https://www.phila.gov/media/20220210082003/FAQs-regarding-the-expiration-of-the-temporary-nexus-waiver-Feb-22.pdf](https://www.phila.gov/media/20220210082003/FAQs-regarding-the-expiration-of-the-temporary-nexus-waiver-Feb-22.pdf)  
21. Pennsylvania and Philadelphia Tax Updates: Considerations for Post-COVID Remote Work | Alerts and Articles | Insights | Ballard Spahr, accessed December 7, 2025, [https://www.ballardspahr.com/insights/alerts-and-articles/2021/06/pennsylvania-and-philadelphia-tax-updates-considerations-for-post-covid-remote-work](https://www.ballardspahr.com/insights/alerts-and-articles/2021/06/pennsylvania-and-philadelphia-tax-updates-considerations-for-post-covid-remote-work)  
22. Philadelphia provides guidance concerning the expiration of temporary nexus relief for telework during the COVID-19 emergency - EY Tax News, accessed December 7, 2025, [https://taxnews.ey.com/news/2022-0343-philadelphia-provides-guidance-concerning-the-expiration-of-temporary-nexus-relief-for-telework-during-the-covid-19-emergency](https://taxnews.ey.com/news/2022-0343-philadelphia-provides-guidance-concerning-the-expiration-of-temporary-nexus-relief-for-telework-during-the-covid-19-emergency)  
23. PHILADELPHIA BUSINESS TAXES ARE CHANGING, accessed December 7, 2025, [https://www.phila.gov/media/20251204091248/Tax-changes-information-tax-year-2025.pdf](https://www.phila.gov/media/20251204091248/Tax-changes-information-tax-year-2025.pdf)  
24. Philadelphia Lowers BIRT Rates & Ends $100K Exclusion in New City Ordinance, accessed December 7, 2025, [https://www.salestaxinstitute.com/resources/philadelphia-birt-rate-reduction-eliminates-100k-exclusion](https://www.salestaxinstitute.com/resources/philadelphia-birt-rate-reduction-eliminates-100k-exclusion)  
25. 2025 Philadelphia Tax Rate Changes - Alloy Silverstein, accessed December 7, 2025, [https://alloysilverstein.com/philadelphia-tax-changes-birt-2025/](https://alloysilverstein.com/philadelphia-tax-changes-birt-2025/)  
26. Guidance on Original and Amended Returns | Department of Revenue | Commonwealth of Pennsylvania, accessed December 7, 2025, [https://www.pa.gov/agencies/revenue/get-assistance/tax-appeals/guidance-on-original-and-amended-returns](https://www.pa.gov/agencies/revenue/get-assistance/tax-appeals/guidance-on-original-and-amended-returns)  
27. Apply for the Voluntary Disclosure Program - Commonwealth of Pennsylvania, accessed December 7, 2025, [https://www.pa.gov/services/revenue/apply-for-the-voluntary-disclosure-program](https://www.pa.gov/services/revenue/apply-for-the-voluntary-disclosure-program)  
28. State voluntary disclosure programs: A practice guide - The Tax Adviser, accessed December 7, 2025, [https://www.thetaxadviser.com/issues/2024/dec/state-voluntary-disclosure-programs-a-practice-guide/](https://www.thetaxadviser.com/issues/2024/dec/state-voluntary-disclosure-programs-a-practice-guide/)