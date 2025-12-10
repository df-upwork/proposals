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
Сегодня 2025-10-07.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021975406834540067227

## 2.2. Title
Tax Attorney for Self-Directed IRA Investment Options

## 2.3. Description
`PD` ≔ 
```text
We are seeking a tax attorney with expertise in self-directed IRA investment options to provide guidance and support.
 The ideal candidate will have a strong understanding of tax laws related to retirement accounts and be able to offer detailed advice on investment strategies, specifically for investing in stocks of other companies. 
 The focus will be on both tax implications and compliance with tax laws.
 
## Deliverables
- Provide legal advice on self-directed IRA investments
- Review and analyze investment options
- Ensure compliance with tax laws 
```

## 2.4. Tags
Tax Law
Trademark Consulting
Legal Consulting
Corporate Tax
Legal Research Tools
Tax Software

# 5. Информация о `ꆜ`
## 5.1. Местоположение

United States
Santa Ana

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
Health & Fitness

### 5.2.2. Количество сотрудников
Individual client

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Feb 22, 2023
### 5.3.2. Hire rate (%)
75
### 5.3.3. Количество опубликованных проектов (jobs posted)
47
### 5.3.4. Total spent (USD)
$26K
### 5.3.5. Количество оплаченных часов в почасовых проектах
1214
### 5.3.6. Средняя почасовая ставка (USD)
16.05

# 6. Что беспокоит `ꆜ`
## 6.1. Риск нарушения правил о «Запрещенных транзакциях» (Prohibited Transactions)
###
`ꆜ` стремится «обеспечить соблюдение налогового законодательства». 
В контексте SDIRA это в первую очередь означает избежание «Запрещенных транзакций» (Prohibited Transactions), которые регулируются Разделом 4975 Налогового кодекса США (IRC Section 4975). 
Эта проблема включает опасения по поводу сделок с заинтересованностью (Self-Dealing) и конфликтов интересов при инвестировании в частные компании.

###
Это опасение является критически важным. 
Правила IRC § 4975 устанавливают строгий запрет на большинство транзакций между IRA и «Дисквалифицированным лицом» (Disqualified Person).

### Ключевые аспекты
#### Дисквалифицированные лица
К ним относятся владелец IRA (`ꆜ`), члены его семьи (супруги, предки, потомки и их супруги), а также юридические лица, в которых дисквалифицированные лица прямо или косвенно владеют 50% и более (IRS.gov).
#### Запрещенные действия
Включают продажу, обмен, кредитование, предоставление услуг или любое использование активов IRA в интересах дисквалифицированного лица (Self-Dealing).

### Применение к инвестициям в акции:
При инвестировании в частные компании возникают специфические риски:

#### Существующее владение
Если `ꆜ` или связанные с ним лица уже владеют значительной долей в целевой компании, инвестиция SDIRA может быть запрещена.
В частности, IRA не может инвестировать в компанию, если совокупное владение дисквалифицированных лиц составляет 50% или более (Mat Sorensen).

#### Самообслуживание и Конфликт интересов
Даже при владении менее 50%, если `ꆜ` занимает должность (директора, сотрудника) в компании, в которую инвестирует его SDIRA, это может быть расценено как косвенная выгода или конфликт интересов. Владелец IRA должен действовать исключительно как пассивный инвестор.

### Последствия
Нарушение правил IRC 4975 приводит к катастрофическим последствиям. 
Счет теряет статус IRA с первого дня года, в котором произошла транзакция. 
Все активы считаются распределенными и облагаются подоходным налогом и штрафами за досрочное снятие.

### Вывод
Риск непреднамеренного совершения запрещенной транзакции при инвестировании в частные компании очень высок, что полностью оправдывает опасения клиента.
 
## 6.2. Неопределенность налоговых последствий (UBIT/UDFI)
###
`ꆜ` запрашивает консультацию по «налоговым последствиям» (tax implications). 
Хотя IRA традиционно освобождены от налогов, клиент, вероятно, осведомлен о существовании Налога на не связанный с основной деятельностью доход (Unrelated Business Income Tax, UBIT). 
Его беспокоит, могут ли инвестиции в акции определенных компаний привести к налогообложению внутри пенсионного счета.

