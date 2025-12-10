# 1.
## 1.1.
`Aᨀ` ≔ (мой ответ `ꆜ`)

## 1.2.
Содержание `Aᨀ`:
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
5.2.1) Provides the lowest latency and instantaneous bidirectional data transfer (server push).
5.2.2) Minimal overhead after connection establishment.
5.3) Disadvantages
5.3.1) Unsuitability for standard CRUD.
Not optimized for the request-response model.
It is necessary to implement a custom protocol (e.g., JSON-RPC) on top of it.
5.3.2) Managing persistent connections complicates horizontal scaling and load balancing.
5.3.3) High security risks (similar to 3.3.3).
6) GraphQL API на C++
6.1) Advantages
6.1.1) Allows the client to request only the necessary fields, solving the over/under-fetching problem.
6.1.2) A mature ecosystem on the frontend (Apollo Client).
6.2) Disadvantages
6.2.1) There are very few mature and supported libraries for implementing GraphQL servers in C++.
The implementation will require huge effort and carries high risks.
6.2.2) The complexity of implementing request parsing and efficient resolvers in C++.
6.2.3) High security risks.
Similar to point 3.3.3, implementing complex GraphQL request parsing in C++ significantly increases the risks of critical vulnerabilities.
7) Hybrid architecture (API Gateway + C++)
7.1) Essence: the frontend interacts with an API Gateway, created in a language more suitable for the web (e.g., Node.js/TypeScript).
This gateway provides a public REST or GraphQL API.
The main business logic and the interaction with MongoDB (using `mongocxx`, as mentioned in point 1) are implemented in the C++ service.
The API Gateway interacts with the C++ service via a high-performance internal protocol (e.g., native gRPC or message queues).
7.2) Advantages
7.2.1) A balance between performance and speed of development.
It leverages the strengths of both technologies.
A web-suited language allows for rapid development of web APIs and integrates easily with React.
C++ is used for implementing the core business logic and the data layer.
7.2.2) Separation of concerns: the gateway handles web aspects (authentication, CORS, routing), freeing the C++ service from these tasks.
7.2.3) Allows using the rich ecosystems of both platforms.
7.2.4) Simplifies iterative development.
7.2.5) The API Gateway is implemented in a memory-safe language.
This eliminates an entire class of vulnerabilities related to memory management on the application's public perimeter.
7.3) Disadvantages
7.3.1) More moving parts (2 services instead of 1).
7.3.2) It introduces an additional network hop (React → Gateway → C++).
8) Judging by the phrase «design solutions from scratch and iterate with the owner to deliver a working product», the priority is development speed and the ability for rapid iterations.
9) Based on point 8:
9.1) Implementing the web layer directly in C++ (the methods from points 3, 5, and 6) will significantly slow down development and complicate iterations due to the language's complexity and the relative immaturity of its web ecosystem.
9.2) The method from point 4 introduces unnecessary infrastructure complexity (a proxy) for a new project.
9.3) Therefore, I recommend the method from point 7.
It provides the best balance for this context.
---
My GitHub profile: https://github.com/dmitrii-fediuk
~~~

# 2.
## 2.1.
`Fᨀ` ≔ (фрагмент `Aᨀ`)

## 2.2.
Содержание `Fᨀ`:
~~~markdown
9) Based on point 8:
9.1) Implementing the web layer directly in C++ (the methods from points 3, 5, and 6) will significantly slow down development and complicate iterations due to the language's complexity and the relative immaturity of its web ecosystem.
9.2) The method from point 4 introduces unnecessary infrastructure complexity (a proxy) for a new project.
9.3) Therefore, I recommend the method from point 7.
It provides the best balance for this context.
~~~

# 3. `᛭T`
Сделай `Fᨀ` короче на 30%.

# 4. Требования к твоему ответу
## 4.1.
Используй все предыдущие пункты моего запроса для понимания обсуждаемой в `Aᨀ` предметной области.

## 4.2.
К угловым кавычкам `«»` не придирайся.

## 4.3.
Писать свою версию `Fᨀ` не нужно: просто укажи свои правки по пунктам.

## 4.4.
Каждую правку нумеруй.

## 4.5.
### 4.5.1.
Не используй Markdown: только plain text.
### 4.5.2.
При этом можно и нужно использовать то форматирование, которое уже есть в оригинале: его не убирай.
### 4.5.3.
Не форматируй веб-ссылки посредством Markdown, если они не отформатированы так в оригинале. 
Например, не пиши так:
```
[https://www.eca.web.tr/eca-nita-esnek-uclu-eviye-bataryasi-beyaz-102118110-308](https://www.eca.web.tr/eca-nita-esnek-uclu-eviye-bataryasi-beyaz-102118110-308)
```
если в оригинале скобок `[]()` нет.

## 4.6.
Форматируй перевод в точности как оригинал. 
В частности:
*) каждый абзац должен содержать ровно одно предложение
*) между абзацами не должно оставаться пустых строк.
*) кавычки используй те же, что и в оригинале: «» и ``.

## 4.7.
Не используй сокращения типа «don't». Все подобные фразы пиши полностью: «do not».

## 4.8.
Не используй жаргон.
Вместо этого используй официальные термины.
### 4.8.1.
В частности, фразы в кавычках используй только в том случае, когда они являются точными цитатами.
Не используй фразы в кавычках для применения жаргонных фраз.
Например, следующий фрагмент текста недопустим, потому что там используется жаргонная фраза «пролетел»: 
```
Например, код, который пушит данные о покупке, подключён асинхронно и загружается с небольшой задержкой, а триггер уже «пролетел».
```

## 4.9.
При обсуждении программного обеспечения используй точные официальные термины на английском языке: именно в том виде, как они указаны в официальной англоязычной документации к этому программному обеспечению.

## 4.10.
Не используй «you need» и другие подобные обращённые к клиенту фразы, перекладывающие действия на него.
Помни: я пишу клиенту или потенциальному клиенту.
Делать в любом случае буду я, а не клиент.
Вместо «you need» используй 2 альтернативы:
### 4.10.1.
Нейтральные фразы типа «it is necessary».
### 4.10.2.
Глаголы в неопределённой форме.
Например, во фрагменте ниже использованы подобные глаголы «set up», «create»:
```
1.2) Set up the transfer of login events from WordPress to Power BI using Fabric / OneLake.
1.2.1) Set up a «Data Pipeline» from the WordPress database table that stores login events (see point 1.1) to Fabric / OneLake.
1.2.2) Set up a connection from Power BI to Fabric / OneLake to pass login events.
1.3) Create the data model in Power BI.
```
Обрати внимание, в этом фрагменте не говорится, кто именно будет выполнять описанные действия: ответственность не перекладывается на клиента, в отличие от «you need».

## 4.11.
Никогда не переводи понятие «сайт» / «веб-сайт» как «site». 
Вместо этого используй форму «website»: это является более профессиональным.

## 4.12.
Никогда не переводи понятие «пункт нумерованного списка» как «item».
Всегда переводи это как «point».

## 4.13.
Вместо «for example» используй «e.g.».
При этом не забывай, что в начале предложения эта фраза должна начинатся с заглавной буквы: «E.g.»