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
Сегодня 2025-11-14.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021989226461858190659

## 2.2. Title
Inventory/COGS Systems Architect (Fishbowl → QuickBooks → Bill.com Cleanup)

## 2.3. Description
`PD` ≔ 
```text
#
We are a fast-growing medical supply distribution company operating multiple warehouses with growing SKU volume. 

# Our tech stack includes:
- Fishbowl (Inventory Management System)
- QuickBooks Online (GL)
- Bill.com (AP)

Multi-warehouse receiving, landed cost components (freight, tariffs, drayage), and multiple sales channels.

#
We are looking for a senior-level systems expert — not a bookkeeper — who specializes in inventory costing, landed cost flow, and Fishbowl ↔ QuickBooks architecture.
This is NOT an ongoing bookkeeping role. 
This is a one-time “surgeon-style” engagement to fix the underlying system issues.

# Scope of Work (One-Time Project):
## 1. Audit our current system flows
- Review existing Fishbowl → QBO mappings
- Identify duplicate COGS pushes
- Review how POs, receipts, adjustments, and landed costs flow
- Identify causes of negative inventory
- Verify what Fishbowl should vs. should not post to QBO

## 2. Fix COGS + Landed Cost Architecture
- Correct costing logic (tariffs, freight, drayage, receiving fees)
- Ensure correct allocation per SKU
- Prevent double-counting of COGS
- Establish clean timing between receiving and cost recognition

## 3. Correct Historical Errors
- Identify discrepancies in COGS
- Identify incorrect or missing landed cost entries
- Reconcile historical periods where needed (light touch)

## 4. Produce SOPs for our accounting team
Step-by-step instructions for:
- Receiving items
- Entering landed cost
- Handling adjustments
- Bill.com workflows
- Month-end inventory reconciliation
- Define EXACTLY what should push into QBO and what should not

# Required Expertise:
- 5+ years working with Fishbowl Inventory
- Deep knowledge of QuickBooks Online + inventory integrations
- Strong experience with landed cost / COGS architecture
- Experience with multi-warehouse environments
- Ability to diagnose and fix duplicate or incorrect mappings
- Proven experience writing SOPs and documenting system flows
- Extremely strong communication and precision

If you do not have direct Fishbowl → QBO experience, please do not apply.

# Deliverables:
- Clean, corrected Fishbowl → QBO integration
- Proper landed cost mapping
- Eliminated duplicate COGS and negative inventory
- Written documentation/SOPs
- A 60–90 minute handoff call with our team

# Budget & Engagement Structure:
This is a project-based “surgery” with a defined start and finish.
We are open to hourly or fixed-fee, depending on your assessment.

# Please include in your proposal:
- Specific examples of Fishbowl cleanup work
- Screenshots or diagrams of previous architecture fixes
- Relevant case studies
- A brief outline of how you would approach diagnosing our setup

# About Us:
We are a U.S.-based medical supply distribution company serving senior living, dental, and government customers nationwide. 
High transaction volume, high SKU volume, multi-warehouse receiving.

#
We need someone who is sharp, fast, decisive, and deeply experienced — a true systems surgeon.

# Deliverables
- Clean, corrected Fishbowl → QBO integration
- Proper landed cost mapping
- Eliminated duplicate COGS and negative inventory
- Written documentation/SOPs
- A 60–90 minute handoff call with our team
```

## 2.4. Tags
Fishbowl
QuickBooks Online
Bill.com

## 2.5. Questions
### 2.5.1.
Have you personally worked on Fishbowl → QuickBooks cleanup projects? 
Describe the LAST one.

### 2.5.2.
Explain how Bill.com AP bills should map if they relate to landed cost versus non-inventory expenses

### 2.5.3.
What should Fishbowl push into QuickBooks — and what should never be pushed?

### 2.5.4.
How do you prevent duplicate COGS entries between Fishbowl and QuickBooks?

### 2.5.5.
What’s your approach to resolving negative inventory and timing mismatches?

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
 Jan 17, 2018
### 5.3.2. Hire rate (%)
81
### 5.3.3. Количество опубликованных проектов (jobs posted)
256
### 5.3.4. Total spent (USD)
827K
### 5.3.5. Количество оплаченных часов в почасовых проектах
45443
### 5.3.6. Средняя почасовая ставка (USD)
16.54

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

### 6.1.1. URL
https://www.upwork.com/jobs/~021984365572324036634

### 6.1.2. Title
Website Development for Subscription Business

### 6.1.3. Description
`P1D` ≔ 
```text
Hi,

We have a subscription business. We currently use Shopify and use the Recharge app. We are looking to develop our own solution as we are facing limitations using Recharge:

- Our customer is billed net 30 days and invoiced outside of Shopify. Recharge requires a credit card. We want the customer to be able to checkout without the need to enter a credit card

- Our customer places multiple subscriptions at the same time under the same account. Each subscription is associated with a particular person. Recharge does allow us to associate a specific subscription with a particular person

- There are multiple users for the same location, but each have their own account. We need to be able to grant all users under the same location access to the subscriptions placed for that location

We will set up a call to discuss details, but I would like applicants to address the solutions to three points above.

Thank you,
Otto
```

### 6.1.4. Publication Date
2 weeks ago

### 6.1.5. Payment Terms (USD) 
#### 6.1.5.1. Expected by `ꆜ`  
12-27 Hourly
#### 6.1.5.2. Actual
неизвестно

### 6.1.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.1.7. Duration (expected by `ꆜ`)
1-3 months

### 6.1.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.2. `P2⁎`

### 6.2.1. URL
https://www.upwork.com/jobs/~021873481824645157887

### 6.2.3. Title
Shopify Product Listing

### 6.2.3. Description
`P2D` ≔ 
```text
Hi,

We are looking for someone to help us create Shopify listings. We will need your help on an as-needed basis (approximately a couple of hours per week).

We will provide the information and images for each listing. While we don't need you to work during specific hours, we do appreciate quick turnaround times.

Thank you in advance for your application.

Otto
```

### 6.2.4. Publication Date
4 quarters ago

### 6.2.5. Payment Terms  (USD) 
#### 6.2.5.1. Expected by `ꆜ`
10-20 Hourly
#### 6.2.5.2. Actual 
4 hrs @ $10.00/hr
Billed: $43.61

### 6.2.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.2.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
6+ months

### 6.2.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.3. `P3⁎`

### 6.3.1. URL
https://www.upwork.com/jobs/~021861536325315934625

### 6.3.2. Title
Virtual Assistant Needed for Hotel Points Management

### 6.3.3. Description
`P3D` ≔ 
```text
We are looking for a detail-oriented Virtual Assistant (VA) to help us collate and submit missing hotel points for our company bookings. The ideal candidate will be responsible for reviewing booking records, identifying missing points, and communicating with hotel partners to ensure all points are accurately submitted. Strong organizational skills and attention to detail are essential for this role. If you have experience in handling hotel bookings and rewards programs, we would love to hear from you!
```

### 6.3.4. Publication Date
4 quarters ago

