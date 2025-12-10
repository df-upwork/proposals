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
Сегодня 2025-09-08.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021965005218985973513

## 2.2. Title
Expert Alteryx Developer Needed for Data Analytics Project

## 2.3. Description
`PD` ≔ 
```text
We are seeking an expert Alteryx developer to assist with our data analytics project.

There is a very specific initial problem to solve with Alteryx that can't make use of any pushdown to databases i.e. all data is coming via excel and all processing has to be done natively within Alteryx.

We have a ragged hierarchy expressed in a set of tables and the complexity is that each hierarchy can be composed of sub-hierarchies that can be expressed at different levels.  This is solved easily in SQL with a conditional outer join, but this is proving tricky to replicate in Alteryx natively.

If we can nail this first requirement, there are ~40 other tables and flows that need to have logic translated from SQL into native alteryx.
```

## 2.4. Tags
SQL
Alteryx Analytic Process Automation Platform
Microsoft Excel

# 3. Информация о `ꆜ`
## 3.1. Местоположение
United Kingdom
London

## 3.2. Характеристики компании
### 3.2.1. Сектор экономики
неизвестно

### 3.2.2. Количество сотрудников
неизвестно

## 3.3. Характеристики учётной записи на `UW`
### 3.3.1. Member since
Apr 7, 2020
### 3.3.2. Hire rate (%)
43
### 3.3.3. Количество опубликованных проектов (jobs posted)
7
### 3.3.4. Total spent (USD)
$14K
### 3.3.5. Количество оплаченных часов в почасовых проектах
276

# 4. Другие проекты `ꆜ` на `UW`
## 4.1. `P1⁎`

## 4.1.1. URL
https://www.upwork.com/jobs/~012114ef5bdeebd265

## 4.1.3. Title
React web app for B2B lead generation service

## 4.1.4. Description
`P1D` ≔ 
```text
We have an existing web app built in React but the developer who started the front end has reached the extent of their capability and is not able to continue with the project.  We need a solid developer who understands React and how to get the most out of the framework to deliver a slick user experience.

We're almost at Beta launch with 5 customers lined up to work with the platform for 1-3 months before we do our official launch.  The platform is a new take on lead generation for very specific markets.  We're starting with one market and one product to start with and then intend to expand into many others after the Beta launch.

The stack we have is:
UI - desktop web using React.  It's responsive for desktop and not really intended for mobile at this stage.  It will come but it's not a priority for our customers at present

API - this is using pgAPI which is a Node package that sits on top of postgresql and serves data from database functions.  This is not particularly user friendly at the moment and we are in the process of redesigning with a view to moving to something more flexible.  At the moment though   the first priority is to work with this existing API.  We would like the new developer to help us help drive the design of the new API. The API is only for our use - it's not for public consumption

Payments - this is with Stripe and is integrated but not particularly well.  Communication has been an issue which has led to some relatively poor implementation choices.  We need help to review this and assess how we make sure this is supportable on day 1 beta and then redesigned for us to confidently scale.

Business logic - This is pretty much all currently implemented in postgresql functions that are served up by pgapi as endpoints.  There are definitely areas for improvement as we design the new API to move some responsibilities from the database to the API.

We need someone who can hit the ground running and would like to start the process by requesting a code review of our existing estate - we're happy to pay for that and then make decisions about whether we develop an ongoing relationship.
```

## 4.2. `P2⁎`

## 4.2.1. URL
https://www.upwork.com/jobs/~01e19c97d5396b58d8

## 4.2.2. Title
GitHub actions to deploy Node and React web app on DigitalOcean

## 4.2.3. Description
`P2D` ≔ 
```text
We have a React app backed by Node using Nginx, and we're committing to a Github repo.  It's in beta at the moment and we're prepping for production launch.

Our infra is on Digital Ocean and we have a fairly simple setup with a front end droplet that has a load balancer sitting in front.  We will move to containers but not right now.

The previous dev was deploying changes to our beta completely manually so we need to fix that.

Our first priority is a very simple automation that allows us to manually trigger a deployment of a branch to the DO server, and make it publicly available.  We're open to suggestions on what that is but we do want something super simple to start with.

Our aim with this first task is to establish a relationship with someone that can deliver what we need and then see how we can start developing a more modern and integrated CICD pipeline to support multiple developers
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
There is a very specific initial problem to solve with Alteryx that can't make use of any pushdown to databases i.e. all data is coming via excel and all processing has to be done natively within Alteryx.
We have a ragged hierarchy expressed in a set of tables and the complexity is that each hierarchy can be composed of sub-hierarchies that can be expressed at different levels.  This is solved easily in SQL with a conditional outer join, but this is proving tricky to replicate in Alteryx natively.
~~~
```

