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
https://www.upwork.com/jobs/~021966093242370912143

## 2.2. Title
Guidance to file Turkish A1/Certificate of coverage social security applications

## 2.3. Description
`PD` ≔ 
```text
We are a UK-based company that will be acting as an authorized agent to file A1/Certificate of Coverage social security applications on behalf of our clients in Turkey. 
To ensure that these applications are managed in full compliance with Turkish requirements, we are seeking a knowledgeable and experienced professional to help us formalize the entire procedure. 
The selected individual will be responsible for preparing a clear, comprehensive, step-by-step guide that our team can follow to achieve both compliance and administrative efficiency.

Key Deliverables

Process Guide: A detailed, step-by-step formal procedure for submitting A1/Certificate of Coverage social security forms in Turkey on behalf of our clients. This should be specifically designed for a UK-based company.

Document Checklist: A comprehensive list of all required documents and information (e.g., employee’s ID, sworn declaration, employment contract) to be collected for each application.

Authority Confirmation: Identification of the official Turkish authority responsible for handling A1 forms, along with their direct contact details for submission.

Submission Method: Clarification on the submission process—whether it is physical, email-based, or through an online portal accessible to foreign entities.

Best Practices & Challenges: An outline of common administrative hurdles, potential pitfalls, and recommended best practices to avoid delays or non-compliance.
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United Kingdom
London

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
Individual client

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Jul 25, 2020
### 5.3.2. Hire rate (%)
53
### 5.3.3. Количество опубликованных проектов (jobs posted)
42 
### 5.3.4. Total spent (USD)
$12K
### 5.3.5. Количество оплаченных часов в почасовых проектах
292
### 5.3.6. Средняя почасовая ставка (USD)
33.21

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

## 6.1.1. URL
https://www.upwork.com/jobs/~021960307715729761874

## 6.1.2. Title
Local representative for Norway

## 6.1.3. Description
`P1D` ≔ 
```text
Who we are: We are a global mobility compliance company based in the UK. We already have a Norwegian NUF and need help agreeing a clear, repeatable approach with NAV for obtaining A1 certificates for employees of our Norwegian corporate clients who work temporarily outside Norway.

What we need:
A practical Norwegian‑speaking coordinator (paralegal/admin/HR/payroll background welcome) to speak with NAV (Medlemskap og avgift) and Altinn support, confirm the exact routes available to an agent (with company POA). This is a short discovery/setup engagement with the option for ongoing support.

Core tasks:
1.Call NAV to confirm when an agent may file A1:
- What’s possible digitally via Altinn (with delegated rights to a named individual)?
- When must we use the postal process?

2. Power of Attorney (POA) requirements (who signs, scope, any Norwegian address requirement).

3. Call Altinn support to confirm which role(s) and delegation steps are required to submit A1 for a company, and whether a D‑number is sufficient.

4. Create a concise process map + checklist for two routes:
(a) Digital via Altinn (roles, step‑by‑step, screens, required docs).
(b) Postal (forms, where to send, cover letter, required docs, tracking).

5. Draft templates (Norwegian + English): POA text, employer confirmation letter, cover letter, email scripts to NAV, and internal checklist.

6. (Optional, if permitted) Test‑run one non‑binding application or fill the form to the last step to validate the workflow.

Must‑haves:
1. Fluent Norwegian + English; confident calling NAV.
2. Experience with NAV/Altinn processes (A1, membership, or similar).
3. Norwegian ID or D‑number with eID (BankID/MinID) if digital delegation is required.

When you apply, please tell us
a. Do you have a Norwegian ID or D‑number and can you accept Altinn delegation?
b. Have you dealt with NAV A1 or Altinn roles before? Briefly explain your approach.
c. Your proposed fee (hourly and/or fixed price for the deliverables above).
d. Your earliest start and availability this week.
```

## 6.1.4. Publication Date
2 weeks ago

## 6.1.5. Payment Terms
### 6.1.5.1. Expected by `ꆜ`  
$23-$100 (Hourly)
### 6.1.5.2. Actual
2 hrs @ $100.00/hr

## 6.1.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.1.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
1-3 months

## 6.1.8. Contractor Location (expected by `ꆜ`)
Norway

## 6.2. `P2⁎`

## 6.2.1. URL
https://www.upwork.com/jobs/~021947596906909127666

## 6.2.3. Title
Singapore Work-Pass Filing – 5-hour feasibility consult (Licensed EA or Immigration Professional)

## 6.2.3. Description
`P2D` ≔ 
```text
We need a quick, hands-on test to confirm that we can file Work Permit and Short-Term Visit Pass (business-visa) applications through the MOM portal. If the test runs smoothly, we’ll explore a longer-term partnership.

Your help (max 5 billable hours)

Time Task
1 h Screen-share session – Log in with your Singpass/CorpPass and show the step-by-step flow for starting a new application.
1 h Checklist – Give us a full list of the data fields and supporting documents required for both passes.
1 h Dummy submission – Using test data you provide, walk through one sample application while our engineer observes. (We’ll withdraw it right after.)
1 h Debrief call – Answer our questions about compliance and typical bottlenecks; highlight anything we should watch out for when we automate the process on our side.
≈1 h buffer Extra time for small follow-ups or clarifications.

What we need from you

✅ A valid Singpass that is linked to your licensed Employment Agency (please state your EA licence number).

✅ Recent experience — at least 50 MOM work-pass filings in the past year.

Deliverables

A short video or call recording of the walk-through.

