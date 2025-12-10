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
# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`C` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `C` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021957814134474185065

## 2.2. Title
Senior Backend Engineer | API Performance Optimization (AWS + MongoDB)

## 2.3. Description
`PD` ≔ 
```text
We’re looking for a Senior Backend Engineer to troubleshoot and fix slow API response times (~5s) in our pre-production environment. You’ll profile our AWS + MongoDB stack, identify bottlenecks (code, database, or infrastructure), and implement optimizations to get latency down to production-ready levels. This is a short-term, urgent engagement for someone experienced in API performance tuning and scalability.

Must-Have Skills:
• Strong experience with backend APIs (Node.js/Python/Java)
• Deep knowledge of MongoDB query optimization and indexing
• Familiarity with AWS services (EC2, ECS, Lambda, API Gateway, CloudWatch)
• Experience implementing caching strategies (Redis, in-memory, etc.)
• Proven track record in diagnosing and reducing API latency

Deliverable:
• Diagnose API latency issues
• Recommend and implement fixes (code, database, infra)
• Reduce API response time from ~5s to  1s (P95 target)
```

## 2.4. Tags
- MongoDB
- Amazon Web Services
- API Development

# 3. Информация о `C`
## 3.1. Местоположение
USA
Kirkland

## 3.2. Характеристики компании
### 3.2.1. Сектор экономики
неизвестно

### 3.2.2. Количество сотрудников
неизвестно

## 3.3. Характеристики учётной записи на `UW`
### 3.3.1. Member since
Jul 6, 2025
### 3.3.2. Hire rate (%)
100
### 3.3.3. Количество опубликованных проектов (jobs posted)
3
### 3.3.4. Total spent (USD)
$17K
### 3.3.5. Количество оплаченных часов в почасовых проектах
210

# 4. Другие проекты `C` на `UW`
## 4.1. `P1⁎`

## 4.1.1. Title
MongoDB Load Testing & Performance Analysis (No Code Changes)

## 4.1.2. Description
`P1D` ≔ 
```text
We’re looking for an experienced backend performance engineer to help us identify and resolve performance bottlenecks in our MongoDB Atlas-backed fantasy sports app.

During our real-time draft feature, we’ve noticed lag as user traffic scales up. The app runs smoothly with a few users (4–5), but slows significantly when more users join (target is 100+). We’re already on an M30 cluster, but MongoDB Atlas shows spikes in:

Query execution time

Documents scanned per returned

Opcounters

We suspect the issue may be related to inefficient queries or missing indexes, but we’re not entirely sure. We do not want code changes — just a detailed, data-driven performance analysis and load simulation.

Scope of Work:
Run load tests (simulate 100+ concurrent users hitting relevant endpoints)

Tools: Artillery, k6, Locust, or similar

Monitor MongoDB Atlas metrics during test runs

Identify key performance bottlenecks

Suggest optimizations (e.g., indexing strategy, query tuning)

Deliver a short findings report with clear action items

Requirements:
Proven experience with MongoDB Atlas performance tuning

Deep knowledge of query profiling, indexing, and load testing tools

Ability to interpret Atlas dashboards (Query Targeting, Execution Time, etc.)

Familiarity with real-time apps or socket-based backends is a plus

Must be comfortable analyzing backend behavior without modifying any code
```

## 4.2. `P2⁎`

## 4.2.1. Title
Full Stack – Stealth Fantasy Football App Launch

## 4.2.2. Description
`P2D` ≔ 
```text
We’re a stealth startup reimagining fantasy football. Instead of managing a team solo, users collaborate with friends to make key decisions together. We’re preparing for a Fall launch on iOS and Android and need a sharp, proactive teammate to help bring the product across the finish line. (Note: Our Upwork account may still show our original name, Huddle.)

Project Scope:
We're hiring a QA/UX Support Specialist to work 5–15 hours/week (flexible based on your availability) to test, polish, and improve our mobile experience before launch.

Responsibilities:

Review and test signup and onboarding flows for usability and functionality

Identify bugs, broken flows, and confusing UI/UX elements

Collaborate with our CTO and backend team to log and resolve issues

Recommend helper screens, tooltips, or first-time user walkthroughs to improve clarity

Ensure the app is intuitive and accessible—even for users new to fantasy sports

What We’re Looking For:

You don’t need to be a fantasy football expert—in fact, we welcome a fresh perspective

Detail-oriented, solution-minded, and self-directed

Strong communicator who can give clear, actionable feedback

Experience in mobile QA, usability testing, or product design is a plus

Timeline:
This role starts immediately and could expand into a broader support role through August, helping ensure we’re ready for App Store and Play Store submission.
```

# 5.
## 5.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`}

## 5.2.
`Ps` ≔⠿ {`P⁎`, `P1⁎`, `P2⁎`}

## 5.3.
`Pi` : `Ps`

# 6.
## 6.1.
`S⁎` ≔ 
```
Startup, о котором `C` пишет о нём в `P2D`:
~~~
We’re a stealth startup reimagining fantasy football
~~~
```

## 6.2.
⊤ (Все `Pi` касаются `S⁎`)