###
Опасение обосновано, поскольку не все доходы внутри IRA освобождены от налогов. 
UBIT применяется к доходам от активной торговли или бизнеса. 
Ставки UBIT соответствуют ставкам для трастов и быстро достигают максимума (до 37% при относительно низком пороге дохода).

### Ключевые аспекты

#### UBTI (Unrelated Business Taxable Income)
Возникает, когда IRA получает доход от активного бизнеса.
#### UDFI (Unrelated Debt-Financed Income)
Возникает, когда для приобретения актива используются заемные средства.

### Применение к инвестициям в акции
Критическое значение имеет юридическая структура компании:

#### C-Corporations 
Инвестиции в акции C-корпораций, как правило, **не** вызывают UBIT. 
Корпорация платит налог на прибыль на своем уровне, а дивиденды, полученные IRA, считаются пассивным доходом и освобождаются от UBIT.

#### Сквозные структуры (Pass-through Entities - LLC, Партнерства)
Если «другая компания» является LLC или партнерством, ведущим активный операционный бизнес, доход, переданный IRA, **облагается** UBIT.

### Вывод
Клиенту необходимо точно понимать структуру целевых компаний. 
Если планируются инвестиции в операционный бизнес через сквозные структуры, риск UBIT реален и требует налогового планирования (например, использования C-Corp в качестве «блокатора»).

## 6.3. Сложность структурирования инвестиций и административные требования
###
`ꆜ` запрашивает «детальные советы по инвестиционным стратегиям» и «анализ вариантов инвестирования».
Это указывает на неопределенность в отношении допустимых типов акций, юридического оформления сделок и последующего соблюдения административных требований IRS при владении непубличными активами.

###
Опасение обосновано, так как существуют дополнительные регуляторные и административные барьеры:

#### Запрет на S-Corporations
IRA по закону **не может** владеть акциями S-Corporation. 
Инвестиция приведет к потере статуса S-Corp для компании.
Клиент должен убедиться, что целевые компании не являются S-Corp.

#### Ежегодная оценка (Valuation)
Акции частных компаний не имеют публичной рыночной цены. 
Владелец IRA обязан ежегодно предоставлять кастодиану справедливую рыночную стоимость (Fair Market Value, FMV) этих активов для отчетности перед IRS (Form 5498). 
Это часто требует дорогостоящей независимой оценки.

#### Оформление и Движение средств
Все инвестиции должны быть оформлены строго на имя IRA, и все средства должны проходить через кастодиана. 
Любое смешение личных и пенсионных средств недопустимо. 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1.
## 2.1.
`Dᨀ` ≔ (мой ответ `ꆜ`)

