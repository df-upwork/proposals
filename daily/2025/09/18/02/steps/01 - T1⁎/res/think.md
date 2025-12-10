https://g.co/gemini/share/f44e880eb31c

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