# 5.
`P†` ≔†
```
Проблема, о которой `C` пишет в `PD`:
~~~
slow API response times (~5s) in our pre-production environment
~~~
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
`D` ≔ (мой ответ `C`)

## 2.2.
Содержание `D`:
~~~markdown
Из анализа всех 3-х ваших проектов для меня очевидны 2 основные причины вашей проблемы с производительностью:
1) Неподходящая модель данных.
1.1) Рассмотрим, например, «драфт в реальном времени» в вашем приложение для фэнтези-спорта. 
Если выборы каждого пользователя хранятся в одном большом документе его команды, и 12 пользователей в лиге делают выборы каждые 30 секунд, этот документ будет постоянно обновляться. 
Это может привести к конфликтам записи и снижению производительности, поскольку MongoDB должна переписывать весь документ при каждом обновлении. 
Это классическая проблема «раздутого документа» или «неограниченного массива».
1.2) Тут всё предельно очевидно: подобные вашему стартапы почти всегда отдают приоритет скорости разработки, а не оптимальному проектированию схемы на начальном этапе.
Самой быстрой в реализации моделью данных может быть создание больших, сильно вложенных документов (например, документ league, содержащий массив teams, которые, в свою очередь, содержат массив players). 
Такую модель легко осмыслить в коде. 
Она идеально работает для нескольких пользователей, так как чтения быстрые (один запрос документа), а конфликты записи редки. 
Однако, когда 100+ пользователей пытаются одновременно обновить этот единственный документ league во время драфта, они создают массовую конкуренцию за запись и блокировки. 
Это идеально объясняет, почему система «значительно замедляется, когда присоединяется больше пользователей».
2) Неэффективная логика доступа к данным (проблема запросов «N+1»)
2.1) Например, ваше приложение для фэнтези-спорта может делать запрос для получения всех команд в лиге пользователя, а затем в цикле N запросов (по одному для каждой команды) для получения их составов игроков. 
2.2) Проблема «N+1» является прямым и убедительным объяснением всех наблюдаемых симптомов: 
- высокой задержки (~5с)
- деградации под нагрузкой 
- всплесков количества запросов («Opcounters»). 
2.3) Причинно-следственная связь.
Предположим, запрос на получение статуса драфта лиги включает паттерн «N+1».
2.3.1) Для лиги из 12 команд это 1 + 12 = 13 запросов на один API-вызов. 
Если каждый запрос имеет скромную задержку в 50 мс на обращение к Atlas, общее время уже составляет 13×50мс=650мс только за счет сетевых накладных расходов, не считая времени выполнения.
2.3.2) Теперь рассмотрим 10 одновременных пользователей, делающих этот запрос. 
Это генерирует 130 запросов, поступающих в базу данных за короткий промежуток времени, что объясняет всплеск «Opcounters». 
База данных должна обслуживать 130 одновременных операций, что приводит к переключению контекста и возможным очередям, увеличивая время выполнения каждого отдельного запроса. 
Сервер приложения (особенно если это однопоточный Node.js) может быть заблокирован в ожидании этих 130 ответов от базы данных, что приведет к постановке в очередь других входящих API-запросов. 
Сочетание сетевых накладных расходов, конкуренции за ресурсы базы данных и очередей на уровне приложения может легко объяснить наблюдаемую задержку в ~5 секунд под нагрузкой. 
~~~

# 3.
## 3.1.
`D2` ≔ (начальная часть `D`, переведённая с `L_SOURCE` на `L_TARGET`)

## 3.2.
Содержание `D2`:
~~~markdown
From my analysis of all 3 of your Upwork projects, 2 main reasons for your performance issue are clear to me:
1) Inappropriate data model.
1.1) Consider, e.g., the «real-time draft» in your fantasy sports application.
If each user's picks are stored in a single large document for their team, and 12 users in a league are making picks every 30 seconds, this document will be constantly updated.
This can lead to write conflicts and performance degradation, as MongoDB has to rewrite the entire document on every update.
This is the classic «bloated document» or «unbounded array» problem.
1.2) The explanation is perfectly straightforward: startups like yours almost always prioritize development speed over optimal schema design at the initial stage.
The quickest data model to implement might be the creation of large, deeply nested documents (e.g., a league document containing an array of teams, which in turn contain an array of players).
Such a model is easy to reason about in code.
It works perfectly for a few users, as reads are fast (a single document query), and write conflicts are rare.
However, when 100+ users attempt to update this single league document simultaneously during the draft, they create massive write contention and locking.
This perfectly explains why the system «slows significantly when more users join».
2) Inefficient data access logic (the «N+1» queries problem).
2.1) E.g., your fantasy sports application may make a query to get all the teams in a user's league, and then in a loop N queries (one for each team) to get their player rosters.
2.2) The «N+1» problem is a direct and compelling explanation for all the observed symptoms:
- high latency (~5s)
- degradation under load
- spikes in the number of requests («Opcounters»).

2.3) Causal relationship.
Let us assume the request to get the league draft status includes the «N+1» pattern.
2.3.1) For a 12-team league, this means 1 + 12 = 13 queries per API call.
If each query has a modest latency of 50 ms for a roundtrip to Atlas, the total time is already 13×50ms=650ms from network overhead alone, not counting execution time.
2.3.2) Now, consider 10 concurrent users making this request.
This generates 130 requests arriving at the database in a short period, which explains the spike in «Opcounters».
~~~

# 4.
## 4.1.
`F` ≔ (фрагмент `D`)

## 4.2.
Содержание `F`:
~~~markdown
Сочетание сетевых накладных расходов, конкуренции за ресурсы базы данных и очередей на уровне приложения может легко объяснить наблюдаемую задержку в ~5 секунд под нагрузкой. 
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
~~~~~~