# 8.
`Aᨀ` ≔ 
```
The Alteryx One Platform: https://www.alteryx.com/products/alteryx-platform)
Именн о ней `ꆜ` пишет в `PD`
```

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
Задача моделирования ragged hierarchy в Alteryx One Platform решается так:
1) Подготовка данных (Основной Workflow)
Перед началом итеративной обработки необходимо консолидировать данные из всех исходных таблиц в единую структуру.
1.1) Импортировать данные.
Использовать инструмент «Input Data» для загрузки всех таблиц Excel, описывающих иерархию.
1.2) Консолидировать и нормализовать структуру.
Объединить данные из разных таблиц в единый поток данных со структурой списка смежности (Adjacency List), то есть в формате Parent-Child.
Этот этап может потребовать сложной логики для соединения таблиц, представляющих разные уровни или суб-иерархии (ragged hierarchy).
Если для связи исходных таблиц требуется логика, аналогичная SQL Conditional Outer Join (как указано в описании проекта), где условия включены в предикат `ON` (e.g., `... ON L.Key = R.Key AND [Condition]`), необходимо реализовать её на этом этапе, используя надежный метод, описанный в пункте 2.2.
Этот метод требует комбинации нескольких инструментов (e.g., «Record ID», «Join», «Filter», «Union») для точной репликации логики SQL и обеспечения корректного количества строк.
Результирующий набор данных (далее `Hierarchy_Data`) должен содержать как минимум поля идентификатора родителя (например, `ParentID`), идентификатора потомка (например, `ChildID`), а также все поля, необходимые для условной логики соединения (далее `ConditionFields`).
Единая структура Parent-Child необходима для универсальной реализации итеративной логики обхода иерархии.
1.3) Определить начальные узлы.
Определить узлы, с которых начнется обход иерархии (например, корневые узлы, где `ParentID` равен `Null`). Использовать инструмент «Filter».
1.4) Подготовить данные для итерации.
Для реализации обхода иерархии (например, для её развертывания в плоский список отношений Предок-Потомок) необходимо добавить служебные поля к начальным узлам. 
Использовать инструмент «Formula» для добавления полей:
- `AncestorID`: Идентификатор предка (изначально равен идентификатору самого узла).
- `CurrentID`: Идентификатор текущего узла (изначально равен идентификатору самого узла).
- `Level`: Уровень иерархии (изначально 0 или 1).
- `PathHistory`: Путь от корня иерархии до текущего узла для обнаружения циклических ссылок (изначально строка, содержащая идентификатор узла с разделителями, e.g., формула `'|' + ToString([CurrentID]) + '|'`).
Этот набор данных (далее `Initial_Nodes`) инициирует процесс.
2) Реализация Conditional Join в Alteryx
Инструмент «Join» в Alteryx поддерживает только соединения на основе равенства (equi-joins).
Поэтому для репликации условной логики необходимо использовать комбинацию инструментов после «Join».
2.1) Реализация Conditional Inner Join.
Если требуется включить в результат только те записи, для которых совпали ключи и выполнено условие:
2.1.1) Использовать инструмент «Join» для соединения по ключам.
2.1.2) Подключить инструмент «Filter» к выходу «J» (Joined) инструмента «Join».
2.1.3) Сконфигурировать «Filter» для проверки дополнительных условий (`ConditionFields`).
2.1.4) Выход «T» (True) инструмента «Filter» содержит результат Conditional Inner Join.
2.2) Реализация Conditional Outer Join (например, Left Outer Join).
Если требуется реплицировать логику SQL `LEFT OUTER JOIN`, где дополнительные условия включены в предикат `ON` (e.g., `... ON L.Key = R.Key AND [Condition]`), необходимо использовать подход, который определяет сам факт успешного соединения на основе всех условий.
Обоснование необходимости этого метода (паттерн «Double Join») заключается в различии между условиями, указанными в предикате `ON` и предикате `WHERE` в SQL.
При `LEFT OUTER JOIN` условия в предикате `ON` определяют, происходит ли соединение, но не приводят к фильтрации записей из левой таблицы, если условие ложно (поля из правой таблицы заполняются `Null`).
Условия в предикате `WHERE` применяются после соединения и фильтруют результирующий набор данных.
Стандартный подход в Alteryx (объединение выходов «L» и «J» инструмента «Join» через «Union») с последующим применением инструмента «Filter» эквивалентен логике предиката `WHERE`.
Этот подход некорректно обрабатывает условное соединение по предикату `ON`, так как может отфильтровать записи левой таблицы, которые должны быть сохранены.
Паттерн «Double Join» точно реплицирует логику предиката `ON`, что критически важно для сохранения целостности данных, особенно при отношениях N-to-M (Many-to-Many).
2.2.1) Обеспечить уникальность записей левой таблицы.
Для однозначной идентификации записей необходимо убедиться, что левый поток данных имеет уникальный идентификатор.
Если его нет, использовать инструмент «Record ID» для создания нового поля (e.g., `L_ID`).
2.2.2) Выполнить Conditional Inner Join.
Реализовать логику, описанную в пункте 2.1, используя подготовленный левый поток (шаг 2.2.1) и правый поток.
Результат (выход «T» инструмента «Filter», далее `Joined_Conditional`) содержит успешно соединенные записи, включая уникальный идентификатор (`L_ID`).
2.2.3) Идентифицировать истинно несоединенные записи (Left Unjoined).
Необходимо найти записи из левого потока, для которых не было найдено ни одного соответствия полному условию соединения.
2.2.3.1) Добавить второй инструмент «Join».
Соединить подготовленный левый поток (шаг 2.2.1, вход «L») и `Joined_Conditional` (шаг 2.2.2, вход «R»).
2.2.3.2) Сконфигурировать соединение по уникальному идентификатору (e.g., `L_ID`).
2.2.3.3) Выход «L» (Left Unjoined) этого инструмента содержит искомые несоединенные записи (далее `Unjoined_L`).
2.2.4) Финальное объединение.
Использовать инструмент «Union» для объединения `Joined_Conditional` (шаг 2.2.2) и `Unjoined_L` (шаг 2.2.3.3).
Инструмент «Union» автоматически согласует схемы данных, заполняя поля из правой таблицы значениями Null для потока `Unjoined_L` (при соответствующей конфигурации, e.g., «Auto Configure by Name»).
2.2.5) Завершение.
При необходимости использовать инструмент «Select» для удаления служебного уникального идентификатора (e.g., `L_ID`) и упорядочивания полей.
3) Создание Iterative Macro
Необходимо создать отдельный Workflow для реализации рекурсивной логики. 
В большинстве случаев для обхода иерархии в рекурсивном шаге используется логика Inner Join (нахождение существующих связей).
3.1) Установить тип Workflow.
В новом Workflow открыть панель «Workflow Configuration». 
На вкладке «Workflow» в разделе «Type» выбрать «Macro», затем «Iterative Macro».
«Iterative Macro» выполняет процесс циклически, передавая результаты одной итерации на вход следующей, что позволяет обрабатывать данные рекурсивно или до выполнения определенного условия. 
3.2) Определить входы макроса.
Добавить два инструмента «Macro Input» из категории «Interface».
3.2.1) Итерационный вход (например, `Input_I`).
Принимает данные для текущей итерации. 
Схема должна соответствовать `Initial_Nodes` (поля `AncestorID`, `CurrentID`, `Level`).
3.2.2) Фиксированный вход (например, `Input_H`).
Принимает полный набор данных иерархии (`Hierarchy_Data`).
3.3) Реализовать логику итерации и условное соединение.
Необходимо найти следующий уровень иерархии.
Для рекурсивного обхода иерархии применяется логика Conditional Inner Join (см. пункт 2.1).
Цель итеративного процесса — обнаружение существующих связей (потомков), удовлетворяющих заданным условиям, для продолжения обхода по этим ветвям.
Логика Conditional Outer Join (упомянутая в описании проблемы) применяется при необходимости сохранения записей, для которых условие не выполнено (например, на этапе консолидации данных в пункте 1.2), но не подходит для механизма рекурсивного обхода внутри «Iterative Macro».
Использование Outer Join приведет к невозможности завершения макроса, так как поток данных, передаваемый на итерационный выход (`Output_I`), никогда не станет пустым (стандартное условие остановки не будет достигнуто).
3.3.1) Добавить инструмент «Join». Соединить `Input_I` (вход «L») и `Input_H` (вход «R»).
3.3.2) Сконфигурировать соединение: `L.CurrentID` = `R.ParentID`.
3.3.3) Добавить инструмент «Filter», подключенный к выходу «J».
3.3.4) Сконфигурировать «Filter» на основе `ConditionFields` из `Input_H` (и, возможно, данных из `Input_I`).
Выход «T» (True) содержит потенциальных кандидатов для следующей итерации (далее `Candidates`).
3.3.5) Реализовать механизм обнаружения циклических ссылок.
Для предотвращения бесконечных циклов необходимо проверить, не был ли новый узел (`ChildID` из `Input_H`) уже посещен в текущей ветви иерархии.
Добавить второй инструмент «Filter», подключенный к потоку `Candidates`.
3.3.6) Сконфигурировать проверку цикла.
Использовать функцию для поиска идентификатора потомка (`R.ChildID`) внутри поля `PathHistory` (из `Input_I`).
E.g., формула `Contains([L.PathHistory], "|" + ToString([R.ChildID]) + "|")`.
Использование разделителей (как определено в пункте 1.4) обеспечивает надежность проверки, предотвращая ложные срабатывания на частичных совпадениях идентификаторов (e.g., ID 12 и ID 123).
3.3.7) Обработать результаты проверки.
Выход «F» (False) содержит валидные соединения без циклов (далее `Valid_Next_Level`).
Выход «T» (True) содержит обнаруженные циклические ссылки (далее `Cyclic_Records`).
3.4) Подготовить данные для следующей итерации.
Поток `Valid_Next_Level` (шаг 3.3.7) содержит успешные соединения. Необходимо обновить данные для следующего шага.
3.4.1) Добавить инструмент «Formula», подключенный к потоку `Valid_Next_Level`.
3.4.2) Обновить поля:
- `AncestorID`: оставить значение из `Input_I` (переносится через итерации).
- `CurrentID`: установить значение `ChildID` из `Input_H` (новый текущий узел).
- `Level`: увеличить значение на 1 (использовать формулу `[Level] + 1`).
- `PathHistory`: добавить новый узел (`CurrentID`) к существующему пути (использовать формулу `[PathHistory] + ToString([CurrentID]) + "|"`).
Системную переменную `[Engine.IterationNumber]` (которая начинается с 0) также можно использовать для расчета уровня.
Однако это требует учета начального уровня, заданного в пункте 1.4 (e.g., формула `[Начальный_Уровень] + [Engine.IterationNumber] + 1`).
Явная передача и инкрементация поля `Level` обеспечивает большую гибкость, если разные ветви иерархии начинаются с разных уровней.
3.4.3) Использовать инструмент «Select» для обеспечения соответствия схемы данных схеме `Input_I`.
Требования к строгости соответствия зависят от выбранного режима «Output Mode» в конфигурации макроса (см. пункт 4.3).
3.5) Определить выходы макроса.
Добавить два инструмента «Macro Output».
3.5.1) Выход результата (например, `Output_R`).
Подключить выход инструмента «Select» (шаг 3.4.3).
На этот выход поступают данные (связи Предок-Потомок), сгенерированные только в рамках текущей итерации (дельта).
Alteryx Engine автоматически выполняет операцию «Union» для накопления результатов всех итераций в финальном выходном потоке макроса.
3.5.2) Итерационный выход (например, `Output_I`).
Также подключить выход инструмента «Select» (шаг 3.4.3). 
Эти данные передаются обратно на `Input_I`. 
Макрос остановится, когда этот выход будет пуст.
3.5.3) Выход циклических данных (например, `Output_C`).
Подключить поток `Cyclic_Records` (шаг 3.3.7).
Этот выход позволяет изолировать и проанализировать записи, формирующие циклические ссылки в иерархии, не включая их в основной результат итеративного процесса.
4) Конфигурация параметров макроса
4.1) Открыть Interface Designer.
Перейти в меню «View» → «Interface Designer».
4.2) Настроить свойства итерации.
Перейти в раздел «Properties» (иконка гаечного ключа или шестеренки).
4.2.1) В поле «Iteration Input» выбрать `Input_I`.
4.2.2) В поле «Iteration Output» выбрать `Output_I`.
4.2.3) В поле «Maximum Number of Iterations» установить достаточно большое значение (например, 100).
Это значение служит механизмом защиты (fail-safe) для предотвращения непредвиденного бесконечного выполнения Workflow, хотя основная логика обнаружения циклических ссылок реализована внутри макроса (шаг 3.3.5).
Обоснование: Эти настройки определяют, как Alteryx Engine управляет потоком данных между итерациями.
4.3) Настроить режим вывода.
Перейти в раздел «Properties» в «Interface Designer».
В поле «Output Mode» выбрать режим объединения результатов итераций.
Рекомендуется использовать «Auto Configure by Name (Wait until all Iterations run)».
При использовании этого режима требуется совпадение имен и типов данных полей; строгий порядок полей не обязателен.
При использовании режима «Auto Configure by Position» требуется точное совпадение типов и порядка полей.
4.4) Сохранить макрос (например, как файл `ProcessHierarchy.yxmc`).
5) Выполнение (Основной Workflow)
5.1) Вставить макрос.
В основном Workflow кликнуть правой кнопкой мыши на холсте → «Insert» → «Macro...» и выбрать файл `ProcessHierarchy.yxmc`.
5.2) Подключить данные.
5.2.1) Соединить `Hierarchy_Data` (шаг 1.2) с входом `Input_H` макроса.
5.2.2) Соединить `Initial_Nodes` (шаг 1.4) с входом `Input_I` макроса.
5.3) Обработать результаты.
Выход `Output_R` макроса содержит развернутую иерархию (все связи Предок-Потомок, начиная с уровня 1).
Описанная логика «Iterative Macro» не включает сами начальные узлы (уровень 0) в этот выходной поток.
Для получения полного набора данных иерархии необходимо использовать инструмент «Union», чтобы объединить начальные узлы (`Initial_Nodes`) с результатом работы макроса (`Output_R`).
~~~

