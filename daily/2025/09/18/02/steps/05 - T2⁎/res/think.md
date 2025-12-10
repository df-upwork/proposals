https://g.co/gemini/share/a7b9eb865f63

# 1\. Подготовка инфраструктуры и ресурсов (Infrastructure and Resource Preparation)

## 1.1. Верификация платформы и версии (Platform and Version Verification)

Уточнить используемую платформу (Elasticsearch или OpenSearch) и её версию для определения доступных функций и синтаксиса API.

### 1.1.1. Elasticsearch

Рекомендуется использовать версию 8.0 или выше для оптимальной поддержки Approximate Nearest Neighbor (ANN) search.

Обоснование: Функциональность Vector search была введена и стабилизирована в этих версиях.

Источник (Elasticsearch Reference. Vector search):

> Introduced in 8.0.0.

### 1.1.2. OpenSearch

Убедиться, что плагин `opensearch-knn` установлен и активирован.

Обоснование: В OpenSearch функциональность векторного поиска обеспечивается через специализированный плагин k-NN.

Источник (OpenSearch Documentation. k-NN plugin):

> The k-NN plugin enables users to search for the k-nearest neighbors to a query vector in an index.

Перевод:

> Плагин k-NN позволяет пользователям искать k-ближайших соседей для вектора запроса в индексе.

## 1.2. Конфигурация ресурсов памяти (Memory Resource Configuration)

Обеспечить достаточный объем оперативной памяти для узлов (nodes) кластера.

Обоснование: Алгоритмы ANN, такие как HNSW (Hierarchical Navigable Small World), хранят векторные графы в памяти (page cache) для обеспечения низкой задержки поиска.

Источник (Elasticsearch Reference. Tune approximate nearest neighbor (ANN) search):

> HNSW builds a graph during indexing that is used for searching. This graph is stored in the node’s page cache in memory. [...] Ensure your nodes have enough memory capacity to accommodate these data structures.

Перевод:

> HNSW строит граф во время индексации, который используется для поиска. Этот граф хранится в страничном кэше узла в памяти. [...] Убедитесь, что ваши узлы имеют достаточный объем памяти для размещения этих структур данных.

# 2\. Подготовка и трансформация данных (Data Preparation and Transformation)

Этот этап преобразует сырые данные, извлеченные на этапе `T1⁎`, в формат, оптимизированный для RAG. Необходимо учесть аспекты, описанные в `O.md`::§16.

## 2.1. Очистка и нормализация контента (Content Cleaning and Normalization)

2.1.1. Очистить текстовые поля (например, `description`) от HTML-разметки, CSS и JavaScript.

Обоснование: HTML и другие нетекстовые элементы вносят шум, который ухудшает качество embeddings и снижает релевантность семантического поиска (`O.md`::§16.1.2).

2.1.2. Убедиться, что все спецификации (EAV attributes) представлены в виде текстовых меток (Labels), а не числовых идентификаторов (Option IDs).

Обоснование: Числовые идентификаторы не несут семантической нагрузки для Language Models. Для эффективной работы RAG требуются текстовые значения (`O.md`::§16.2).

## 2.2. Стратегия гранулярности и обработка вариантов (Granularity Strategy and Variant Handling)

Индексировать каждый вариант продукта (Simple Product, являющийся частью Configurable Product) как отдельный документ.

Обоснование: В электронной коммерции цена, наличие и спецификации зависят от конкретного варианта. Индексация на уровне вариантов обеспечивает точность информации, предоставляемой RAG-системой (`O.md`::§16.3).

## 2.3. Стратегия чанкинга и консолидация текста (Chunking Strategy and Consolidation)

Использовать стратегию "один вариант/продукт = один фрагмент (chunk)". Сформировать единый текстовый документ (Synthesized Document) путем объединения всех релевантных полей (название, бренд, описание, спецификации).

Пример структуры:
`Название: {Name}. Бренд: {Brand}. Описание: {Cleaned Description}. Спецификации: {Attribute1}: {Value1}, {Attribute2}: {Value2}.`

Обоснование: Данные о продукте обычно компактны и семантически целостны. Генерация одного вектора, инкапсулирующего всю информацию, предпочтительнее разделения на мелкие фрагменты, так как это предотвращает фрагментацию контекста (`O.md`::§16.1.3).

# 3\. Генерация векторных представлений (Embedding Generation)

## 3.1. Выбор модели эмбеддингов (Embedding Model Selection)

Выбрать модель для преобразования текстовых chunks в плотные векторы (dense vectors). Рекомендуется использовать модели OpenAI, например, `text-embedding-3-small`.

Обоснование: Задача предполагает интеграцию с ChatGPT (`O.md`::§2.3). Использование моделей от того же поставщика (OpenAI) обеспечивает согласованность векторного пространства.

Источник (OpenAI. New embedding models and API updates):

