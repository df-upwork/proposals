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
https://www.upwork.com/jobs/~021986484338862376732

## 2.2. Title
Legal Expert for Complex Real Estate Transaction

## 2.3. Description
`PD` ≔ 
```text
Seeking a legal expert to assist with a residential investment property acquisition in Pennsylvania. 
The transaction involves a hybrid financing model with three funding sources, requiring meticulous legal coordination to ensure compliance and enforceability across all instruments. 
Must be expert in Real Estate/Contract Law in Pennsylvania specifically in Seller Financing.

# Transaction Summary
I am in the process of acquiring a residential investment property in Pennsylvania through a hybrid financing model that integrates three distinct funding sources:

- Primary Financing: 80% DSCR or similar loan from a private lender
- Seller Financing: 20% promissory note directly from the property seller
- Down Payment: Supplied by a transactional lender to facilitate same-day closing

# Legal Support Requested
To execute this transaction successfully, I am seeking your assistance with:
1. Drafting and reviewing all legal documents, including the purchase agreement, seller note, security instruments, and inter-party coordination agreements
2. Ensuring lien priority and enforceable security interests across all financing layers
3. Structuring the closing process to meet the transactional lender’s requirement that all components be executed within the same title office on the same day
4. Providing or coordinating title services, if available through your firm, to streamline execution and minimize risk
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
Edison

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Sep 13, 2022
### 5.3.2. Hire rate (%)
48
### 5.3.3. Количество опубликованных проектов (jobs posted)
17
### 5.3.4. Total spent (USD)
9.7K 
### 5.3.5. Количество оплаченных часов в почасовых проектах
61
### 5.3.6. Средняя почасовая ставка (USD)
50

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

## 6.1.1. URL
https://www.upwork.com/jobs/~021985002728310471288

## 6.1.2. Title
Expert Social Media Marketer for AI & Digital Marketing

## 6.1.3. Description
`P1D` ≔ 
```text
Join Everything AI, LLC as a Social Media Marketing expert to manage and grow our brand across major platforms. This role offers stability and potential for a long-term salaried position. We seek a skilled SMM pro with experience in social media management, marketing, and video editing.

Deliverables
Manage and grow brand across major platforms
Optimize content for Facebook, IG, TikTok, LinkedIn, X, Pinterest, YouTube
Create engaging and standout content
Collaborate on marketing strategies
Potential for long-term partnership
```

## 6.1.4. Publication Date
5 days ago

## 6.1.5. Payment Terms (USD) 
### 6.1.5.1. Expected by `ꆜ`  
неизвестно
### 6.1.5.2. Actual
неизвестно

## 6.1.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.1.7. Duration (expected by `ꆜ`)
More than 30 hrs/week
6+ months

## 6.1.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.2. `P2⁎`

## 6.2.1. URL
https://www.upwork.com/jobs/~01318ff8aa7fc4665f

## 6.2.3. Title
Credit Specialist Needed

## 6.2.3. Description
`P2D` ≔ 
```text
I need a credit specialist to remove charge offs, late payments and a few negative items on my credit report. 
I am looking for someone experienced and am willing to work with you per hour or a flat rate in order to increase my credit score.
```

## 6.2.4. Publication Date
2 years ago

## 6.2.5. Payment Terms  (USD) 
### 6.2.5.1. Expected by `ꆜ`
3-10 Hourly 
### 6.2.5.2. Actual 
Fixed-price $210.00

## 6.2.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.2.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

## 6.2.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.3. `P3⁎`

## 6.3.1. URL
https://www.upwork.com/jobs/~01093db6b8309c1c72

## 6.3.2. Title
Appeals Paralegal Needed for the Third Circuit Court of Appeals

## 6.3.3. Description
`P3D` ≔ 
```text
Hello,

My Name is Farkhan Shah and I am writing to you because I need a Paralegal who can help with appeals in the Third Circuit of Appeals. A small breakdown of my case so you can decide whether or not you wish to take on this Appeals job.

    1. There were material facts in controversy especially since spoliation of evidence and perjury was committed by opposing side and the Judge still moved for Motion Summary Judgement which is not allowed in the Federal Rules of Civil Procedure under Rule 56, 60 (b), and 12(h)(3).

    2. The federal Judge had Venue but lacked subject matter jurisdiction and ruled on documents that were

            Rejected by the Clerk of The Court on July 23-24, 2021 and Counsel were asked to resubmit

            The July 26, 2021 submission was 3 days late where even the Third circuit did not have Jurisdiction

    3. The Judge made a secret ruling in her chambers where the public did not have access to Judicial scrutiny which the Supreme Court Ruled is a First amendment violation which also gives perception of Judicial Abuse.

    4. The Judge Ruled on documents from a Fashion corporation that was unauthorized to practice Law in New Jersey under Rule 1:21- Practice of Law governing the state of New Jersey.

    5. Due process was violated and the first, fourth, fifth, seventh eleventh and fourteenth amendment was violated.

I would like to appeal this case. Could you help me? I filed a 56 page motion to vacate summary Judgement with over 42 exhibits, however that will not be decided until after October 10, 2022. I need to file a brief as soon as possible. Please advise if you can help.

Sincerely,


Farkhan Shah

1-732-374-1422
```

## 6.3.4. Publication Date
3 years ago

## 6.3.5. Payment Terms (USD) 
### 6.3.5.1. Expected by `ꆜ`  
$3,500 Fixed Price
### 6.3.5.2. Actual
$3,200

## 6.3.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.3.7. Duration (expected by `ꆜ`)
Not specified

## 6.3.8. Contractor Location (expected by `ꆜ`)
Not specified

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`, `P4⁎`, `P5⁎`, `P6⁎`, `P7⁎`, `P8⁎`}

## 7.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 7.3.
`Pi` : `Ps`


# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
 assist with a residential investment property acquisition in Pennsylvania
~~~
```

# 9.
## 9.1.
`T1⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Drafting and reviewing all legal documents, including the purchase agreement, seller note, security instruments, and inter-party coordination agreements
~~~
```

## 9.2.
`T2⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Ensuring lien priority and enforceable security interests across all financing layers
~~~
```

## 9.3.
`T3⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Structuring the closing process to meet the transactional lender’s requirement that all components be executed within the same title office on the same day
~~~
```

## 9.4.
`T4⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Providing or coordinating title services, if available through your firm, to streamline execution and minimize risk
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