### 6.3.5. Payment Terms (USD) 
#### 6.3.5.1. Expected by `ꆜ`  
8-15 Hourly
#### 6.3.5.2. Actual
36 hrs @ $13.00/hr
Billed: $507.37

### 6.3.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.3.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

### 6.3.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.4. `P4⁎`

### 6.4.1. URL
https://www.upwork.com/jobs/~018f8c975c81124b02

### 6.4.2. Title
Urgently Seeking Packing Facility Near Weifang

### 6.4.3. Description
`P4D` ≔ 
```text
We are urgently looking for a facility in or close to Weifang, China that can pack PE gloves into packs of 10. The gloves are ready to be transported to the facility. We need to move very quickly and secure a facility today November 29, 2023. There is no room for delay.
```

### 6.4.4. Publication Date
2 years ago

### 6.4.5. Payment Terms (USD) 
#### 6.4.5.1. Expected by `ꆜ`  
20-35 Hourly
#### 6.4.5.2. Actual
39 hrs @ $25.00/hr
Billed: $1,350.65

### 6.4.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.4.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

### 6.4.8. Contractor Location (expected by `ꆜ`)
China

## 6.5. `P5⁎`

### 6.5.1. URL
https://www.upwork.com/jobs/~01a913babab0fae1d4

### 6.5.2. Title
Seeking Virtual Assistant to print/ship product samples and government bids

### 6.5.3. Description
`P5D` ≔ 
```text
Hello!

We are a small, family owned and operated supplier of medical and paper products. We are looking for a super efficient, speedy VA who can take over the printing, labelling, and shipping of product samples and government bids.

This role will involve receiving samples from our suppliers via FedEx/UPS/USPS, keeping track of samples inventory in a Google spreadsheet, and shipping samples to customers when requested. Besides product samples, we will also count on you to print and deliver government bids.

We ship samples and bids with UPS. We are expecting samples and bids to be shipped same-day when requested, and usually with little notice, so ideally you're someone who works from home and can quickly move on the request and ship when requested. All communication related to samples will take place on Slack.

Required:
- Highly detail-oriented and FAST
- Located in the US
- Live close to a UPS drop box or location that has preferably late drop-off times Monday through Friday
- Have an efficient printer to print shipping labels and documents (bids can be 50-100 pages in some cases)
- Able to ship samples same-day with short notice, almost always in the mid-late afternoon. [include the word fog in your proposal so I know you've read these details!]. Sometimes we may get a lead and only have 30min-60min notice.
```

### 6.5.4. Publication Date
last year

### 6.5.5. Payment Terms (USD) 
#### 6.5.5.1. Expected by `ꆜ`  
15-25 Hourly
#### 6.5.5.2. Actual
19 hrs @ $20.00/hr
Billed: $398.07

### 6.5.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.5.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
3-6 months

### 6.5.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.6. `P6⁎`

### 6.6.1. URL
https://www.upwork.com/jobs/~017a96a68bfc23ed8b

### 6.6.2. Title
Medical Supplies Company Looking for Part-Time Cold Calling Expert

### 6.6.3. Description
`P6D` ≔ 
```text
Hi,

We are a Florida-based supplier of medical products looking for a part-time business development rep. Your job is simple: you will be calling leads/prospects to gather data, not to sell. We are building a database of specific information about our industry, which we can later use to help us sell.    

What we expect of you:
- You would be asked to work a few hours (approx. 5hrs to start) per week during US business hours (flexible)
- Fluent in English
- VERY comfortable making calls and therefore a great communicator

You do not need to be an expert in our field, but we will expect you to have a basic understanding of our products which we will teach you.

Thanks,
Otto
```

### 6.6.4. Publication Date
2 years ago

### 6.6.5. Payment Terms (USD) 
#### 6.6.5.1. Expected by `ꆜ`  
15-35 Hourly
#### 6.6.5.2. Actual
728 hrs @ $35.00/hr
Billed: $26,982.91

### 6.6.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.6.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
1-3 months

### 6.6.8. Contractor Location (expected by `ꆜ`)
Europe, United States

## 6.7. `P7⁎`

### 6.7.1. URL
https://www.upwork.com/jobs/~021852454032592886367

### 6.7.2. Title
Order Fulfilment Expert Needed

### 6.7.3. Description
`P7D` ≔ 
```text
Hi,

We are a US-based national distributor of medical supplies seeking someone who can support our order fulfilment team in processing orders.

We receive orders from the following sources: emailed POs, Shopify, various procurement software. The orders are either synced or inputted manually into our Inventory Management Software (Fishbowl) where they are then sent out to our various 3PL warehouse and fulfilment partners to ship.

Your responsibilities will include:
- Input orders into Fishbowl manually
- Send out orders to our 3PL partners
- Update tracking numbers on SOs in Fishbowl  

What we're looking for:
- Fluent/highly proficient in English
- Experience fulfilling ecommerce orders
- Available during US business hours (part-time: expected to work 15-20 hours per week)
- Experience with Fishbowl Inventory would be a big plus
- Extremely communicative. We all work remote, so maintaining a high level of communication is a must  

Please add the word "Wow" at the top of your application so that I know you have read through the job description.

Thank you,
Otto
```

### 6.7.4. Publication Date
last year

### 6.7.5. Payment Terms (USD) 
#### 6.7.5.1. Expected by `ꆜ`  
5-15 Hourly
#### 6.7.5.2. Actual
971 hrs @ $10.00/hr
Billed: $10,211.86

### 6.7.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.7.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
1-3 months

### 6.7.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.8. `P8⁎`

### 6.8.1. URL
https://www.upwork.com/jobs/~01fa16a12a701caed3

### 6.8.2. Title
Data Entry of UPS Tracking Numbers to Zoho Inventory

### 6.8.3. Description
`P8D` ≔ 
```text
Hi,

We are looking for someone to help with data entry of UPS tracking numbers for our ecommerce store.

The task will involve assisting our logistics and order fulfilment team by updating Zoho Inventory with the UPS tracking numbers for orders from our various sales channels.  

Availability: US business hours
Time: This will vary based the order volume (normally, the 1st week of the month is the busiest), but should be 10-20 hours per week

Thanks,
Otto
```

### 6.8.4. Publication Date
2 years ago

### 6.8.5. Payment Terms (USD) 
#### 6.8.5.1. Expected by `ꆜ`  
6-10 Hourly
#### 6.8.5.2. Actual
2,534 hrs @ $7.00/hr
Billed: $18,571.33

### 6.8.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.8.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
3-6 months

### 6.8.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.9. `P9⁎`

### 6.9.1. URL
https://www.upwork.com/jobs/~01f784d6af2cf3bac7

### 6.9.2. Title
Business Development Assistant - Personalized Prospect Outreach for Medical Supplies Distributor

