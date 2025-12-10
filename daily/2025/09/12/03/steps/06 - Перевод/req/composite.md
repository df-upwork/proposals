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
https://www.upwork.com/jobs/~021965983086153990364

## 2.2. Title
Consultation with Real Estate Attorney for Security Deposit Refund

## 2.3. Description
`PD` ≔ 
```text
We are seeking a knowledgeable Real Estate Attorney to provide legal assistance regarding the refund of a security deposit. 
We have received a notice about delay in refunding the security deposit in the state of Illinois. We wanted to explain the entire situation and get feedback on next steps. 
The ideal candidate will offer a thorough review of our situation, assess the legal implications, and provide an expert opinion on the best course of action. 
Experience in tenant law and security deposit disputes is crucial. 
If you have a strong understanding of real estate regulations and a proven track record in handling similar cases, we invite you to apply for this opportunity.
```

## 2.4. Tags
Legal
Legal Consulting
Real Estate
Contract Law

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
Sammamish

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Dec 10, 2016
### 5.3.2. Hire rate (%)
50
### 5.3.3. Количество опубликованных проектов (jobs posted)
36 
### 5.3.4. Total spent (USD)
$5.4K 
### 5.3.5. Количество оплаченных часов в почасовых проектах
173
### 5.3.6. Средняя почасовая ставка (USD)
$19.34

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

## 6.1.1. URL
https://www.upwork.com/jobs/~018d2d2c634c30e1b7

## 6.1.2. Title
Need help with filing Form 5472 for IRS

## 6.1.3. Description
`P1D` ≔ 
```text
We have a C Corp which has a foreign owner. This C corp has advanced loan to another S Corp which has shared owners (Not the exact ownership % but one of the owner is common). We would like to know if we need to file Form 5472 for this transaction
```

## 6.1.4. Publication Date
last year

## 6.1.5. Payment Terms
### 6.1.5.1. Expected by `ꆜ`  
$20 - $50 (Hourly)
### 6.1.5.2. Actual
4 hrs @ $9.00/hr
Billed: $22.36

## 6.1.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.1.7. Duration (expected by `ꆜ`)
< 1 month, Less than 30 hrs/week

## 6.1.8. Contractor Location  (expected by `ꆜ`)
Not specified

## 6.2. `P2⁎`

## 6.2.1. URL
https://www.upwork.com/jobs/~01f55812e3dd3f706e

## 6.2.3. Title
Need guidance on GST/HST filing in Canada

## 6.2.3. Description
`P2D` ≔ 
```text
We have a small entity in Canada. We could use guidance on how to record and report GST/HST in Canada. Our clients pay us GST. We also pay GST to our vendors. My assumption is that the net GST is to be paid to the Canada Revenue Agency. What forms are to be filled for this? How do we track GST payable in Quickbooks. If I am based out in British Columbia but our vendor is based out of Ontario region, do we need to do reporting to Federal authorities or to Ontario authorities? Need guidance on topics like this
```

## 6.2.4. Publication Date
2 years ago

## 6.2.5. Payment Terms
### 6.2.5.1. Expected by `ꆜ`  
$15 - $25 (Hourly)
### 6.2.5.2. Actual
7 hrs @ $20.00/hr
Billed: $122.52

## 6.2.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.2.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

## 6.2.8. Contractor Location (expected by `ꆜ`)
Canada

## 6.3. `P3⁎`

## 6.3.1. URL
https://www.upwork.com/jobs/~015d5243e684e91a2d

## 6.3.2. Title
Need training in Kotlin

## 6.3.3. Description
`P3D` ≔ 
```text
Hi, My son has chosen to build a mobile app as part of his personal project for his school. He is good in logic and algorithms. He knows Python coding really well. However, he is new to Kotlin or mobile app development. We are looking for someone who can connect on a regular basis, coach him on Kotlin and guide him through completion of his mobile application project.
```

## 6.3.4. Publication Date
2 years ago

