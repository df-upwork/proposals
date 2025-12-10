https://g.co/gemini/share/32d39d595cf7

# 1\. Архитектура и выбор фреймворка (Architecture and Framework Selection)

## 1.1. Определение архитектуры конвейера (Define the Pipeline Architecture)

Реализовать RAG workflow как часть Backend сервиса (соответствующего `T5⁎`, `O.md`::§7.5). Этот сервис будет принимать запросы пользователя, взаимодействовать с `E༄` и OpenAI API, и возвращать финальный ответ.

Обоснование: RAG workflow требует координации между несколькими компонентами (Vector Database, Embedding Model, LLM), что реализуется в рамках Application Logic.

Источник (Elasticsearch Reference. Retrieval Augmented Generation (RAG)):

> RAG is an architectural approach that leverages the strengths of both retrieval-based methods and generative models. It combines the precision of information retrieval systems, which search a large corpus of data to find relevant information, with the ability of LLMs to generate coherent and context-aware responses.

Перевод:

> RAG — это архитектурный подход, который использует сильные стороны как методов, основанных на поиске (retrieval-based methods), так и генеративных моделей. Он сочетает точность систем поиска информации, которые ищут в большом корпусе данных для нахождения релевантной информации, со способностью LLM генерировать связные и контекстуально осведомленные ответы.

## 1.2. Выбор фреймворка оркестрации (Select an Orchestration Framework)

Использовать LangChain или LlamaIndex для построения RAG-конвейера на Python или Node.js.

Обоснование: Эти фреймворки предоставляют готовые абстракции (например, Vector Stores, Retrievers, Chains) и интеграции (с `E༄` и OpenAI), что ускоряет разработку и упрощает управление сложными цепочками операций. Это соответствует требованиям проекта (`O.md`::§2.3).

Источник (LangChain Documentation. What is LangChain?):

> LangChain is a framework for developing applications powered by language models. [...] It enables applications that: Are context-aware: connect a language model to sources of context [...]

Перевод:

> LangChain — это фреймворк для разработки приложений, работающих на основе языковых моделей. [...] Он позволяет создавать приложения, которые: Осведомлены о контексте: подключают языковую модель к источникам контекста [...]

# 2\. Обработка и векторизация запроса (Query Processing and Embedding)

## 2.1. Получение запроса пользователя (Receive User Query)

Принять входящий текстовый запрос пользователя (например, “What are the specs for item X?”).

## 2.2. Генерация вектора запроса (Generate Query Embedding)

Преобразовать текстовый запрос в Dense Vector (эмбеддинг), используя OpenAI API endpoint `/v1/embeddings`.

Обоснование: Для выполнения семантического поиска (k-Nearest Neighbor search) необходимо представить запрос в том же векторном пространстве, что и индексированные документы.

Источник (OpenAI API Reference. Create embeddings):

> Creates an embedding vector representing the input text.

Перевод:

> Создает вектор эмбеддинга, представляющий входной текст.

## 2.3. Консистентность модели эмбеддингов (Embedding Model Consistency)

Использовать ту же модель эмбеддингов, которая применялась на этапе индексации `T2⁎` (например, `text-embedding-3-small`, `O.md`::§17.3.1).

Обоснование: Использование разных моделей для индексации и запроса приведет к несоответствию векторных пространств и, как следствие, к нерелевантным результатам поиска.

Источник (Elasticsearch Reference. k-nearest neighbor (kNN) search):

> The query vector. This vector must have the same number of dimensions as the field’s dims parameter.

Перевод:

> Вектор запроса. Этот вектор должен иметь то же количество измерений, что и параметр dims поля.

# 3\. Стратегия поиска (Retrieval Strategy)

## 3.1. Использование гибридного поиска (Implement Hybrid Search)

Применять стратегию гибридного поиска, комбинируя семантический поиск (Approximate Nearest Neighbor, ANN) с традиционным полнотекстовым поиском (например, BM25).

Обоснование: В контексте электронной коммерции гибридный поиск значительно повышает релевантность (`O.md`::§12.1.3). Семантический поиск помогает понять намерение пользователя, а полнотекстовый поиск обеспечивает точность при поиске по артикулам (SKU), брендам или специфическим терминам.

