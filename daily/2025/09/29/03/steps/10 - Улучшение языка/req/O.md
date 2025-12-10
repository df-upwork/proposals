# 0.
Сегодня 2025-09-29.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021972536833841278706

## 2.2. Title
QuickBooks Online Sales Tax Setup Expert Needed


## 2.3. Description
`PD` ≔ 
```text
I have a setup issue in Quickbooks I need help with.   
My clients are all within the Bay Area, but each one is in different cities and counties with their own sales tax rate.  
Throughout the year I have fairly large hardware/computer related orders to each of them, and each one has a different sales tax rate.   
Now this is where it gets different. 
I have a 3rd party tool I’m setting up that manages my client support needs, billing, and hardware quotes and orders.  
It needs to bring in the sales tax rate for each client.  
I’m using quickbooks online and the new sales tax setup makes no sense, and seems that sales tax rate needs to be added manually.  
The customer section has a box checked for “sales tax” but there is nothing further than that.  
When my 3rd party tool brings in clients, there is no associated sales tax rate.
I need to have clients sales tax rates setup and flowing to 3rd party tool.
```

## 2.4. Tags
Intuit QuickBooks
Bookkeeping
Bank Reconciliation
Accounting
QuickBooks Online
Excel

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
South San Francisco

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Jan 28, 2014
### 5.3.2. Hire rate (%)
82
### 5.3.3. Количество опубликованных проектов (jobs posted)
11 
### 5.3.4. Total spent (USD)
$34K
### 5.3.5. Количество оплаченных часов в почасовых проектах
877 
### 5.3.6. Средняя почасовая ставка (USD)
38

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

## 6.1.1. URL
https://www.upwork.com/jobs/~021972536157992677128

## 6.1.2. Title
Rippling and HR Advisory Services

## 6.1.3. Description
`P1D` ≔ 
```text
I have an IT consulting practice in the Bay Area and I need help with Rippling and an HR advisor.
I want to clean up my rippling flows (on-boarding and off-boarding).  
I need assistance with the various Apps in Rippling to make sure I’m doing things correctly.  
I need time and attendance working correctly/setup
I have general HR questions and need throughout the year.  
HR Advice/Documentation

# Deliverables
- Provide HR advisory services
- Assist with Rippling setup and management
- Streamline HR processes using Rippling
```

## 6.1.4. Publication Date
40 minutes ago

## 6.1.5. Payment Terms (USD) 
### 6.1.5.1. Expected by `ꆜ`  
35-70 (Hourly / Fixed Price)
### 6.1.5.2. Actual
неизвестно

## 6.1.6. Contractor Level (expected by `ꆜ`)
Intermediate

## 6.1.7. Duration (expected by `ꆜ`)
Less than 30 hrs/week
1-3 months

## 6.1.8. Contractor Location (expected by `ꆜ`)
Not specified

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`}

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
I have an IT consulting practice in the Bay Area
~~~
```

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9. Что беспокоит ꆜ
## 9.1. Контекст: QuickBooks Online и Automated Sales Tax (AST)
Важно понимать, что QuickBooks Online (QBO) перешел на систему автоматизированного расчета налога с продаж — **Automated Sales Tax (AST)**. 
Эта система кардинально отличается от ручного управления налогами. 
AST рассчитывает налог динамически в момент совершения транзакции на основе точного адреса доставки, категории продаваемого товара и налогового статуса клиента.
Большинство проблем, описанных клиентом, проистекает из непонимания этой новой модели и её технических ограничений.
# 9.2. Выявленные проблемы и анализ их обоснованности
На основании описания проекта (`PD`; `O.md`::§2.3) можно выделить несколько ключевых проблем, сгруппированных по трем направлениям.
### 9.2.1. Сложность управления налогами в Bay Area
#### Описание проблемы 
Клиент ведет бизнес (`C⁎`), продавая оборудование клиентам по всему Bay Area. 
Он отмечает сложность, связанную с тем, что в разных городах и округах действуют разные ставки налога с продаж.

