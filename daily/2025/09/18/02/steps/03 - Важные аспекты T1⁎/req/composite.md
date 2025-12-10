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
Сегодня 2025-09-18.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021968656983289523372

## 2.2. Title
AI Developer – Magento Product Catalog Integration with ChatGPT

## 2.3. Description
`PD` ≔ 
```text
We run a Magento 2 (Hyvä theme) e-commerce platform and want to make our product catalog searchable directly through ChatGPT.

The goal is for ChatGPT users to be able to ask:
• “Where can I buy this product?”
• “What are the specs for item X?”
• “What’s the price and where can I get it?”

…and receive answers that include product details, pricing, and links to our product pages.

⸻

Scope of Work
• Connect Magento 2 (via REST/GraphQL API) to extract product data (names, specs, attributes, pricing, URLs).
• Build an indexing pipeline with embeddings and a vector database (Pinecone, Weaviate, Qdrant, or pgvector).
• Implement a retrieval-augmented generation (RAG) workflow so ChatGPT responses include our product info + links.
• Set up automated catalog syncing (daily/weekly updates).
• Deliver a backend/API that can power both ChatGPT integration and optionally an on-site chatbot widget.

⸻

Required Skills
• Strong Magento 2 API experience (Hyvä theme knowledge a plus).
• Backend development (Python or Node.js).
• Experience with ChatGPT/OpenAI API and LangChain or LlamaIndex.
• Knowledge of vector search databases.
• Prior work on AI chatbots for e-commerce.

⸻

Deliverables
• Working ChatGPT integration that serves product specs, pricing, and product links.
• Automated data refresh pipeline.
• Documentation for internal handover.
• on site AI powered Chatbot, for users to find products and information about it, as well as answer FAQs
```

## 2.4. Tags
ChatGPT API Integration
AI Bot
Python
PHP
Magento 2
LLaMA
vector search
AI Chatbot
LaingChain
API Integration

## 2.5. Questions
### 2.5.1.
Have you worked with Magento 2 REST or GraphQL APIs to extract product catalogs before?

### 2.5.2.
Have you built a project that connects ChatGPT (OpenAI API) to a custom data source (e.g., a database, product catalog, or documents)? 
If yes, describe what the user could query and how the system responded.

### 2.5.3.
Which vector databases have you used (Pinecone, Weaviate, Qdrant, pgvector)? 
Briefly describe how you set up embeddings and search.

### 2.5.4.
Have you implemented a RAG pipeline (query → embedding → vector search → ChatGPT answer)? 
Please explain the stack you used (LangChain/LlamaIndex/etc.).

### 2.5.5.
Have you implemented a system that inserts metadata (like URLs) into ChatGPT answers?

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United Arab Emirates
Dubai 

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Dec 31, 202
### 5.3.2. Hire rate (%)
100
### 5.3.3. Количество опубликованных проектов (jobs posted)
5
### 5.3.4. Total spent (USD)
$2.1K
### 5.3.5. Количество оплаченных часов в почасовых проектах
29
### 5.3.6. Средняя почасовая ставка (USD)
38

# 6.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
The goal is for ChatGPT users to be able to ask:
• “Where can I buy this product?”
• “What are the specs for item X?”
• “What’s the price and where can I get it?”