The data-field & document checklist (Excel or CSV is fine).

A brief written summary of key compliance points.

Timeline

Complete everything within 7 calendar days of contract start.

Why this matters

This five-hour pilot lets us verify the steps with a real EA account before we invest further. If it works, we’ll discuss a formal, ongoing engagement.

(No need to know automation tools — our team handles all technical integration.)
```

## 6.2.4. Publication Date
2 months ago

## 6.2.5. Payment Terms
### 6.2.5.1. Expected by `ꆜ`  
$10 - $40 (Hourly)
### 6.2.5.2. Actual
4 hrs @ $50.00/hr
Billed: $198.97

## 6.2.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.2.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

## 6.2.8. Contractor Location (expected by `ꆜ`)
Singapore

## 6.3. `P3⁎`

## 6.3.1. URL
https://www.upwork.com/jobs/~021909239818734616716

## 6.3.2. Title
local representative in Portugal

## 6.3.3. Description
`P3D` ≔ 
```text
I am seeking a local representative of our UK company in Portugal who would be able to liaise with the local Portuguese authorities on our behalf, receive letters, and discuss things with them in Portuguese.

We are a UK base technology company which helps all the organisations file Social Security certificates in Seg-Social government portal.
```

## 6.3.4. Publication Date
last quarter

## 6.3.5. Payment Terms
### 6.3.5.1. Expected by `ꆜ`  
$11-$40 Hourly)
### 6.3.5.2. Actual
Fixed-price

## 6.3.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.3.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
6+ months

## 6.3.8. Contractor Location (expected by `ꆜ`)
Portugal

## 6.4. `P4⁎`

## 6.4.1. URL
https://www.upwork.com/jobs/~021889751180431763711

## 6.4.2. Title
Spanish Tax Advisor for A1 Certificate Filing

## 6.4.3. Description
`P4D` ≔ 
```text
We are seeking an experienced Spanish tax advisor who has direct access to the system for filing Spanish A1 certificates. The ideal candidate will have a strong understanding of Spanish tax regulations and the specific requirements for A1 social security certificates.

Requirements
1. Assist our clients in navigating the filing process efficiently and accurately.
2. Assist us in obtaining a NIF and  FMNT Digital Certificate from the Spanish tax agency ( AEAT) so we can file these ourselves in future
```

## 6.4.4. Publication Date
2 quarters ago

## 6.4.5. Payment Terms
### 6.4.5.1. Expected by `ꆜ`  
$50-$120 (Hourly )
### 6.4.5.2. Actual
Feb 2025 - Present
6 hrs @ $50.00/hr

## 6.4.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.4.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
1-3 months

## 6.4.8. Contractor Location (expected by `ꆜ`)
Spain

## 6.5. `P5⁎`

## 6.5.1. URL
https://www.upwork.com/jobs/~021883841142854498972

## 6.5.2. Title
Cyber Security Specialist for Client Security Questionnaires

## 6.5.3. Description
`P5D` ≔ 
```text
We are a dynamic B2B start-up seeking an experienced cyber security specialist to help us navigate and respond to security questionnaires from our clients. Your expertise will ensure that our responses accurately reflect our security practices and meet client requirements. The ideal candidate will have a strong understanding of cyber security principles and experience in handling client security inquiries. Join us in strengthening our client trust and security posture.
```

## 6.5.4. Publication Date
2 quarters ago

## 6.5.5. Payment Terms (USD) 
### 6.5.5.1. Expected by `ꆜ`  
20-50 (Hourly)
### 6.5.5.2. Actual
31 hrs @ $60.00/hr
Billed: $1,979.92

## 6.5.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.5.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
1-3 months

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
## 8.1.
`С⁎` ≔ 
```
Компания STUB, о которой `ꆜ` пишет в `Ps`:
~~~
We are a UK-based company that will be acting as an authorized agent to file A1/Certificate of Coverage social security applications on behalf of our clients
~~~
```

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`G𐏐` ≔ (Стратегическая цель `С⁎`, для достижения которой она хочет выполнить `P⁎`)



 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1. `᛭T`
## 1.1.
Проанализируй `G𐏐`:
1) Кому намерена помогать `С⁎`: британским или туецким работодателям?
2) В какую страну будут командированы сотрудники работодателя (клиента `С⁎`): в Великобританию или Турцию?
3) От уплаты взносов в систему социального обеспечения какой страны `С⁎` намерена освобождать командированных сотрудников: Великобритании или Турции?
## 1.2.
Как ты видишь, у всех вопросов пункта 1.1 есть 2 варианта ответа.
Для каждого из вопросов действуй пошагово:
1) Внимательно проанализируй оба варианта.
2) Укажи доводы «за» каждый вариант с оценкой правдоподобности от 0 до 100.
3) Укажи доводы «против» каждый варианта с оценкой правдоподобности от 0 до 100.
4) Вынеси итоговый вердикт с оценкой правдоподобности от 0 до 100.

# 2. Источники информации
## 4.1.
В своём анализе используй в первую очередь официальные юридические источники информации:
1) на турецком языке: касающиеся турецкого законодательства
2) на английском языке: касающиеся законодательства других стран и международного
## 4.2.
В своём ответе сошлись на конкретные пункты конкретных нормативных актов, с конкретными цитатами из них.
Цитаты давай как в оригинальном варианте (как они записаны в нормативном акте), так и в своём переводе.

# 3. Требования к ответу
Свой ответ дай на русском языке. 
~~~~~~