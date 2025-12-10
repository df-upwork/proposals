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
Сегодня 2025-11-09.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021986799195969079068

## 2.2. Title
Pharma Domain with DataBricks and Snowflake Expertise for Assessment


## 2.3. Description
`PD` ≔ 
```text
We are seeking an expert in the Pharma domain with extensive experience in DataBricks and Snowflake to conduct a comprehensive assessment project. 
The project involves analyzing current system usage, assessing migration feasibility, comparing data processing features, pricing, and evaluating integration platforms.

# Deliverables
- Analyze current system usage and assess migration feasibility
- Compare data processing features of Snowflake and DataBricks
- Evaluate pricing and cost structures
- Assess integration platforms like Oracle Boomi, Mulesoft, Azure Data Factory
```

## 2.5. Questions
### 2.5.1.
Analyze current system usage and assess migration feasibility

### 2.5.2.
Compare data processing features of Snowflake and DataBricks

### 2.5.3.
Evaluate pricing and cost structures

### 2.5.4.
Assess integration platforms like Oracle Boomi, Mulesoft, Azure Data Factory

# 5. Информация о `ꆜ`
## 5.1. Местоположение
USA
Moorpark

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Apr 16, 2024
### 5.3.2. Hire rate (%)
46
### 5.3.3. Количество опубликованных проектов (jobs posted)
11
### 5.3.4. Total spent (USD)
14K
### 5.3.5. Количество оплаченных часов в почасовых проектах
441
### 5.3.6. Средняя почасовая ставка (USD)
27.86

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

## 6.1.1. URL
https://www.upwork.com/jobs/~021964047431815561436

## 6.1.2. Title
Senior Salesforce QA Lead – Pharma

## 6.1.3. Description
`P1D` ≔ 
```text
We are seeking a highly experienced QA Lead with strong Salesforce testing expertise, pharma domain knowledge, and validation background. 
This role requires leadership in defining strategy, guiding a QA team, executing and reviewing test scripts, and ensuring compliance. 
Immediate availability with at least 4 hrs overlap during India business hours is required. 

# Deliverables
- Define test strategy, plans, and quality metrics for Salesforce–pharma projects.
- Lead QA team, provide mentoring, review and execute scripts, validate deliverables.
- Oversee functional, regression, UAT, UI, integration, data, migration, configuration, and compliance testing.
- Manage SIT/UAT/Pre-Production testing cycles, ensure readiness.
- Build test documentation aligned to pharma validation (CSV, 21 CFR Part 11, Annex 11).
- Collaborate with dev and business teams for defect triage and release readiness.
- Monitor progress, report metrics, and escalate issues promptly.
- Drive scenario-based, risk-based testing, and quality improvements.
- Act as QA point of contact for stakeholders and auditors.

#
- Have you worked on pharma/life sciences projects with GxP, CSV, or 21 CFR Part 11 requirements?
- Can you work over weekend hours of India ?
- Availability of working in India business hours
- Describe your recent experience with similar projects
```

## 6.1.4. Publication Date
2 months ago

## 6.1.5. Payment Terms (USD) 
### 6.1.5.1. Expected by `ꆜ`  
16-24 Hourly
### 6.1.5.2. Actual
133 hrs @ $20.00/hr
Billed: $2,384.99

## 6.1.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.1.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
< 1 month

## 6.1.8. Contractor Location (expected by `ꆜ`)
India

## 6.2. `P2⁎`

## 6.2.1. URL
https://www.upwork.com/jobs/~021964050017726666505

## 6.2.3. Title
Salesforce Tech lead

## 6.2.3. Description
`P2D` ≔ 
```text
# Senior Technical Lead – Salesforce (SFDC)

We are seeking a highly skilled Senior Salesforce Technical Lead to take ownership of an existing Salesforce-based application developed earlier this year. 
This role requires advanced Salesforce development expertise with the ability to design, develop, and guide delivery of scalable solutions, while overseeing enhancements, bug fixes, and integration with enterprise systems.

# Responsibilities:
- Lead design and development of Apex classes, triggers, batch jobs, APIs, and integrations.
- Build, review, and optimize Lightning Web Components (LWC), Flow automations, and workflow logic.
- Resolve defects from prior releases, ensuring code quality, performance, and compliance with governor limits.
- Provide technical leadership, code reviews, and mentorship to developers.
- Collaborate with business teams to translate requirements into robust solutions.
- Partner with DevOps for CI/CD pipelines, release management, and environment strategy.

# Qualifications:
- 7+ years Salesforce development (Apex, LWC, APIs, integrations).
- Proven experience as Technical Lead with strong mentoring and code review skills.
- Expertise in workflow automation, security, and performance optimization.
- Experience with CI/CD, Git, and Salesforce DevOps practices.
- Salesforce certifications preferred.

# Responsibilities
- Development of Apex classes, triggers, batch jobs, and APIs to extend Salesforce functionality.
- Build and optimize Lightning Web Components (LWC) and Flow automations to streamline complex business processes.
- Troubleshoot and optimize code for performance, security, and compliance with governor limits.
- Partner with DevOps teams to support CI/CD pipelines and release management.

# Deliverables
- New Feature Development
- Design, develop, and deploy new Salesforce functionalities (Apex, LWC, Flow automation) based on evolving business requirements.
- Bug Fixes & Enhancements
- Analyze, troubleshoot, and resolve defects from past releases while ensuring performance optimization and code stability.
- Technical Leadership & Code Reviews
- Provide guidance to junior developers, enforce coding standards, conduct peer reviews, and mentor the team on best practices.
- Integration & API Development
- Deliver secure, scalable integrations with enterprise applications and external systems via REST/SOAP APIs.
- DevOps & Release Management
- Support CI/CD pipelines, ensure smooth deployments across environments (SIT, UAT, Production), and maintain release governance.

#
- State you experience in handling complex customized code in SFDC
- Are you available during India Business hours ?
- Are you available during the weekend ?
- Describe your recent experience with similar projects
- Please list any certifications related to this project
```