## 6.3.5. Payment Terms
### 6.3.5.1. Expected by `ꆜ`  
STUB (Hourly / Fixed Priced
### 6.3.5.2. Actual
91 hrs @ $15.00/hr
Billed: $1,429.94

## 6.3.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.3.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
1-3 months

## 6.3.8. Contractor Location (expected by `ꆜ`)
India

## 6.4. `P4⁎`

## 6.4.1. URL
https://www.upwork.com/jobs/~011319a9a2bda3eb49

## 6.4.2. Title
Need an addendum to be drafted for an MSA

## 6.4.3. Description
`P4D` ≔ 
```text
I am entering into a contract with a company (ABC Group) for staffing an IT Resource. MSA has a Non Compete clause included. However, I am already working at the same client through a different partner. I have requested ABC Group to edit their MSA but they are not willing to do so. Instead they offered to sign an addendum that will allow me to work at the same client through more than one vendor partner.
This MSA is governed by State of New York jurisdiction. Would be nice to be worked by someone who is familiar with State of New York interpretation
```

## 6.3.4. Publication Date
2 years ago

## 6.3.5. Payment Terms
### 6.3.5.1. Expected by `ꆜ`  
$250 (Fixed Price)
### 6.3.5.2. Actual
неизвестно

## 6.3.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.5. `P5⁎`

## 6.5.1. URL
https://www.upwork.com/jobs/~01fedd1cd5af961f96

## 6.5.2. Title
Request content editing for an Information Technology initiative

## 6.5.3. Description
`P5D` ≔ 
```text
We are working on building a non-profit initiative to motivate more people from minority communities underrepresented in technology to take up IT jobs.
I have put together some thoughts but I feel this can be improvised considerably. Audience of this brochure would be the prospective interns (Who want to know about the program), prospective clients (Clients who are willing to give opportunity to the trained interns) etc.,

I am looking at this as a two step process. First get the content ready and then follow up with a brochure design.

If you have experience working in the technology space, that would be an added plus. Also if you have experience promoting non profit initiatives that would be an added plus
```

## 6.5.4. Publication Date
3 years ago

## 6.5.5. Payment Terms
### 6.5.5.1. Expected by `ꆜ`  
not specified
### 6.5.5.2. Actual
2 hrs @ $43.00/hr
Billed: $83.17

## 6.5.6. Contractor Level (expected by `ꆜ`)
Expert

## 6.5.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
< 1 month

## 6.5.8. Contractor Location (expected by `ꆜ`)
Not specified

## 6.6. `P6⁎`

## 6.6.1. URL
https://www.upwork.com/jobs/~01e2801c1561f46e44

## 6.6.2. Title
Seeking Music Tutor to Create Acoustic Guitar songs along with the backing

## 6.6.3. Description
`P6D` ≔ 
```text
Hello,

I'm in search of an experienced music tutor who can assist me in creating captivating non-vocal songs using instruments like bass, drums, and guitar. My objective is to acquire a solid foundation in music composition and production, enabling me to craft engaging instrumental compositions.

Regards,
NIkhil
```

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`, `P4⁎`, `P5⁎`, `P6⁎`}

## 7.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 7.3.
`Pi` : `Ps`

# 9.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
We have received a notice about delay in refunding the security deposit in the state of Illinois
~~~
```

# 10.
⊤ (`ꆜ` в контексте `P⁎` является арендатором, не арендодателем)

# 11.
## 11.1.
`S⠿` ≔ ⠿~ (Способы решения `P†` для `ꆜ`)

## 11.2.
`Sᵢ` : `S⠿`


# 12.
`NⰀ` ≔ («notice about delay», о котором `ꆜ` пишет в `PD`)


 
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
1) Ваша ситуация регулируется конкретным законом  (`A`): Security Deposit Return Act, 765 ILCS 710 
https://www.ilga.gov/Legislation/ILCS/Articles?ActID=2202&ChapterID=62
2) Пункт 1(a) `A` устанавливает следующие временные рамки для lessor:
2.1) 30 дней после выезда арендатора: cрок для предоставления детализированного списка повреждений с указанием стоимости ремонта, если планируются удержания за ущерб.
2.2) 45 дней после выезда арендатора: cрок для возврата депозита в полном объеме, если детализированный список не был предоставлен в течение первых 30 дней.
3) Обратите внимание, что сроки пункта 2 применяются только в том случае, если арендатор предоставил арендодателю свой новый адрес (почтовый или электронный).
Согласно пункту 1(a) `A`, если арендатор не предоставляет адрес для связи, арендодатель не несет ответственности за ущерб или штрафы.
4) 
4.1) The «notice about delay», который вы получили, не освобождает арендодателя от соблюдения сроков, установленных в пункте 2.
4.2) Содержание этого «notice» имеет значение: если оно включает детализированный список повреждений, оно может рассматриваться как попытка (возможно, запоздалая) выполнить требования пункта 1(a) `A`.
5) Обратите внимание, что Штат Иллинойс позволяет муниципалитетам принимать собственные постановления, регулирующие отношения арендодателей и арендаторов. 
В частности, такие города, как Чикаго и Эванстон, имеют значительно более жесткие правила (например, Chicago Residential Landlord and Tenant Ordinance, RLTO), чем законодательство штата.
Эти местные законы могут устанавливать более короткие сроки возврата депозита, требовать его хранения на отдельном счете и предусматривать более суровые штрафы за нарушения.
Поскольку точное местоположение арендуемой недвижимости в штате Иллинойс неизвестно, невозможно определить, подпадает ли ваш случай под действие такого усиленного местного регулирования.
Любая стратегия, основанная исключительно на законодательстве штата Иллинойс, может оказаться неполной и неэффективной, если на данной территории действует более строгий местный акт.
6) В любом случае (даже с учётом пункта 5) при обращении в суд вы наверняка выиграете дело, если арендодатель нарушил сроки, указанные в пункте 2.
7) Согласно `A`, после выигрыша вами суда, lessor будет обязан:
7.1) выплатить сумму, равную двойному размеру депозита (an amount equal to twice the amount of the security deposit).
7.2) оплатить судебные издержки (court costs) и разумные гонорары адвоката (reasonable attorney's fees).
8) Суд обяжет lessor выплатить штраф, только если установит, что арендодатель отказался (refused) предоставить детализированный список повреждений, или предоставил его недобросовестно («in bad faith»), И не вернул депозит в установленные сроки.
9) Перед началом любых юридических действий необходимо собрать и сохранить все доказательства.
К ним относятся: 
9.1) договор аренды
9.2) подтверждение уплаты депозита (e.g., квитанция или выписка по счёту)
9.3) документация о состоянии жилья при въезде и выезде (фотографии, видеозаписи, отчёты об инспекции) копия полученного «notice about delay»
9.4) вся переписка с арендодателем (включая электронные письма и текстовые сообщения)
9.5) подтверждение точной даты выезда и предоставления нового адреса
10) Если вы хотите сэкономить время, то перед обращением в суд можно отправить lessor Formal Demand Letter.
Это письмо необходимо отправить через USPS Certified Mail с обязательным использованием опции «Return Receipt Requested» (с уведомлением о вручении).
Это обеспечит юридически значимое доказательство получения письма адресатом.
11) Для максимальной эффективности Formal Demand Letter должно содержать следующую информацию:
11.1) Точную дату выезда и сумму уплаченного депозита.
11.2) Новый адрес арендатора и подтверждение того, что он был ранее предоставлен арендодателю.
11.3) Прямую ссылку на применимое законодательство (Security Deposit Return Act, 765 ILCS 710/1, и местное законодательство, если применимо).
11.4) Требование о возврате депозита в полном объеме (и процентов, если применимо согласно 765 ILCS 715).
11.5) Упоминание предусмотренных законом штрафных санкций в случае отказа (включая двойной размер депозита и reasonable attorney's fees).
12) В Formal Demand Letter важно установить короткий срок ответа (e.g., 7 дней).
13) Обратите внимание, что lessor не обязан отвечать на Formal Demand Letter, но отсутствие ответа может быть использовано в суде как дополнительное свидетельство недобросовестности («bad faith»).
~~~

