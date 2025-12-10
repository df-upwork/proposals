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
Сегодня 2025-11-06.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021985762335391313624

## 2.2. Title
Automate Dynamic Content in Adobe Illustrator (XML or Data-Linked Workflow)

## 2.3. Description
`PD` ≔ 
```text
# Objective
We need to build an automated link between our packaging artwork in Adobe Illustrator and an external XML (or similar structured data) source, so that product information such as ingredients, nutrition panels, names, and claims can be updated automatically, without manual text edits.

The final outcome should allow:
- Dynamic content updates pulled from a single data source (XML, CSV, or API).
- Style consistency (font, size, color) retained when data changes.
- Error handling for overflow and missing fields.
- Templates ready for print with minimal manual intervention.

We’re open to any proven method that achieves this goal, whether it’s using Esko Dynamic Content, ExtendScript (Illustrator scripting), or another data-driven automation workflow.

# Key Requirements
- Map key text fields (product name, ingredients, nutrition info, claims, flavour, usage) to a live data source.
- Support live data refresh or easy re-linking to an XML/CSV feed.
- Maintain Illustrator text styles and layout during updates.
- Handle overflow or missing data gracefully.
- Deliver documentation so our design team can update and reuse templates.

# Deliverables
- Working Illustrator Template (.ai / .ait)
- Dynamic text fields linked to XML/CSV data
- Tested with a sample feed
- Documentation (2–3 pages)
- How to link/update data
- Common troubleshooting and error handling

# Optional
- Script or automation file (if Esko isn’t used)
- Recommendations for best-fit workflow for long-term scalability

# What We’ll Provide
- Sample packaging Illustrator file (e.g. PERFORM Vanilla 936g pouch)
- Sample XML/CSV structure with real content
- Brand fonts, styles, and layout guidelines

# Ideal Candidate

We’re looking for someone who can design smart, scalable automation for packaging workflows.
Relevant backgrounds could include:
- Illustrator scripting / ExtendScript / UXP automation
- Variable data or data-driven design workflows (InDesign, Illustrator, Esko, etc.)
- XML / JSON / API data integration
- Workflow documentation and QA
```

## 2.4. Tags
API Integration
XML
Scripting
API
Automation

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United Kingdom
Winscombe

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
Health & Fitness

### 5.2.2. Количество сотрудников
100-1,000 people

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Jan 29, 2022
### 5.3.2. Hire rate (%)
65
### 5.3.3. Количество опубликованных проектов (jobs posted)
37
### 5.3.4. Total spent (USD)
$28K
### 5.3.5. Количество оплаченных часов в почасовых проектах
660
### 5.3.6. Средняя почасовая ставка (USD)
29.25

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

## 6.1.1. URL
https://www.upwork.com/jobs/~021985764820062073322

## 6.1.2. Title
Print Designer – Packaging Artwork & Prepress (FMCG / Supplements)

## 6.1.3. Description
`P1D` ≔ 
```text
Objective
We’re looking for an experienced Print Designer with strong knowledge of packaging artwork and prepress workflows.
Your role will be to manage packaging artwork changes, ensure print accuracy, and liaise directly with printers to deliver production-ready files on time.

This position requires someone with meticulous attention to detail, excellent communication, and a deep understanding of FMCG or supplement packaging standards.

Key Responsibilities

- Artwork Updates & Version Control
  Receive packaging change requests (ingredient updates, claims, legal text, etc.) and apply them accurately across multiple SKUs.

- Maintain naming conventions and versioning discipline.

- Print-Ready File Preparation
  Check all dielines, bleed, overprint, and separations.
  Ensure all images, fonts, and colour profiles (Pantone/CMYK) are embedded and correct before release.

- Export and package final files for print vendors in required formats (.ai, .pdf, .zip).

- Printer Liaison & Technical Support
  Communicate directly with print partners to clarify technical specifications, spot potential issues early, and troubleshoot artwork queries.

- Ensure all print feedback is incorporated efficiently.

Quality & Consistency
- Ensure packaging adheres to brand guidelines and product hierarchies.
- Manage consistency across variants (flavour, size, language).

Turnaround Speed & Accuracy
- Deliver updates quickly while maintaining 100% accuracy across multiple SKUs.
- Work in an organised, system-driven way to avoid human error.


What You’ll Be Working On
* Supplement & nutrition product packaging (pouches, cartons, labels)
* Multi-language layouts (EN / DE / FR / IT)
* CMYK & Pantone workflows for digital and litho printing
* Coordination with both internal designers and external printers

Deliverables
1. Updated print-ready packaging files (.ai, .pdf)
2. Version control tracker (file naming + changelog)
3. Clear communication logs/responses to printer queries

Ideal Experience
* 3+ years working in **FMCG, supplements, or food packaging**
* Expert in **Adobe Illustrator** and **Adobe Acrobat for prepress checks**
* Strong grasp of **dielines, print finishes, and color management**
* Familiar with preflight checks**, or **print proofing systems** (a plus, not essential)
* Experience managing multiple SKU variants efficiently
* Confidence working directly with print suppliers

Key Skills
* Packaging Artwork & Prepress
* Adobe Illustrator (Advanced)
* Print Production
* Colour Management (CMYK, Pantone)
* File Setup & Delivery
* Version Control
* Attention to Detail
* Communication with Print Vendors

Project Type
* Ongoing or recurring work (packaging updates across multiple product lines)
* Remote collaboration with structured task handovers
```