Источник (Elasticsearch Reference. Hybrid search):

> Hybrid search combines the strengths of both traditional full-text search and vector search. Traditional search excels at finding exact keyword matches, while vector search captures the semantic meaning and context of the query. By combining these two approaches, hybrid search provides more accurate and relevant search results.

Перевод:

> Гибридный поиск сочетает сильные стороны как традиционного полнотекстового поиска, так и векторного поиска. Традиционный поиск превосходно находит точные совпадения по ключевым словам, в то время как векторный поиск улавливает семантическое значение и контекст запроса. Комбинируя эти два подхода, гибридный поиск обеспечивает более точные и релевантные результаты поиска.

## 3.2. Метод комбинирования оценок (Score Combination Method)

Использовать Reciprocal Rank Fusion (RRF) для объединения результатов векторного и полнотекстового поиска.

Обоснование: RRF является эффективным методом для гибридного поиска, так как он не требует настройки весовых коэффициентов (boosts) или нормализации оценок (scores). Он работает на основе рангов документов в каждом из списков результатов.

Источник (Elasticsearch Reference. Hybrid search. Combine results using Reciprocal Rank Fusion (RRF)):

> Reciprocal Rank Fusion (RRF) is a search result combination method that takes the search results from multiple search methods, ranks them, and combines the ranks to produce a single result set. [...] This method avoids having to tune boosts for different search methods.

Перевод:

> Reciprocal Rank Fusion (RRF) — это метод комбинирования результатов поиска, который берет результаты из нескольких методов поиска, ранжирует их и объединяет ранги для получения единого набора результатов. [...] Этот метод позволяет избежать необходимости настройки весовых коэффициентов (boosts) для разных методов поиска.

Примечание: Доступность и реализация RRF различаются в Elasticsearch и OpenSearch (см. §4 и §5).

# 4\. Выполнение поиска в Elasticsearch (Executing Search in Elasticsearch)

Если в качестве `E༄` используется Elasticsearch (рекомендуется версия 8.14+ для использования Retrievers), выполнить запрос к Search API (`POST /product-catalog/_search`).

## 4.1. Использование Retrievers (Using Retrievers)

Использовать абстракцию `retriever` для определения конвейера гибридного поиска.

Обоснование: Retrievers (представлены в 8.14) предоставляют стандартизированный и упрощенный API для определения сложных поисковых стратегий, заменяя необходимость комбинирования `query`, `knn` и `rank` на верхнем уровне.

Источник (Elasticsearch Docs. Retrievers):

> Retrievers are a new type of abstraction in the \_search API that describes how to retrieve a set of top documents. [...] Retrievers are a standard, more general and simpler API that replaces other various \_search elements like kNN and query.

Перевод:

> Retrievers — это новый тип абстракции в \_search API, который описывает, как извлечь набор топовых документов. [...] Retrievers — это стандартный, более общий и простой API, который заменяет другие различные элементы \_search, такие как kNN и query.

## 4.2. Конфигурация RRF Retriever (RRF Retriever Configuration)

Определить `retriever` верхнего уровня с типом `rrf`.

4.2.1. В параметре `retrievers` перечислить дочерние Retrievers для комбинирования.
4.2.2. Использовать `standard` Retriever для полнотекстового поиска (BM25). Внутри определить `query` (например, `multi_match`).
4.2.3. Использовать `knn` Retriever для векторного поиска. Внутри указать `field` и `query_vector` (из §2.2).

## 4.3. Пример запроса (Example Query)

```json
POST /product-catalog/_search
{
  "retriever": {
    "rrf": {
      "retrievers": [
        {
          "standard": {
            "query": {
              "multi_match": {
                "query": "User input text",
                "fields": ["name", "description", "sku"]
              }
            }
          }
        },
        {
          "knn": {
            "field": "product_vector",
            "query_vector": [ /* Вектор запроса из §2.2 */ ],
            "k": 50
          }
        }
      ],
      "rank_window_size": 100
    }
  },
  "size": 5,
  "_source": ["name", "sku", "price", "url", "description", "specs"]
}
```

# 5\. Выполнение поиска в OpenSearch (Executing Search in OpenSearch)