> We are introducing two new embedding models: a smaller and highly efficient text-embedding-3-small model, and a larger and more powerful text-embedding-3-large model.

Перевод:

> Мы представляем две новые модели эмбеддингов: меньшую и высокоэффективную модель text-embedding-3-small и большую и более мощную модель text-embedding-3-large.

## 3.2. Определение размерности (Vector Dimensions)

Зафиксировать количество измерений (dimensions) выбранной модели. Для `text-embedding-3-small` это 1536.

Обоснование: Это значение необходимо для конфигурации индекса (§4).

## 3.3. Архитектура генерации (Generation Architecture)

Рекомендуется использовать внешнюю генерацию (External Generation). Генерировать embeddings во внешнем приложении (backend сервис на Python или Node.js), которое управляет процессом ETL. Приложение вызывает OpenAI API и формирует финальный JSON документ перед отправкой в Elasticsearch/OpenSearch.

Обоснование: Этот подход обеспечивает максимальную гибкость в выборе моделей, контроль над процессом и позволяет разгрузить кластер Elasticsearch/OpenSearch от задач инференса (inference).

Источник (Elasticsearch Guide. When to perform inference outside of Elasticsearch):

> If you want to use a model that is not supported to import to Elasticsearch, you can perform inference externally. In this case, you need to generate the embeddings by running the model on your client side or some other application server and then ingest the data into Elasticsearch.

Перевод:

> Если вы хотите использовать модель, импорт которой в Elasticsearch не поддерживается, вы можете выполнять инференс внешне. В этом случае вам нужно генерировать embeddings, запустив модель на вашей клиентской стороне или на каком-либо другом сервере приложений, а затем загрузить данные в Elasticsearch.

# 4\. Конфигурация индекса (Index Configuration)

Создать индекс с корректной схемой (mapping) для хранения метаданных и векторов.

## 4.1. Определение полей метаданных (Metadata Fields Mapping)

Настроить mapping для метаданных (SKU, цена, URL, категории). Использовать тип `keyword` для полей, требующих точной фильтрации, и числовые типы (например, `float`).

Обоснование: Эти поля необходимы для реализации гибридного поиска (Hybrid Search), фильтрации результатов и предоставления точной информации в ответе RAG.

## 4.2. Конфигурация векторного поля в Elasticsearch (Elasticsearch Vector Field Configuration)

Использовать тип `dense_vector`.

4.2.1. Установить `dims` равным размерности модели (например, 1536).
4.2.2. Установить `index: true` для включения ANN поиска с использованием HNSW.
4.2.3. Установить `similarity`. Рекомендуется `cosine`.

Обоснование: Параметры необходимы для корректной индексации и поиска векторов. Модели OpenAI нормализованы, что делает `cosine` эффективной метрикой сходства.

Источник (OpenAI Help Center. Embeddings FAQ):

> OpenAI embeddings are normalized to length 1 [...]

Перевод:

> Эмбеддинги OpenAI нормализованы до длины 1 [...]

Источник (Elasticsearch Reference. Dense vector field type):

> dims
> (Required, integer) Number of dimensions in the vector.
> similarity
> (Required, string) The vector similarity metric.

Перевод:

> dims
> (Обязательный, целое число) Количество измерений в векторе.
> similarity
> (Обязательный, строка) Метрика векторного сходства.

Пример Mapping (Elasticsearch):

```json
PUT /product-catalog
{
  "mappings": {
    "properties": {
      "product_vector": {
        "type": "dense_vector",
        "dims": 1536,
        "index": true,
        "similarity": "cosine"
      },
      "sku": { "type": "keyword" },
      "url": { "type": "keyword" },
      "price": { "type": "float" }
    }
  }
}
```

## 4.3. Конфигурация векторного поля в OpenSearch (OpenSearch Vector Field Configuration)

Использовать тип `knn_vector`.

4.3.1. В настройках индекса (settings) установить `index.knn: true`.
4.3.2. Установить `dimension` равным размерности модели.
4.3.3. Определить `method`, указав `engine` (например, `faiss` или `lucene`), `name`: `hnsw`, и `space_type`: `cosinesimil` (аналог `cosine`).

Обоснование: OpenSearch имеет отличный синтаксис и требования для настройки векторного поиска.

Источник (OpenSearch Documentation. k-NN. Methods):

> The method object defines the ANN algorithm that you want to use for your k-NN vector field. It contains the engine, name, space\_type, and parameters.

Перевод:

> Объект method определяет алгоритм ANN, который вы хотите использовать для вашего поля k-NN вектора. Он содержит engine, name, space\_type и parameters.

Пример Mapping (OpenSearch):

```json
PUT /product-catalog
{
  "settings": {
    "index.knn": true
  },
  "mappings": {
    "properties": {
      "product_vector": {
        "type": "knn_vector",
        "dimension": 1536,
        "method": {
          "name": "hnsw",
          "space_type": "cosinesimil",
          "engine": "faiss"
        }
      },
      "sku": { "type": "keyword" }
    }
  }
}
```

