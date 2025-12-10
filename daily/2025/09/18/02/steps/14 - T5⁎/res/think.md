Пошаговая инструкция для `T5⁎` (Deliver a backend/API) при использовании стратегий `T1⁎-A3` (Гибридный подход к извлечению данных) и `T2⁎-E༄` (Использование Elasticsearch/OpenSearch).

# 1. Архитектура и технологический стек (Architecture and Technology Stack)

## 1.1. Определение архитектурного паттерна (Define Architectural Pattern)

Реализовать Backend как набор независимых Microservices.

Обоснование: Этот подход обеспечивает архитектурное разделение (Decoupling) между платформой Magento (PHP) и функциональностью RAG (Python/Node.js). Это позволяет независимо масштабировать сервисы, изолировать сбои и защищает стабильность платформы электронной коммерции, что является ключевым преимуществом стратегии `T1⁎-A3` (`O.md`::§31.3).

Источник (Microsoft Azure Architecture Center. Microservices architecture style):
> In a microservices architecture, services are small, independent, and loosely coupled. [...] Services can be deployed independently.
Перевод:
> В архитектуре Microservices сервисы малы, независимы и слабо связаны. [...] Сервисы могут быть развернуты независимо.

## 1.2. Определение архитектуры индексов (Define Index Architecture)

Принять архитектуру Dual Index в кластере Elasticsearch/OpenSearch (`E༄`):

1.  Native Magento Index (Source): Индекс, управляемый Magento. В соответствии со стратегией `T1⁎-A3`, этот индекс предварительно обогащается через PHP-модуль (`O.md`::§29) и служит источником данных для RAG.
2.  Dedicated RAG Index (Target): Отдельный индекс, управляемый Backend сервисом, содержащий векторы (Embeddings) и оптимизированный для RAG.

Обоснование: Magento полностью контролирует жизненный цикл своего Native Index, включая его удаление при полной переиндексации (`O.md`::§26.3). Невозможно безопасно добавлять векторы в нативный индекс. Необходим отдельный RAG Index (`O.md`::§31.2.1.3).

## 1.3. Определение компонентов системы (Define System Components)

Разделить Backend функциональность на два основных сервиса:

1.  Indexing Service (ETL): Отвечает за Data Synchronization Pipeline. Реализует извлечение данных (часть `T1⁎-A3`), генерацию Embeddings (`T2⁎`) и автоматическую синхронизацию (`T4⁎`).
2.  RAG Runtime Service (API): Обрабатывает запросы пользователей в реальном времени. Реализует RAG Workflow (`T3⁎`) и предоставляет API для интеграций.

Обоснование: Разделение позволяет изолировать ресурсоемкие, фоновые задачи индексации от чувствительного к задержкам (latency-sensitive) API, обслуживающего запросы пользователей.

## 1.4. Выбор технологического стека (Select Technology Stack)

### 1.4.1. Язык программирования (Programming Language)

Использовать Python или Node.js.

Обоснование: Соответствует требованиям проекта (`O.md`::§2.3).

### 1.4.2. Web Framework

Использовать высокопроизводительный Web Framework для RAG Runtime Service, например, FastAPI (Python) или Express.js (Node.js).

### 1.4.3. Orchestration Framework

Использовать LangChain или LlamaIndex для реализации RAG Workflow и управления Data Pipeline.

Обоснование: Эти фреймворки предоставляют необходимые абстракции (например, Vector Stores, Retrievers) и интеграции с `E༄` и OpenAI API, что ускоряет разработку (`O.md`::§21.1.2).

# 2. Реализация Data Synchronization Pipeline (Indexing Service)

Этот сервис реализует процесс ETL (Extract, Transform, Load) для переноса данных из Native Magento Index в Dedicated RAG Index.

## 2.1. Extraction (Извлечение данных)

Реализовать логику чтения данных из Native Magento Index. Это соответствует компоненту чтения стратегии `T1⁎-A3` (`O.md`::§29).

### 2.1.1. Использование Point in Time (PIT) и `search_after`

Использовать Point in Time (PIT) API в сочетании с параметром `search_after`.

Обоснование: Это рекомендуемый метод для эффективного и консистентного извлечения больших наборов данных (Deep Pagination). PIT создает "снимок" индекса, гарантируя консистентность данных во время длительного процесса извлечения.

Источник (Elasticsearch Reference. Paginate search results):
> If you need to preserve the index state while paging through more than 10,000 hits, use the search_after parameter with a point in time (PIT).
Перевод:
> Если вам нужно сохранить состояние индекса при постраничном просмотре более 10 000 результатов, используйте параметр search_after с point in time (PIT).

### 2.1.2. Использование Slicing для параллелизации

Использовать механизм Slicing для распараллеливания процесса извлечения.