## 2.2.
Содержание `Dᨀ`:
~~~markdown
1) Compliance. 
1.1) In the context of a self-directed IRA (SDIRA), compliance primarily means avoiding prohibited transactions.
IRC §4975 establishes a strict prohibition on most transactions between an IRA and a «disqualified person» (hereinafter `DP`).
The definition of a `DP`: https://www.law.cornell.edu/uscode/text/26/4975#e_2
The list of prohibited transactions: https://www.law.cornell.edu/uscode/text/26/4975#c_1
1.2) Investing in private companies involves specific risks:
1.2.1) Existing ownership.
If the aggregate `DP` ownership in the company is 50% or more before the transaction, the company itself is a `DP`.
Any direct or indirect sale or exchange of property between an IRA and a `DP` is prohibited.
Therefore, the IRA cannot acquire stock (e.g., in a new issuance) directly from such a company.
The acquisition of stock in such a company from an unrelated third party does not formally constitute a direct transaction with a `DP`.
However, such an investment poses extremely high risks described in point 1.2.3.
1.2.2) Initial capitalization.
The status of a `DP` is determined immediately before the transaction.
A new company that has no shareholders before the IRA's investment is not a `DP` at the time of the initial stock issuance.
Consequently, the initial acquisition of stock by the IRA from such a company is not formally prohibited, even if the IRA will own 100% of the stock as a result.
The company becomes a `DP` only after the completion of this transaction.
Any subsequent transactions between the IRA and this company will be prohibited.
1.2.3) Self-dealing and conflict of interest.
Even if a transaction is formally permitted, extremely high risks of violating other provisions of IRC §4975 persist.
These include prohibitions against the use of plan assets for the benefit of a `DP` and acts by a fiduciary involving a conflict of interest.
If the IRA owner (hereinafter `O`) holds a position (director, employee) in the company in which the SDIRA invests, this may be construed as receiving an indirect benefit or a conflict of interest.
`O` must act solely as a passive investor.
2) Tax implications.
2.1) The Unrelated Business Income Tax (UBIT) is levied on Unrelated Business Taxable Income (UBTI).
The definition of UBTI: https://www.law.cornell.edu/uscode/text/26/512#a_1
IRC §512(b) provides for a number of modifications to the definition: https://www.law.cornell.edu/uscode/text/26/512#b
2.2) The IRA's income is subject to UBIT in 2 primary scenarios:
2.2.1) Unrelated Trade or Business Income.
If an IRA participates (directly or through pass-through entities) in an active trade or business, the income received constitutes UBTI.
The exceptions for passive income do not apply to such income.
2.2.2) Unrelated Debt-Financed Income (UDFI).
If an asset is acquired with acquisition indebtedness, the income from that asset (even if it is passive) is included in UBTI in proportion to the share of the debt financing.
2.3) The legal structure of a company is of critical importance when investing in its equity, as it determines the form of ownership (stocks or interests):
2.3.1) Investments in entities taxed as C-Corporations (including LLCs that have elected this status under the «Check-the-Box Regulations») generally do not trigger UBIT.
Such an entity pays income tax at its own level (acting as a «blocker»).
Dividends and capital gains received by an IRA are considered passive income and are generally exempt from UBIT.
2.3.2) If an IRA acquires membership interests or partnership interests in pass-through entities (such as partnerships or LLCs taxed as partnerships or disregarded entities) engaged in an active trade or business, the income passed through to the IRA is subject to UBIT.
3) Some additional remarks
3.1) An IRA cannot own stock in an S-Corp.
The investment will result in the loss of S-Corp status for the company.
3.2) `O` is required to provide the custodian annually with the Fair Market Value (FMV) of the stocks for reporting to the IRS (Form 5498).
This often requires a costly independent valuation.
3.3) All investments must belong to the retirement plan.
This is achieved by titling assets directly in the name of the IRA (direct ownership) or in the name of a legal entity (e.g., an LLC or partnership) in which the IRA is a member (indirect ownership).
With direct ownership, all funds must pass through the custodian.
With indirect ownership, the IRA can be either the sole member (e.g., in a Single-Member LLC) or one of multiple members (e.g., in a Multi-Member LLC or a partnership).
A structure where the IRA is the sole member and `O` acts as the manager allows `O` to conduct transactions directly from the legal entity's bank account after its initial funding by the custodian.
Regardless of the structure, any commingling of personal and retirement funds is prohibited.
~~~

# 2. `᛭T`
Я хочу опубликовать `Dᨀ` в виде статьи на своём сайте и в виде документа PDF.
Для этих целей мне нужно озаглавить `Dᨀ`.
Твоя задача: предложить 10 вариантов заголовка (`T๏`) для `Dᨀ`.

# 3. Требования к `T๏`
## 3.1.
`T๏` должен быть на английском языке.
## 3.2.
Для каждого `T๏` укажи своё обоснование.
## 3.3.
Не пиши каждое слово с заглавной буквы. 
Вместо этого пиши нормальным образом, как обычное предложение.
## 3.4.
Не повторяй варианты §5.

# 4. Пожелания к `T๏`
## 4.1.
Желательно использовать профессиональный язык предметных областей `P⁎` и `Dᨀ`.

## 4.2.
Желательно указать характер проделанной мной работы, например:
- consultation 
- expert opinion
- guidance

## 4.3.
Попробуй использовать варианты §5 как основу для твоей работы.

# 5. Варианты `T๏`, которые мне пока нравятся больше всего
отсутствуют

~~~~~~