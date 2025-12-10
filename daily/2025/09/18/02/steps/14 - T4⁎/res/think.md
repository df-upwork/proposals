Пошаговая инструкция для `T4⁎` (Настройка автоматической синхронизации каталога) при использовании `T1⁎-A3` (Гибридный подход к извлечению данных) и `T2⁎-E༄` (Использование Elasticsearch/OpenSearch в качестве векторной базы данных).

# 1\. Определение архитектуры и стратегии синхронизации (Architecture and Strategy Definition)

## 1.1. Определение ролей индексов (Index Roles Definition)

Определить следующую структуру индексов в кластере `E༄` (Elasticsearch или OpenSearch):

1.  Source Index: Нативный индекс Magento, содержащий данные каталога, обогащенные согласно компоненту `T1⁎-A1` стратегии `T1⁎-A3`. Этот индекс является источником данных.
2.  Target Index (RAG Index): Отдельный индекс, содержащий метаданные и векторные представления (embeddings), оптимизированный для RAG-workflow (`T3⁎`).

Обоснование: Magento полностью управляет жизненным циклом Source Index и может удалить его во время операций reindexing (`O.md`::§26.3). Модификация Source Index напрямую (например, добавление векторов) небезопасна. Необходимо использовать отдельный Target Index для обеспечения стабильности RAG-системы (`O.md`::§31.2.1.3).

## 1.2. Выбор стратегии синхронизации (Synchronization Strategy Selection)

Использовать стратегию Periodic Full Synchronization (периодическая полная синхронизация). Процесс синхронизации реализуется как ETL (Extract, Transform, Load) конвейер между Source Index и Target Index.

Обоснование: Elasticsearch и OpenSearch не предоставляют нативного механизма Change Data Capture (CDC) для надежного отслеживания изменений и удалений документов внешними потребителями (`O.md`::§31.2.1.1). Учитывая требования проекта к частоте обновления (daily/weekly, `O.md`::§2.3), полная синхронизация является наиболее надежным подходом, гарантирующим консистентность данных.

## 1.3. Реализация Zero-Downtime с использованием Index Aliases (Zero-Downtime Implementation using Index Aliases)

Использовать механизм Index Aliases для обеспечения нулевого времени простоя RAG-сервиса во время синхронизации.

1.3.1. Создать Index Alias (например, `rag-catalog-live`), который будет использоваться RAG-сервисом для выполнения всех поисковых запросов.

1.3.2. Во время синхронизации выполнять загрузку данных в новый Target Index с уникальным именем (например, `rag-catalog-YYYYMMDDHHMMSS`).

1.3.3. После успешного завершения загрузки атомарно переключить Index Alias со старого индекса на новый (§5.2).

Обоснование: Index Aliases позволяют отделить имя, используемое приложением, от фактического имени индекса. Атомарное переключение позволяет обновить данные без влияния на доступность сервиса.

Источник (Elasticsearch Reference. Aliases):

> You can use aliases to reindex data with zero downtime.

Перевод:

> Вы можете использовать aliases для переиндексации данных с нулевым временем простоя.

Источник (OpenSearch Documentation. Index aliases):

> If you need to change the index that an alias refers to, you can do so with zero downtime.

Перевод:

> Если вам нужно изменить индекс, на который ссылается alias, вы можете сделать это с нулевым временем простоя.

# 2\. Процесс синхронизации: Этап извлечения (Extraction Phase)

Этот этап реализует компонент `T1⁎-A2` стратегии `T1⁎-A3` (чтение данных из Source Index).

## 2.1. Создание консистентного снапшота с использованием Point in Time (PIT) (Create Consistent Snapshot using Point in Time)

Перед началом извлечения данных создать Point in Time (PIT) для Source Index.

Обоснование: Извлечение большого объема данных занимает время. PIT фиксирует состояние индекса на момент начала операции, гарантируя, что изменения, происходящие в Source Index во время процесса извлечения, не повлияют на консистентность извлекаемых данных.

Источник (Elasticsearch Reference. Point in time API):

> The point in time (PIT) feature preserves the index state over a period of time. This allows you to run multiple search requests against the same dataset, which is fixed in time.

