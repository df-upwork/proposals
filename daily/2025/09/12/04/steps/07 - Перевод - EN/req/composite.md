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
߷⠿ ≔ ⠿~ (приложеные к этому запросу файлы)
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
Сегодня 2025-09-12.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021966379507218738106

## 2.2. Title
US customs broker with experience in Foreign Importer of Record

## 2.3. Description
`PD` ≔ 
```text
I am looking for a US customs broker with experience in Foreign Importer of Record.

I currently have a DHL express shipment waiting for customs clearance China to US (LA)

They are requesting information to clear the shipment, however I would prefer my UK company to remain the Foreign Importer of Record. The UK company does not have an EIN or presence in US - so looking for someone who specialises in this.
```

## 2.4. Tags
International Taxation
Logistics Management
Business Services

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United Kingdom
Salisbury

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
Individual client

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
 Sep 29, 2022
### 5.3.2. Hire rate (%)
100
### 5.3.3. Количество опубликованных проектов (jobs posted)
21
### 5.3.4. Total spent (USD)
$14K
### 5.3.5. Количество оплаченных часов в почасовых проектах
265
### 5.3.6. Средняя почасовая ставка (USD)
$37.47

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

## 6.1.1. URL
https://www.upwork.com/jobs/~021964256140211896525

## 6.1.2. Title
Connect Orbe Geo redirect app to shopify plus store

## 6.1.3. Description
`P1D` ≔ 
```text
I have shopify plus with Multi expansion stores for different countries.

I need someone to connect Orbe geo location app to my expansion stores so when a customer comes onto the main store the are redirected to the correct countries shopify store.

I am open to using another Geo location app if you think another is better.

Need this done immediately today
```

## 6.1.4. Publication Date
6 days ago

## 6.1.5. Payment Terms
### 6.1.5.1. Expected by `ꆜ`  
Not specified
### 6.1.5.2. Actual
10 hrs @ $25.00/hr
Billed: $197.77

## 6.1.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.1.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

## 6.1.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.2. `P2⁎`

## 6.2.1. URL
https://www.upwork.com/jobs/~021949010188391384864

## 6.2.3. Title
USA company formation for foreign individual

## 6.2.3. Description
`P2D` ≔ 
```text
I am looking to register a business in Delaware as a foreign individual (UK) - I would then like to register in NJ as a foreign business.

I will be opening and operating a small fulfilment centre for my established fashion ecommerce brand within NJ

Ideally the candidate can offer a full service of company formation, banking set up, ongoing legal and accounting advice as I am a foreign individual.
```

## 6.2.4. Publication Date
2 months ago

## 6.2.5. Payment Terms
### 6.2.5.1. Expected by `ꆜ`  
Not specified
### 6.2.5.2. Actual
18 hrs @ $60.00/hr
Billed: $1,189.53

## 6.2.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.2.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
6+ months

## 6.2.8. Contractor Location (expected by `ꆜ`)
United States

## 6.3. `P3⁎`

## 6.3.1. URL
https://www.upwork.com/jobs/~0192fac9785d6e2c21

## 6.3.2. Title
Logistics and Shipping Specialist

## 6.3.3. Description
`P3D` ≔ 
```text
Logistics and Shipping Specialist


I own a factory in Lviv Ukraine manufacturing women’s dresses. 
I am looking for someone to assist on a regular basis with logistics and shipping. 
I currently have a fully functioning factory manufacturing 70 - 100 dresses per week and we are growing rapidly, we expect to double this by spring next year.

I have a business consultancy who provide all legal and accountancy advice, however I am looking for someone with experience in Logistics and shipping / imports and exports to help navigate this complex area. I already have relationships with my suppliers, who supply my UK production, however I need this supply to now come into Ukraine for Production

Main duties:

Finding the most cost efficient shipping services to export goods in smaller shipments of approx 50 dresses at a time , shipments may be larger in the future, however we are currently working on gaining preferential origin for the goods produced and receiving EUR1. The exports must be official and generate the correct paper work, such as bill of lading / air waybill needed for accounting. Shipments will need to be made on a regular basis - weekly. This is the first stage of our exports, shipping goods to my UK warehouse.

For the long term we will look to ship individual dresses direct to customers from Ukraine. Options are direct shipping or consolidation. - I have a company in mind for this in Ukraine who consolidate shipments to UK, USA and Europe (Our sales are 85% to USA, 5% to UK , 5% to Europe, 5% to Australia). I need to understand if they can generate the correct paperwork as needed by accounts to verify the export.

Assisting with imports from Turkey and China. Currently we have shipments from Turkey set up, however I am still looking at ways to ship from China cost efficiently. I am looking for companies with consolidation from Guangzhou to Ukraine - I do have a contact for this, however need a Ukrainian speaker to communicate with.

Generally being an intermediary for myself (English speaking only) and a customs agent / broker and shipper. Also advising on and assisting with the complex nature of the Ukrainian legislation in terms of exports and imports.


In summary I am looking for an experienced logistician who can implement a smooth and reliable supply chain of import and exports, whilst helping to educate me as to the complexities of the Ukrainian legislations around importing and exporting.

This is a long term ongoing project.
```