#### Обоснованность
Высокая.
Калифорния имеет одну из самых сложных структур налогообложения в США, сочетающую налоги штата, округов, городов и специальных районов. 
Ставки в Bay Area существенно различаются (например, от 8.625% в Сан-Франциско до 10.75% в некоторых частях округа Аламида). 
Поскольку клиент продает физические товары (hardware), он обязан применять ставку по месту доставки (destination-based tax). 
Управление этим процессом объективно является сложной задачей для бизнеса.

### 9.2.2. Непонимание и неприятие новой системы QBO (AST)
Клиент столкнулся с рядом трудностей при адаптации к AST:

#### 9.2.2.1. Система «не имеет смысла»
##### Описание проблемы 
Клиент заявляет: «новая настройка налога с продаж не имеет смысла» (the new sales tax setup makes no sense).
##### Обоснованность 
Обоснована (субъективно).
AST представляет собой смену парадигмы. 
Вместо ручного контроля пользователь должен полагаться на автоматизацию. 
Корректность расчета в AST критически зависит от точности введенных адресов и правильной налоговой категоризации товаров. 
Если данные неточны, система выдает ошибки. 
Для пользователей, привыкших к старой модели, логика AST часто кажется непрозрачной и запутанной.

#### 9.2.2.2. Убежденность в необходимости ручного ввода
##### Описание проблемы 
Клиент предполагает, что «ставку налога с продаж нужно добавлять вручную» (sales tax rate needs to be added manually).
##### Обоснованность
Необоснована (основана на недопонимании).
Это утверждение противоречит цели AST, которая заключается именно в *устранении* необходимости ручного ввода и отслеживания ставок. 
Вероятно, клиент пришел к такому выводу, не найдя привычных инструментов для назначения ставки (см. §9.2.2.3) или столкнувшись с ошибками автоматического расчета.

#### 9.2.2.3. Отсутствие ставки налога в профиле клиента
##### Описание проблемы 
Клиент не может задать ставку для конкретного заказчика: «В разделе клиентов стоит галочка "налог с продаж", но дальше этого ничего нет».
##### Обоснованность
Фактически верное наблюдение, но основанное на неверных ожиданиях.
В модели AST ставка налога *не хранится* в профиле клиента. 
Это сделано намеренно, так как ставка зависит от адреса доставки в конкретной транзакции, который может меняться. 
Галочка лишь определяет, подлежит ли клиент налогообложению в принципе. 
Клиент ожидает увидеть функционал старой системы, которого в AST нет.

### 9.2.3. Сбой интеграции со сторонним инструментом (Ключевая проблема)
#### Описание проблемы 
Клиент использует сторонний инструмент для управления заказами и выставления счетов. 
Этот инструмент должен получать ставку налога для каждого клиента из QBO, но этого не происходит: «Когда мой сторонний инструмент импортирует клиентов, связанной с ними ставки налога с продаж нет».

#### Обоснованность
Высокая (критическая техническая проблема).
Это наиболее серьезная операционная проблема, являющаяся прямым следствием изменения модели данных QBO (см. §9.2.2.3). 
Сторонний инструмент, вероятно, разработан в расчете на старую модель и ожидает найти фиксированную ставку в профиле клиента.
Проблема усугубляется известными ограничениями API (интерфейса программирования приложений) QuickBooks Online при работе с AST:
##### Динамический расчет 
API затрудняет для стороннего приложения возможность узнать ставку налога до того, как транзакция будет создана и сохранена непосредственно в QBO.
##### Несовместимость моделей 
Инструменты, ожидающие статический налоговый код, не могут напрямую работать с динамической моделью AST.
##### Переопределение данных 
Движок AST в QBO часто игнорирует налоговые данные, передаваемые сторонними приложениями, и использует собственный расчет.

Сбой интеграции является следствием фундаментальной несовместимости стороннего инструмента с архитектурой QBO Automated Sales Tax.