Обоснование: Slicing позволяет разбить процесс извлечения на несколько независимых задач, выполняемых параллельно, что значительно увеличивает общую пропускную способность (`O.md`::§31.2.2.2).

Источник (Elasticsearch Reference. Slicing):
> To speed up the retrieval process, you can use slicing to break down the PIT search into multiple smaller, independent searches that can run in parallel.
Перевод:
> Чтобы ускорить процесс извлечения, вы можете использовать slicing для разбиения PIT-поиска на несколько меньших, независимых поисковых запросов, которые могут выполняться параллельно.

## 2.2. Transformation и Embedding (Трансформация и Генерация векторов)

Обработать извлеченные данные и сгенерировать Embeddings (`T2⁎`).

### 2.2.1. Подготовка текста и Chunking (Text Preparation and Chunking)

Сформировать единый текстовый документ (Chunk) для каждого продукта/варианта, объединив релевантные поля (название, описание, спецификации).

Обоснование: Использование стратегии "один продукт = один chunk" предотвращает фрагментацию контекста для компактных данных электронной коммерции (`O.md`::§17.2.3).

### 2.2.2. Генерация Embeddings (Embedding Generation)

Вызвать OpenAI API endpoint `/v1/embeddings` для преобразования текстовых Chunks в Dense Vectors. Использовать модель, например, `text-embedding-3-small`.

Обоснование: Внешняя генерация в Indexing Service обеспечивает гибкость и снижает нагрузку на кластер `E༄` (`O.md`::§17.3.3).

### 2.2.3. Пакетная обработка и обработка ошибок (Batching and Error Handling)

1.  Отправлять несколько текстовых inputs в одном API запросе (Batching) для повышения эффективности.
2.  Реализовать механизм повторных попыток с Exponential Backoff для обработки ошибок API (например, Rate Limits).

Обоснование: OpenAI API имеет ограничения скорости. Надежный конвейер должен корректно обрабатывать эти ограничения.

Источник (OpenAI Documentation. Rate limits):
> If you hit a rate limit, we recommend using a randomized exponential backoff.
Перевод:
> Если вы достигли Rate Limit, мы рекомендуем использовать рандомизированную экспоненциальную задержку (Exponential Backoff).

## 2.3. Loading (Загрузка данных)

Загрузить обработанные данные (метаданные и векторы) в Dedicated RAG Index.

### 2.3.1. Конфигурация RAG Index Mapping

Настроить схему (Mapping) RAG Index. Использовать тип `dense_vector` (Elasticsearch) или `knn_vector` (OpenSearch). Установить размерность (`dims`/`dimension`) и метрику сходства (`similarity`, например, `cosine`).

Обоснование: Корректная конфигурация необходима для выполнения ANN (Approximate Nearest Neighbor) поиска (`O.md`::§17.4).

### 2.3.2. Использование Bulk API и параллелизация

Использовать Bulk API для загрузки документов. Отправлять Bulk-запросы параллельно из нескольких потоков Indexing Service.

Обоснование: Bulk API значительно повышает скорость индексации. Параллельная отправка позволяет полнее использовать ресурсы кластера (`O.md`::§17.5.2, §17.5.3.2).

Источник (Elasticsearch Reference. Bulk API):
> The bulk API makes it possible to perform many index/delete operations in a single API call. This can greatly increase the indexing speed.
Перевод:
> Bulk API позволяет выполнять множество операций индексации/удаления в одном вызове API. Это может значительно увеличить скорость индексации.

## 2.4. Стратегия синхронизации и автоматизация (Synchronization Strategy and Automation)

Реализация `T4⁎` (Automated catalog syncing).

### 2.4.1. Стратегия полной синхронизации (Full Re-synchronization Strategy)

Реализовать стратегию периодической полной синхронизации (Full Re-index).

Обоснование: `E༄` не предоставляет нативного механизма Change Data Capture (CDC) (`O.md`::§31.2.1.1). Высокая производительность извлечения (PIT и Slicing) делает полную синхронизацию практичной и соответствующей требованиям проекта (daily/weekly updates, `O.md`::§2.3).

### 2.4.2. Реализация Zero-Downtime с использованием Index Alias

Реализовать обновление индекса без простоя сервиса с помощью Index Aliases (стратегия Blue/Green deployment).

1.  Создать новый временный RAG Index (например, `products-rag-YYYYMMDD-HHMMSS`).
2.  Выполнить полный цикл ETL (§2.1-§2.3) в этот новый индекс.
3.  После успешного завершения использовать Aliases API для атомарного переключения рабочего Alias (например, `products-rag-active`) со старого индекса на новый.
4.  Удалить старый индекс.

Обоснование: RAG Runtime Service должен обращаться к Alias. Атомарное переключение гарантирует, что пользователи не заметят процесса обновления индекса.