## 6.2.4. Publication Date
2 months ago

## 6.2.5. Payment Terms  (USD) 
### 6.2.5.1. Expected by `ꆜ`
15-30 Hourly
### 6.2.5.2. Actual 
145 hrs @ $30.00/hr
Billed: $4,561.99

## 6.2.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.2.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
< 1 month

## 6.2.8. Contractor Location (expected by `ꆜ`)
India

## 6.3. `P3⁎`

## 6.3.1. URL
https://www.upwork.com/jobs/~021929638246113572976

## 6.3.2. Title
Tableau Advanced Analytics Consultant – Pharma Commercial Domain

## 6.3.3. Description
`P3D` ≔ 
```text
Job Title: Tableau Advanced Analytics Consultant – Pharma Commercial Domain
Job Requirements
• Pharma Commercial Domain Expertise: commercial pharma operations, including sales analytics, marketing performance, field force effectiveness, and patient access strategies.
• Advanced Tableau Analytics Proficiency: hands-on expertise with Tableau Next, Einstein Analytics (Tableau CRM), and Pulse dashboards, including AI-driven analytics, predictive modeling, natural language querying, and real-time monitoring.
• Self-Service Analytics Design & Governance: Ability to assess, optimize, and implement scalable self-service analytics frameworks, ensuring best practices for user enablement and data governance.
• Salesforce Integration Experience: Strong background integrating Tableau Analytics with Salesforce platforms (Einstein, Pulse, Next) for unified, end-to-end analytics solutions.
• Enablement & Adoption Leadership: Experience developing enablement plans, conducting user training, and establishing sustainable analytics governance for long-term adoption.
Role Responsibilities:
• Review the existing Tableau self-service design and framework.
• Recommend and implement enhancements aligned with best practices for scalable self-service analytics.
• Collaborate with stakeholders to define PoC use cases and success criteria.
• Support integration or alignment with Salesforce Einstein or Pulse if required.
```

## 6.3.4. Publication Date
2 quarters ago

## 6.3.5. Payment Terms (USD) 
### 6.3.5.1. Expected by `ꆜ`  
45-75 Hourly
### 6.3.5.2. Actual
23 hrs @ $71.25/hr
Billed: $1,730.70

## 6.3.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.3.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

## 6.3.8. Contractor Location (expected by `ꆜ`)
New Jersey

## 6.4. `P4⁎`

## 6.4.1. URL
https://www.upwork.com/jobs/~021960506304541752822

## 6.4.2. Title
Salesforce Advance level developer


## 6.4.3. Description
`P4D` ≔ 
```text
This is an existing Salesforce based application developed earlier this year. Advanced level salesforce coding skill needed for 1) Development of New functionalities requested by business 2) Bug fixes of past release.  .

We are seeking a highly skilled Senior Salesforce Developer with expertise in Apex, Lightning, and advanced workflow automation. This role will drive the design and development of scalable Salesforce solutions, ensuring seamless integration with enterprise systems and delivering high-value business outcomes.
Responsibilities
• Development of Apex classes, triggers, batch jobs, and APIs to extend Salesforce functionality.
• Build and optimize Lightning Web Components (LWC) and Flow automations to streamline complex business processes.
• Troubleshoot and optimize code for performance, security, and compliance with governor limits.
• Partner with DevOps teams to support CI/CD pipelines and release management.

- State you experience in handling complex customized code in SFDC
- Describe your recent experience with similar projects
= Please list any certifications related to this project
```

## 6.4.4. Publication Date
3 months ago

## 6.4.5. Payment Terms (USD) 
### 6.4.5.1. Expected by `ꆜ`  
20-35 Hourly
### 6.4.5.2. Actual
103 hrs @ $27.00/hr
Billed: $2,925.04

## 6.4.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.4.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
1-3 months

## 6.4.8. Contractor Location (expected by `ꆜ`)
India

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`, `P4⁎`, `P5⁎`, `P6⁎`, `P7⁎`, `P8⁎`}

## 7.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 7.3.
`Pi` : `Ps`


# 8.
## 8.1.
`Q1⁎` ≔ (Вопрос `ꆜ` §2.5.1)

## 8.2.
`Q2⁎` ≔ (Вопрос `ꆜ` §2.5.2)

## 8.3.
`Q3⁎` ≔ (Вопрос `ꆜ` §2.5.3)

## 8.4.
`Q4⁎` ≔ (Вопрос `ꆜ` §2.5.4)

 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1. `᛭T`
1) Выяви все проблемы, которые беспокоят `ꆜ` в `P⁎`.
2) Проанализируй обоснованность каждой из выявленных проблем.

# 2. Источники информации
В своём анализе используй авторитетные источники информации на английском языке.

# 3. Требования к ответу
Свой ответ дай на русском языке. 
~~~~~~