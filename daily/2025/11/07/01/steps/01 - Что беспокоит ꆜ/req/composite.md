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
Сегодня 2025-11-07.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021986564640463298853

## 2.2. Title
Compliance & Secure Data Migration Consultant

## 2.3. Description
`PD` ≔ 
```text
We are seeking an experienced consultant to guide the migration of PII from Stripe and Buttondown to AWS, ensuring compliance with GDPR, CCPA, and PCI DSS. 
The role involves designing secure AWS architecture and creating operational policies for data rights and breach response.

# Deliverables
- Design secure AWS architecture
- Create operational policies for data rights
- Ensure compliance with GDPR, CCPA, and PCI DSS
- Develop implementation roadmap
- Review DPA
```

## 2.4. Tags
Amazon Web Services
Amazon EC
Stripe
Buttondown
GDPR Complianc
Data Privacy
Cloud Security
Compliance Consulting
PCI DSS
Amazon S3
Amazon RDS
AWS KMS
AWS CloudTrail
AWS Identity and Access Management
Data Protection Impact Assessment
CCPA Compliance
Risk Assessment
Information Security Management
AWS
Stripe
Buttondown
CloudTrail
KMS
GDPR Toolkit

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
Ann Arbot

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
Education

### 5.2.2. Количество сотрудников
10-99 people

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Feb 24, 2015
### 5.3.2. Hire rate (%)
100
### 5.3.3. Количество опубликованных проектов (jobs posted)
136 
### 5.3.4. Total spent (USD)
1.5M
### 5.3.5. Количество оплаченных часов в почасовых проектах
34947 
### 5.3.6. Средняя почасовая ставка (USD)
30.11

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

## 6.1.1. URL
https://www.upwork.com/jobs/~01032f366456cd071e

## 6.1.2. Title
Seeking Virtual Content Assistant

## 6.1.3. Description
`P1D` ≔ 
```text
The Really Useful Information Company (TRUiC) is a hub of entrepreneurial resources and tools designed to help business owners succeed. 
We’re looking for a virtual assistant to provide support on a variety of content-related tasks for our authority websites, https://howtostartanllc.com/ and https://startupsavant.com/.

Duties/Responsibilities:

Content Management and Workflow
-Proofread, format, and prep written content to send over to our data and optimization team
-Content curation; generate lists and/or spreadsheets of credible, trending business/startup resources as needed

Online Research and Data Entry
-Research on topics for website articles, videos, social media posts, etc.
-Study competitors and pitch new ideas for content we’re missing; create reports/presentations on your findings
-Keyword + SEO research for new and/or existing content
-Create and enter data into spreadsheets as needed

Social Media
-Prep social media posts for Twitter and LinkedIn
-Pitch new ideas for social media posts on any platform depending on trending topics
-Encouraged, but not required: engage with the TRUiC brand by commenting on our website articles, and/or watching, liking, and/or commenting on our YouTube videos

Cold Email Outreach
-Build email contact lists as needed
-Create email outreach templates for connecting with journalists, startup founders, etc.

Required Skills:
-Excellent communication skills
-Fluent in English (spoken and written)
-Excellent time management and organizational skills
-Excellent follow-through on projects
-Comfortable learning new tools/technologies and skills
-Creativity and flexibility

Be Open to Learning:
-Content management workflow
-Content brief creation
-Online content writing
-Search engine optimization (SEO)

This is a flexible role; expect to spend between 10 and 20 hours per week on the above duties and other related content tasks as they come up. I will train anyone I work with as well as provide helpful training materials and documentation.

Please only apply if you are open to learning and working within the processes, guidelines, and best practices used by our company. We have a few different websites that projects will flow from, but you will work primarily with howtostartanllc.com and startupsavant.com. You can learn more about our company and sites here: https://truic.com/about-us.

To apply, please submit your resume and answer the screening questions.

Thank you for your application! I look forward to speaking with you.
```

## 6.1.4. Publication Date
3 years ago

## 6.1.5. Payment Terms (USD) 
### 6.1.5.1. Expected by `ꆜ`  
15-20 Hourly 
### 6.1.5.2. Actual
221 hrs @ $18.00/hr
Billed: $4,086.05

## 6.1.6. Contractor Level (expected by `ꆜ`)
Entry level

## 6.1.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
3-6 months

## 6.1.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.2. `P2⁎`

## 6.2.1. URL
https://www.upwork.com/jobs/~01e93cc6457baf83b7

## 6.2.3. Title
Social media & podcast video editor

## 6.2.3. Description
`P2D` ≔ 
```text
We are looking for a video editor with experience in long form and vertical video editing to help with promotional videos for our podcast, Startup Savant.

Tasks include:
- Editing provided podcast clips to more snappy and engaging for TikTok, IG, and YouTube shorts
- Editing videos with our podcast host, video clips and script provided
- Editing full-length podcast interviews for YouTube, provided footage via Riverside.fm as well as thumbnails, photo shop templates, and mastered audio

Please visit https://www.youtube.com/@StartupSavantPodcast/ for examples of both vertical and full-length podcast videos.

To learn more about our show: https://startupsavant.com/startup-savant-podcast
```

## 6.2.4. Publication Date
2 years ago

## 6.2.5. Payment Terms  (USD) 
### 6.2.5.1. Expected by `ꆜ`
18-20 Hourly
### 6.2.5.2. Actual 
420 hrs @ $20.00/hr
Billed: $8,827.00

## 6.2.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.2.7. Duration (expected by `ꆜ`)

3-6 months

## 6.2.8. Contractor Location (expected by `ꆜ`)
Not specified

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`, `P4⁎`, `P5⁎`, `P6⁎`, `P7⁎`, `P8⁎`}

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
The Really Useful Information Company (TRUiC) is a hub of entrepreneurial resources and tools designed to help business owners succeed. 
~~~
```

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
guide the migration of PII from Stripe and Buttondown to AWS, ensuring compliance with GDPR, CCPA, and PCI DSS
~~~
```

# 9.
## 9.1.
`T1⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Design secure AWS architecture
~~~
```

## 9.2.
`T2⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Create operational policies for data rights
~~~
```

## 9.3.
`T3⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Ensure compliance with GDPR, CCPA, and PCI DSS
~~~
```

## 9.4.
`T4⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Develop implementation roadmap
~~~
```

## 9.5.
`T5⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Review DPA
~~~
```

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