### 6.9.3. Description
`P9D` ≔ 
```text
Business Development Assistant

About the Role:
We're on the hunt for a go-getter Business Development Assistant to team up with the young and ambitious owners behind a medical supply business that's been thriving since 2020. Starting off, this role will be part-time, requiring your magic touch for 10-15 hours per week and scaling up from there if all goes well. Get ready to dive into tailored outreach, from crafting cool emails to brainstorming personalized gifts and nifty follow-up plans. Your magic touch will amp up customer growth and make our mark in the scene, reaching out to organizations in senior living, skilled nursing, dental, and urgent care (in that order of importance).

What You'll Be Up To:
- Co-conspiring on custom outreach to prospects.
- Whipping up awesome email drafts and snazzy gift ideas.
- Sketching out follow-up game plans for spot-on timing.
- Being the keeper of records for all things outreach and replies.
- Adding your wisdom to finesse our outreach tricks.
- Rocking our values and WOW vibe like it's second nature.
- Coordinating with our data wizards to ensure prospect contact info is fresher than fresh.
- Double-checking our CRM data against LinkedIn and the prospect's own website.

What We're Looking For:
- A degree in Business, Marketing, or something rad (or street smarts, anyone?).
- Showcasing skills in business hustle, sales charm, or customer love.
- Wordsmith skills, both typed and spoken.
- Thriving in the fast lane, flying solo like a boss.
- If you're medical supply savvy, that's the cherry on top.

Why You Should Jump In:
You're stoked about cranking up business buzz, sparking connections, and leaving your mark on our medical supplies game. If this vibes with you, hop on board. We're all about turning every chat into a WOW moment.

So, ready to fuel growth, crank up connections, and join the hustle in our medical supplies scene? Hit us up – let's add a WOW touch to every move we make.
```

### 6.9.4. Publication Date
2 years ago

### 6.9.5. Payment Terms (USD) 
#### 6.9.5.1. Expected by `ꆜ`  
7-20 Hourly
#### 6.9.5.2. Actual
1 hrs @ $25.00/hr
Billed: $18.13

### 6.9.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.9.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
6+ months

### 6.9.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.10. `P10⁎`

### 6.10.1. URL
https://www.upwork.com/jobs/~01b54e44f526afc25a

### 6.10.2. Title
Government Contract/Bid Award Data Retrieval & Tabulation - Medical Supplies

### 6.10.3. Description
`P10D` ≔ 
```text
We are a distributor of medical supplies looking for ongoing assistance with retrieving medical supplies & paper supplies bid award data from various government agencies.

Role will involve:
- Identifying relevant, expired bids using the bid search engine we use.
- Retrieving bid tabulations and award data from the agency's website or by requesting it from the agency via phone or email.
- Organizing the award data into an easy-to-read and filterable Google Sheet that we can consult when preparing government proposals.
- Quickly retrieving award data for ongoing, sometimes time-sensitive opportunities being worked on by our company

We are focused principally on medical supplies and paper supplies such as disposable gloves, medicine cups, paper cups, can liners, toilet tissue, facial tissues.

We'd like to begin with 5-10 hours per week and scale up from there over time. We are looking to obtain as much useful data as possible during the allotted hours.

If you have any questions, please let us know.
```

### 6.10.4. Publication Date
2 years ago

### 6.10.5. Payment Terms (USD) 
#### 6.10.5.1. Expected by `ꆜ`  
10-15 Hourly
#### 6.10.5.2. Actual
11 hrs @ $20.00/hr
Billed: $250.65

### 6.10.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.10.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
6+ months

### 6.10.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.11. `P11⁎`

### 6.11.1. URL
https://www.upwork.com/jobs/~0157e68501ee24312b

### 6.11.2. Title
Seeking Virtual Assistant to print/ship product samples and government bids

### 6.11.3. Description
`P11D` ≔ 
```text
Hello!

We are a small, family owned and operated supplier of medical and paper products. We are looking for a super efficient, speedy VA who can take over the printing, labelling, and shipping of product samples and government bids.

This role will involve receiving samples from our suppliers via FedEx/UPS/USPS, keeping track of samples inventory in a Google spreadsheet, and shipping samples to customers when requested. Besides product samples, we will also count on you to print and deliver government bids.

We ship samples and bids with UPS. We are expecting samples and bids to be shipped same-day when requested, and usually with little notice, so ideally you're someone who works from home and can quickly move on the request and ship when requested. All communication related to samples will take place on Slack.

Required:
- Highly detail-oriented and FAST
- Located in the US
- Live close to a UPS drop box or location that has preferably late drop-off times Monday through Friday
- Have an efficient printer to print shipping labels and documents (bids can be 50-100 pages in some cases)
- Able to ship samples same-day with short notice, almost always in the mid-late afternoon. [include the word fog in your proposal so I know you've read these details!]. Sometimes we may get a lead and only have 30min-60min notice.
```

### 6.11.4. Publication Date
2 years ago

### 6.11.5. Payment Terms (USD) 
#### 6.11.5.1. Expected by `ꆜ`  
15-25 Hourly
#### 6.11.5.2. Actual
158 hrs @ $30.00/hr
Billed: $4,997.30

### 6.11.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.11.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

### 6.11.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.12. `P12⁎`

### 6.12.1. URL
https://www.upwork.com/jobs/~014abd3c15cc61b124

### 6.12.2. Title
PPE Pricing Analyst & Bid Monitoring (Dual Role) - Government Sales/Bids/Tenders

### 6.12.3. Description
`P12D` ≔ 
```text
We are looking to hire, on a part-time basis (est. 10hrs/week), a PPE Pricing/Market Research Analyst and Bid Monitoring Specialist (dual role).

As a Pricing Researcher acting within the Government Sales department of our company, you will be responsible for researching, qualifying, compiling, and reporting winning pricing from awarded government/public sector contracts. Our product categories of focus are disposable gloves and can liners. The objective behind this role is to provide valuable market research, specifically the winning prices at which government contracts are being awarded to vendors supplying products within our categories of focus, which will allow the company to compete effectively on active and future government agency solicitations.

As a Bid Monitoring Specialist acting within the Government Sales department of our company, you will be responsible for monitoring the status of bids submitted by our company in response to government/public sector solicitations. The objective behind this role is to keep the company informed on the quotes it has submitted to government agencies (win/loss/other), to ensure that any solicitation reopenings are immediately discovered, to ensure that any announcements related to contract award and winning pricing are communicated to the Sales team.

This is very much an ‘ownership’ position, one where a growing small business will rely on you end-to-end to execute the required duties at a high level, with little to no error and little supervision beyond initial training.

What’s in it for you:

Work with a small but passionate core team
Join a company with a culture driven by ambition, gratitude, and a people-first approach. A company with strong ethics and principles.
Own your responsibilities end-to-end, be a STAR! Say goodbye to lengthy approvals and discussions. Your ideas are valued and if objectively superior to the current way things are done, will be implemented rapidly. The company’s only focus is to grow, become better, and more efficient day by day.

You responsibilities:

Market Research Analyst:

Research relevant, expired bids on the BidPrime platform.
Investigate said bids thoroughly and extract awarded pricing and contract details.
Investigation may involve contacting the government agency via phone or email in order to receive needed information and documents.
The unique terms and details of the contract/solicitation need to be extracted for reporting, as these terms and details affect the Sales team’s interpretation of pricing data. Below are some of the most important terms and details that will need to be considered and extracted for reporting alongside pricing data:
Award Method: Are all line items in the contract going to be awarded to one vendor? Or will the agency evaluate each line item individually and award multiple vendors, if needed?
Ordering Quantities & Method: Does the solicitation/contract specify ordering quantities? If yes, will the agency order these quantities on an ‘as needed’ basis or one-time?
For example, a line item might have a quantity of 500 cases listed for nitrile gloves, however will these 500 cases be ordered all at once or in unknown smaller chunks over the period of the contract?
Contract Period/Year(s)/Date(s)
Compile and categorize data into a detailed and filterable Google Sheet.
Our two key product categories at this time each have several variants/attributes that need to be reported in every data entry within the ongoing Market Research report.
Side note, mention the word 'analyst' if you read this far. For example, disposable gloves attributes include: material type, thickness (if mentioned), AQL score (if mentioned), latex and powder free (Y/N; if mentioned), etc. Reporting per set attributes allows Bid Managers to filter quickly and seamlessly when computing a quote for an active solicitation.
Collecting data for attributes may require you to investigate into the solicitation’s Q&A section, all published addenda, the ITB itself, pricing excel file, and/or other documents contained within the solicitation package. Some solicitations even mention that one must call to receive addenda via email.


Tools you will be using:
Google Sheets
BidPrime
Government Agency Portals (such as: BidSync, IonWave, Central Bidding, etc.)
Sam.Gov
Upwork (TBC)
Slack
RingCentral/Phone

We are looking for someone:
Relentless & tenacious
Detail-oriented
Positive
Tech savvy, can learn new technologies and applications quickly
Google Sheet data wizard
Efficient, works fast
….and specifically to this role: Realizes that 100% accuracy of data is imperative since  it will be relied upon by both the sourcing and sales departments when making decisions and taking actions - all of which affects the reputation and success of the company.

Plus:
Familiarity with PPE and product attributes of disposable gloves and can liners
Familiarity with government/public sector solicitations
```