Если в качестве `E༄` используется OpenSearch, выполнить запрос к Search API (`POST /product-catalog/_search`). Реализация гибридного поиска осуществляется через Search Pipelines.

## 5.1. Конфигурация Search Pipeline (Search Pipeline Configuration)

Создать Search Pipeline, который будет обрабатывать результаты поиска для комбинирования оценок.

Источник (OpenSearch Documentation. Search pipelines):

> A search pipeline is a sequence of processors that process search requests and responses.

Перевод:

> Конвейер поиска (search pipeline) — это последовательность процессоров, которые обрабатывают поисковые запросы и ответы.

### 5.1.1. Использование RRF (OpenSearch 2.19+)

Если используется OpenSearch 2.19+ с плагином Neural Search, настроить процессор `rrf`.

```json
PUT /_search/pipeline/hybrid-pipeline
{
  "phase_results_processors": [
    {
      "rrf": {
        "rank_constant": 60
      }
    }
  ]
}
```

Источник (OpenSearch Blog. Introducing reciprocal rank fusion for hybrid search):

> OpenSearch 2.19 introduces reciprocal rank fusion (RRF), a new feature in the Neural Search plugin that enhances hybrid search.

Перевод:

> OpenSearch 2.19 представляет reciprocal rank fusion (RRF), новую функцию в плагине Neural Search, которая улучшает гибридный поиск.

### 5.1.2. Использование нормализации (Альтернатива RRF)

Если RRF недоступен, использовать `normalization-processor` для нормализации (например, `min_max`) и комбинирования (например, `arithmetic_mean`) оценок.

```json
PUT /_search/pipeline/hybrid-pipeline
{
  "phase_results_processors": [
    {
      "normalization-processor": {
        "normalization": { "technique": "min_max" },
        "combination": {
          "technique": "arithmetic_mean",
          "parameters": { "weights": [0.5, 0.5] }
        }
      }
    }
  ]
}
```

Обоснование: Оценки BM25 и Vector Search имеют разные диапазоны. Нормализация необходима для их корректного взвешивания при линейной комбинации.

Источник (OpenSearch Documentation. Hybrid search. Normalization processor):

> A score-based processor that normalizes and combines document scores from multiple query clauses, rescoring the documents using the selected normalization and combination techniques.

Перевод:

> Процессор, основанный на оценках, который нормализует и комбинирует оценки документов из нескольких условий запроса, пересчитывая оценки документов с использованием выбранных техник нормализации и комбинирования.

## 5.2. Конфигурация Hybrid Query (Hybrid Query Configuration)

Использовать `hybrid` query для объединения результатов нескольких запросов.

Источник (OpenSearch Documentation. Hybrid query):

> The hybrid query allows you to combine the results of multiple queries.

Перевод:

> Запрос hybrid позволяет комбинировать результаты нескольких запросов.

5.2.1. Внутри `hybrid` использовать `knn` query для векторного поиска.
5.2.2. Внутри `hybrid` использовать `multi_match` для полнотекстового поиска.
5.2.3. Указать созданный Search Pipeline в параметре URL `search_pipeline`.

## 5.3. Пример запроса (Example Query)

```json
POST /product-catalog/_search?search_pipeline=hybrid-pipeline
{
  "query": {
    "hybrid": {
      "queries": [
        {
          "multi_match": {
            "query": "User input text",
            "fields": ["name", "description", "sku"]
          }
        },
        {
          "knn": {
            "product_vector": {
              "vector": [ /* Вектор запроса из §2.2 */ ],
              "k": 50
            }
          }
        }
      ]
    }
  },
  "size": 5,
  "_source": ["name", "sku", "price", "url", "description", "specs"]
}
```

# 6\. Формирование контекста и промпт-инжиниринг (Context Assembly and Prompt Engineering)

## 6.1. Извлечение контекста (Context Extraction)

Из результатов поиска (ответ `E༄`) извлечь релевантные документы (hits). Сформировать текстовый контекст, объединив необходимую информацию (название, спецификации, цена, URL) из поля `_source` каждого документа.

## 6.2. Конструирование промпта (Prompt Construction)

Создать промпт для LLM (ChatGPT), используя формат Chat Completions API. Промпт должен включать System message и User message.