# 5\. Процесс индексации (Indexing Process)

Реализовать конвейер, который выполняет подготовку данных (§2), генерацию embeddings (§3) и загрузку в индекс (§4).

## 5.1. Управление идентификаторами документов (Document ID Management)

Присваивать уникальные идентификаторы (`_id`) документам в индексе на основе стабильных идентификаторов из Magento (например, `entity_id` или `sku` варианта).

Обоснование: Использование стабильных идентификаторов позволяет обновлять существующие документы при изменении данных в каталоге, что критически важно для процесса синхронизации (`T4⁎`).

## 5.2. Пакетная загрузка (Bulk Indexing)

Использовать Bulk API для загрузки документов в индекс.

Обоснование: Bulk API позволяет выполнять множество операций в одном запросе, что значительно повышает скорость индексации по сравнению с отправкой документов по одному.

Источник (Elasticsearch Reference. Bulk API):

> The bulk API makes it possible to perform many index/delete operations in a single API call. This can greatly increase the indexing speed.

Перевод:

> Bulk API позволяет выполнять множество операций индексации/удаления в одном вызове API. Это может значительно увеличить скорость индексации.

## 5.3. Оптимизация производительности (Performance Optimization)

5.3.1. Определить оптимальный размер пакета (Bulk Size) экспериментально (например, 5-15 МБ на запрос).

Обоснование: Оптимальный размер зависит от характеристик оборудования и сложности документов. Слишком большие пакеты могут вызвать избыточное потребление памяти.

Источник (Elastic Docs. Tune for indexing speed):

> In order to know the optimal size of a bulk request, you should run a benchmark [...] When the indexing speed starts to plateau then you know you reached the optimal size of a bulk request for your data.

Перевод:

> Чтобы узнать оптимальный размер bulk-запроса, вам следует провести бенчмарк [...] Когда скорость индексации перестает расти, вы знаете, что достигли оптимального размера bulk-запроса для ваших данных.

5.3.2. Использовать несколько потоков или процессов для отправки Bulk-запросов параллельно.

Обоснование: Параллельная отправка позволяет полнее использовать ресурсы кластера и максимизировать пропускную способность индексации.

Источник (Elastic Docs. Tune for indexing speed):

> A single thread sending bulk requests is unlikely to be able to max out the indexing capacity of an Elasticsearch cluster. In order to use all resources of the cluster, you should send data from multiple threads or processes.

Перевод:

> Один поток, отправляющий bulk-запросы, вряд ли сможет максимально использовать индексирующую способность кластера Elasticsearch. Чтобы использовать все ресурсы кластера, вы должны отправлять данные из нескольких потоков или процессов.

## 5.4. Обработка ошибок и надежность (Error Handling and Reliability)

Реализовать логику обработки ошибок, в частности кодов ответа HTTP 429 (TOO\_MANY\_REQUESTS). При получении 429 использовать механизм экспоненциальной задержки (exponential backoff).

Обоснование: Код 429 указывает на то, что кластер не справляется с текущей скоростью индексации. Механизм повторных попыток необходим для обеспечения надежности автоматизированного конвейера (`O.md`::§16.6.3).

Источник (Elastic Docs. Tune for indexing speed):

> Make sure to watch for TOO\_MANY\_REQUESTS (429) response codes [...] When it happens, you should pause indexing a bit before trying again, ideally with randomized exponential backoff.

Перевод:

> Обязательно следите за кодами ответа TOO\_MANY\_REQUESTS (429) [...] Когда это происходит, вам следует немного приостановить индексацию, прежде чем пытаться снова, в идеале с рандомизированной экспоненциальной задержкой.

# 6\. Верификация конвейера (Pipeline Verification)

## 6.1. Проверка индексации (Indexing Check)

Убедиться, что количество документов в индексе соответствует ожидаемому количеству продуктов/вариантов, используя Count API. Проверить случайные документы на наличие заполненного векторного поля.

## 6.2. Тестирование векторного поиска (Test Vector Search)

Выполнить тестовый запрос kNN search.

6.2.1. Сгенерировать embedding для тестовой фразы, используя ту же модель (§3.1).
6.2.2. Выполнить запрос к Search API, используя опцию `knn` (Elasticsearch) или `knn` query clause (OpenSearch).
6.2.3. Убедиться, что результаты релевантны запросу.

Обоснование: Этот шаг подтверждает, что весь конвейер, от подготовки данных до конфигурации ANN индекса, функционирует корректно.

Источник (Elasticsearch Reference. k-nearest neighbor (kNN) search):

> With the knn option, you can search for the k-nearest vectors to a query vector, as measured by a similarity metric.

Перевод:

> С помощью опции knn вы можете искать k ближайших векторов к вектору запроса, измеряемых метрикой сходства.