## 9.3. Заключение
Проблемы, описанные клиентом `ꆜ`, реальны и создают существенные препятствия для его бизнес-процессов. 
Они вызваны сочетанием объективной сложности налогообложения в Bay Area, непонимания клиентом принципов работы QBO AST и, самое главное, технической несовместимостью используемого стороннего инструмента с моделью данных и API QuickBooks Online.

# 10.
## 10.1.
`P1†` ≔† (Проблема, описанная в §9.2.1)

## 10.2.
`P2†` ≔† (Проблема, описанная в §9.2.2.1)

## 10.3.
`P3†` ≔† (Проблема, описанная в §9.2.2.2)

## 10.4.
`P4†` ≔† (Проблема, описанная в §9.2.3)

# 11.
## 11.1.
`Aᨀ` ≔ (мой ответ `ꆜ`)

## 11.2.
Содержание `Aᨀ`:
~~~markdown
1) «the new sales tax setup makes no sense»
The system has a clear logic designed for compliance with complex tax legislation.
California uses a modified origin sourcing model for intrastate sales.
State, county, and city taxes are origin-based.
District taxes are destination-based.
AST automates handling these complex rules and thousands of jurisdictions in the Bay Area, which is practically impossible to do manually.
2) «seems that sales tax rate needs to be added manually» 
That is incorrect.
The purpose of AST is specifically to eliminate the need for manual tracking and input of tax rates.
Intuit automatically updates the rates when the legislation changes.
3) «The customer section has a box checked for “sales tax” but there is nothing further than that»
Since the rate depends on the exact shipping address in a specific transaction, which can change, storing a static rate in the customer profile is incorrect.
Therefore, AST intentionally does not store the rate in the customer profile.
The profile only determines the tax status (Taxable/Exempt).
Intuit removed the ability to set a default tax code upon AST activation.
4) «I need to have clients sales tax rates setup and flowing to 3rd party tool»
4.1) The QBO Automated Sales Tax (AST) system calculates tax dynamically.
The standard QuickBooks Online Accounting REST API (V3) does not allow a third-party application to retrieve the tax rate calculated by AST before a transaction is created and saved in QBO.
4.2) There are two main approaches to solving this integration problem.
I outline them in points 5 and 6 below.
The feasibility of either approach depends on the technical capabilities of the third-party tool and its ability to integrate with external APIs or to modify its synchronization logic with QBO.
5) Approach 1: Implementing a specialized tax service (e.g., Avalara, TaxCloud, TaxJar).
The third-party tool integrates with the API of this service to retrieve the accurate tax rate in real time.
6) Approach 2: Integrating the third-party tool with the Intuit Sales Tax API (GraphQL) to retrieve the AST-calculated rate in real time.
7) In both approaches, during the subsequent synchronization of a transaction with QBO via the Accounting REST API (V3), it is necessary to use the Sales Tax Override mechanism.
This requires not only passing the total tax amount via the `TxnTaxDetail.TotalTax` field.
For a reliable override, a reference to a Custom Sales Tax Code (`USER_DEFINED` type) via the `TxnTaxDetail.TxnTaxCodeRef` field and the use of an up-to-date API version (`minorversion`) are also required.
8) Approach 1 has the following advantages compared to Approach 2:
8.1) Increased accuracy and compliance.
Specialized services use advanced address validation and geolocation methods (address-level accuracy) to account for all local and district taxes.
This ensures maximum calculation accuracy in complex jurisdictions (Bay Area).
8.2) Provides its own powerful API.
The third-party tool can be integrated directly with this software to retrieve rates in real-time, bypassing the limitations of the QBO Accounting REST API.
8.3) Compliance automation.
Automatic rate updates, accurate reporting for the CDTFA, and automated tax filing (AutoFile).
8.4) A stable, scalable solution that is independent of the limitations or changes in the Intuit API.
---
My GitHub profile: https://github.com/dmitrii-fediuk
~~~
 