…and receive answers that include product details, pricing, and links to our product pages.
~~~
```

# 7.
## 7.1.
`T1⁎` ≔
```
Подзадача `T⁎`, о которой `ꆜ` пишет в `PD`:
~~~
Connect Magento 2 (via REST/GraphQL API) to extract product data (names, specs, attributes, pricing, URLs).
~~~
```

## 7.2.
`T2⁎` ≔
```
Подзадача `T⁎`, о которой `ꆜ` пишет в `PD`:
~~~
Build an indexing pipeline with embeddings and a vector database (Pinecone, Weaviate, Qdrant, or pgvector).
~~~
```

## 7.3.
`T3⁎` ≔
```
Подзадача `T⁎`, о которой `ꆜ` пишет в `PD`:
~~~
Implement a retrieval-augmented generation (RAG) workflow so ChatGPT responses include our product info + links.
~~~
```

## 7.4.
`T4⁎` ≔
```
Подзадача `T⁎`, о которой `ꆜ` пишет в `PD`:
~~~
Set up automated catalog syncing (daily/weekly updates).
~~~
```

## 7.5.
`T5⁎` ≔
```
Подзадача `T⁎`, о которой `ꆜ` пишет в `PD`:
~~~
Deliver a backend/API that can power both ChatGPT integration and optionally an on-site chatbot widget.
~~~
```

# 8.
## 8.1.
`VD⠿` ≔~ (Vector databases)
```yaml
- Pinecone
- Weaviate
- Qdrant
- pgvector
```

## 8.2.
`VDᵢ` : `VD⠿`

# 9.
`H1` ≔? 
```
Существует `VDᵢ`, не упомянутая `ꆜ`, которая подходит для `T⁎` лучше, чем `VDᵢ`, упоминутые `ꆜ`
```

# 10. Пошаговая инструкция для `T1⁎`
~~~markdown

# 1\. Настройка аутентификации и авторизации (Authentication and Authorization Setup)

Для обеспечения безопасного доступа к данным каталога Magento 2 из внешнего приложения (server-to-server integration) необходимо настроить аутентификацию на основе токенов (Token-based authentication).

## 1.1. Метод аутентификации (Authentication Method)

Использовать Integration tokens.

Обоснование: Этот тип токенов предназначен для интеграций, которым требуется доступ к определенным ресурсам, и они не имеют срока действия по умолчанию, что подходит для автоматизированной синхронизации каталога.

Источник (Adobe Developer. Token-Based Authentication):

> Token type: Integration
> Description: The merchant determines which Commerce resources the integration can access.
> Default lifetime: Indefinite. It lasts until it is manually revoked.

Перевод:

> Тип токена: Integration
> Описание: Продавец определяет, к каким ресурсам Commerce интеграция может получить доступ.
> Срок действия по умолчанию: Неограниченный. Он длится до тех пор, пока не будет отозван вручную.

## 1.2. Конфигурация OAuth (OAuth Configuration)

Необходимо убедиться, что конфигурация Magento позволяет использовать Access Token интеграции в качестве самостоятельного Bearer Token.

1.2.1. Перейти в «Stores» → «Settings» → «Configuration».
1.2.2. В левой панели развернуть «Services» и выбрать «OAuth».
1.2.3. Развернуть секцию «Consumer Settings».
1.2.4. Установить параметр «Allow OAuth Access Tokens to be used as standalone Bearer tokens» в значение «Yes».
1.2.5. Нажать «Save Config».

Обоснование: В современных версиях Magento поведение, позволяющее использовать Access Token интеграции для Token-based authentication, может быть отключено по умолчанию из соображений безопасности.

Источник (Adobe Developer. Token-Based Authentication):

> In previous versions of Commerce, the access token could be used on its own for token-based authentication. This behavior is no longer enabled by default.
> [...]
> However, while it is not recommended, this behavior can be restored in the Admin by setting the Stores \> Configuration \> Services \> OAuth \> Consumer Settings \> Allow OAuth Access Tokens to be used as standalone Bearer tokens option to Yes.

Перевод:

> В предыдущих версиях Commerce access token мог использоваться самостоятельно для аутентификации на основе токенов. Это поведение больше не включено по умолчанию.
> [...]
> Однако, хотя это и не рекомендуется, это поведение можно восстановить в Admin, установив для параметра Stores \> Configuration \> Services \> OAuth \> Consumer Settings \> Allow OAuth Access Tokens to be used as standalone Bearer tokens значение Yes.

## 1.3. Создание Integration (Creating Integration)

Создать новую запись Integration в Magento Admin Panel.

1.3.1. Перейти по пути «System» → «Extensions» → «Integrations».
1.3.2. Нажать кнопку «Add New Integration».
1.3.3. В поле «Name» ввести уникальный идентификатор (например, `RAG_Catalog_Sync`).
1.3.4. В поле «Your Password» ввести пароль текущего администратора для подтверждения.

Обоснование: Это стандартная процедура для настройки доступа внешних систем к Magento API.

Источник (Adobe Experience League. Integrations):

> On the Admin sidebar, go to System \> Extensions \> Integrations.
> In the upper-right corner, click Add New Integration.
> Enter the Name of the integration...

Перевод:

> На боковой панели Admin перейдите в System \> Extensions \> Integrations.
> В правом верхнем углу нажмите Add New Integration.
> Введите Name интеграции...

## 1.4. Настройка разрешений API (API Permissions)

Определить ресурсы (ACL resources), к которым будет предоставлен доступ.

1.4.1. Перейти на вкладку «API».
1.4.2. В настройке «Resource Access» выбрать «Custom».
1.4.3. В дереве «Resources» отметить необходимые элементы для доступа к каталогу. Минимально необходимый ресурс: «Catalog» (включая «Inventory» → «Products»).
1.4.4. Нажать кнопку «Save».

Обоснование: Необходимо предоставить доступ только к тем ресурсам, которые требуются для выполнения задачи.

Источник (Adobe Experience League. Integrations):

> In the left panel, choose API and do the following:
> Set Resource Access to one of the following: All. Custom.
> For custom access, select the checkbox of each resource that is needed.

Перевод:

> На левой панели выберите API и выполните следующие действия:
> Установите Resource Access в одно из следующих значений: All. Custom.
> Для выборочного доступа установите флажок для каждого необходимого ресурса.

## 1.5. Активация и получение Access Token (Activation and obtaining Access Token)

Активировать интеграцию для генерации Access Token.

1.5.1. Найти созданную Integration в списке.
1.5.2. Нажать ссылку «Activate» в колонке «Action».
1.5.3. Подтвердить разрешения, нажав кнопку «Allow».
1.5.4. Скопировать и безопасно сохранить значение «Access Token» из раздела «Integration Tokens for Extensions».

Обоснование: Активация генерирует токен, который служит ключом для доступа к API.

Источник (Adobe Experience League. Integrations):

> Find the newly created integration and click the Activate link.
> [...]
> This action displays the Integration Tokens for Extensions.
> Copy this information to a secure, encrypted location for use with your integration.

Перевод:

> Найдите вновь созданную интеграцию и нажмите ссылку Activate.
> [...]
> Это действие отображает Integration Tokens for Extensions.
> Скопируйте эту информацию в безопасное зашифрованное место для использования в вашей интеграции.

# 2\. Стратегия извлечения данных (Data Extraction Strategy)

## 2.1. Выбор API (API Selection)

Magento 2 предоставляет REST API и GraphQL API. Для данной задачи рекомендуется использовать GraphQL API.

Обоснование: GraphQL позволяет точно указать, какие поля необходимы (names, specs, pricing, URLs), в одном запросе. Это уменьшает избыточность данных (over-fetching) и повышает эффективность по сравнению с REST API.

Источник (Adobe Experience League. Perform a query using GraphQL):

> The query expresses exactly the fields that you want, and the returned data is formatted.

Перевод:

> Запрос точно выражает поля, которые вы хотите получить, и возвращаемые данные форматируются соответствующим образом.

## 2.2. Конфигурация атрибутов (Attribute Configuration)

Перед извлечением данных необходимо убедиться, что все требуемые спецификации (EAV attributes) доступны через GraphQL API.

2.2.1. Перейти в «Stores» → «Attributes» → «Product».
2.2.2. Открыть нужный атрибут (например, содержащий технические характеристики).
2.2.3. Перейти в раздел «Storefront Properties».
2.2.4. Убедиться, что атрибут настроен для отображения на витрине (например, «Visible on Catalog Pages on Storefront» установлено в «Yes») или используется в поиске/листингах.

Обоснование: Доступность EAV атрибутов в стандартном запросе GraphQL зависит от их видимости на витрине.

Источник (Adobe Developer. Add custom attributes to a query):

> If the attribute is an EAV attribute, then you must ensure the attribute is visible on the storefront.

Перевод:

> Если атрибут является EAV атрибутом, вы должны убедиться, что атрибут виден на витрине.

# 3\. Извлечение данных через GraphQL API (Data Extraction via GraphQL API)

## 3.1. Endpoint и метод (Endpoint and Method)

Использовать стандартный GraphQL endpoint (например, `https://<magento_host>/graphql`) и метод HTTP POST.