# 3.
## 3.1.
`D2` ≔ (начальная часть `D`, переведённая с `L_SOURCE` на `L_TARGET`)

## 3.2.
Содержание `D2`:
~~~markdown
1) Your situation is governed by a specific act (`A`): Security Deposit Return Act, 765 ILCS 710 https://www.ilga.gov/Legislation/ILCS/Articles?ActID=2202&ChapterID=62
2) Point 1(a) of `A` establishes the following timeframes for the lessor:
2.1) 30 days after the tenant vacates: the deadline to provide an itemized list of damages indicating the cost of repair, if deductions for damages are planned.
2.2) 45 days after the tenant vacates: the deadline to return the deposit in full if the itemized list was not provided within the first 30 days.
3) It should be noted that the deadlines outlined in point 2 apply only if the tenant has provided the landlord with their new address (mailing or email).
According to point 1(a) of `A`, if the tenant does not provide a forwarding address, the landlord is not liable for damages or penalties.
4) 
4.1) The «notice about delay» that you received does not exempt the lessor from complying with the deadlines set forth in point 2.
4.2) The content of this «notice» is relevant: if it includes an itemized list of damages, it can be considered an attempt (perhaps a belated one) to comply with the requirements of point 1(a) of `A`.
5) Note that the State of Illinois allows municipalities to adopt their own ordinances governing landlord-tenant relationships. In particular, cities such as Chicago and Evanston have significantly stricter rules (e.g., the Chicago Residential Landlord and Tenant Ordinance, RLTO) than state law.
These local ordinances may establish shorter deadlines for the return of the security deposit, require it to be held in a separate account, and provide for stricter penalties for violations.
Since the exact location of the rental property in Illinois is unknown, it is impossible to determine whether your case falls under such stricter local regulation.
Any strategy based solely on Illinois state law may prove to be incomplete and ineffective if a stricter local act is in effect in the given territory.
6) In any case (even considering point 5), you will certainly win the case in court if the lessor violated the deadlines specified in point 2.
7) According to A, in the event of a favorable judgment, the lessor will be required to:
7.1) pay an amount equal to twice the amount of the security deposit.
7.2) pay court costs and reasonable attorney's fees.
8) The court will order the lessor to pay a penalty only if it finds that the lessor refused to provide an itemized list of damages, or provided it «in bad faith», AND did not return the deposit within the established timeframes.
9) Before initiating any legal action, it is necessary to collect and preserve all evidence.
This includes:
9.1) the lease agreement
9.2) proof of the deposit payment (e.g., a receipt or account statement)
9.3) documentation of the property's condition upon move-in and move-out (photographs, video recordings, inspection reports), a copy of the received «notice about delay»
9.4) all correspondence with the landlord (including emails and text messages)
9.5) proof of the exact move-out date and of providing the new address
~~~

# 4.
## 4.1.
`F` ≔ (фрагмент `D`)

## 4.2.
Содержание `F`:
~~~markdown
12) В Formal Demand Letter важно установить короткий срок ответа (e.g., 7 дней).
13) Обратите внимание, что lessor не обязан отвечать на Formal Demand Letter, но отсутствие ответа может быть использовано в суде как дополнительное свидетельство недобросовестности («bad faith»).
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