## 6.3.4. Publication Date
2 years ago

## 6.3.5. Payment Terms
### 6.3.5.1. Expected by `ꆜ`  
Not specified
### 6.3.5.2. Actual
165 hrs @ $40.00/hr
Billed: $6,944.71

## 6.3.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.3.7. Duration (expected by `ꆜ`)
6+ months

## 6.3.8. Contractor Location (expected by `ꆜ`)
Ukraine

## 6.4. `P4⁎`

## 6.4.1. URL
https://www.upwork.com/jobs/~014f25fe03a1d142df

## 6.4.2. Title
HS code to qualify for 0% duty

## 6.4.3. Description
`P4D` ≔ 
```text
I am looking for someone to assist with determining the HS code and preferential origin status of an import from Ukraine to UK of women's dresses - synthetic fibres. I am looking at obtaining pref origin to receive 0% duty.


The goods to be imported, i believe should be under the HS code womens dress - synthetic fibres  but then will not qualify for pref origin, unless they can be proved as made up of maximum 40% non originating materials. I do not have the EUR1's for the originating fabrics, so am finding it hard to prove this.

I am looking to find a way to prove origin for preferential 0% duty or finding a HS code that could be used
```

## 6.4.4. Publication Date
2 years ago

## 6.4.5. Payment Terms
### 6.4.5.1. Expected by `ꆜ`  
Not specified
### 6.4.5.2. Actual
4 hrs @ $28.00/hr
Billed: $125.45

## 6.4.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.4.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

## 6.4.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.5. `P5⁎`

## 6.5.1. URL
https://www.upwork.com/jobs/~01e98b3c99b5195e4f

## 6.5.2. Title
HS code clarification and pref origin advice Ukraine to UK

## 6.5.3. Description
`P5D` ≔ 
```text
I am looking for someone to assist with determining the HS code and preferential origin status of an import from Ukraine of women's dresses - synthetic fibres. I am looking at obtaining pref origin to receive 0% duty.

The goods to be imported, i believe should be under the HS code womens dress - synthetic fibres  but then will not qualify for pref origin, unless they can be proved as made up of maximum 40% non originating materials. I do not have the EUR1's for the originating fabrics, so am finding it hard to prove this.

When I look on .gov online tariff support - the ruling states that the if the product is 'Women's, girls' and babies' clothing and clothing accessories for babies, embroidered' (embroidered being a separate classification, but not a separate HS code)- the requirement becomes 'Manufacture from unembroidered fabric, provided that the value of the unembroidered fabric used does not exceed 40% of the ex-works price of the product.'

I am looking for clarification on the classification of the 'embroidered' part of this section as there does not seem to be a specific HS code that defines womens dress  - synthetic fibres  as embroidered.

The dresses are made of fabrics which are then embroidered in Ukraine as part of the processing into dresses, so does this qualify, if so how is it proven?

In summary I am trying to make sense of how to import these goods as 0% duty, if at all possible
```

## 6.5.4. Publication Date
2 years ago

## 6.5.5. Payment Terms
### 6.5.5.1. Expected by `ꆜ`  
Not specified
### 6.5.5.2. Actual
Fixed-price $120.00

## 6.5.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.5.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