## 6.1.4. Publication Date
2 days ago

## 6.1.5. Payment Terms (USD) 
### 6.1.5.1. Expected by `ꆜ`  
20-40 Hourly
### 6.1.5.2. Actual
неизвестно

## 6.1.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.1.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
3-6 months

## 6.1.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.2. `P2⁎`

## 6.2.1. URL
https://www.upwork.com/jobs/~021958907002611761467

## 6.2.3. Title
Landing Page Designer with Strong Figma Expertise

## 6.2.3. Description
`P2D` ≔ 
```text
Job Title: Landing Page Designer with Strong Figma Expertise

Overview
We’re looking for a highly skilled designer who specializes in creating high-converting landing pages. This role is perfect for someone with deep experience in Figma, a strong eye for design, and a track record of building landing pages that balance aesthetics with performance.

What You’ll Do

- Design landing pages in Figma that are visually engaging and conversion-focused

- Translate brand identity and messaging into clean, modern layouts

- Work with existing brand guidelines but bring fresh creative ideas

- Design responsive experiences (desktop + mobile)

- Collaborate with our team to refine user journeys and ensure designs support business goals

Requirements

- Expert in Figma with proven work in landing page design

- Portfolio that demonstrates strong UX/UI principles (must include landing pages)

- Understanding of conversion rate optimization (CRO) fundamentals

- Ability to balance creativity with clarity and simplicity

- Strong communication skills and ability to explain design decisions

Nice-to-Haves

- Experience working with wellness, lifestyle, or e-commerce brands

- Knowledge of how design translates into development (basic HTML/CSS understanding a plus)

What We’re Looking For
We don’t want cookie-cutter templates, we want designs rooted in clarity, usability, and brand personality. The right designer will understand how to guide users with layout, hierarchy, and storytelling, not just make things look pretty.

How to Apply

- Share your portfolio with at least 3 live landing pages you’ve designed

- Briefly describe your design process when creating a new landing page
```

## 6.2.4. Publication Date
3 months ago

## 6.2.5. Payment Terms  (USD) 
### 6.2.5.1. Expected by `ꆜ`
25-47 Hourly
### 6.2.5.2. Actual 
15 hrs @ $70.00/hr
Billed: $1,052.34

## 6.2.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.2.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
6+ months

## 6.2.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.3. `P3⁎`

## 6.3.1. URL
https://www.upwork.com/jobs/~021943240378429664483

## 6.3.2. Title
Create static adverts for digital advertising

## 6.3.3. Description
`P3D` ≔ 
```text
We’re looking for a Freelance Ad Creator (2 days/week) to join the team.

We seeking someone who can take our existing brand assets, photos (from our photographer), headlines and sublines, and turn them into stunning, enganging static ads.

You’ll have some guidance from our templates and from our Senior designer, but we’re after someone who can really bring ideas to life—blending strong graphic design with AI tools where it makes sense.

Must-haves:

- Solid graphic design skills

- Experience creating ads (especially static)

- Light experience with AI tools (we’ll guide where needed)

This is 2 days per week. Flexible, remote. Let’s create scroll-stopping ads together.
```

## 6.3.4. Publication Date
last quarter