Обоснование: Все операции GraphQL выполняются через единый endpoint методом POST.

Источник (Adobe Developer. GraphQL basics):

> All GraphQL queries must be performed using the POST method.

Перевод:

> Все GraphQL запросы должны выполняться с использованием метода POST.

## 3.2. Заголовки HTTP (HTTP Headers)

Добавить обязательные HTTP-заголовки в запрос.

3.2.1. `Content-Type: application/json`.
3.2.2. `Authorization: Bearer <Access_Token>` (используя токен, полученный на шаге 1.5.4).

Обоснование: Для доступа к защищенным ресурсам необходимо передавать токен в заголовке запроса.

Источник (Adobe Developer. Authorization tokens):

> You must specify the token in the Authorization request header with the Bearer authentication scheme:
> Authorization: Bearer \<authentication-token\>

Перевод:

> Вы должны указать токен в заголовке запроса Authorization со схемой аутентификации Bearer:
> Authorization: Bearer \<authentication-token\>

3.2.3. `Store: <store_view_code>` (например, `default`).

Обоснование: Заголовок Store определяет контекст магазина (язык, валюта и т.д.) для запроса.

Источник (Adobe Developer. GraphQL basics. HTTP headers):

> Store | String | The store-view code.

Перевод:

> Store | String | Код представления магазина (store-view code).