# 3.
## 3.1.
`D2` ≔ (начальная часть `D`, переведённая с `L_SOURCE` на `L_TARGET`)

## 3.2.
Содержание `D2`:
~~~markdown
The problem of modeling a ragged hierarchy in Alteryx One Platform is solved as follows:
1) Data Preparation (Main Workflow)
Before starting the iterative processing, it is necessary to consolidate the data from all source tables into a single structure.
1.1) Import data.
Use the «Input Data» tool to load all Excel tables describing the hierarchy.
1.2) Consolidate and normalize the structure.
Combine the data from the various tables into a single data stream with an adjacency list structure (Adjacency List), that is, in a Parent-Child format.
This stage may require complex logic to join the tables representing different levels or sub-hierarchies (ragged hierarchy).
If the logic analogous to the SQL Conditional Outer Join (as specified in the project description) is required to connect the source tables, where the conditions are included in the `ON` predicate (e.g., `... ON L.Key = R.Key AND [Condition]`), it is necessary to implement it at this stage using the reliable method described in point 2.2.
This method requires a combination of several tools (e.g., «Record ID», «Join», «Filter», «Union») to accurately replicate the SQL logic and ensure the correct number of rows.
The resulting data set (hereinafter `Hierarchy_Data`) must contain at least the parent identifier field (e.g., `ParentID`), the child identifier field (e.g., `ChildID`), and all fields required for the conditional join logic (hereinafter `ConditionFields`).
A unified Parent-Child structure is necessary for the universal implementation of the iterative hierarchy traversal logic.
1.3) Define the initial nodes.
Define the nodes where the hierarchy traversal will start (e.g., the root nodes where `ParentID` is `Null`). Use the «Filter» tool.
1.4) Prepare data for iteration.
To implement the hierarchy traversal (e.g., to expand it into a flat list of Ancestor-Descendant relationships), it is necessary to add auxiliary fields to the initial nodes.
Use the «Formula» tool to add fields:
- `AncestorID`: The ancestor identifier (initially equal to the identifier of the node itself).
- `CurrentID`: The current node identifier (initially equal to the identifier of the node itself).
- `Level`: The hierarchy level (initially 0 or 1).
- `PathHistory`: The path from the root of the hierarchy to the current node to detect cyclical references (initially a string containing the node identifier with delimiters, e.g., the formula `'|' + ToString([CurrentID]) + '|'`).
This data set (hereinafter `Initial_Nodes`) initiates the process.
2) Implementation of Conditional Join in Alteryx
The «Join» tool in Alteryx supports only equality-based joins (equi-joins).
Therefore, to replicate the conditional logic, it is necessary to use a combination of tools after the «Join» tool.
2.1) Conditional Inner Join Implementation.
If it is required to include in the result only those records for which the keys match and the condition is met:
2.1.1) Use the «Join» tool to join by keys.
2.1.2) Connect the «Filter» tool to the «J» (Joined) output of the «Join» tool.
2.1.3) Configure the «Filter» tool to check the additional conditions (`ConditionFields`).
2.1.4) The «T» (True) output of the «Filter» tool contains the result of the Conditional Inner Join.
2.2) Implementation of the Conditional Outer Join (e.g., Left Outer Join).
If it is required to replicate the logic of the SQL `LEFT OUTER JOIN`, where additional conditions are included in the `ON` predicate (e.g., `... ON L.Key = R.Key AND [Condition]`), it is necessary to use an approach that determines the very fact of a successful join based on all conditions.
The rationale for this method (the «Double Join» pattern) is based on the difference between the conditions specified in the `ON` predicate and the `WHERE` predicate in SQL.
In a `LEFT OUTER JOIN`, the conditions in the `ON` predicate determine whether a join occurs but do not filter records from the left table if the condition is false (the fields from the right table are populated with `Null`).
The conditions in the `WHERE` predicate are applied after the join and filter the resulting data set.
The standard approach in Alteryx (combining the «L» and «J» outputs of the «Join» tool via the «Union» tool) with the subsequent application of the «Filter» tool is equivalent to the logic of the `WHERE` predicate.
This approach incorrectly handles the conditional join on the `ON` predicate, as it may filter out records from the left table that must be preserved.
The «Double Join» pattern accurately replicates the logic of the `ON` predicate, which is critical for preserving data integrity, especially in N-to-M (Many-to-Many) relationships.
2.2.1) Ensure the uniqueness of the records in the left data stream.
To uniquely identify the records, it is necessary to ensure that the left data stream has a unique identifier.
If one does not exist, use the «Record ID» tool to create a new field (e.g., `L_ID`).
2.2.2) Perform the Conditional Inner Join.
Implement the logic described in point 2.1, using the prepared left stream (step 2.2.1) and the right stream.
The result (the «T» output of the «Filter» tool, hereinafter `Joined_Conditional`) contains successfully joined records, including the unique identifier (`L_ID`).
2.2.3) Identify the truly unjoined records (Left Unjoined).
It is necessary to find the records from the left stream for which not a single match was found for the full join condition.
2.2.3.1) Add a second «Join» tool.
Join the prepared left stream (step 2.2.1, «L» input) and `Joined_Conditional` (step 2.2.2, «R» input).
2.2.3.2) Configure the join by the unique identifier (e.g., `L_ID`).
2.2.3.3) The «L» (Left Unjoined) output of this tool contains the target unjoined records (hereinafter `Unjoined_L`).
2.2.4) Final union.
Use the «Union» tool to union `Joined_Conditional` (step 2.2.2) and `Unjoined_L` (step 2.2.3.3).
The «Union» tool automatically reconciles the data schemas, populating the fields from the right table with Null values for the `Unjoined_L` stream (with the appropriate configuration, e.g., «Auto Configure by Name»).
2.2.5) Completion.
If necessary, use the «Select» tool to remove the auxiliary unique identifier (e.g., `L_ID`) and order the fields.
3) Creating an Iterative Macro
It is necessary to create a separate Workflow to implement the recursive logic.
In most cases, to traverse the hierarchy in the recursive step, the Inner Join logic is used (finding existing connections).
3.1) Set the Workflow type.
In a new Workflow, open the «Workflow Configuration» pane.
On the «Workflow» tab, in the «Type» section, select «Macro», then «Iterative Macro».
The «Iterative Macro» executes a process iteratively, passing the results of one iteration to the input of the next, which allows data to be processed recursively or until a certain condition is met.
3.2) Define the macro inputs.
Add two «Macro Input» tools from the «Interface» category.
3.2.1) Iterative input (e.g., `Input_I`).
Accepts data for the current iteration.
The schema must match `Initial_Nodes` (fields `AncestorID`, `CurrentID`, `Level`).
3.2.2) Fixed input (e.g., `Input_H`).
Accepts the complete hierarchy data set (`Hierarchy_Data`).
3.3) Implement the iteration and conditional join logic.
It is necessary to find the next level of the hierarchy.
For the recursive traversal of the hierarchy, the Conditional Inner Join logic is applied (see point 2.1).
The purpose of the iterative process is to detect existing relationships (descendants) that satisfy the specified conditions, to continue the traversal along these branches.
The Conditional Outer Join logic (mentioned in the problem description) is applied when it is necessary to preserve records for which the condition is not met (e.g., at the data consolidation stage in point 1.2), but it is not suitable for the recursive traversal mechanism inside the «Iterative Macro».
The use of an Outer Join will make it impossible for the macro to complete, as the data stream passed to the iterative output (`Output_I`) will never become empty (the standard stopping condition will not be met).
3.3.1) Add a «Join» tool. Join `Input_I` (the «L» input) and `Input_H` (the «R» input).
3.3.2) Configure the join: `L.CurrentID` = `R.ParentID`.
3.3.3) Add a «Filter» tool, connected to the «J» output.
3.3.4) Configure the «Filter» based on `ConditionFields` from `Input_H` (and, possibly, data from `Input_I`).
The «T» (True) output contains potential candidates for the next iteration (hereinafter `Candidates`).
3.3.5) Implement a cyclic reference detection mechanism.
To prevent infinite loops, it is necessary to check whether the new node (`ChildID` from `Input_H`) has already been visited in the current branch of the hierarchy.
Add a second «Filter» tool connected to the `Candidates` stream.
3.3.6) Configure the cycle check.
Use a function to search for the child identifier (`R.ChildID`) inside the `PathHistory` field (from `Input_I`).
E.g., the formula `Contains([L.PathHistory], "|" + ToString([R.ChildID]) + "|")`.
The use of delimiters (as defined in point 1.4) ensures the reliability of the check, preventing false positives on partial identifier matches (e.g., ID 12 and ID 123).
3.3.7) Process the check results.
The «F» (False) output contains the valid connections without cycles (hereinafter `Valid_Next_Level`).
The «T» (True) output contains the detected cyclical references (hereinafter `Cyclic_Records`).
3.4) Prepare data for the next iteration.
The `Valid_Next_Level` stream (step 3.3.7) contains the successful joins. It is necessary to update the data for the next step.
3.4.1) Add the «Formula» tool connected to the `Valid_Next_Level` stream.
3.4.2) Update the fields:
- `AncestorID`: leave the value from `Input_I` (carried over through iterations).
- `CurrentID`: set the value to `ChildID` from `Input_H` (the new current node).
- `Level`: increase the value by 1 (use the formula `[Level] + 1`).
- `PathHistory`: add the new node (`CurrentID`) to the existing path (use the formula `[PathHistory] + ToString([CurrentID]) + "|"`).
The system variable `[Engine.IterationNumber]` (which starts at 0) can also be used to calculate the level.
However, this requires taking into account the initial level set in point 1.4 (e.g., the formula `[Initial_Level] + [Engine.IterationNumber] + 1`).
Explicitly passing and incrementing the `Level` field provides greater flexibility if different branches of the hierarchy start at different levels.
3.4.3) Use the «Select» tool to ensure the data schema matches the `Input_I` schema.
The required strictness of the match depends on the selected «Output Mode» in the macro configuration (see point 4.3).
3.5) Define the macro outputs.
Add two «Macro Output» tools.
3.5.1) Result output (e.g., `Output_R`).
Connect the output of the «Select» tool (step 3.4.3).
The data (Ancestor-Descendant relationships), generated only within the current iteration (the delta), is sent to this output.
The Alteryx Engine automatically performs the «Union» operation to accumulate the results of all iterations in the final output stream of the macro.
3.5.2) Iterative output (e.g., `Output_I`).
Also connect the output of the «Select» tool (step 3.4.3).
This data is passed back to `Input_I`.
The macro will stop when this output is empty.
3.5.3) Cyclical data output (e.g., `Output_C`).
Connect the `Cyclic_Records` stream (step 3.3.7).
This output allows to isolate and analyze the records that form cyclical references in the hierarchy, without including them in the main result of the iterative process.
~~~

# 4.
## 4.1.
`F` ≔ (фрагмент `D`)

## 4.2.
Содержание `F`:
~~~markdown
Описанная логика «Iterative Macro» не включает сами начальные узлы (уровень 0) в этот выходной поток.
Для получения полного набора данных иерархии необходимо использовать инструмент «Union», чтобы объединить начальные узлы (`Initial_Nodes`) с результатом работы макроса (`Output_R`).
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