## 6.5.8. Contractor Location (expected by `ꆜ`)
Not specified

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`, `P4⁎`, `P5⁎`}

## 7.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 7.3.
`Pi` : `Ps`

# 8.
`P†⠿` ≔⠿~
```
Проблемы `ꆜ` в `PD`:
~~~markdown
# 1. Операционный кризис: Задержка груза на таможне
Непосредственная и критическая проблема заключается в том, что экспресс-отправление DHL из Китая в США (Лос-Анджелес) остановлено и «ожидает таможенного оформления» (`waiting for customs clearance`).

# 2. Процедурное препятствие: Невозможность предоставить информацию
Таможенные органы или DHL запрашивают информацию для очистки груза (`requesting information to clear the shipment`), которую клиент не может предоставить в требуемом формате.

# 3. Стратегическая цель: Сохранение статуса Иностранного Импортёра Записи (FIOR)
Клиент намерен использовать свою британскую компанию (`UK company`) в качестве официального импортёра (Importer of Record, IOR). В данном случае это статус Foreign Importer of Record (FIOR).

# 4. Воспринимаемый регуляторный барьер: Отсутствие EIN и присутствия в США
Клиент полагает, что невозможность выступить в роли FIOR связана с тем, что у британской компании нет американского Идентификационного номера работодателя (Employer Identification Number, EIN) и физического присутствия (`presence`) в США.