## 3.3. Конструирование запроса `products` (Constructing the `products` query)

Сконструировать GraphQL query для получения требуемых данных.

Обоснование: Запрос `products` предназначен для поиска, фильтрации и извлечения информации об элементах каталога.

Источник (Adobe Developer. products query):

> The products query returns information about products that match the criteria specified in the filter, search, or sort attributes.

Перевод:

> Запрос products возвращает информацию о продуктах, которые соответствуют критериям, указанным в атрибутах filter, search или sort.

Пример запроса:

```graphql
query GetCatalogData($pageSize: Int!, $currentPage: Int!) {
  products(pageSize: $pageSize, currentPage: $currentPage) {
    total_count
    items {
      # Названия (Names)
      sku
      name
      # Цены (Pricing)
      price_range {
        minimum_price {
          final_price {
            value
            currency
          }
        }
      }
      # URL
      url_key
      url_suffix
      # Спецификации и Атрибуты (Specs and Attributes)
      description {
        html
      }
      # Добавить другие Custom Attributes по их кодам (например, material, color)
    }
    # Информация для пагинации
    page_info {
      current_page
      total_pages
    }
  }
}
```

## 3.4. Реализация пагинации (Pagination Implementation)

Реализовать логику итерации по страницам для извлечения всего каталога, используя параметры `pageSize` и `currentPage`.

3.4.1. Определить оптимальный размер страницы (`pageSize`) (например, 100).
3.4.2. Начать с `currentPage` = 1.
3.4.3. Выполнять запросы, увеличивая `currentPage`, до тех пор, пока не будет достигнут `total_pages` (из объекта `page_info`).

Обоснование: API ограничивает количество результатов за один запрос. Пагинация необходима для управления большими наборами данных.

Источник (Adobe Developer. products query):

> The pageSize attribute specifies the maximum number of items to return.
> [...]
> The currentPage attribute specifies which page of results to return.

Перевод:

> Атрибут pageSize определяет максимальное количество возвращаемых элементов.
> [...]
> Атрибут currentPage определяет, какую страницу результатов возвращать.

# 4\. Извлечение данных через REST API (Альтернативный метод) (Data Extraction via REST API - Alternative Method)

Если использование GraphQL невозможно, следует использовать REST API.

## 4.1. Endpoint и `searchCriteria`

Использовать endpoint `GET /V1/products` (например, `https://<magento_host>/rest/V1/products`) с параметрами `searchCriteria`. Аутентификация выполняется аналогично §3.2.2 через заголовок `Authorization`.

Обоснование: REST API использует `searchCriteria` в URL для фильтрации и пагинации при запросе коллекций.

Источник (Adobe Developer. Search using REST endpoints):

> For search APIs that invoke a \*Repository::getList(SearchCriteriaInterface \*) call, the searchCriteria must be specified in the URL of the GET request.

