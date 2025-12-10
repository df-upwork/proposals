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
```
▶ A
```
означает, что в описываемой мной ситуации я использую `A`.



~~~~~~

# 3. `O.md`
~~~~~~markdown
# 0.
Сегодня 2025-09-10.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021965504255206958232

## 2.2. Title
Find contact information

## 2.3. Description
`PD` ≔ 
```text
Hello - I need help finding the CEO for this company, and their contact information (email address, cell phone, address, etc).

https://hospicetools.com/

I will have other ad-hoc requests and will pay you per successful lead found.
```

## 2.4. Tags
Company Research
List Building
Contact List
Data Entry


# 3. Информация о `ꆜ`
## 3.1. Местоположение
United States
Skokie

## 3.2. Характеристики компании
### 3.2.1. Сектор экономики
Finance & Accounting

### 3.2.2. Количество сотрудников
Small company (2-9 people)

## 3.3. Характеристики учётной записи на `UW`
### 3.3.1. Member since
Member since Aug 11, 2023
### 3.3.2. Hire rate (%)
79
### 3.3.3. Количество опубликованных проектов (jobs posted)
66 
### 3.3.4. Total spent (USD)
$3.6K
### 3.3.5. Количество оплаченных часов в почасовых проектах
181 
### 3.3.6. Средняя почасовая ставка (USD)
$9.32

# 4. Другие проекты `ꆜ` на `UW`
## 4.1. `P1⁎`

## 4.1.1. URL
https://www.upwork.com/jobs/~021965553307814536344

## 4.1.3. Title
Create Google Sheet with index match formulas into new files

## 4.1.4. Description
`P1D` ≔ 
```text
I have 5-10 Google Sheets.  I need you to copy a template I have in one Google Sheet, and add it to the 5-10 Google Sheets.  The template will require you to update index match formulas in Google Sheets and make sure the data makes sense.  

If you are interested, I will have a sample for you to review.  We will agree on a fixed number of Google Sheets you cover in one hour per your rate to ensure both sides are happy with the product.  I'd expect this shouldn't take more than 10 minutes for someone who is proficient in Google Sheets or Excel because I have the template already available.
```

## 4.2. `P2⁎`

## 4.2.1. URL
https://www.upwork.com/jobs/~021960476547009277834

## 4.2.2. Title
Validate addresses and create Mail Merge Documents

## 4.2.3. Description
`P2D` ≔ 
```text
I need help validating the address listed on the company's website, and then taking the validated addresses and running the Mail Merge process in a Microsoft Word Document to create the final templates for each letter.

1) Open a Google Sheet with a list of companies.  Go to the URL, find the address, and confirm it matches what is in the Google Sheet for the company's address.
2) Run the automation to check the address is valid
3) Once all addresses are validated, please export the Google Sheet and run the Mail Merge process to create personalized letters for all companies and recipients in the original Google Sheet File.  You will send this file to me as the final deliverable.

Please propose your price per company reviewed (e.g. $0.05 per company validated via their website).  We will agree on this pricing structure.
```

## 4.3. `P3⁎`

## 4.3.1. URL
https://www.upwork.com/jobs/~021960042341755587830

## 4.3.2. Title
Completing Contact Us Forms for Investment Banks

## 4.3.3. Description
`P3D` ≔ 
```text
I need your help to visit the website of a company on my list, submit a contact us form, and complete certain identifying information about the website.

I am paying hourly, however we will agree to a certain number of companies you complete per hour.

For example, you will visit a Google Sheet with a list of 5,000 investment banks.  This is an example of one company: https://chapman-usa.com/.  You will visit the website, look for the contact us section, and fill out the form per the information that I provide.   You will then update the Google Sheet to confirm your submission and any other notes about the submission process.  You will also note that for a company like this (https://chapman-usa.com/), you will mention that I need to call the business directly and provide the contact information and flag an open items for me.

Attention to detail and full fluency in English is required.
```

## 4.4. `P4⁎`

## 4.4.1. URL
https://www.upwork.com/jobs/~021960473963688076882

## 4.4.2. Title
Add USPS address verticiation API to Google Sheet

## 4.4.3. Description
`P3D` ≔ 
```text
I need help adding automation to a Google Sheet to check whether an address is valid with the USPS API (https://developer.usps.com/apis).

We have the fields Company City, Company State, Mailing Street, and Postal Code.  

Here is the Google Sheet that needs to be automated so you can see the fields: https://docs.google.com/spreadsheets/d/17S4-xUy-E9Y-9RrcGSaN00Ioz0tI-2f7ejdjmGvoAfE/edit?usp=sharing

In your response to me, please address the following: your proposed budget and an ETA of when this is complete.  Please let me know if the USPS API will charge me for usage, and address how I can handle this.
```

## 4.5. `P5⁎`

## 4.5.1. URL
https://www.upwork.com/jobs/~021958639476108523140

