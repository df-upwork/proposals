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
Сегодня 2025-11-20.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021991164946451422479

## 2.2. Title
Payments and Credit Card Charging Specialist Advice Needed for US Project

## 2.3. Description
`PD` ≔ 
```text
We are looking for a US-based payments and credit card charging specialist to provide expert advice on managing new sales ledgers for our upcoming payments project. 
The ideal candidate will have experience in navigating the complexities of payment systems within the US market. 
We need some advice on how to implement new sales ledger in our middleware service.
```

## 2.4. Tags
Accounting Advisory
Finance & Banking Chatbot
Accounting

# 5. Информация о `ꆜ`
## 5.1. Местоположение
Ireland
Dun Laoghaire

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Aug 31, 2015
### 5.3.2. Hire rate (%)
87
### 5.3.3. Количество опубликованных проектов (jobs posted)
100
### 5.3.4. Total spent (USD)
359K
### 5.3.5. Количество оплаченных часов в почасовых проектах
9930
### 5.3.6. Средняя почасовая ставка (USD)
30.48

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

### 6.1.1. URL
https://www.upwork.com/jobs/~021991120726856457487

### 6.1.2. Title
NIST SP Basic Assessment Assistance

### 6.1.3. Description
`P1D` ≔ 
```text
We are seeking a knowledgeable professional to assist in completing the NIST SP Basic Assessment. We need some support preparing the submission based on the policy documents we have in place and then need some simple guidance about how to implement some of the policies and required elements. Hopefully this initial phase can be done over 2-3 short sessions.

More work to follow in 2026 on this also!
```

### 6.1.4. Publication Date
yesterday

### 6.1.5. Payment Terms (USD) 
#### 6.1.5.1. Expected by `ꆜ`  
1000 (Fixed Price)
#### 6.1.5.2. Actual
неизвестно

### 6.1.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.1.7. Duration (expected by `ꆜ`)
неизвестно

### 6.1.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.2. `P2⁎`

### 6.2.1. URL
https://www.upwork.com/jobs/~021956752743986131111

### 6.2.3. Title
.NET Developer with OPC Simulator Experience Needed

### 6.2.3. Description
`P2D` ≔ 
```text
We are seeking a skilled .NET developer who has hands-on experience with OPC simulators and connecting .NET applications to OPC devices. The ideal candidate will have a strong understanding of the .NET framework and be able to troubleshoot and resolve connectivity issues. Your expertise will be crucial in developing robust solutions for our project. If you are passionate about automation technologies and have experience in the OPC space, we would love to hear from you!
```

### 6.2.4. Publication Date
last quarter

### 6.2.5. Payment Terms  (USD) 
#### 6.2.5.1. Expected by `ꆜ`
15-35 Hourly
#### 6.2.5.2. Actual 
63 hrs @ $20.00/hr
Billed: $1,437.99

### 6.2.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.2.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
1-3 months

### 6.2.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.3. `P3⁎`

### 6.3.1. URL
https://www.upwork.com/jobs/~021762939815665479680

### 6.3.2. Title
Dietitian or Nutritionist for remote work with European technology startup

### 6.3.3. Description
`P3D` ≔ 
```text
We have developed a new AI platform for dietitians in Europe (HQ in Dublin, Ireland) and we are bringing the platform to the US. We are seeking a dietician and/or nutritionist to help us navigate the process and help us understand the industry in more detail.

The job is not specifically about content writing - there was no option to select a category for Health or Health-tech. There is also no requirement to have any technology background and we are simply looking for consultants to help define a much broader strategy for the product and platform.

We have a relaxed approach to how we work and we are also flexible in terms of how to collaborate - just a few hours per week or potentially full time. The job will be fully remote. If you are interested in discussing please get in touch.

```

### 6.3.4. Publication Date
last year

### 6.3.5. Payment Terms (USD) 
#### 6.3.5.1. Expected by `ꆜ`  
50-100 Hourly
#### 6.3.5.2. Actual
6 hrs @ $60.00/hr
Billed: $380.95

### 6.3.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.3.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
6+ months

### 6.3.8. Contractor Location (expected by `ꆜ`)
United States

## 6.4. `P4⁎`

### 6.4.1. URL
https://www.upwork.com/jobs/~0181476386d63979d0

### 6.4.2. Title
FDA Consultant for Class II Medical Device

### 6.4.3. Description
`P4D` ≔ 
```text
We are seeking an experienced FDA consultant to assist us with the regulatory requirements for our Class II medical device and also submitting our 501K. We also need advice regarding ISO and IEC certifications that we may not have in place already.

We are happy to engage on a short term or long term basis. Please contact me to discuss.

Many thanks
Kieran Walkin
```

### 6.4.4. Publication Date
last year

### 6.4.5. Payment Terms (USD) 
#### 6.4.5.1. Expected by `ꆜ`  
30-80 Hourly
#### 6.4.5.2. Actual
3 hrs @ $30.00/hr
Billed: $83.70

### 6.4.6. Contractor Level (expected by `ꆜ`)
Expert

### 6.4.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
3-6 months

### 6.4.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.5. `P5⁎`

### 6.5.1. URL
https://www.upwork.com/jobs/~016582da55e0681845

### 6.5.2. Title
Microfluidic device development

### 6.5.3. Description
`P5D` ≔ 
```text
We are in the early stages of the development of a new portable device to be used for blood testing (and other sample testing) in remote areas. 
We have developed machine learning algorithms to examine samples under microscope but need to develop a number of additional tests using microfluidic devices. 
In particular we have been tasked with developing a device to test PSA levels without the need to send samples to a lab. We are looking for a consultant for ongoing advice with experience in this field.
```

### 6.5.4. Publication Date
4 years ago

### 6.5.5. Payment Terms (USD) 
#### 6.5.5.1. Expected by `ꆜ`  
20-30 Hourly
#### 6.5.5.2. Actual
0 hrs @ $30.00/hr
Billed: $50.00

### 6.5.6. Contractor Level (expected by `ꆜ`)
Intermediate

### 6.5.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
3-6 months

### 6.5.8. Contractor Location (expected by `ꆜ`)
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
Компания `ꆜ` 
```

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
provide expert advice on managing new sales ledgers for our upcoming payments project
~~~
```

# 10.
## 10.1.
`T1⁎` ≔ 
```		
Подзадача из `PD`:
~~~
how to implement new sales ledger in our middleware service
~~~
```

 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1. `᛭T`
Найди в Интернете как можно больше информации про `С⁎`.

# 2. Источники информации
В своём анализе используй авторитетные источники информации на английском языке.

# 3. Требования к ответу
1) Свой ответ дай на русском языке. 
2) Не мусори словами и не пиши о системах, не относящихся к `С⁎`.
~~~~~~