### 6.12.4. Publication Date
3 years ago

### 6.12.5. Payment Terms (USD) 
#### 6.12.5.1. Expected by `ꆜ`  
15-30 Hourly
#### 6.12.5.2. Actual
103 hrs @ $20.00/hr
Billed: $1,921.13

### 6.12.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.12.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
6+ months

### 6.12.8. Contractor Location (expected by `ꆜ`)
Not specified


# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`, `P4⁎`, `P5⁎`, `P6⁎`, `P7⁎`, `P8⁎`, `P9⁎`, `P10⁎`, `P11⁎`, `P12⁎`}

## 7.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 7.3.
`Pi` : `Ps`

# 8.
## 8.1.
`С⁎` ≔ 
```
Компания STUB, о которой `ꆜ` пишет в `Ps`:
~~~
medical supply distribution company
~~~
```

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)


# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
Fishbowl → QuickBooks → Bill.com Cleanup
~~~
```

# 9.
## 9.1.
`T1⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Identify duplicate COGS pushes
~~~
```

## 9.2.
`T2⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Identify causes of negative inventory
~~~
```

## 9.3.
`T3⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Correct costing logic (tariffs, freight, drayage, receiving fees)
~~~
```

## 9.4.
`T4⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Ensure correct allocation per SKU
~~~
```

## 9.5.
`T5⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Prevent double-counting of COGS
~~~
```

## 9.6.
`T6⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Establish clean timing between receiving and cost recognition
~~~
```

# 10.
## 10.1.
`Q1⁎` ≔ (Вопрос `ꆜ` §2.5.1)

## 10.2.
`Q2⁎` ≔ (Вопрос `ꆜ` §2.5.2)

## 10.3.
`Q3⁎` ≔ (Вопрос `ꆜ` §2.5.3)

## 10.4.
`Q4⁎` ≔ (Вопрос `ꆜ` §2.5.4)

## 10.5.
`Q5⁎` ≔ (Вопрос `ꆜ` §2.5.5)

# 11. Что беспокоит `ꆜ` (анализ выполнен Gemini Deep Research)
https://gemini.google.com/share/c735eafadd88

## **Часть 1: Архитектура Интеграции (ꆜ и P⁎): Конфликт Операционного и Финансового Контуров**

Для выявления и анализа проблем, возникающих в интегрированной среде ꆜ (Fishbowl) и P⁎ (QuickBooks), необходимо прежде всего установить фундаментальную архитектурную парадигму их взаимодействия. Понимание этой парадигмы является необходимым условием для диагностики, поскольку практически все последующие ошибки и расхождения являются прямым следствием ее нарушения.

### **1.1 Определение Ролей: Fishbowl как "Мастер" Операций, QuickBooks как "Леджер" Финансов**

Интеграция Fishbowl (ꆜ) с QuickBooks (P⁎) не является "синхронизацией" двух равноправных систем. По своей сути, это процесс *замещения* функционала. С момента активации интеграции Fishbowl становится единственной и основной системой (Master System) для управления всеми операционными аспектами бизнеса: управлением запасами, закупками, продажами, производством и складскими операциями.1

Ключевым требованием этого процесса является то, что после завершения интеграции все функции, связанные с управлением запасами (Inventory) и заказами на закупку (Purchase Orders), в QuickBooks *должны быть принудительно отключены*.1 QuickBooks перестает отслеживать *физические* остатки, их перемещения или статусы заказов; он оперирует исключительно *стоимостным* выражением этих активов.4

Поток данных строго регламентирован: Fishbowl управляет операциями (например, приемка товара на склад, отгрузка клиенту, корректировка остатков) и по мере их выполнения *отправляет* в QuickBooks сводные финансовые транзакции. Как правило, это записи в Главный Журнал (General Journal Entries - GJE) для обновления Главной книги.5 Фактически, Fishbowl "инструктирует" QuickBooks: "Операция по продаже товара X завершена, необходимо создать запись для Себестоимости (COGS) и Дохода" 6 или "Товар Y получен от поставщика, необходимо оприходовать Актив и отразить Обязательство".7

### **1.2 Золотое Правило Интеграции: Недопустимость Прямого Ввода Операционных Данных в P⁎**

После интеграции экосистема становится архитектурно хрупкой. Ее целостность полностью зависит от 100% соблюдения *однонаправленного* потока данных для всех операционных транзакций: **ꆜ (Fishbowl) -> P⁎ (QuickBooks)**.

Первопричина практически всех сбоев и расхождений баланса заключается в нарушении этого правила. Любая операционная транзакция (например, ручная корректировка остатков, создание счета-фактуры от поставщика за товар, изменение заказа на продажу), инициированная *непосредственно* в QuickBooks, *необратимо* нарушает баланс между системами.4 Fishbowl *никогда* не получит информацию об этом изменении, поскольку интеграция не предполагает обратного потока операционных данных. Системы процедурно не защищены от такого вмешательства; целостность данных зависит исключительно от строгой дисциплины пользователей.

### **1.3 Таблица 1: Матрица Разделения Ответственности за Данные (ꆜ vs. P⁎)**

Для обеспечения операционной ясности, разделение функций должно быть строго закреплено.

| Бизнес-функция | Ответственная система (ꆜ или P⁎) | Обоснование / Процесс | Источники |
| :---- | :---- | :---- | :---- |
| **Управление запасами** (Остатки, Перемещения, Корректировки) | ꆜ (Fishbowl) | FB отключает эту функцию в QB. Все корректировки, включая циклические инвентаризации (Cycle Counts) 11, происходят *только* в FB. | 1 |
| **Заказы на закупку (PO)** | ꆜ (Fishbowl) | PO создаются и управляются в FB. QB не должен использоваться для создания PO.12 | 1 |
| **Приемка товаров (Receiving)** | ꆜ (Fishbowl) | Физическая приемка регистрируется в модуле FB Receiving.13 Это действие генерирует GJE для оприходования актива и создания обязательства на счете "Holding".7 | 7 |
| **Счета от поставщиков (AP Bills) - *Товарные*** | ꆜ (Fishbowl) | Счета вводятся через модуль "Reconcile" в FB.13 Этот модуль выполняет 3-стороннюю сверку (Bill vs. PO vs. Receipt). | 10 |
| **Счета от поставщиков (AP Bills) - *Нетоварные*** | P⁎ (QuickBooks) / Bill.com | Счета за аренду, коммунальные услуги, телефонию и т.д. вводятся напрямую в QB (или через Bill.com), так как они не влияют на оценку товарных активов. | (Логический вывод) |
| **Заказы на продажу (SO)** | ꆜ (Fishbowl) | Полный цикл: создание SO, комплектация (picking), упаковка (packing), отгрузка (shipping) – все управляется в FB.6 | 1 |
| **Выставление счетов (Invoicing)** | ꆜ (Fishbowl) | FB генерирует счет-фактуру (Invoice) клиенту *после* отгрузки и отправляет готовую транзакцию в QB.1 | 1 |
| **Прием платежей от клиентов** | ꆜ (Fishbowl) или P⁎ (QuickBooks) | FB может принимать платежи и передавать их в QB как "Sales Receipt".1 QB также может принимать платежи по счетам, созданным FB. | 1 |
| **Оплата счетов (Bill Payment)** | P⁎ (QuickBooks) | QB (или Bill.com) обрабатывает *фактическую оплату* счетов поставщикам, которые были *созданы* (для товаров) в FB и экспортированы в QB.1 | 1 |

Анализ данной архитектуры показывает, что проблемы, с которыми сталкивается пользователь, с высокой вероятностью носят не *технический* (сбой ПО), а *процедурный* характер. Они вызваны нарушением фундаментальной архитектуры "Master/Ledger". Данные из источников 10 подтверждают, что сбои происходят, когда команды пытаются продолжать работать в обеих системах (например, "running POs through Quickbooks still" 12).

Эта архитектура чрезвычайно хрупка, поскольку она требует, чтобы финансовый отдел (бухгалтерия, AP-отдел) полностью отказался от своих привычных инструментов в QB для товарных операций и принял рабочий процесс, диктуемый складской/производственной системой (FB). Данные указывают на "культурное" сопротивление: "Sometimes the QuickBooks folks just do not respect Fishbowl".10 Таким образом, ᛭T сталкивается не с технической, а с организационной проблемой: отдел AP и склад ведут "войну" за контроль над процессом, и AP-отдел, используя QB и сторонние инструменты (например, Bill.com), выигрывает операционные "битвы" (быстро вводя счета), но проигрывает финансовую "войну", разрушая целостность данных.

## **Часть 2: Выявление Ключевых Проблем Экосистемы (Ответ на Задачу 1)**

Нарушение описанной архитектуры проявляется в виде ряда критических "симптомов" — конкретных проблем, которые, вероятно, наблюдаются в финансовых и операционных отчетах.

### **2.1 Симптом 1: Хронические Расхождения в Оценке Складских Запасов и COGS**

Это наиболее распространенная и очевидная проблема. Общая стоимость запасов (счет "Inventory Asset") на Балансовом отчете в P⁎ (QuickBooks) *категорически не совпадает* с данными отчета о стоимости запасов (например, "Inventory Valuation Summary") в ꆜ (Fishbowl).1 Аналогичным образом, себестоимость проданных товаров (COGS) в отчете о Прибылях и Убытках (P&L) в QB не коррелирует с ожидаемыми значениями, рассчитанными на основе отгрузок в FB.4

### **2.2 Симптом 2: Феномен "Отрицательных Складских Остатков" (Negative Inventory)**

В системе P⁎ (QuickBooks) (а в некоторых запущенных случаях и в ꆜ) появляются отрицательные значения по количеству товаров на складе.10 Это является логистической и бухгалтерской невозможностью и указывает на фундаментальный сбой в учете. Этот симптом часто возникает, когда пользователь QB вручную изменяет счет-фактуру, созданную FB, и использует "старый" артикул QB (который должен быть неактивен) вместо специального артикула, используемого FB (например, "FB_Item"). Это действие заставляет QB некорректно продублировать транзакцию COGS, что приводит к списанию несуществующего товара и появлению отрицательного остатка.10

### **2.3 Симптом 3: Удвоение Кредиторской Задолженности (AP) и Активов Запасов**

Это крайне специфическая и опасная финансовая ошибка. Пользователь в P⁎ (QuickBooks) видит "Item Receipt" (Приходный ордер), автоматически созданный Fishbowl в результате приемки товара. Следуя *старому* рабочему процессу (до-Fishbowl), бухгалтер *вручную* преобразует этот "Item Receipt" в "Bill" (Счет-фактуру) в QuickBooks.

Это действие *мгновенно удваивает* как запасы (Inventory Asset), так и кредиторскую задолженность (Accounts Payable).10 Fishbowl, не зная об этом ручном вмешательстве, позже (после выполнения шага "Reconcile") отправляет *свою* собственную, корректную транзакцию GJE для создания этого же счета, что приводит к полному хаосу в учете обязательств и активов.

### **2.4 Симптом 4: Разрывы в Учете Дополнительных Расходов (Landed Costs)**

Стоимость запасов в P⁎ (QuickBooks) оказывается систематически заниженной. Это происходит из-за того, что дополнительные расходы, связанные с закупкой (такие как фрахт, таможенные пошлины, страхование 15), не включаются в себестоимость товара (не капитализируются).

Fishbowl имеет специальный модуль "Landed Cost" в процессе "Reconcile" 13, предназначенный именно для *распределения* этих затрат на себестоимость полученных товаров.3 Однако, если счет за фрахт (который часто приходит от отдельного поставщика-экспедитора 15) оплачивается через QB или, что более вероятно, через Bill.com, он *минует* этот обязательный модуль FB. В результате, фрахт ошибочно учитывается как *операционный расход* (Expense) периода, а не как часть *актива* (Inventory Asset), что прямо искажает COGS, оценку запасов и валовую маржинальность.

### **2.5 Симптом 5: Конфликты Рабочего Процесса при Интеграции Bill.com**

Вероятно, ᛭T использует Bill.com для автоматизации кредиторской задолженности (AP). Однако Bill.com "нативно" интегрируется *только* с P⁎ (QuickBooks) 16, но *не* имеет прямой интеграции с ꆜ (Fishbowl).

Это создает катастрофический "треугольник" интеграции. Bill.com отправляет счета (Bills) напрямую в QB. Fishbowl, в свою очередь, *также* отправляет счета (Bills) в QB в рамках своего рабочего процесса.7 Это неизбежно приводит к дублированию счетов, путанице и, что наиболее важно, делает невозможным выполнение 3-сторонней сверки (Three-Part Match: PO vs. Receipt vs. Bill) 10, которая является ядром и главным преимуществом системы FB. Существование сторонних консультаций, предлагающих "2 метода" для их совместной работы 20, лишь подтверждает отсутствие штатной, бесшовной интеграции.

### **2.6 Симптом 6: Системная Нестабильность и Неадекватная Поддержка**

Помимо процедурных сбоев, сама платформа ꆜ (Fishbowl) (on-premise версия) может быть нестабильной. Пользователи в сети характеризуют систему как "суетливую" (fussy).21 Сообщается о проблемах с синхронизацией, когда Fishbowl "меняет конфигурации базы данных", что QuickBooks "не всегда хорошо обрабатывает".22

Наибольшую тревогу вызывают рекомендации, приписываемые представителям поддержки Fishbowl 21:

1. Требование предоставить им *консольный доступ* (console login) к серверу для еженедельных изменений.  
2. Рекомендация переместить сервер FB с "мощного VM-сервера" на "отдельную рабочую станцию" для *улучшения* производительности.  
3. Предложение использовать *внешний USB-диск* в качестве решения для аварийного восстановления (disaster recovery).

Эти рекомендации указывают на архитектурно устаревшее, не масштабируемое и небезопасное приложение, которое плохо работает в современных виртуализированных средах и создает значительные риски для безопасности и непрерывности бизнеса. Эта техническая хрупкость может *провоцировать* процедурные ошибки: когда автоматическая синхронизация GJE из FB в QB дает сбой 22, AP-отдел, не видя счета в QB, решает, что "система сломалась", и *вручную* вводит счет 10, тем самым разрушая данные.

## **Часть 3: Анализ Обоснованности: Диагностика Первопричин (Ответ на Задачу 2)**

Этот раздел связывает "симптомы", описанные в Части 2, с их фундаментальными "болезнями" (первопричинами), опираясь на архитектуру из Части 1.

### **3.1 Таблица 2: Диагностическая Карта: Сопоставление Симптомов и Первопричин**

| Симптом (Проблема) | Первопричина (Обоснование) | Источники |
| :---- | :---- | :---- |
| Расхождения в оценке запасов / COGS 4 | 1. **Нарушение "Единого источника"** (Ручные правки в QB).4 2. **Ошибки сопоставления счетов** (Mapping).8 3. **Ошибки дат** (Back-dating).8 | 4 |
| Отрицательные остатки 10 | 1. **Создание транзакций запасов в QB**.10 2. **Использование "старых" артикулов QB** на счетах.10 3. **Удаление транзакций, созданных FB,** в QB.10 | 10 |
| Удвоение AP и Активов 10 | 1. **Ручное преобразование "Item Receipt" в "Bill"** в QB.10 2. **Непонимание 3-сторонней сверки** в FB.10 | 10 |
| Разрывы в учете Landed Costs 13 | 1. **Ввод счетов за фрахт/пошлины через [Bill.com/QB](https://Bill.com/QB)**, а не через модуль Landed Cost в ꆜ.13 | 13 |
| Конфликт Bill.com 20 | 1. **Отсутствие нативной интеграции** ꆜ <-> Bill.com. 2. **Архитектурный конфликт:** Обе системы пытаются быть "мастером" AP для QB.16 | 16 |

### **3.2 Первопричина 1: Нарушение "Единого Источника Истины" (Source of Truth)**

Это *главная* и наиболее вероятная причина всех проблем. Официальная документация Fishbowl 4 и отчеты независимых консультантов 10 единогласны: **"Making changes in instead of Fishbowl"** (Внесение изменений в QuickBooks вместо Fishbowl) — это причина №1 для расхождений.

Когда пользователь в P⁎ (QuickBooks) *удаляет* GJE, созданный ꆜ, *изменяет* его суммы или *создает* новую транзакцию запасов (например, "Inventory Adjustment" или "Bill" за товар) 10, он создает финансовую "реальность" в QB, которая *не существует* в FB. С этого момента балансы *никогда* не сойдутся, потому что FB не имеет механизма для обнаружения этого ручного вмешательства. Как отмечает один из консультантов, бухгалтерия QB "просто не уважает" Fishbowl 10 и вносит изменения (например, меняет артикул "FB_Item" на старый артикул QB на счете), что и приводит к хаосу, включая отрицательные остатки.10

### **3.3 Первопричина 2: Ошибки Конфигурации и Сопоставления (Mapping)**

При первоначальной настройке 3 пользователь *должен* вручную сопоставить счета (Chart of Accounts) из Fishbowl со счетами в QuickBooks. Ошибки на этом этапе приводят к "тихим", но постоянным расхождениям.

1. Неверное сопоставление по умолчанию 4: Например, счет "Inventory Asset" в Fishbowl сопоставлен *не* со счетом "Inventory Asset" в QuickBooks, а с каким-либо другим.  
2. Неверное сопоставление на уровне артикула 4: Fishbowl позволяет разным артикулам (Parts/Products) сопоставляться с *разными* счетами COGS или Asset в QB. Если ᛭T ожидает, что *все* запасы попадут на один счет в QB, а часть артикулов настроена иначе (например, на "COGS - Retail" и "COGS - Wholesale"), он увидит расхождение в главном счете, хотя технически система отработала "правильно" согласно своей (неверной) настройке.8  
3. **Непонимание служебных счетов:** Неверное сопоставление или непонимание назначения критически важных счетов, таких как "Holding" 7 или "Inventory Adjustment".7

### **3.4 Первопричина 3: Процедурные и Временные Рассогласования**

Эти проблемы связаны не с *тем*, *что* было введено, а *когда* и *как*.

1. **Ошибки при Запуске (Go-Live):** Балансы в QB и FB *не совпадали* в "День 1".4 Если интеграция началась с этого "первородного греха" (например, в QB было запасов на $100,000, а в FB на $95,000), балансы никогда не сойдутся без очищающей проводки.  
2. **Ретроактивное Датирование (Back-Dating):** Пользователь в FB вводит транзакцию (например, приемку товара) задним числом 8, за *уже закрытый и сверенный* финансовый период. Это изменяет GJE за прошлый месяц, что немедленно приводит к расхождению в текущем.  
3. **Пропуск Сверок (Skipped Reconciliation):** ᛭T, вероятно, не проводит *регулярную* (в идеале — ежедневную) сверку балансов FB и QB.4 Консультанты настоятельно рекомендуют автоматизировать ежедневный запуск отчетов FB "Asset Valuation By Account" и QB "Inventory Asset" и сверять их.14 Отсутствие этой процедуры позволяет мелким ошибкам накапливаться, превращаясь через месяцы в неразрешимый ком.

### **3.5 Первопричина 4: Фундаментальное Непонимание Цикла Закупки (Purchasing Workflow) в ꆜ**

Это наиболее технически сложная, но критически важная причина сбоев в AP. Многие пользователи не понимают *двухэтапный* процесс закупки в Fishbowl и ключевую роль "Holding Account" (Иногда называемого "Goods Received Not Invoiced").

**Корректный процесс 3-сторонней сверки:**

1. **Шаг 1: Приемка (Receive).** Когда товар физически поступает на склад, сотрудник склада в ꆜ (Fishbowl) *получает* его в модуле "Receiving".13 В этот самый момент FB автоматически отправляет в P⁎ (QuickBooks) первую GJE для *оприходования* актива 7:  
   * **Дебет:** $Inventory Asset$ (Актив увеличился)  
   * **Кредит:** $Holding Account$ (Обязательство увеличилось)  
   * *На этом этапе "Accounts Payable" (AP) еще не затронут.*  
2. **Шаг 2: Сверка (Reconcile).** Спустя дни или недели, в AP-отдел приходит *счет* (Bill) от поставщика. Сотрудник AP *должен* войти в ꆜ (Fishbowl), открыть модуль "Reconcile" 13, найти соответствующую приемку (Receipt), сверить цены и количество со счетом и PO (выполняя 3-стороннюю сверку 10). Только *после* нажатия кнопки "Finish" в этом модуле, FB отправляет в P⁎ (QuickBooks) вторую GJE:  
   * **Дебет:** $Holding Account$ (Служебное обязательство "Holding" закрывается)  
   * **Кредит:** $Accounts Payable$ (Открывается реальное обязательство "AP" к оплате)

**Точка Сбоя:** Проблема ᛭T почти наверняка заключается в том, что **Шаг 2 никогда не выполняется в Fishbowl**. Вместо этого, AP-отдел получает счет (Bill) и, следуя своему привычному процессу, вводит его *напрямую в Bill.com или QB*. Эта ручная транзакция (например, Дебет $Expense$, Кредит $AP$) *никогда не очищает* "Holding Account" в QB, который был создан на Шаге 1.

**Финансовое Последствие:** На балансе ᛭T *одновременно* висят *два* обязательства за *одну* поставку: [Кредит $Holding Account$] (из Шага 1 в FB) и [Кредит $Accounts Payable$] (из ручного ввода в [Bill.com/QB](https://Bill.com/QB)). Таким образом, ᛭T систематически *удваивает* свои обязательства. "Holding Account" 7 на его балансе, вероятно, представляет собой "черную дыру" из тысяч незакрытых кредитовых записей, которые на самом деле являются уже оплаченными (через ручной ввод) счетами.

## **Часть 4: Глубокий Анализ Сложных Операционных Модулей и Рисков**

Применение вышеописанных первопричин к конкретным, сложным рабочим процессам выявляет неизбежность сбоев в текущей конфигурации.

### **4.1 Анализ: Рабочий Процесс списания Дополнительных Расходов (Landed Costs)**

Fishbowl *может* корректно обрабатывать дополнительные расходы. В модуле "Reconcile" (Шаг 2 выше) есть специальный этап "Landed Cost".13 На этом этапе пользователь AP может *добавить* стоимость фрахта, пошлин и других сборов к общей стоимости приемки. Fishbowl затем *автоматически распределяет* эту дополнительную стоимость (например, $500 за фрахт) пропорционально на себестоимость *каждого* товара в данной приемке.13

**Точка сбоя:** Эта функциональность *требует*, чтобы счет за фрахт (от экспедитора) был введен *внутрь* Fishbowl через модуль "Reconcile".13 Однако, в экосистеме ᛭T (с использованием Bill.com), этот счет почти наверняка вводится *отдельно* в [Bill.com/QB](https://Bill.com/QB) как обычный расход.

**Результат:** Фрахт учитывается как операционный расход (Opex), а не как часть COGS/Актива. Это приводит к трем негативным последствиям:

1. Стоимость активов (Inventory Asset) на балансе *занижена*.  
2. Валовая прибыль (Gross Profit) *искусственно завышена* (так как COGS занижен).  
3. Чистая прибыль (Net Income) *искажена* (так как Opex завышен), что делает анализ маржинальности по продуктам невозможным.

### **4.2 Анализ: Рабочий Процесс AP с Использованием Bill.com**

Как было установлено, это *главный архитектурный конфликт*. ᛭T пытается заставить работать три системы, где ꆜ (Fishbowl) и Bill.com ведут "войну" за право быть "мастером" кредиторской задолженности (AP) для P⁎ (QuickBooks).16

Проблема *абсолютно обоснована*. Эти две системы не предназначены для совместной работы в данном рабочем процессе. Консультанты 20 упоминают "методы" (workarounds), чтобы заставить их работать, но это не интеграция, а ручные процедуры:

1. **Метод 1 (Строгая Сегрегация):** *Все* нетоварные счета (аренда, телефония) вводятся в Bill.com. *Все* товарные счета (материалы, товары) И *все связанные с ними* счета (фрахт, пошлины для Landed Costs) *вручную* вводятся *только* в Fishbowl (через модуль "Reconcile").13 Этот метод требует железной дисциплины от AP-отдела, который должен физически сортировать 100% входящих счетов и решать, в какую систему их вводить.  
2. **Метод 2 (Только Оплата):** (Гипотетически) Bill.com используется *только* для *оплаты* (Bill Payment) счетов, которые были *уже созданы в Fishbowl*, экспортированы в QB, и затем импортированы в Bill.com для оплаты. Это громоздко и полностью ломает основную ценность Bill.com (автоматизацию ввода и утверждения счетов).

Комбинация Landed Costs 13 и Bill.com 16 представляет собой *неразрешимый* конфликт в текущей архитектуре. ᛭T *должен* выбрать: либо отказаться от Bill.com для *всех* товарных и связанных с ними счетов, либо отказаться от *корректного* учета Landed Cost в Fishbowl.

### **4.3 Диагностика и Устранение Отрицательных Остатков**

**Причины (Резюме):** Как указано в 10 и 10, отрицательные остатки — это *симптом* того, что транзакции списания запасов (продажи, корректировки) были созданы в P⁎ (QuickBooks) *в обход* ꆜ (Fishbowl).

Пример 10:

1. FB отгружает товар и создает в QB счет с артикулом "FB_Item". QB корректно списывает GJE: (для "FB_Item").  
2. Бухгалтер в QB, "не уважая" FB 10, *редактирует* этот счет и меняет артикул на "старый" (например, "QB_Part").  
3. Это изменение заставляет QB *дополнительно* создать вторую GJE: (для "QB_Part").  
4. **Итог:** COGS удвоен, а остаток по "QB_Part" уходит в минус, так как он был списан, не будучи оприходованным (приход был на "FB_Item").

**Решение (Процедурное):**

1. **Запретить:** Немедленно, через права доступа в QB, запретить всем пользователям (кроме, возможно, одного контролера) редактировать или создавать транзакции, связанные с запасами.  
2. **Исправление:** Все исправления *должны* производиться *только* в ꆜ (Fishbowl). Для исправления некорректных остатков используются модули "Cycle Count" (Циклическая инвентаризация) 11 или "Add Inventory" (Добавление запасов).24  
3. **Историческое Исправление:** Для исправления *исторических* отрицательных остатков требуется полный аудит (с использованием отчета FB "Inventory Event History report" 25) и, вероятно, крупная "очищающая" корректировка (через "Cost Adjustment" 24 или GJE в QB) для приведения балансов в соответствие.

### **4.4 Оценка Системных и Инфраструктурных Рисков**

Проблемы ᛭T усугубляются (или даже *вызываются*) хрупкой технической базой. Отчет 21 о том, что поддержка FB рекомендует перейти с "мощного VM-сервера" на "отдельную рабочую станцию" и использовать "внешний USB-диск" для бэкапа, является *крайне тревожным*.

Это с высокой вероятностью указывает на то, что on-premise версия ꆜ (Fishbowl) — это старое приложение (возможно, 32-битное), которое "капризно" 21, плохо работает в виртуализированных средах (VM) и не способно утилизировать ресурсы современного сервера. Оно требует постоянного "присмотра" и ручного вмешательства.

Влияние (Причинно-следственная связь):  
Эта техническая хрупкость 21 и сбои синхронизации (когда FB "меняет конфигурации базы данных" 22) приводят к отказам экспорта GJE из FB в QB. Эти сбои провоцируют пользователей на процедурные нарушения:

1. FB-сервер "зависает" 21 или sync-процесс 22 дает сбой.  
2. Экспорт GJE (например, создание Bill в QB после "Reconcile") не проходит.  
3. AP-отдел ждет, но счета в QB нет. Поставщик требует оплаты.  
4. AP-отдел *вынужден* нарушить процедуру и ввести Bill *вручную* через Bill.com, чтобы оплатить поставщику.  
5. Это создает ошибку "удвоения AP/Holding".7

Таким образом, ᛭T не сможет решить свои финансовые проблемы *только* обучением персонала; он должен *сначала* стабилизировать техническую платформу, которая провоцирует эти ошибки.

## **Часть 5: Заключительные Выводы и Стратегические Рекомендации по Восстановлению Целостности**

Для устранения выявленных проблем требуется комплексный, четырехэтапный план действий, сочетающий немедленную изоляцию, финансовую сверку, реинжиниринг процессов и стратегические технологические решения.

### **5.1 Фаза 1: Немедленные Действия (Триаж и Изоляция)**

1. **Остановить Кровотечение (Блокировка P⁎):** Немедленно изменить права доступа в QuickBooks. Запретить всем пользователям, кроме одного "супер-администратора" (вероятно, ᛭T), вносить *любые* изменения или создавать транзакции, затрагивающие счета: $Inventory Asset$, $COGS$, $Accounts Payable$ (для товарных счетов) и $Holding$.  
2. **Изолировать Bill.com:** Немедленно выпустить директиву о *полном прекращении* ввода *всех* товарных счетов и счетов за связанные услуги (фрахт, пошлины, Landed Costs) через Bill.com.  
3. **Установить "Точку Истины":** Выбрать дату и время (например, конец текущего рабочего дня). В этот момент ꆜ (Fishbowl) объявляется единственным "источником истины" для всех данных по запасам.

### **5.2 Фаза 2: Диагностика и Сверка (Reconciliation)**

1. **Запустить Ключевые Отчеты:**  
   * В ꆜ (Fishbowl): Запустить отчет "Asset Valuation By Account".14 Это — *истинная* стоимость запасов.  
   * В P⁎ (QuickBooks): Запустить "Balance Sheet" и получить баланс счета "Inventory Asset".  
   * В P⁎ (QuickBooks): Запустить "Balance Sheet" и получить баланс счета "Holding".7  
2. **Выполнить Очищающую Проводку (GJE):** Рассчитать разницу (Delta) между "Asset Valuation" из FB и "Inventory Asset" из QB. Создать одну (вероятно, очень большую) GJE в QuickBooks, чтобы *привести* баланс QB в полное соответствие с FB.4 Второй стороной этой проводки (корреспондирующим счетом), скорее всего, будет "Inventory Adjustment", "COGS" или "Retained Earnings" (в зависимости от периода ошибки).  
3. **Аудит "Holding Account":** Провести полный аудит счета "Holding" 7 в QB. Все кредитовые записи на этом счете — это *незакрытые* (неотсчитанные) приемки. ᛭T должен вручную сопоставить их с записями AP (оплаченными через Bill.com). Все дубликаты должны быть сторнированы через GJE (Дебет $Holding Account$, Кредит $Accounts Payable$ или $Expense$, в зависимости от того, куда был отнесен ручной Bill).

### **5.3 Фаза 3: Внедрение Строгих Операционных Процедур (SOP)**

1. **Принудительное Переобучение Команд:** Провести *обязательное* обучение для:  
   * **Склада:** По процессу "Receive".13  
   * **Отдела AP:** По процессу "Reconcile" и "Landed Cost" *внутри Fishbowl*.13  
2. **Новый SOP для AP (Сегрегация):**  
   * Все входящие счета от поставщиков физически сортируются.  
   * *Нетоварные* (аренда, утилиты) -> Вводятся, как и раньше, в Bill.com.  
   * *Товарные* (материалы, товары) И *Связанные* (фрахт, пошлины) -> Передаются "FB AP-специалисту", который вводит их *только* через модуль ꆜ (Fishbowl) "Reconcile".13  
3. **Новый SOP для Сверки (Ежедневно):** Внедрить *ежедневную* процедуру сверки.4 Каждое утро контролер должен запускать отчеты FB "Asset Valuation By Account" и QB "Inventory Asset". Балансы должны совпадать до цента. Любые расхождения должны быть найдены и устранены *в течение 24 часов*.

### **5.4 Фаза 4: Стратегические Решения**

1. **Решить Проблему Инфраструктуры:** Немедленно пересмотреть инфраструктуру развертывания on-premise FB.21 ᛭T должен инвестировать в выделенный, правильно настроенный сервер (физический или VM) с *профессиональной* системой резервного копирования (не USB-диск) и планом аварийного восстановления.  
2. **Рассмотреть Миграцию в Облако:** Оценить переход на Fishbowl Online.5 Это, вероятно, устранит корень проблем нестабильности сервера 21 и сбоев синхронизации 22, так как интеграция с QuickBooks Online (QBO) является более "нативной" и поддерживаемой.6  
3. **Привлечь Внешних Экспертов:** Признать, что команда не справляется.12 Нанять сертифицированного консультанта по Fishbowl 21 для проведения аудита, контроля над Фазой 2 (Сверка) и помощи во внедрении Фазы 3 (Обучение и SOPs). Текущие проблемы носят системный характер и слишком глубоки, чтобы решать их "на лету" силами неподготовленного персонала.
 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1
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