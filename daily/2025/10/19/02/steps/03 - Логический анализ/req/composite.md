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
Сегодня 2025-10-19.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021979266630306721217

## 2.2. Title
Infor Lawson Troubleshooting Expert Needed

## 2.3. Description
`PD` ≔ 
```text
We are seeking an expert to troubleshoot and resolve recurring issues with our on-premise Infor Lawson installation on a Windows 2016 Server. 
The application becomes unresponsive every 2-3 weeks, requiring a server reboot. 
A SQL DBA has ruled out SQL server issues, so we need someone with expertise in Infor Lawson and Windows Server to identify and fix the problem. 
This is a one-time engagement focused on troubleshooting and repair.

# Deliverables
- Perform a thorough review of the Infor Lawson installation
- Identify the cause of application unresponsiveness
- Implement a solution to prevent future issues
- Provide a report on findings and actions taken
```

## 2.4. Tags
Windows Server
Windows Administration
Microsoft Active Directory
Microsoft Server
Infor Lawson
Windows Server 2016
SQL Server

# 5. Информация о `ꆜ`
## 5.1. Местоположение

United States
San Francisco

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
100-1,000 people

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Oct 4, 2017
### 5.3.2. Hire rate (%)
75
### 5.3.3. Количество опубликованных проектов (jobs posted)
39
### 5.3.4. Total spent (USD)
246K
### 5.3.5. Количество оплаченных часов в почасовых проектах
2279
### 5.3.6. Средняя почасовая ставка (USD)
103.51

# 6.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
The application becomes unresponsive every 2-3 weeks, requiring a server reboot.
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
In my experience, your problem is most likely caused by one of the following 3 reasons:
1) Java Heap Leak
1.1) Essence
Infor Lawson often runs on Java application servers, such as IBM WebSphere.
A heap memory leak occurs when the application retains references to objects that are no longer in use.
The Garbage Collector (`GC`) cannot free this memory because the objects are considered active.
Over 2-3 weeks, these objects accumulate, filling up the available heap.
This leads to frequent and prolonged GC Thrashing, which consumes CPU resources and makes the application extremely slow or completely unresponsive.
1.2) Rationale
Symptoms of gradual performance degradation ending in unresponsiveness are a classic sign of a Java memory leak.
The 2-3 week periodicity indicates a slow leak, which is characteristic of complex enterprise systems.
Even if an `OutOfMemoryError` does not occur, continuous `GC` activity can completely paralyze the application.
There are known cases of leaks in WebSphere components, e.g., during the processing of EJB calls, which led to memory exhaustion.
2) Connection Pool Exhaustion
2.1) Essence
The application uses a connection pool on the application server to interact with SQL Server.
A connection leak occurs when the application retrieves a connection from the pool but, due to errors in the code, does not return it after use.
Over time, all available connections in the pool become occupied.
New requests to the application hang while waiting for an available connection, which makes the application unresponsive.
2.2) Rationale
Connection pool exhaustion is a common cause of application unresponsiveness when the application itself and the database appear to be functioning correctly.
This issue occurs on the application server side, which is why the database administrator (DBA), who only checked the SQL Server, might have missed it.
In WebSphere, this problem often manifests as the `J2CA0045E` error (`ConnectionWaitTimeoutException`), when the maximum number of connections is reached.
The use of shared connections in combination with long-running transactions can hold connections even after the application has called the `close` method.
3) Windows handle leak or WMI resource exhaustion
3.1) Essence
Handles are Windows resources used for tracking open objects, such as files, threads, registry keys, and network connections.
If a process (the Lawson application or monitoring services) does not close handles after use, a leak occurs.
Frequent or inefficient queries to Windows Management Instrumentation (WMI) can cause a memory or handle leak in the WMI service (Winmgmt) or the `WmiPrvse.exe` process.
When the handle count reaches the system limit or the WMI service becomes unstable, the application and the server slow down and hang.
3.2) Rationale
Handle leaks accumulate slowly and match the 2-3 week timeframe.
WMI issues caused by problematic or frequent queries from monitoring systems are a common cause of performance degradation on Windows servers.
~~~

# 2.
# 2.1.
`Fⰳ(§p)` ≔ (Пункт `§p` из `Aᨀ`)

# 2.2.
`Fⰳ(§a-§b)` ≔ (Фрагмент `Aᨀ` с пункта `§a` по пункт `§b` включительно)

# 3.
`Fᨀ` ≔ `Fⰳ(3)`

# 4. `᛭T`
Проанализируй `Fᨀ`:
1) Есть ли там логические ошибки?
2) Есть ли там фактические ошибки?

# 5. Требования к твоему ответу
## 5.1.
Отвечай на русском языке.
## 5.2.
Мой вопрос не пересказывай.
## 5.3.
Уже сформулированную мной информацию не пересказывай.
## 5.4.
Писать свою версию `Fᨀ` не нужно: просто укажи свои замечания по пунктам.
## 5.5.
До и после списка замечаний ничего не пиши.
## 5.6.
Нумерация замечаний должна быть сквозной.
## 5.7.
Для каждого своего замечания указывай свою степень уверенности в нём по шкале от 0 до 100:
- 0 означает, что твоё замечание безосновательно (ошибочно).
- 100 означает, что ты полностью уверен в правоте своего замечания.

# 6. К чему не надо придираться
## 6.1.
Если большая часть `Fᨀ` — на русском языке, то не придирайся к смешению в `Fᨀ` русского и английского языков.
Это смешение — временное и будет устранено позже.
~~~~~~