Перевод:

> Функция point in time (PIT) сохраняет состояние индекса в течение определенного периода времени. Это позволяет выполнять несколько поисковых запросов к одному и тому же набору данных, зафиксированному во времени.

Источник (OpenSearch Documentation. Point in Time):

> Point in Time (PIT) is a search type that allows you to run different queries against a dataset that is fixed in time.

Перевод:

> Point in Time (PIT) — это тип поиска, который позволяет выполнять различные запросы к набору данных, зафиксированному во времени.

## 2.2. Использование `search_after` для глубокой пагинации (Use `search_after` for Deep Pagination)

Использовать параметр `search_after` в сочетании с PIT ID для итеративного извлечения всех документов.

Обоснование: Стандартная пагинация с использованием `from` и `size` неэффективна и ограничена (по умолчанию 10000 документов) для извлечения больших наборов данных. `search_after` предоставляет эффективный механизм курсора.

Источник (Elasticsearch Reference. Paginate search results):

> If you need to preserve the index state while paging through more than 10,000 hits, use the search\_after parameter with a point in time (PIT).

Перевод:

> Если вам нужно сохранить состояние индекса при пагинации более чем 10 000 результатов, используйте параметр search\_after с point in time (PIT).

## 2.3. Использование Slicing для параллельного извлечения (Use Slicing for Parallel Extraction)

(Только для Elasticsearch) Использовать механизм Slicing для разделения PIT на несколько независимых сегментов (slices) и выполнения извлечения параллельно несколькими workers.

Обоснование: Параллельное извлечение значительно увеличивает общую пропускную способность и сокращает время, необходимое для синхронизации (`O.md`::§31.2.2.2).

Источник (Elasticsearch Reference. Slicing):

> To speed up the retrieval process, you can use slicing to break down the PIT search into multiple smaller, independent searches that can run in parallel.

Перевод:

> Чтобы ускорить процесс извлечения, вы можете использовать slicing для разбиения PIT-поиска на несколько меньших, независимых поисковых запросов, которые могут выполняться параллельно.

Примечание: В OpenSearch Slicing в настоящее время не поддерживается в сочетании с PIT. В этом случае следует использовать последовательное извлечение с PIT и `search_after`.

# 3\. Процесс синхронизации: Этап трансформации (Transformation Phase)

## 3.1. Подготовка данных (Data Preparation)

Для каждого извлеченного документа выполнить очистку, нормализацию и формирование единого текстового фрагмента (chunk), как определено в стратегии `T2⁎` (`O.md`::§17.2).

## 3.2. Генерация Embeddings (Embedding Generation)

Сгенерировать векторные представления (dense vectors) для текстовых фрагментов, используя OpenAI API (например, модель `text-embedding-3-small`).

Обоснование: Необходимо использовать ту же модель, которая была выбрана на этапе `T2⁎` (`O.md`::§17.3).

## 3.3. Пакетная обработка запросов к API (Batch API Requests)

Группировать текстовые фрагменты в пакеты (batches) при отправке запросов к OpenAI API.

Обоснование: Отправка массива текстов в одном запросе снижает сетевые задержки и увеличивает общую пропускную способность генерации embeddings.

Источник (OpenAI API Reference. Create embeddings. input):

> To embed multiple inputs in a single request, pass an array of strings or array of token arrays.

Перевод:

> Чтобы встроить несколько входных данных в одном запросе, передайте массив строк или массив массивов токенов.

## 3.4. Обработка ошибок OpenAI API (OpenAI API Error Handling)

Реализовать логику обработки ошибок, связанных с превышением лимитов (Rate Limits) OpenAI API, используя механизм Exponential Backoff.

Источник (OpenAI Documentation. Rate limits. Error mitigation):

> A optimization optimization is to use exponential backoff. Exponential backoff means performing a short sleep when a rate limit error is hit, then retrying the unsuccessful request.

Перевод:

> Оптимизацией является использование exponential backoff. Exponential backoff означает выполнение короткой паузы при получении ошибки rate limit, а затем повторную попытку выполнения неуспешного запроса.

