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
https://www.upwork.com/jobs/Fullstack-engineer_~021965240525051208856

## 2.2. Title
https://www.upwork.com/jobs/Fullstack-engineer_~021965240525051208856

## 2.3. Description
`PD` ≔ 
```text
Looking for a full stack developer who can utilize C++ backend, react front end and link it up to MongoDB.

Ideal candidate will be able to design solutions from scratch and iterate with the owner to deliver a working product.
```

## 2.4. Tags
C++
JavaScript
React
MongoDB


# 3. Информация о `ꆜ`
## 3.1. Местоположение
United States

## 3.2. Характеристики компании
### 3.2.1. Сектор экономики
неизвестно

### 3.2.2. Количество сотрудников
неизвестно

## 3.3. Характеристики учётной записи на `UW`
### 3.3.1. Member since
Sep 9, 2025
### 3.3.2. Hire rate (%)
0
### 3.3.3. Количество опубликованных проектов (jobs posted)
1
### 3.3.4. Total spent (USD)
0
### 3.3.5. Количество оплаченных часов в почасовых проектах
0
### 3.3.6. Средняя почасовая ставка (USD)
0

# 4. Другие проекты `ꆜ` на `UW`
отсутствуют

# 5.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
utilize C++ backend, react front end and link it up to MongoDB
~~~
```

# 6
`S⠿` ≔ ⠿~ (Способы решения `T⁎`)

# 12
`Sᵢ` : `S⠿`


 
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
1) Способ интеграции C++ с MongoDB очевиден — `mongocxx`: https://github.com/mongodb/mongo-cxx-driver
2) А вот для интеграции C++ с React я вижу 5 альтернатив.
Их я описываю в пунктах 3-7 ниже.
Лучшую из них я намеренно описываю последней (пункт 7): чтобы понять, что она — лучшая, надо сначала увидеть недостатки других.
3) REST API на C++
3.1) Суть: бэкенд на C++ реализует HTTP-сервер (используя фреймворки, такие как Drogon, Oat++, или библиотеки вроде Boost.Beast) и предоставляет RESTful эндпоинты.
React использует стандартные HTTP-клиенты (Fetch, Axios).
3.2) Достоинства
3.2.1) REST/JSON является отраслевым стандартом, что упрощает разработку на React, отладку и интеграцию.
3.2.2) Простота развертывания и горизонтального масштабирования (Stateless).
3.2.3) Современные C++ фреймворки обеспечивают высокую пропускную способность и низкую задержку. 
3.3) Недостатки
3.3.1) Реализация веб-сервисов на C++ значительно сложнее и медленнее, чем на языках, ориентированных на веб (Node.js, Python). 
3.3.2) Ограниченная экосистема: меньшее количество зрелых библиотек для типичных веб-задач (аутентификация, интеграции).
3.3.3) Высокие риски безопасности.
C++ является memory-unsafe языком.
Реализация публичных веб-сервисов непосредственно на C++ значительно повышает риски уязвимостей, связанных с управлением памятью (e.g., buffer overflow, use-after-free).
4) gRPC и gRPC-Web
4.1) Суть: gRPC — это высокопроизводительный RPC-фреймворк, использующий Protocol Buffers (Protobuf) для бинарной сериализации и HTTP/2 для транспорта.
4.2) Достоинства
4.2.1) Бинарный формат и HTTP/2 обеспечивают более быструю связь и меньший размер сообщений по сравнению с REST/JSON.
4.2.2) Строгая типизация и генерация кода: контракт API определяется в `.proto` файлах, из которых генерируется код клиента (TypeScript) и сервера (C++), минимизируя ошибки.
4.2.3) Нативная поддержка потоковой передачи данных.
4.3) Недостатки
4.3.1) Браузеры не поддерживают нативный gRPC.
Требуется использование gRPC-Web и развертывание proxy для трансляции запросов между протоколами gRPC-Web и gRPC.
Это усложняет архитектуру и DevOps.
4.3.2) Сложность отладки: бинарный формат затрудняет инспекцию сетевых запросов стандартными инструментами.
5) WebSockets
5.1) Суть: WebSockets — это протокол, обеспечивающий постоянное, полнодуплексное соединение между React и C++ (с использованием библиотек вроде WebSocket++ или uWebSockets).
5.2) Достоинства
5.2.1) Обеспечивает наименьшую задержку и мгновенную двунаправленную передачу данных (Server Push).
5.2.2) Минимальные накладные расходы после установки соединения.
5.3) Недостатки
5.3.1) Непригодность для стандартного CRUD. 
Не оптимизирован для модели запрос-ответ.
Необходимо реализовывать собственный протокол (например, JSON-RPC) поверх него. 
5.3.2)  Управление постоянными соединениями усложняет горизонтальное масштабирование и балансировку нагрузки.
5.3.3) Высокие риски безопасности.
Аналогично пункту 3.3.3, реализация публичного WebSocket сервера на C++ значительно повышает риски критических уязвимостей.
6) GraphQL API на C++
6.1) Достоинства
6.1.1) Эффективность данных: Позволяет клиенту запросить только нужные поля, решая проблему over/under-fetching.
6.1.2) Отличный Developer Experience (DX) в React: Зрелая экосистема на фронтенде (Apollo Client).
6.2) Недостатки
6.2.1) Крайне незрелая экосистема C++
Существует очень мало зрелых и поддерживаемых библиотек для реализации GraphQL-серверов на C++. 
Реализация потребует огромных усилий и несет высокие риски. 
6.2.2) Высокая сложность бэкенда: Сложность реализации парсинга запросов и эффективных резолверов на C++.
6.2.3) Высокие риски безопасности.
Аналогично пункту 3.3.3, реализация сложного парсинга GraphQL запросов на C++ значительно повышает риски критических уязвимостей.
7) Гибридная архитектура (API Gateway + C++)
7.1) Суть: фронтенд взаимодействует с API Gateway, созданным на языке, более приспособленном для веба (e.g., Node.js/TypeScript).
Этот шлюз предоставляет публичный REST или GraphQL API.
Основная бизнес-логика и взаимодействие с MongoDB (используя `mongocxx`, как указано в пункте 1) реализуются в сервисе на C++.
API Gateway взаимодействует с сервисом на C++ через высокопроизводительный внутренний протокол (e.g., нативный gRPC или очереди сообщений).
7.2) Достоинства
7.2.1) Баланс производительности и скорости разработки.
Использует сильные стороны обеих технологий.
Node.js позволяет быстро разрабатывать веб-API и легко интегрируется с React.
C++ используется для реализации основной бизнес-логики и слоя данных.
7.2.2) Разделение ответственности: шлюз обрабатывает веб-аспекты (аутентификация, CORS, маршрутизация), освобождая сервис на C++ от этих задач.
7.2.3) Позволяет использовать богатые экосистемы обеих платформ.
7.2.4) Упрощает итеративную разработку.
7.2.5) Повышенная безопасность.
API Gateway реализуется на memory-safe языке (e.g., Node.js/TypeScript, Go).
Это устраняет целый класс уязвимостей, связанных с управлением памятью, на публичном периметре приложения.
7.3) Недостатки
7.3.1) Больше движущихся частей (два сервиса вместо одного). 
7.3.2) Увеличение задержки: вводит дополнительный сетевой прыжок (React → Gateway → C++).
8) Анализ требований и приоритетов.
8.1) Судя по фразе «design solutions from scratch and iterate with the owner to deliver a working product», приоритетом является скорость разработки и возможность быстрых итераций.
8.2) При этом требование использовать C++ для backend в контексте веб-приложения само по себе является главным препятствием для быстрого создания продукта.
Разработка на C++ значительно сложнее и медленнее, чем на языках, более ориентированных на веб (e.g., Node.js, Python, Go).
9) Выводы 
Исходя из пункта 8.1:
9.1) Реализация веб-слоя непосредственно на C++ (способы пунктов 3, 5, 6) значительно замедлит разработку и усложнит итерации из-за сложности языка и относительной незрелости его веб-экосистемы.
9.2) Способ пункта 4 вводит неоправданную сложность инфраструктуры (Envoy proxy) для нового проекта.
9.3) Поэтому я рекомендую способ пукта 7.
Он обеспечивает наилучший баланс для данного контекста. 
Он удовлетворяет требованию использования C++ backend для реализации основной бизнес-логики, одновременно используя более подходящую технологию (например, Node.js) для веб-слоя. 
Это позволит быстро создать рабочий продукт.

~~~

# 3.
## 3.1.
`D2` ≔ (начальная часть `D`, переведённая с `L_SOURCE` на `L_TARGET`)

## 3.2.
Содержание `D2`:
~~~markdown
1) The method for integrating C++ with MongoDB is obvious — `mongocxx`: https://github.com/mongodb/mongo-cxx-driver
2) As for integrating C++ with React, I see 5 alternatives.
I describe them in points 3-7 below.
The best of them I intentionally describe last (point 7): to understand why it is the best, it is necessary to first see the disadvantages of the others.
3) REST API in C++
3.1) Essence: the C++ backend implements an HTTP server (using frameworks such as Drogon, Oat++, or libraries like Boost.Beast) and provides RESTful endpoints.
React uses standard HTTP clients (Fetch, Axios).
3.2) Advantages
3.2.1) REST/JSON is an industry standard, which simplifies development in React, debugging, and integration.
3.2.2) Ease of deployment and horizontal scaling (stateless).
3.2.3) Modern C++ frameworks provide high throughput and low latency.
3.3) Disadvantages
3.3.1) Implementing web services in C++ is significantly more complex and slower than in web-oriented languages (Node.js, Python).
3.3.2) Limited ecosystem: fewer mature libraries for typical web tasks (authentication, integrations).
3.3.3) High security risks.
C++ is a memory-unsafe language.
Implementing public web services directly in C++ significantly increases the risks of vulnerabilities related to memory management (e.g., buffer overflow, use-after-free).
4) gRPC and gRPC-Web
4.1) Essence: gRPC is a high-performance RPC framework that uses Protocol Buffers (Protobuf) for binary serialization and HTTP/2 for transport.
4.2) Advantages
4.2.1) The binary format and HTTP/2 provide faster communication and smaller message sizes compared to REST/JSON.
4.2.2) Strict typing and code generation: the API contract is defined in .proto files, from which client (TypeScript) and server (C++) code is generated, minimizing errors.
4.2.3) Native support for data streaming.
4.3) Disadvantages
4.3.1) Browsers do not support native gRPC.
It requires using gRPC-Web and deploying a proxy to translate requests between the gRPC-Web and gRPC protocols.
This complicates the architecture and DevOps.
4.3.2) Debugging complexity: the binary format makes it difficult to inspect network requests with standard tools.
5) WebSockets
5.1) Essence: WebSockets is a protocol that provides a persistent, full-duplex connection between React and C++ (using libraries such as WebSocket++ or uWebSockets).
5.2) Advantages
5.2.1) Provides the lowest latency and instantaneous bidirectional data transfer (Server Push).
5.2.2) Minimal overhead after connection establishment.
5.3) Disadvantages
5.3.1) Unsuitability for standard CRUD.
Not optimized for the request-response model.
It is necessary to implement a custom protocol (e.g., JSON-RPC) on top of it.
5.3.2) Managing persistent connections complicates horizontal scaling and load balancing.
5.3.3) High security risks.
Similar to point 3.3.3, implementing a public WebSocket server in C++ significantly increases the risks of critical vulnerabilities.
6) GraphQL API на C++
6.1) Advantages
6.1.1) Data efficiency: Allows the client to request only the necessary fields, solving the over/under-fetching problem.
6.1.2) Excellent Developer Experience in React: A mature ecosystem on the frontend (Apollo Client).
6.2) Disadvantages
6.2.1) Extremely immature C++ ecosystem
There are very few mature and supported libraries for implementing GraphQL servers in C++.
The implementation will require huge effort and carries high risks.
6.2.2) High backend complexity: The complexity of implementing request parsing and efficient resolvers in C++.
6.2.3) High security risks.
Similar to point 3.3.3, implementing complex GraphQL request parsing in C++ significantly increases the risks of critical vulnerabilities.
7) Hybrid architecture (API Gateway + C++)
7.1) Essence: the frontend interacts with an API Gateway, created in a language more suitable for the web (e.g., Node.js/TypeScript).
This gateway provides a public REST or GraphQL API.
The main business logic and the interaction with MongoDB (using `mongocxx`, as mentioned in point 1) are implemented in the C++ service.
The API Gateway interacts with the C++ service via a high-performance internal protocol (e.g., native gRPC or message queues).
~~~

# 4.
## 4.1.
`F` ≔ (фрагмент `D`)

## 4.2.
Содержание `F`:
~~~markdown
9.3) Поэтому я рекомендую способ пукта 7.
Он обеспечивает наилучший баланс для данного контекста. 
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