# 5. Потребность в специализированной экспертизе
Клиент осознаёт нехватку знаний для разрешения этой ситуации и ищет таможенного брокера, специализирующегося на работе с FIOR без регистрации в США.
~~~
```

# 9. Анализ обоснованности `P†⠿`
~~~markdown
# 1. Анализ проблем 1 и 2 (Задержка груза и запрос информации)
Эти проблемы **полностью обоснованы** и отражают фактическое положение дел.

Для ввоза коммерческих товаров в США необходимо идентифицировать Importer of Record — сторону, несущую юридическую ответственность за соблюдение импортного законодательства и уплату пошлин. CBP требует наличия действительного идентификационного номера импортёра. Задержка груза (§1.1) и запрос информации (§1.2) являются прямым следствием того, что британская компания не зарегистрирована в системах CBP.

# 2. Анализ проблемы 4 (Отсутствие EIN и присутствия как барьер)
Обеспокоенность клиента по этому поводу **обоснована лишь частично** и базируется на неполном понимании регуляторной среды США.

## 2.1. Требование физического присутствия
**Не обосновано.** Законодательство США не требует наличия офиса или юридического лица в стране для выполнения функций FIOR (также известного как Non-Resident Importer).

## 2.2. Требование EIN
**Не обосновано.** Хотя EIN является стандартным идентификатором для американских компаний, он не является обязательным для иностранных импортёров, если они не ведут иной деятельности в США, требующей его получения.

## 2.3. Альтернативный механизм идентификации: CAIN
CBP предусматривает альтернативу для FIOR. Если у компании нет EIN, она должна получить **CBP Assigned Importer Number (CAIN)** — номер, присваиваемый таможней.

**Вывод:** Реальная проблема заключается не в отсутствии EIN, а в отсутствии *любой* формы регистрации в CBP (в данном случае — CAIN). Именно это привело к остановке груза.

# 3. Анализ проблемы 3 (Желание выступить в роли FIOR)
Это **обоснованное и юридически допустимое** намерение. Однако для его реализации необходимо выполнить несколько ключевых требований, помимо получения CAIN:

## 3.1. Таможенная облигация (Customs Bond)
FIOR обязан предоставить финансовую гарантию уплаты пошлин, налогов и сборов. Это может быть разовая (Single Entry Bond) или непрерывная (Continuous Bond) облигация.

## 3.2. Конечный грузополучатель в США (Ultimate Consignee)
Критически важным требованием является назначение Конечного грузополучателя (Ultimate Consignee) — лица или компании, которая физически принимает товар на территории США. Этот получатель **обязан иметь адрес в США и действительный американский налоговый идентификатор** (EIN или SSN).

Учитывая, что клиент недавно занимался открытием фулфилмент-центра в США (`O.md`::§6.2), эта новая американская структура, если она уже функционирует и имеет EIN, может выступить в роли Ultimate Consignee.

# 4. Анализ проблемы 5 (Потребность в экспертизе)
Эта проблема **абсолютно обоснована**. Процесс регистрации FIOR является комплексным и требует обязательного участия лицензированного таможенного брокера США.

Брокер необходим для выполнения следующих действий:

1.  **Получение CAIN (Форма 5106):** Брокер подает форму CBP 5106 («Importer Identity Form») от имени клиента. Это требует предоставления пакета документов, включая:
    *   Таможенную доверенность (Customs Power of Attorney, POA). Для иностранных компаний CBP часто требует, чтобы POA была подписана двумя должностными лицами компании.
    *   Документы, подтверждающие легитимность иностранной компании и полномочия подписантов.
2.  **Оформление Customs Bond:** Брокер помогает приобрести облигацию у поручителя (Surety company) и зарегистрировать её в CBP.
3.  **Взаимодействие с CBP и DHL:** Брокер выступает в качестве уполномоченного агента для урегулирования вопросов по задержанной поставке.

Поиск брокера, имеющего опыт работы с процедурой регистрации FIOR, полностью оправдан.
~~~

# 10.
## 10.1.
`S⠿` ≔⠿~ (способы удалённого решения `P†⠿`)

## 10.2.
`Sᵢ` : `S⠿`

# 11.
## 11.1.
`С⁎` ≔ (Компания , о которой `ꆜ` пишет в `P2D`)

## 11.2.
⊤ (Допустим, что `С⁎` уже оформлена)

# 12.
`Sᨀ` ≔? (Решение `P†⠿` посредством `С⁎`)
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1.
## 1.1. 
`L_SOURCE` ≔ (Русский язык)

## 1.2. 
`L_TARGET` ≔ (English)

# 2.
## 2.1.
`D` ≔ (мой ответ `ꆜ`)

## 2.2.
Содержание `D`:
~~~markdown
1) Ваша UK company (далее — `C1`) не может «remain» the Foreign Importer of Record (FIOR), потому что она им не является.
Статус FIOR требует активной регистрации (форма 5106) и формального признания со стороны U.S. Customs and Border Protection (CBP).
2) Вы ошибочно фокусируетесь на отсутствии EIN, тогда как для иностранного импортера он не требуется: вместо него требуется Customs Assigned Importer Number (CAIN).
3) 2 месяца назад вы регистрировали компанию (далее — `C2`) в США: https://www.upwork.com/jobs/~021949010188391384864
В большинстве случаев самым разумным решением сейчас будет использовать именно `C2` в роли Importer of Record (IOR).
Для этого, правда, ей надо будет получить EIN, если у него его ещё нет.
Использование `C2` упрощает структуру импортной операции, поскольку она может выступать одновременно как IOR, так и Ultimate Consignee.
4) Даже если бы `C1` выступала в роли FIOR, ей всё равно потребовалось бы назначить Ultimate Consignee на территории США с действительным американским налоговым идентификатором.
Это требование закреплено в 19 CFR § 142.3(a)(6).
5) Для любого IOR, как резидента (типа `C2`), так и FIOR (которым гипотетически в будущем может стать `C1`), CBP обязательно потребует Customs Bond (`CB`).
Отсутствие `CB` — абсолютный барьер для ввоза коммерческих партий товара. 
`CB` представляет собой финансовую гарантию, предоставляемую правительству США через лицензированную американскую страховую компанию (surety), и подтверждает, что импортер выполнит все свои обязательства по уплате пошлин, налогов и сборов, а также будет соблюдать все таможенные правила. 
~~~

# 3.
## 3.1.
`D2` ≔ (начальная часть `D`, переведённая с `L_SOURCE` на `L_TARGET`)

## 3.2.
Содержание `D2`:
~~~markdown
1) Your UK company (hereinafter `C1`) cannot «remain» the Foreign Importer of Record (FIOR), because it is not one.
The FIOR status requires active registration (form 5106) and formal recognition from U.S. Customs and Border Protection (CBP).
2) You are mistakenly focusing on the absence of an EIN, whereas it is not required for a foreign importer: a Customs Assigned Importer Number (CAIN) is required instead.
3) 2 months ago you registered a company (hereinafter `C2`) in the USA: https://www.upwork.com/jobs/~021949010188391384864
In most cases, the most reasonable solution now is to use `C2` as the Importer of Record (IOR).
To do this, however, it will have to obtain an EIN if it does not have one yet.
Using `C2` simplifies the structure of the import operation, as it can act simultaneously as both the IOR and the Ultimate Consignee.
4) Even if `C1` were to act as the FIOR, it would still be required to designate an Ultimate Consignee in the United States with a valid U.S. tax identification number. 
This requirement is established in 19 CFR § 142.3(a)(6).
~~~

# 4.
## 4.1.
`F` ≔ (фрагмент `D`)

## 4.2.
Содержание `F`:
~~~markdown
`CB` представляет собой финансовую гарантию, предоставляемую правительству США через лицензированную американскую страховую компанию (surety), и подтверждает, что импортер выполнит все свои обязательства по уплате пошлин, налогов и сборов, а также будет соблюдать все таможенные правила. 
~~~

# 5. `᛭T`
Переведи `F` на `L_TARGET`, с учётом:
- контекста `D`
- `D2`: уже переведённой части `D`
- `᛭O`

# 6. Правила перевода
## 6.1.
Переводи именно в той стилистике, как написано на `L_SOURCE`.
Не делай перевод более вежливым, чем оригинал.

## 6.2.
Те предложения, которые сейчас полностью на `L_TARGET` — оставь без изменения.

## 6.3.
### 6.3.1.
Не используй Markdown: только plain text.
### 6.3.2.
При этом можно и нужно использовать то форматирование, которое уже есть в оригинале: его не убирай.
### 6.3.3.
Не форматируй веб-ссылки посредством Markdown, если они не отформатированы так в оригинале. 
Например, не пиши так:
```
[https://www.eca.web.tr/eca-nita-esnek-uclu-eviye-bataryasi-beyaz-102118110-308](https://www.eca.web.tr/eca-nita-esnek-uclu-eviye-bataryasi-beyaz-102118110-308)
```
если в оригинале скобок `[]()` нет.

## 6.4.
Форматируй перевод в точности как оригинал. 
В частности:
*) каждый абзац должен содержать ровно одно предложение
*) между абзацами не должно оставаться пустых строк.
*) кавычки используй те же, что и в оригинале: «» и ``.

## 6.5.
Не используй сокращения типа «don't». Все подобные фразы пиши полностью: «do not».

## 6.6.
Не используй жаргон.
Вместо этого используй официальные термины.
### 6.6.1.
В частности, фразы в кавычках используй только в том случае, когда они являются точными цитатами.
Не используй фразы в кавычках для применения жаргонных фраз.
Например, следующий фрагмент текста недопустим, потому что там используется жаргонная фраза «пролетел»: 
```
Например, код, который пушит данные о покупке, подключён асинхронно и загружается с небольшой задержкой, а триггер уже «пролетел».
```

## 6.7.
При обсуждении программного обеспечения используй точные официальные термины на английском языке: именно в том виде, как они указаны в официальной англоязычной документации к этому программному обеспечению.

## 6.8.
Не используй «you need» и другие подобные обращённые к клиенту фразы, перекладывающие действия на него.
Помни: я пишу клиенту или потенциальному клиенту.
Делать в любом случае буду я, а не клиент.
Вместо «you need» используй 2 альтернативы:
### 6.8.1.
Нейтральные фразы типа «it is necessary».
### 6.8.2.
Глаголы в неопределённой форме.
Например, во фрагменте ниже использованы подобные глаголы «set up», «create»:
```
1.2) Set up the transfer of login events from WordPress to Power BI using Fabric / OneLake.
1.2.1) Set up a «Data Pipeline» from the WordPress database table that stores login events (see point 1.1) to Fabric / OneLake.
1.2.2) Set up a connection from Power BI to Fabric / OneLake to pass login events.
1.3) Create the data model in Power BI.
```
Обрати внимание, в этом фрагменте не говорится, кто именно будет выполнять описанные действия: ответственность не перекладывается на клиента, в отличие от «you need».

## 6.9.
Никогда не переводи понятие «сайт» / «веб-сайт» как «site». 
Вместо этого используй форму «website»: это является более профессиональным.

## 6.10.
Никогда не переводи понятие «пункт нумерованного списка» как «item».
Всегда переводи это как «point».

## 6.11.
Вместо «for example» используй «e.g.».
При этом не забывай, что в начале предложения эта фраза должна начинатся с заглавной буквы: «E.g.»
~~~~~~