Источник (Elasticsearch Reference. Aliases API):
> Applications can use an alias instead of an index name. This allows you to reindex data without downtime or changes to your application’s search requests.
Перевод:
> Приложения могут использовать alias вместо имени индекса. Это позволяет вам переиндексировать данные без простоя или изменений в поисковых запросах вашего приложения.

### 2.4.3. Планирование (Scheduling)

Настроить запуск Indexing Service по расписанию (например, с использованием Kubernetes CronJobs или встроенных планировщиков Cloud-провайдеров).

# 3. Реализация RAG Runtime Service (API)

Этот сервис обрабатывает запросы пользователей в реальном времени (`T3⁎`) и предоставляет API.

## 3.1. Реализация Core RAG Workflow

Реализовать основной RAG Workflow с использованием выбранного Orchestration Framework (LangChain/LlamaIndex).

### 3.1.1. Query Embedding (Векторизация запроса)

Преобразовать запрос пользователя в Dense Vector, используя ту же модель OpenAI, что и на этапе ETL (§2.2.2).

Обоснование: Необходимо для выполнения семантического поиска в том же векторном пространстве (`O.md`::§21.2.3).

### 3.1.2. Retrieval (Поиск релевантных данных)

Выполнить поиск в Dedicated RAG Index (используя Alias).

#### 3.1.2.1. Реализация Hybrid Search

Применять стратегию Hybrid Search, комбинируя семантический поиск (ANN) с полнотекстовым поиском (BM25).

Обоснование: Hybrid Search значительно повышает релевантность в контексте электронной коммерции (`O.md`::§21.3.1).

Источник (Elasticsearch Reference. Hybrid search):
> Hybrid search combines the strengths of both traditional full-text search and vector search. [...] By combining these two approaches, hybrid search provides more accurate and relevant search results.
Перевод:
> Гибридный поиск сочетает сильные стороны как традиционного полнотекстового поиска, так и векторного поиска. [...] Комбинируя эти два подхода, гибридный поиск обеспечивает более точные и релевантные результаты поиска.

#### 3.1.2.2. Использование Reciprocal Rank Fusion (RRF)

Использовать Reciprocal Rank Fusion (RRF) для объединения результатов.

Обоснование: RRF является эффективным методом, который не требует сложной настройки весовых коэффициентов (boosts) (`O.md`::§21.3.2).

### 3.1.3. Generation (Генерация ответа)

#### 3.1.3.1. Prompt Engineering

Сконструировать Prompt для LLM. В System message явно инструктировать модель основываться только на контексте (Grounding) и включать цены и URL.

Обоснование: Это необходимо для минимизации галлюцинаций и выполнения целей проекта `T⁎` (`O.md`::§21.6).

#### 3.1.3.2. Вызов OpenAI API

Отправить Prompt в OpenAI Chat Completions API. Использовать актуальную модель (например, `gpt-4o`) с низким значением параметра `temperature` (например, 0.0 - 0.2).

Обоснование: Низкая температура обеспечивает детерминированность и точность ответов, основанных на фактах (`O.md`::§21.7.3).

Источник (OpenAI API Reference. Create chat completion. temperature):
> [...] lower values like 0.2 will make it more focused and deterministic.
Перевод:
> [...] более низкие значения, такие как 0.2, сделают его более сфокусированным и детерминированным.

## 3.2. Дизайн и реализация API (API Design and Implementation)

### 3.2.1. Определение спецификации API (Define API Specification)

Определить контракт API с использованием OpenAPI Specification (OAS).

Обоснование: OAS предоставляет стандартизированный способ описания REST API, что необходимо для документации и интеграции с ChatGPT.

### 3.2.2. Реализация API для On-site Chatbot (RAG API)

Создать основной Endpoint (например, `POST /api/v1/chat/completions`), который выполняет полный RAG Workflow (§3.1).

#### 3.2.2.1. Совместимость с форматом OpenAI API

Реализовать Endpoint, совместимый по формату запроса (Messages History) и ответа с OpenAI Chat Completions API.

Обоснование: Это значительно упрощает интеграцию на стороне клиента (On-site Widget), позволяя использовать стандартные клиентские библиотеки OpenAI и поддерживать контекст разговора.

#### 3.2.2.2. Реализация Streaming ответов

Реализовать поддержку Streaming ответов с использованием Server-Sent Events (SSE).

Обоснование: Streaming значительно улучшает User Experience (UX), отображая ответ по мере его генерации (токен за токеном), аналогично интерфейсу ChatGPT.

Источник (OpenAI API Reference. Create chat completion. stream):
> If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only server-sent events as they become available [...]
Перевод:
> Если установлено, будут отправляться частичные дельты сообщений, как в ChatGPT. Токены будут отправляться как server-sent events только с данными по мере их доступности [...]