# 4\. Процесс синхронизации: Этап загрузки (Loading Phase)

## 4.1. Создание нового Target Index (Create New Target Index)

Создать новый Target Index с уникальным именем (§1.3.2). При создании применить предопределенные Mappings (схема полей, включая `dense_vector` или `knn_vector`) и Settings (`O.md`::§17.4).

## 4.2. Оптимизация настроек для индексации (Optimize Settings for Indexing)

Перед началом загрузки данных изменить динамические настройки нового индекса для максимизации скорости индексации.

### 4.2.1. Отключение `refresh_interval`

Установить `index.refresh_interval` в `-1`.

Обоснование: Операция refresh делает документы доступными для поиска. Это ресурсоемкий процесс, который замедляет индексацию. Во время массовой загрузки его следует отключить.

Источник (Elasticsearch Reference. Tune for indexing speed. Disable refresh):

> If the indexing process is building a new index from scratch, setting this value to -1 to disable automatic refreshes altogether maximizes the indexing speed.

Перевод:

> Если процесс индексации создает новый индекс с нуля, установка этого значения в -1 для полного отключения автоматических обновлений (automatic refreshes) максимизирует скорость индексации.

### 4.2.2. Отключение репликации (Disable Replicas)

Установить `index.number_of_replicas` в `0`.

Обоснование: Репликация данных на другие узлы увеличивает время индексации. Реплики будут созданы после завершения загрузки (§4.5.2).

Источник (Elasticsearch Reference. Tune for indexing speed. Disable replicas):

> When creating a large index from scratch, setting index.number\_of\_replicas to 0 disables replication entirely, which can sometimes speed up indexing.

Перевод:

> При создании большого индекса с нуля установка index.number\_of\_replicas в 0 полностью отключает репликацию, что иногда может ускорить индексацию.

## 4.3. Использование Bulk API для загрузки (Use Bulk API for Loading)

Использовать Bulk API для загрузки трансформированных документов и их векторов в новый Target Index.

Обоснование: Bulk API позволяет выполнять множество операций в одном запросе, что значительно эффективнее отправки документов по одному (`O.md`::§17.5.2).

## 4.4. Параллельная загрузка и надежность (Parallel Loading and Reliability)

### 4.4.1. Параллельная отправка запросов (Parallel Requests)

Использовать несколько параллельных потоков или процессов (workers) для отправки Bulk-запросов.

Обоснование: Параллельная отправка позволяет полнее использовать ресурсы кластера и максимизировать пропускную способность индексации (`O.md`::§17.5.3.2).

Источник (Elasticsearch Reference. Tune for indexing speed. Use multiple threads/workers):

> In order to use all resources of the cluster, you should send data from multiple threads or processes.

Перевод:

> Чтобы использовать все ресурсы кластера, вы должны отправлять данные из нескольких потоков или процессов.

### 4.4.2. Обработка ошибок `E༄` и Exponential Backoff

Реализовать логику обработки ошибок HTTP 429 (TOO\_MANY\_REQUESTS) при выполнении Bulk-запросов с использованием механизма Exponential Backoff.

Обоснование: Код 429 указывает на перегрузку кластера. Механизм повторных попыток с задержкой необходим для обеспечения надежности автоматизированного конвейера (`O.md`::§17.5.4).

Источник (Elasticsearch Reference. Tune for indexing speed):

> Make sure to watch for TOO\_MANY\_REQUESTS (429) response codes [...] When it happens, you should pause indexing a bit before trying again, ideally with randomized exponential backoff.

Перевод:

> Обязательно следите за кодами ответа TOO\_MANY\_REQUESTS (429) [...] Когда это происходит, вам следует немного приостановить индексацию, прежде чем пытаться снова, в идеале с рандомизированной exponential backoff.

## 4.5. Восстановление настроек и оптимизация (Restore Settings and Optimization)

После завершения загрузки данных восстановить настройки индекса и оптимизировать его для поиска.

### 4.5.1. Восстановление `refresh_interval`

Установить `index.refresh_interval` в рабочее значение (например, `1s`).

### 4.5.2. Включение репликации (Enable Replicas)