Обоснование: Промпт предоставляет LLM необходимую информацию и инструкции для генерации точного и релевантного ответа, основанного на данных каталога.

Источник (OpenAI Documentation. Prompt engineering):

> Prompts are how we "program" the model, usually by providing some instructions or a few examples.

Перевод:

> Промпты — это то, как мы "программируем" модель, обычно предоставляя некоторые инструкции или несколько примеров.

## 6.3. System Message (Инструкции и Роль)

В System message определить роль ассистента и инструкции.

### 6.3.1. Инструкции по использованию контекста (Grounding Instructions)

Явно указать, что ответ должен основываться исключительно на предоставленном контексте. Это помогает минимизировать галлюцинации.

Источник (OpenAI Documentation. Prompt engineering. Give the model an "out"):

> It may be helpful to give the model a way to say "I don't know" if it is unable to answer a particular question.

Перевод:

> Может быть полезно предоставить модели способ сказать "Я не знаю", если она не может ответить на конкретный вопрос.

### 6.3.2. Инструкции по форматированию (Formatting Instructions)

Явно потребовать включение цен и ссылок (URL) на продукты в ответ.

Обоснование: Это необходимо для выполнения целей проекта `T⁎` (`O.md`::§6).

## 6.4. User Message (Контекст и Запрос)

Включить извлеченный контекст (§6.1) и исходный запрос пользователя (§2.1). Использовать разделители для четкого отделения контекста от запроса.

Источник (OpenAI Help Center. Best practices for prompt engineering):

> Put instructions at the beginning of the prompt and use \#\#\# or """ to separate the instruction and context.

Перевод:

> Размещайте инструкции в начале prompt и используйте \#\#\# или """, чтобы отделить инструкцию от контекста.

## 6.5. Пример структуры промпта (Example Prompt Structure)

System Message:

> Вы являетесь экспертом по продуктам интернет-магазина. Отвечайте на вопросы пользователя, используя ТОЛЬКО предоставленный контекст о продуктах. Если контекст не содержит ответа, сообщите, что информация не найдена. При упоминании продукта ОБЯЗАТЕЛЬНО указывайте его цену и ссылку (URL).

User Message:

> Контекст Продуктов:
> """
> Продукт 1: Название: {Name}. Цена: {Price}. URL: {URL}. Спецификации: {Specs}.
> Продукт 2: Название: {Name}. Цена: {Price}. URL: {URL}. Спецификации: {Specs}.
> """
> Вопрос пользователя: {User Query}

# 7\. Генерация ответа (Response Generation)

## 7.1. Вызов OpenAI API (Call OpenAI API)

Отправить сконструированный промпт (§6.2) в OpenAI Chat Completions API (`POST /v1/chat/completions`).

Источник (OpenAI API Reference. Create chat completion):

> Creates a model response for the given chat conversation.

Перевод:

> Создает ответ модели для данного чат-разговора.

## 7.2. Выбор модели (Model Selection)

Выбрать подходящую модель LLM (например, `gpt-4o` или `gpt-3.5-turbo`).

Обоснование: Выбор модели влияет на качество ответа, скорость и стоимость. `gpt-4o` обеспечивает высокое качество рассуждений, что предпочтительно для сложных запросов.

Источник (OpenAI. Models):

> GPT-4o (“o” for “omni”) is our most advanced model.

Перевод:

> GPT-4o ("o" для "omni") — наша самая продвинутая модель.

## 7.3. Настройка параметров генерации (Generation Parameters Configuration)

Установить параметр `temperature` в низкое значение (например, 0.0 или 0.1).

Обоснование: В RAG-системах требуется высокая точность и детерминированность ответов, основанных на фактах (контексте). Низкая температура уменьшает креативность и случайность генерации.

Источник (OpenAI API Reference. Create chat completion. temperature):

> What sampling temperature to use, between 0 and 2. [...] lower values like 0.2 will make it more focused and deterministic.

Перевод:

> Какую температуру сэмплинга использовать, от 0 до 2. [...] более низкие значения, такие как 0.2, сделают его более сфокусированным и детерминированным.

## 7.4. Обработка ответа (Response Handling)

Получить сгенерированный ответ от API и вернуть его пользователю или в интерфейс чат-бота.