### 3.2.3. Реализация API для ChatGPT Integration (Action API)

Для интеграции с ChatGPT через Custom GPT Actions необходимо реализовать специализированный API.

#### 3.2.3.1. Определение Action API Endpoint (Retrieval Only)

Определить отдельный API Endpoint (например, `POST /api/v1/actions/retrieve_products`), который выполняет только этап Retrieval (§3.1.2) и возвращает релевантный контекст о продуктах (JSON).

Обоснование: При использовании Custom GPT Actions, ChatGPT выступает в роли оркестратора и генератора ответа. Backend сервис предоставляет необходимые данные (контекст) через Action API. RAG Runtime Service не должен выполнять этап Generation в этом сценарии.

Источник (OpenAI Documentation. GPTs. Actions):
> Actions allow GPTs to talk to external APIs. [...] When a user makes a query that triggers an action, the GPT [...] makes the API call, and uses the API response to answer the user’s query.
Перевод:
> Actions позволяют GPT взаимодействовать с внешними API. [...] Когда пользователь делает запрос, который активирует Action, GPT [...] выполняет вызов API и использует ответ API для ответа на запрос пользователя.

#### 3.2.3.2. Публикация OpenAPI Specification

Предоставить OpenAPI Specification (§3.2.1), описывающую RAG API и Action API, для конфигурации Custom GPT.

# 4. Сквозная функциональность и эксплуатация (Cross-Cutting Concerns and Operations)

## 4.1. Реализация безопасности (Implement Security)

### 4.1.1. Управление учетными данными (Credential Management)

Использовать переменные окружения (Environment Variables) или системы управления секретами для хранения API ключей OpenAI и учетных данных `E༄`. Не хранить учетные данные в коде.

Источник (OpenAI. API security best practices):
> Store API keys in environment variables or a secrets management system.
Перевод:
> Храните API-ключи в переменных окружения или в системе управления секретами.

### 4.1.2. Аутентификация и авторизация (Authentication and Authorization)

1.  Для Action API (ChatGPT): Реализовать механизм аутентификации, требуемый платформой (например, API Keys или OAuth 2.0), и описать его в OpenAPI Specification.
2.  Для RAG API (On-site Widget): Ограничить доступ к API с помощью CORS (Cross-Origin Resource Sharing), разрешив только домен интернет-магазина.

Обоснование: CORS необходим для работы веб-приложений, таких как Chatbot Widget.

Источник (MDN Web Docs. Cross-Origin Resource Sharing (CORS)):
> Cross-Origin Resource Sharing (CORS) is an HTTP-header based mechanism that allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources.
Перевод:
> Cross-Origin Resource Sharing (CORS) — это механизм, основанный на HTTP-заголовках, который позволяет серверу указывать любые источники (домен, схему или порт), кроме своего собственного, с которых браузер должен разрешить загрузку ресурсов.

### 4.1.3. Реализация Rate Limiting

Реализовать Rate Limiting для публичных Endpoints для защиты от злоупотреблений и DoS-атак.

## 4.2. Реализация Observability (Implement Observability)

Интегрировать системы логирования, мониторинга метрик и трассировки.

### 4.2.1. Мониторинг метрик (Metrics Monitoring)

Отслеживать ключевые метрики: Latency запросов API (Retrieval и Generation), пропускную способность индексации, частоту ошибок и Cost Monitoring (Token Usage).

### 4.2.2. Использование инструментов трассировки (Tracing Tools)

Использовать специализированные инструменты (например, LangSmith, OpenTelemetry) для детальной трассировки выполнения цепочек RAG.

Обоснование: RAG workflow состоит из множества шагов. Трассировка позволяет визуализировать выполнение, выявлять узкие места и отлаживать качество ответов LLM в Production среде.

Источник (LangChain Documentation. LangSmith):
> LangSmith is a platform for building production-grade LLM applications. It lets you debug, test, evaluate, and monitor chains [...]
Перевод:
> LangSmith — это платформа для создания LLM-приложений Production уровня. Она позволяет отлаживать, тестировать, оценивать и мониторить цепочки [...]

## 4.3. Контейнеризация (Containerization)

Контейнеризировать Indexing Service и RAG Runtime Service с использованием Docker. Создать `Dockerfile` для каждого сервиса.

Обоснование: Контейнеризация обеспечивает консистентность среды выполнения и упрощает развертывание на современных платформах оркестрации (например, Kubernetes).

Источник (Docker Documentation. What is a container?):
> A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.
Перевод:
> Контейнер — это стандартная единица программного обеспечения, которая упаковывает код и все его зависимости, чтобы приложение быстро и надежно работало в разных вычислительных средах.