## 6.3.5. Payment Terms (USD) 
### 6.3.5.1. Expected by `ꆜ`  
20-35 Hourly
### 6.3.5.2. Actual
84 hrs @ $25.00/hr
Billed: $2,296.22

## 6.3.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.3.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
6+ months

## 6.3.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.4. `P4⁎`

## 6.4.1. URL
https://www.upwork.com/jobs/~021893378902299399803

## 6.4.2. Title
Post Production Video Editor

## 6.4.3. Description
`P4D` ≔ 
```text
We're excited to welcome a talented post production video editor to our creative team! If you have a knack for crafting cinematic content for social media and love telling stories through video, we’d love to hear from you. This role involves editing 10 engaging videos per month that leave audiences feeling energised, entertained and inspired.

Key Responsibilities:

- Cinematic Magic: Transform raw footage into polished, cinematic stories that truly connect.
- Bold Typography: Bring energy to every frame by incorporating dynamic, bold typography and graphic elements that capture attention.
- Audio Excellence: Enhance your edits with sound FX and smooth music transitions that deepen the emotional impact of the content.
- Creative B-Roll: Search for and select the perfect stock footage to use as B-roll, keeping your edits fresh and engaging.
- Brand Harmony: Follow our brand style guidelines and creative cues to ensure every video feels uniquely ours.
-On-Time Delivery: Manage your workflow to deliver a minimum of 10 fantastic video projects each month.

What We Provide:
All the essential assets, including raw video, voice overs, and a clear brand art direction
Some additional B-roll to support your creative vision

Who We’re Looking For:
- Someone with a portfolio that reflects a style aligned with our vision
- Experience working with diverse brands and social media content
- A creative professional who’s comfortable using top editing tools like Adobe Premiere Pro and After Effects
- A friendly, independent spirit who can juggle multiple projects while meeting deadlines
```

## 6.4.4. Publication Date
STUB

## 6.4.5. Payment Terms (USD) 
### 6.4.5.1. Expected by `ꆜ`  
15-50 3 quarters ago
### 6.4.5.2. Actual
8 hrs @ $20.00/hr
Billed: $55.39

## 6.4.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.4.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
6+ months

## 6.4.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.5. `P5⁎`

## 6.5.1. URL
https://www.upwork.com/jobs/~01268897d3fe56d657

## 6.5.2. Title
Keyword Research Google, Youtube and Tiktok

## 6.5.3. Description
`P5D` ≔ 
```text
Objective: Research the most popular keywords across Google, YouTube, and TikTok within specific health and nutrition categories to inspire at least 20 content creation ideas for a health supplement brand.

Categories:
- Protein
- Omega 3
- Anti-aging, Collagen, Hair/Skin/Nails

Classification: Divide the findings into two groups: Recipes keyword and informational questions keywords.

Required Data for Each Keyword:
- Category (Protein, Omega 3, or Anti-aging)
- Monthly Keyword Traffic (Number of searches per month)
- Competition (How competitive the keyword is in terms of SEO)
- Content Brief, including:
   - Content Title (Suggested title for a piece of content)
   - Content Recommendation (Brief description of what the content should cover)
   - Target Keywords (Additional keywords to enhance SEO ranking)

Format: Present the data in a list format, organized by the aforementioned parameters, the list to include at least 20 options (at least 10 of them recipes options)

Can you please list the tools you plan to use.
```

## 6.5.4. Publication Date
2 years ago

## 6.5.5. Payment Terms (USD) 
### 6.5.5.1. Expected by `ꆜ`  
100, Fixed Price
### 6.5.5.2. Actual
неизвестно

## 6.5.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.5.7. Duration (expected by `ꆜ`)
неизвестно

## 6.5.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.6. `P6⁎`

## 6.6.1. URL
https://www.upwork.com/jobs/~013fa4cb7f11f8f7c3

## 6.6.2. Title
Review of "Shareholders' Agreement" and Drafting of New "Articles of Association"