Установить `index.number_of_replicas` в требуемое значение для обеспечения отказоустойчивости (например, `1`). Дождаться завершения репликации (Index health станет `green`).

### 4.5.3. Выполнение Force Merge (Execute Force Merge)

Выполнить операцию Force Merge для нового Target Index. Рекомендуется установить `max_num_segments` в небольшое значение (например, `1`).

Обоснование: Массовая индексация создает множество мелких сегментов. Force Merge объединяет их, что улучшает производительность поиска (включая ANN search) и снижает потребление памяти.

Источник (Elasticsearch Reference. Force merge API):

> The force merge operation allows to reduce the number of segments by merging them.

Перевод:

> Операция force merge позволяет уменьшить количество сегментов путем их слияния.

# 5\. Активация и очистка (Activation and Cleanup)

## 5.1. Верификация нового индекса (Verify New Index)

Проверить корректность нового Target Index. Сравнить количество документов (используя Count API) в новом индексе с количеством документов в Source Index (на момент PIT). Выполнить тестовые векторные запросы.

## 5.2. Атомарное переключение Alias (Atomic Alias Switchover)

Использовать Update Aliases API (`POST /_aliases`) для атомарного переключения Index Alias (§1.3.1) со старого Target Index на новый.

Обоснование: API позволяет выполнить добавление нового индекса и удаление старого в одной атомарной операции, гарантируя Zero-Downtime.

Источник (Elasticsearch Reference. Update aliases API):

> You can use the update aliases API to perform one or more alias actions in a single atomic operation.

Перевод:

> Вы можете использовать API update aliases для выполнения одного или нескольких действий с alias в одной атомарной операции.

Пример запроса (Elasticsearch и OpenSearch):

```json
POST /_aliases
{
  "actions": [
    {
      "remove": {
        "index": "rag-catalog-OLDTIMESTAMP",
        "alias": "rag-catalog-live"
      }
    },
    {
      "add": {
        "index": "rag-catalog-NEWTIMESTAMP",
        "alias": "rag-catalog-live"
      }
    }
  ]
}
```

## 5.3. Очистка ресурсов (Cleanup Resources)

### 5.3.1. Закрытие PIT (Close PIT)

Закрыть Point in Time контекст, созданный на этапе §2.1, используя Close PIT API.

Обоснование: Активные PIT потребляют ресурсы кластера. Их необходимо освобождать после завершения использования.

Источник (Elasticsearch Reference. Close point in time API):

> The close point in time API closes a point in time (PIT). This API releases resources that maintain the state of an index for a PIT.

Перевод:

> API close point in time закрывает point in time (PIT). Этот API освобождает ресурсы, которые поддерживают состояние индекса для PIT.

### 5.3.2. Удаление старого индекса (Delete Old Index)

Удалить старый Target Index после успешного переключения Alias. Рекомендуется сохранять несколько последних индексов для возможности быстрого отката (Rollback).

Обоснование: Освобождение дискового пространства и памяти в кластере.

# 6\. Автоматизация и мониторинг (Automation and Monitoring)

## 6.1. Планирование выполнения (Scheduling)

Настроить автоматический запуск ETL-конвейера (Шаги 2-5) в соответствии с требуемым расписанием (daily/weekly).

### 6.1.1. Выбор планировщика (Scheduler Selection)

Использовать надежный планировщик задач (например, Kubernetes CronJob, AWS EventBridge Scheduler) или оркестратор рабочих процессов (например, Apache Airflow).

### 6.1.2. Выбор времени выполнения (Execution Time)

Планировать выполнение синхронизации в периоды наименьшей нагрузки на кластер `E༄`.

Обоснование: Интенсивные операции чтения и записи создают нагрузку на кластер `E༄`, который также обслуживает основной поиск витрины магазина.

## 6.2. Мониторинг и оповещения (Monitoring and Alerting)

Реализовать мониторинг процесса синхронизации.

6.2.1. Логировать ключевые метрики: время выполнения каждого этапа, количество обработанных документов, количество ошибок (включая ошибки OpenAI API и `E༄` API).

6.2.2. Настроить оповещения о сбоях конвейера или значительном отклонении метрик.