## 4.5.2. Title
List Consolidation and finding websites for 2K companies

## 4.5.3. Description
`P5D` ≔ 
```text
I need help with two things.

1) I need to confirm all companies in four separate tabs are listed in the new tab.  

2) I need help finding the website of 2K companies.  We have the names.  You can use AI to help with this, as long as you check it manually (e.g. make sure the website is dealing with business brokers or M&A).

I need this in two business days.
```

## 4.6. `P6⁎`

## 4.6.1. URL
https://www.upwork.com/jobs/~021951385906231757304

## 4.6.2. Title
Data matching and cleaning

## 4.6.3. Description
`P6D` ≔ 
```text
Per the attached file, I need help finding websites for company names, determining if that website matches a list I already have of companies, and if there is a match identifying if the person listed is a match to anyone on the list.  

I have formal instructions in the attache spreadsheet and both datasets.

I need this completed by 8/3/2025 at 12pm EST.  

I will only accept job offers from people that actually read this and mention "Broker" in your response back to me.

This is Part 1 of the project.  There is a part 2 if this is done well, which will be under an additional milestone.
```

# 5.
## 5.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`, `P4⁎`, `P5⁎`, `P6⁎`}

## 5.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 5.3.
`Pi` : `Ps`

# 6.
N/A

# 7.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
I need help finding the CEO for this company, and their contact information (email address, cell phone, address, etc).

https://hospicetools.com/
~~~
```


 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1.
## 1.1.
`Aᨀ` ≔ (мой ответ `ꆜ`)

## 1.2.
Содержание `Aᨀ`:
~~~markdown
1) Владельцем Hospice Tools LLC (hospicetools.com) является семья Klein: отец-основатель Michael A. Klein и его многочисленные сыновья.
Здесь на фото он с 3 из них: https://voyagechicago.com/interview/meet-michael-klein-chaim-klein-eli-klein-ben-klein-unity-hospice-chicagoland
Но сыновей у него больше, в том числе участвующих в управлении компании.
2) The Michael's e-mail опубликован в пункте 1.3 в приложенном файле `Contract.pdf`.
Upwork запрещает мне писать его прямо в тексте proposal.
3) Все сыновья Michael присутствуют на LinkedIn, в частности:
Yonah: https://www.linkedin.com/in/yonah-klein-cpa-2a09ab170
Eli: https://www.linkedin.com/in/eli-klein-b9599066
Chaim: https://www.linkedin.com/in/chaim-klein-0a047311a
Ben: https://www.linkedin.com/in/ben-klein-6892b061
Часть из них — из вашего маленького городка Skokie 
4) Сам Michael не сидит в соцсетях в силу своего возраста.
5) «CEO» у Hospice Tools LLC  нет: Illinois Limited Liability Company Act не требует от LLC иметь в своей структуре должность CEO.
Законными полномочиями управлять компанией и действовать от её имени обладает «Manager» — на эту роль  Michael назначил своего сына Chaim: смотрите выписку из реестра штата Иллинойс во вложении (`Hospice Tools LLC.pdf`).
Выше я давал ссылку на его LinkedIn.
6) Для оперативного управления они наняли Daniel Goldmeier, назвав его должность «VP Sales and Marketing»: 
https://www.linkedin.com/in/daniel-goldmeier-0775646
7) У Michael больше дюжины компаний в сфере хосписа.
Многие их них (включая Hospice Tools LLC) зарегистрированы в вашем городке Skokie, причём по одному и тому же адресу: 4101 MAIN STREET, SKOKIE, IL 60076-2753.
8) Во всех его компаниях руководящими полномочиями официально владеют либо он, либо его сыновья.
9) Основные 2 его организации: 
9.1) Unity Hospice Management, Inc. 
Выписка из реестра: `Unity Hospice Management, Inc.pdf`.
9.2) Unity Hospice and Palliative Care Foundation, Inc.
Выписка из реестра: `Unity Hospice and Palliative Care Foundation, Inc.pdf`
10) В обеих организациях пункта 9 Michael — «President» и «Director», его сын Doniel — «Accounts Payable».
Во второй организации «Registered Agent» — его сын Yonah, в первой — он сам.
11) Hospice Tools LLC они создали для выделе
~~~

# 2. `᛭T`
Проанализируй `Aᨀ`:
## 2.1.
1) Есть ли там логические ошибки?
2) Есть ли там фактические ошибки?
3) Упущено ли в `Aᨀ` нечто важное?

# 3. Требования к твоему ответу
## 3.1.
Отвечай на русском языке.
## 3.2.
Мой вопрос не пересказывай.
## 3.3.
Уже сформулированную мной информацию не пересказывай.
## 3.4.
Писать свою версию `Aᨀ` не нужно: просто укажи свои замечания по пунктам.
## 3.5.
До и после списка замечаний ничего не пиши.
## 3.6.
Нумерация замечаний должна быть сквозной.
~~~~~~