## 6.6.3. Description
`P6D` ≔ 
```text
BACKGROUND:
We have an existing "Shareholders' Agreement" in place. As part of our ongoing efforts to ensure consistency and clarity in our governance documents, we are seeking a comprehensive review of this agreement. Additionally, we require the drafting of a new set of "Articles of Association" that aligns with the provisions of the "Shareholders' Agreement".

SCOPE OF WORKS:

Review existing Shareholders' Agreement:
- Conduct a detailed review to ensure the agreement is legally sound and aligns with best practices.
- Identify any ambiguities, inconsistencies, or potential legal pitfalls.
- Recommend modifications or additions to enhance clarity, protect the company's interests, and ensure the fair treatment of shareholders.

Drafting of New Articles of Association:
- Create a new set of "Articles of Association" that aligns with the provisions and intent of the "Shareholders' Agreement".
- Ensure that the new Articles do not conflict with the Shareholders' - - - Agreement and that they complement each other.
- The new Articles should incorporate modern governance practices and be compliant with applicable laws and regulations.
- Incoporate 'Bcorps' requirments, this info will be supplied.

Key Concerns:
Share: Ensure that provisions related to shares are consistent between both documents and protect both the company's and shareholders' interests.
Director Rights and Responsibilities: Ensure clarity and consistency regarding the roles, responsibilities, and potential liabilities of directors.

DELIVERABLES:
- A revised "Shareholders' Agreement" with tracked changes and accompanying explanatory notes.
- A draft of the new "Articles of Association" for VIVOSTORE LTD.
- A brief summary report highlighting key changes made and the rationale behind them.
```

## 6.6.4. Publication Date
2 years ago

## 6.6.5. Payment Terms (USD) 
### 6.6.5.1. Expected by `ꆜ`  
350, Fixed Price
### 6.6.5.2. Actual
неизвестно

## 6.6.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.6.7. Duration (expected by `ꆜ`)
неизвестно

## 6.6.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.7. `P7⁎`

## 6.7.1. URL
https://www.upwork.com/jobs/~01c632ab7705735923

## 6.7.2. Title
Digital Banner adverts

## 6.7.3. Description
`P7D` ≔ 
```text
We are a plant based functional food company and looking for support in our upcoming marketing campaign.

This job is to create 10 banner advert collections and convert them into German, French and Italian. (I have attached some examples for your information)

We require the adverts to be created on https://www.creatopy.com/, which is a easy to use software that make creating banner ads easier to update text, and translate.

We will provide the following:
- Assets (images, fonts, colours)
- Brand Guidlines
- Copywrite
- Translations
- Access to software www.creatopy.com

We require you to have a good graphic design eye and skills to bring all the asset together, and make them look sharp, attractive & engaging in align with our brand guidelines.

This is just one small project as part of many other graphic design project, so we are looking for a freelance graphic design partner to help us on going.
```

## 6.7.4. Publication Date
3 years ago

## 6.7.5. Payment Terms (USD) 
### 6.7.5.1. Expected by `ꆜ`  
15-35 Hourly
### 6.7.5.2. Actual
336 hrs @ $30.00/hr
Billed: $10,284.75

## 6.7.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.7.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

## 6.7.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.8. `P8⁎`

## 6.8.1. URL
STUB

## 6.8.2. Title
STUB

## 6.8.3. Description
`P8D` ≔ 
```text
STUB
```

## 6.8.4. Publication Date
STUB

## 6.8.5. Payment Terms (USD) 
### 6.8.5.1. Expected by `ꆜ`  
STUB (Hourly / Fixed Price)
### 6.8.5.2. Actual
неизвестно

## 6.8.6. Contractor Level (expected by `ꆜ`)
STUB

## 6.8.7. Duration (expected by `ꆜ`)
STUB

## 6.8.8. Contractor Location (expected by `ꆜ`)
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
Компания, о которой `ꆜ` пишет в `Ps`:
~~~
VIVOSTORE LTD.
~~~
,
~~~
We are a plant based functional food company
~~~
```

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
build an automated link between our packaging artwork in Adobe Illustrator and an external XML (or similar structured data) source, so that product information such as ingredients, nutrition panels, names, and claims can be updated automatically, without manual text edits.
~~~
```
 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1. `᛭T`
1) Проанализируй:
1.1) Каким бизнесом занимается `ꆜ`?
1.2) Каким образом он зарабатывает деньги?
1.3) Кто и за что ему платит?
1.4) Какие услуги и кому он предоставляет?
1.5) Кому и что он продаёт?
1.6) Зачем ему нужно решать `T⁎`?
В чём заключается его стратегическая цель?

# 2. Источники информации
В своём анализе используй авторитетные источники информации на английском языке.

# 3. Требования к ответу
Свой ответ дай на русском языке. 
~~~~~~