Перевод:

> Для API поиска, которые вызывают \*Repository::getList(SearchCriteriaInterface \*), searchCriteria должны быть указаны в URL GET-запроса.

## 4.2. Пагинация и оптимизация (Pagination and Optimization)

4.2.1. Использовать параметры `searchCriteria[pageSize]` и `searchCriteria[currentPage]` для пагинации.

Пример запроса:
`GET /rest/V1/products?searchCriteria[pageSize]=100&searchCriteria[currentPage]=1`

Обоснование: Эти параметры управляют размером страницы и текущим смещением в REST API.

Источник (Adobe Developer. Search using REST endpoints):

> searchCriteria[pageSize] - Specifies the maximum number of items to return.
> [...]
> searchCriteria[currentPage] - Returns the current page.

Перевод:

> searchCriteria[pageSize] - Определяет максимальное количество возвращаемых элементов.
> [...]
> searchCriteria[currentPage] - Возвращает текущую страницу.

4.2.2. Использовать параметр `fields` для ограничения возвращаемых данных только необходимыми атрибутами.

Пример:
`GET /rest/V1/products?searchCriteria[pageSize]=100&fields=items[sku,name,price,custom_attributes],total_count`

Обоснование: Параметр `fields` позволяет уменьшить объем ответа, запрашивая только указанные поля.

Источник (Adobe Developer. Retrieve filtered search responses):

> You can use the fields query parameter to specify a filtered list of fields to return.

Перевод:

> Вы можете использовать параметр запроса fields, чтобы указать отфильтрованный список полей для возврата.

## 4.3. Обработка атрибутов (Attribute Handling)

При использовании REST API значения атрибутов типа `select` или `multiselect` (например, цвет, производитель) возвращаются в виде идентификаторов опций (Option IDs), а не текстовых меток (Labels). Необходимо выполнить дополнительные шаги для получения меток.

4.3.1. Определить атрибуты, для которых требуются текстовые метки.
4.3.2. Использовать endpoint `GET /V1/products/attributes/:attributeCode/options` для получения соответствия ID и меток для каждого такого атрибута (например, `/V1/products/attributes/color/options`).
4.3.3. Заменить идентификаторы опций в данных продукта на соответствующие текстовые метки.

Обоснование: Для использования данных в RAG-модели необходимы текстовые значения спецификаций. REST API требует этого дополнительного шага нормализации.

Источник (Adobe Developer. Retrieve product attribute option labels):

> When you retrieve a product, the value of a dropdown or multi-select attribute is the option ID, not the label. You must perform a separate query to determine the label.

Перевод:

> Когда вы извлекаете продукт, значением атрибута типа dropdown или multi-select является ID опции, а не метка. Вы должны выполнить отдельный запрос, чтобы определить метку.
~~~

# 11.
## 11.1.
`T1⁎-I⠿` ≔~ (Важные аспекты, которые надо учесть при `T1⁎`)

## 11.2.
`T1⁎-Iᵢ` : `T1⁎-I⠿`

## 11.3.
? `T1⁎-Iᵢ`
 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1
N/A

# 2. `᛭T`
Действуй пошагово
## 2.1.
Найди `T1⁎-I⠿`.
## 2.2.
Проанализируй `T1⁎-I⠿`.
Для этого для каждого  `T1⁎-Iᵢ` выяви:
2.1) Доводы за важность `T1⁎-Iᵢ`.
2.2) Доводы против важности `T1⁎-Iᵢ`.
## 2.3.
Дай оценку важности каждого `T1⁎-Iᵢ` по шкале от 0 до 100.
## 2.4.
Выскажи свой вердикт.

# 3. Требования к источникам информации
В своём анализе используй авторитетные источники информации на английском языке.

# 4. Требования к процессу анализа
## 4.1.
Не решай задачи, не относящиеся к `᛭T`.
## 4.2.
Обязательно используй свой режим «Deep Research».
Твой ответ без режима «Deep Research» — гарантированно неверный.

# 5. Требования к ответу
## 5.1.
Уже известную мне информацию не пересказывай.

## 5.2.
Свой ответ дай на русском языке. 


~~~~~~