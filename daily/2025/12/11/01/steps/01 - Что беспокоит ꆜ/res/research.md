https://gemini.google.com/share/abbaebeb2f0d

## **1. Стратегический обзор архитектурных вызовов в условиях высокой кардинальности**

Проект RunRepeat.com (в дальнейшем именуемый "Проект P⁎"), представляющий собой масштабную платформу агрегации обзоров и электронной коммерции, столкнулся с рядом критических проблем производительности и стабильности инфраструктуры кэширования. Анализ симптоматики, предоставленной технической командой клиента, указывает на классическую, но сложную в диагностике дихотомию между "утечкой памяти" (memory leak) и "раздуванием кэша" (cache bloat). В контексте высоконагруженных систем, использующих Varnish Cache в качестве HTTP-акселератора, эти понятия часто смешиваются, приводя к ошибочным стратегиям оптимизации.

Современные архитектуры e-commerce, подобные RunRepeat, характеризуются использованием фасетной навигации — системы глубокой фильтрации контента по множеству атрибутов (размер, цвет, бренд, технические характеристики обуви).1 Это создает среду с экстремально высокой кардинальностью URL-адресов. В отсутствие строгих механизмов нормализации запросов, Varnish Cache вынужден обрабатывать комбинаторный взрыв уникальных объектов, что неизбежно приводит к исчерпанию ресурсов оперативной памяти. Однако, как показывает детальное изучение технических данных, проблема RunRepeat выходит за рамки простого управления объектами и затрагивает фундаментальные механизмы взаимодействия демона varnishd с подсистемой управления памятью операционной системы Linux.

Центральной гипотезой данного исследования является утверждение, что наблюдаемая нестабильность вызвана тремя взаимосвязанными факторами:

1. **Фрагментация кучи (Heap Fragmentation):** Неэффективность стандартного аллокатора glibc при работе с паттернами аллокации Varnish, приводящая к росту RSS (Resident Set Size) процесса без реального увеличения полезной нагрузки.3  
2. **Аномалии временного хранилища (Transient Storage):** Неконтролируемый рост "Transient" хранилища, которое по умолчанию не имеет верхнего лимита памяти и используется для короткоживущих объектов и буферизации потоковой передачи данных.5  
3. **Кэш-блоттинг (Cache Bloat):** Заполнение хранилища дубликатами контента из-за отсутствия нормализации Query String и заголовков User-Agent, что превращает полезный кэш в хранилище мусорных данных.7

В данном отчете представлен исчерпывающий анализ каждого из этих слоев, подкрепленный техническими данными и рекомендациями по переходу к устойчивой архитектуре.

## ---

**2. Глубинный анализ подсистемы управления памятью: Аллокаторы и Фрагментация**

Для понимания природы "утечек памяти", о которых сообщает клиент, необходимо рассмотреть механизм взаимодействия Varnish с системной памятью. Varnish не управляет физической памятью напрямую; вместо этого, при использовании бэкенда хранения malloc, он делегирует эту задачу стандартному системному аллокатору через вызовы malloc() и free().8

### **2.1. Механика взаимодействия Varnish и системного аллокатора**

Когда Varnish настроен с параметром -s malloc,256G, это создает иллюзию, что потребление памяти жестко ограничено 256 гигабайтами. В реальности этот лимит применяется только к *полезной нагрузке* кэшированных объектов. Он не учитывает накладные расходы на структуры данных ядра Varnish (overhead), такие как struct object, struct objcore и struct objhead, которые необходимы для отслеживания заголовков, сроков действия (TTL) и состояния объектов. Оценки показывают, что накладные расходы составляют примерно 1 КБ на каждый объект.8

Для сайта масштаба RunRepeat, где количество объектов может исчисляться десятками миллионов (из-за вариативности фильтров), накладные расходы могут составлять десятки гигабайт сверх установленного лимита -s.

| Тип памяти | Описание | Управляемость лимитом -s |
| :---- | :---- | :---- |
| **Object Storage** | Тело кэшированного объекта (HTML, JSON, изображения) | **Да** (Жесткий лимит) |
| **Object Overhead** | Метаданные (заголовки, баны, указатели) ~1KB/объект | **Нет** (Линейный рост от кол-ва объектов) |
| **Transient Storage** | Временные объекты, streaming buffers, hit-for-miss | **Нет** (По умолчанию unbounded) |
| **Workspace Memory** | Память потоков (workspace_client, thread_pool_stack) | **Нет** (Зависит от кол-ва потоков) |
| **Fragmentation** | Потерянная память внутри аллокатора ("дыры") | **Нет** (Зависит от эффективности аллокатора) |

### **2.2. Проблема фрагментации в glibc malloc**

Стандартным аллокатором в большинстве дистрибутивов Linux (RHEL, Debian, Ubuntu) является реализация malloc из библиотеки glibc (основанная на ptmalloc). Анализ источников указывает на то, что glibc крайне неэффективен для паттернов нагрузки, характерных для Varnish: высокая конкурентность, частые аллокации и деаллокации объектов различного размера.3

Проблема заключается в механизме работы с "аренами" (arenas). Для уменьшения блокировок (lock contention) в многопоточной среде, glibc создает несколько арен памяти. Когда память освобождается (free()), она возвращается в арену, но не всегда возвращается операционной системе. Если Varnish запрашивает блок памяти, который не помещается в существующие "дыры" фрагментированной кучи, аллокатор запрашивает новые страницы у ОС. Это приводит к росту виртуальной памяти (VSZ) и резидентной памяти (RSS), даже если внутренние счетчики Varnish показывают наличие свободного места в хранилище.4

Клиент интерпретирует это как утечку памяти, так как процесс varnishd потребляет все больше RAM, в то время как объем полезных данных в кэше может оставаться стабильным. Это классический пример внешней фрагментации. В особо тяжелых случаях, описанных в технических отчетах, переключение с glibc на альтернативные аллокаторы позволяло сократить потребление памяти с 192 ГБ до 18 ГБ.10

### **2.3. Превосходство jemalloc в высоконагруженных средах**

Техническим стандартом де-факто для высокопроизводительных приложений управления памятью (таких как Redis, Varnish, Firefox) является использование аллокатора jemalloc, разработанного Джейсоном Эвансом.

jemalloc использует принципиально иную стратегию управления памятью, разделяя объекты на классы по размеру (size classes) и используя структуру "chunks" и "runs". Это позволяет минимизировать фрагментацию, так как объекты одного размера группируются вместе. Освобождение блока памяти в jemalloc с гораздо большей вероятностью приводит к освобождению целого чанка, который может быть немедленно возвращен операционной системе.3

Кроме того, jemalloc предоставляет расширенные возможности интроспекции и настройки, такие как параметры "decay", управляющие скоростью возврата "грязных" страниц (dirty pages) ядру ОС. Установка агрессивных параметров decay может существенно снизить RSS процесса ценой незначительного увеличения нагрузки на CPU.12

Для RunRepeat.com критически важно верифицировать, с какой библиотекой слинкован исполняемый файл varnishd. В системах на базе RHEL/CentOS jemalloc часто не является дефолтным и требует явной установки пакета jemalloc и настройки systemd unit-файла для предзагрузки библиотеки или использования специально скомпилированной версии Varnish.14 Игнорирование этого фактора делает любые настройки VCL косметическими мерами на фоне фундаментальной утечки ресурсов.

## ---

**3. Парадокс временного хранилища (Transient Storage)**

Одной из наиболее коварных и наименее очевидных причин нестабильности Varnish является механизм Transient Storage. Анализ конфигурации и симптомов указывает на высокую вероятность того, что именно этот компонент ответственен за неконтролируемые всплески потребления памяти, приводящие к срабатыванию OOM Killer.15

### **3.1. Архитектура Transient Storage**

В архитектуре Varnish предусмотрено специальное хранилище для объектов, которые считаются "короткоживущими". По умолчанию, любой объект, чей TTL (Time To Live) меньше значения параметра shortlived (по умолчанию 10.0 секунд), автоматически помещается в Transient Storage, а не в основное хранилище (например, malloc или file).17

Критическая уязвимость конфигурации по умолчанию заключается в том, что Transient Storage использует **неограниченный** (unbounded) бэкенд malloc. Это означает, что если сайт подвергается атаке, или бэкенд начинает отдавать массовые ошибки с коротким TTL, или происходит всплеск посещаемости на страницах с отключенным кэшированием (hit-for-miss), Varnish будет аллоцировать память под эти объекты до полного исчерпания физической RAM сервера, игнорируя любые лимиты, установленные для основного хранилища.5

### **3.2. Векторы атаки через короткоживущие объекты**

Для RunRepeat.com существует несколько сценариев, при которых Transient Storage становится вектором отказа в обслуживании:

1. **Массовое создание объектов Hit-For-Miss:** Если Varnish настроен на создание hit-for-miss объектов (запоминание того, что страница не кэшируется) для запросов с уникальными параметрами, и TTL этих записей мал (например, 2 минуты, что является дефолтом для uncacheable_ttl 20), они могут попадать в Transient Storage, если параметр shortlived настроен некорректно или если логика VCL явно не переопределяет хранилище.  
2. **Буферизация потоков (Streaming Buffering):** Когда Varnish получает ответ от бэкенда, который нельзя кэшировать (например, из-за заголовка Set-Cookie), но который нужно передать медленному клиенту, данные буферизируются. Эти байты учитываются в счетчиках Transient Storage (SMA.Transient.c_bytes). При большом количестве одновременных подключений (high concurrency) объем этих буферов может достигать гигабайт.6  
3. **Синтетические ответы:** Ошибки, генерируемые внутри Varnish (vcl_backend_error), также часто попадают в Transient Storage. При сбое бэкенда лавина ошибок 503 может заполнить память.22

### **3.3. Стратегия ограничения (Bounding)**

Решение проблемы Transient Storage является императивным требованием для стабильности. Необходимо явно определить лимит для этого хранилища в параметрах запуска демона varnishd.

Синтаксис для ограничения Transient Storage:

Bash

-s malloc,20G   
-s Transient=malloc,2G

В данной конфигурации основное хранилище получает 20 ГБ, а временное жестко ограничено 2 ГБ. При достижении лимита в 2 ГБ Varnish начнет применять политику вытеснения (LRU) к временным объектам, вместо того чтобы аварийно завершать работу всего процесса.23

Также рекомендуется пересмотреть значение параметра shortlived. Установка его в 0s заставит Varnish помещать все объекты, независимо от их TTL, в основное хранилище, которое имеет строгие лимиты. Это предотвратит "скрытое" потребление памяти, хотя может усилить фрагментацию основного хранилища из-за частого удаления короткоживущих объектов.

## ---

**4. Феномен Cache Bloat в условиях фасетной навигации**

Проект RunRepeat.com обладает архитектурной особенностью, которая делает его экстремально уязвимым к раздуванию кэша (Cache Bloat) — это сложная система фильтрации товаров. Исследование структуры URL показывает наличие множественных параметров фильтрации: size, width, brand, color, drop, terrain и других.2

### **4.1. Комбинаторный взрыв URL-адресов**

Varnish кэширует объекты, используя хэш, вычисляемый (по умолчанию) на основе URL и заголовка Host. Это означает, что порядок параметров в строке запроса имеет значение.

Рассмотрим два запроса:

1. /running-shoes?brand=Nike&size=10&color=Black  
2. /running-shoes?size=10&brand=Nike&color=Black

С точки зрения логики приложения (бэкенда), эти запросы идентичны и возвращают одинаковый HTML. С точки зрения Varnish, это **два разных объекта**.

Количество возможных перестановок параметров растет факториально. Если пользователь может выбрать 5 фильтров из доступных 20, количество уникальных URL-адресов превышает количество атомов во вселенной. Поисковые боты и сканеры, перебирающие фильтры в произвольном порядке, могут генерировать миллионы уникальных запросов в сутки. Это явление называется "Cache Bloat" — заполнение кэша низкополезными дубликатами, что приводит к вытеснению (eviction) действительно востребованного контента (например, главной страницы или популярных категорий).7

Счетчик n_lru_nuked в varnishstat является главным индикатором этой проблемы. Высокие значения этого счетчика свидетельствуют о том, что Varnish вынужден агрессивно удалять объекты, чтобы освободить место для новых, зачастую бесполезных вариаций.27

### **4.2. Маркетинговые метки и "мусорные" параметры**

Помимо функциональных фильтров, e-commerce трафик насыщен маркетинговыми параметрами: utm_source, utm_medium, gclid, fbclid и уникальными идентификаторами сессий. Если эти параметры попадают в хэш кэша, каждый переход пользователя из рекламной рассылки создает уникальную копию страницы в памяти.

Для сайта с посещаемостью RunRepeat один популярный newsletter может мгновенно инвалидировать эффективность кэширования для целевых страниц, заполнив память тысячами копий одной и той же страницы, отличающихся лишь меткой utm_id.

## ---

**5. Стратегии нормализации VCL: От хаоса к порядку**

Решение проблемы Cache Bloat лежит исключительно в плоскости конфигурации VCL (Varnish Configuration Language). Необходима жесткая нормализация входящих запросов в процедуре vcl_recv **до** того, как будет вычислен хэш объекта.

### **5.1. Алгоритмическая сортировка параметров (Query String Sorting)**

Единственным надежным способом борьбы с комбинаторным взрывом перестановок является алфавитная сортировка параметров запроса. Это гарантирует, что запросы ?a=1&b=2 и ?b=2&a=1 будут преобразованы в единую каноническую форму перед поиском в кэше.

Использование модуля vmod_querystring (или функционала std в современных версиях Varnish) позволяет реализовать это одной строкой кода.

**Пример реализации (VCL):**

Code snippet

import std;  
import querystring;

sub vcl_recv {  
    # Сортировка параметров для канонизации URL  
    set req.url = std.querysort(req.url);  
      
    # Альтернативно с использованием vmod_querystring для очистки  
    set req.url = querystring.sort(req.url);  
}

Внедрение сортировки немедленно устраняет дублирование, вызванное произвольным порядком кликов пользователя или поведением ботов.29

### **5.2. Санитизация маркетинговых параметров**

Необходимо внедрить белый (whitelist) или черный (blacklist) список параметров. Для RunRepeat, учитывая сложность фильтров, черный список (удаление известного мусора) может быть более безопасным стартом, но белый список (разрешение только известных фильтров) является идеалом архитектурной чистоты.

**Рекомендуемый VCL для очистки:**

Code snippet

sub vcl_recv {  
    # Удаление стандартных меток Google Analytics и Facebook  
    if (req.url ~ "(?|&)(utm_source|utm_medium|utm_campaign|gclid|fbclid|cx|ie|cof|siteurl)=") {  
        set req.url = regsuball(req.url, "&(utm_source|utm_medium|utm_campaign|gclid|fbclid|cx|ie|cof|siteurl)=([A-z0-9_-.%25]+)", "");  
        set req.url = regsub(req.url, "(?&)", "?");  
        set req.url = regsub(req.url, "?$", "");  
    }  
}

Этот код удаляет параметры, которые нужны только клиентскому JavaScript (Google Analytics), но не влияют на генерацию HTML на бэкенде. Это позволяет отдавать один и тот же кэшированный объект пользователям, пришедшим из разных рекламных каналов.7

### **5.3. Нормализация заголовка User-Agent**

Еще одним вектором раздувания кэша является заголовок Vary: User-Agent. Если бэкенд RunRepeat выдает этот заголовок (что часто случается в PHP-фреймворках для разделения мобильной и десктопной версий), Varnish будет хранить копию страницы для *каждой* версии браузера Chrome, Safari, Firefox и т.д.

Учитывая тысячи вариаций User-Agent, это катастрофически снижает Hit Rate. Решением является нормализация User-Agent в vcl_recv до ограниченного набора бакетов: "mobile", "tablet", "desktop".

Code snippet

sub vcl_recv {  
    if (req.http.User-Agent ~ "(?i)(mobile|android|iphone)") {  
        set req.http.X-UA-Device = "mobile";  
    } else {  
        set req.http.X-UA-Device = "desktop";  
    }  
    # Опционально: перезаписать User-Agent для бэкенда или использовать X-UA-Device в vcl_hash  
}

Если сайт использует адаптивный дизайн (Responsive Design) и HTML не меняется в зависимости от устройства, заголовок Vary: User-Agent следует принудительно удалять в vcl_backend_response.30

## ---

**6. Тонкая настройка инфраструктуры и многопоточности**

Помимо управления памятью и нормализации запросов, стабильность Varnish под нагрузкой зависит от конфигурации пулов потоков (thread pools) и рабочих областей памяти (workspaces).

### **6.1. Динамика Thread Pools**

Клиент может наблюдать большое количество потоков или "дубликатов процессов". Varnish использует модель пула потоков для обработки соединений. Параметры thread_pool_min и thread_pool_max определяют границы масштабирования.

Распространенной ошибкой является установка слишком низкого значения thread_pool_min (по умолчанию 100). В условиях трафика RunRepeat резкие всплески нагрузки (micro-bursts) могут приводить к задержкам, пока Varnish спавнит новые потоки. Это явление, известное как "Thundering Herd" на уровне планировщика потоков.

**Рекомендация:** Увеличить thread_pool_min до 500-1000, чтобы держать "горячий" резерв потоков. При этом thread_pool_max не должен превышать лимиты файловых дескрипторов системы. Важно мониторить счетчик sess_dropped, который показывает количество соединений, сброшенных из-за переполнения очереди ожидания потоков.6

### **6.2. Расчет Workspace Memory**

Каждый поток Varnish имеет выделенную область памяти (workspace_client и workspace_backend) для обработки заголовков и выполнения логики VCL. Для e-commerce сайтов с большим количеством Cookie и длинными URL (из-за фильтров), дефолтный размер (обычно 64k) может быть недостаточен.

Переполнение workspace приводит к ошибкам 500/503. Увеличение workspace_client до 128k или 256k является безопасной мерой оптимизации, незначительно влияющей на общее потребление памяти, но критически важной для стабильности обработки сложных запросов.32

## ---

**7. Мониторинг, Наблюдаемость и Форензика**

Переход от реактивного устранения сбоев к проактивному управлению требует внедрения правильных метрик. Утилита varnishstat предоставляет сырые данные, которые необходимо интерпретировать в контексте бизнес-логики.

### **7.1. Матрица критических метрик**

В таблице ниже представлены ключевые счетчики, мониторинг которых обязателен для диагностики описанных проблем.

| Метрика (Counter) | Описание | Интерпретация для RunRepeat | Порог тревоги |
| :---- | :---- | :---- | :---- |
| **SMA.s0.g_bytes** | Байты в основном хранилище | Должна выходить на плато у лимита -s. Если падает резко — возможен перезапуск. | > 95% от лимита |
| **SMA.Transient.g_bytes** | Байты во временном хранилище | **Главный индикатор утечки.** Неконтролируемый рост указывает на проблему unbounded storage. | > 1-2 ГБ |
| **n_lru_nuked** | Принудительно удаленные объекты | Индикатор Cache Bloat. Высокая скорость роста означает, что полезный кэш вымывается мусорными вариациями. | Рост > 100/сек |
| **n_object** | Количество объектов | Сравнить с каталогом товаров. Если n_object >> кол-ва товаров * вариации, значит нормализация не работает. | Аномальный рост |
| **cache_hit** / **cache_miss** | Попадания/Промахи | Hit Rate = hits / (hits + misses). Низкий Hit Rate при высоком n_object подтверждает проблему дубликатов. | < 60-70% |
| **sess_dropped** | Сброшенные сессии | Нехватка потоков или перегрузка CPU. | > 0 |

21

### **7.2. Интерпретация сценариев сбоя**

* **Сценарий А: OOM Killer убивает Varnish.**  
  * Проверка: Если SMA.s0.g_bytes стабилен, а системный RAM исчерпан, виноват либо glibc (фрагментация), либо SMA.Transient (скрытый рост).  
  * Действие: Сверить графики RSS процесса и SMA.Transient.g_bytes.  
* **Сценарий Б: Низкая производительность, высокий Backend Load.**  
  * Проверка: Высокий n_lru_nuked. Varnish "молотит" память, постоянно записывая и удаляя объекты.  
  * Действие: Внедрить нормализацию Query String.

## ---

**8. Перспективы Enterprise-решений: MSE и Memory Governor**

В контексте долгосрочной стратегии развития RunRepeat.com стоит рассмотреть возможности коммерческой версии Varnish Enterprise, которая предлагает архитектурные решения описанных проблем "из коробки".

### **8.1. Massive Storage Engine (MSE)**

В отличие от malloc (память) и file (файл с mmap), движок MSE разработан для работы с большими наборами данных (dataset), превышающими объем RAM. Он использует собственную систему аллокации, которая полностью устраняет проблему фрагментации, присущую glibc. Кроме того, MSE поддерживает персистентность (сохранение кэша при перезагрузке), что критично для минимизации нагрузки на бэкенд при обслуживании ("Cache Warming").8

### **8.2. Memory Governor**

Функция Memory Governor в Varnish Enterprise динамически управляет размером кэша. Вместо жесткого лимита на *объекты*, администратор задает целевой объем памяти для *всего процесса*. Memory Governor автоматически уменьшает размер хранилища объектов, если растут накладные расходы или потребление Transient Storage, гарантируя, что процесс никогда не выйдет за пределы выделенного бюджета памяти и не будет убит OOM Killer.16

## ---

**9. Стратегический план ремедиации (Remediation Roadmap)**

На основании проведенного аудита предлагается следующий пошаговый план действий для стабилизации инфраструктуры RunRepeat.com.

### **Фаза 1: Немедленная стабилизация (Infrastructure & Config)**

1. **Замена Аллокатора:**  
   * Проверить текущий линковщик: ldd /usr/sbin/varnishd.  
   * Внедрить jemalloc. Если используется systemd, добавить в override.conf:  
     Environment="LD_PRELOAD=/usr/lib64/libjemalloc.so.2" (путь может отличаться).  
   * Это решит проблему фрагментации и снизит RSS на 15-30%.9  
2. **Ограничение Transient Storage:**  
   * Изменить параметры запуска varnishd.  
   * Было: -s malloc,24G (пример).  
   * Стало: -s malloc,20G -s Transient=malloc,2G.  
   * Это предотвратит OOM при атаках на некэшируемый контент.  
3. **Корректировка параметров потоков:**  
   * Установить thread_pool_min=500.

### **Фаза 2: Логическая оптимизация (VCL)**

1. **Нормализация запросов (Query Sort):**  
   * Внедрить модуль std или vmod_querystring.  
   * Добавить в vcl_recv: set req.url = std.querysort(req.url);.  
   * Реализовать удаление utm_* меток.  
2. **Управление Vary:**  
   * Проанализировать заголовки бэкенда.  
   * Удалить или нормализовать Vary: User-Agent.  
   * Заменить на Vary: X-UA-Device с предварительным детектированием устройства в VCL.

### **Фаза 3: Мониторинг и валидация**

1. **Настройка Dashboard:**  
   * Вывести графики SMA.Transient.g_bytes и n_lru_nuked в систему мониторинга (Grafana/Datadog).  
   * Настроить алертинг на превышение 80% заполнения Transient Storage.  
2. **Стресс-тестирование:**  
   * Провести нагрузочное тестирование с использованием рандомизированных URL (имитация ботов) для проверки эффективности нормализации и стабильности памяти при новом аллокаторе.

Реализация данного плана трансформирует Varnish Cache из источника нестабильности в надежный и предсказуемый слой акселерации, способный эффективно справляться с высокой кардинальностью данных проекта RunRepeat.

#### **Works cited**

1. RunRepeat: 1000+ shoes reviewed and cut in half, accessed December 11, 2025, [https://runrepeat.com/](https://runrepeat.com/)  
2. 100+ Running Shoe Reviews - RunRepeat, accessed December 11, 2025, [https://runrepeat.com/catalog/running-shoes](https://runrepeat.com/catalog/running-shoes)  
3. libmalloc, jemalloc, tcmalloc, mimalloc - Exploring Different Memory Allocators, accessed December 11, 2025, [https://dev.to/frosnerd/libmalloc-jemalloc-tcmalloc-mimalloc-exploring-different-memory-allocators-4lp3](https://dev.to/frosnerd/libmalloc-jemalloc-tcmalloc-mimalloc-exploring-different-memory-allocators-4lp3)  
4. Solving unbounded Java Process memory growth using JEMalloc - Medium, accessed December 11, 2025, [https://medium.com/@sohelcts/solving-unbounded-java-process-memory-growth-using-jemalloc-a43de47e5d0b](https://medium.com/@sohelcts/solving-unbounded-java-process-memory-growth-using-jemalloc-a43de47e5d0b)  
5. Storage backends - Varnish Cache - Read the Docs, accessed December 11, 2025, [https://varnish-cache.readthedocs.io/users-guide/storage-backends.html](https://varnish-cache.readthedocs.io/users-guide/storage-backends.html)  
6. Varnish memory usage keeps increasing - Stack Overflow, accessed December 11, 2025, [https://stackoverflow.com/questions/76209998/varnish-memory-usage-keeps-increasing](https://stackoverflow.com/questions/76209998/varnish-memory-usage-keeps-increasing)  
7. Example VCL template - Varnish Developer Portal, accessed December 11, 2025, [https://www.varnish-software.com/developers/tutorials/example-vcl-template/](https://www.varnish-software.com/developers/tutorials/example-vcl-template/)  
8. Understanding Varnish Cache Memory Usage - Resources, accessed December 11, 2025, [https://info.varnish-software.com/blog/understanding-varnish-cache-memory-usage](https://info.varnish-software.com/blog/understanding-varnish-cache-memory-usage)  
9. jemalloc vs glibc malloc: Memory Allocation Performance Comparison | by Binita Bharati, accessed December 11, 2025, [https://medium.com/@binitabharati/jemalloc-vs-glibc-malloc-memory-allocation-performance-comparison-fbaeda1740de](https://medium.com/@binitabharati/jemalloc-vs-glibc-malloc-memory-allocation-performance-comparison-fbaeda1740de)  
10. Picking a global allocator : r/rust - Reddit, accessed December 11, 2025, [https://www.reddit.com/r/rust/comments/1ifjzvv/picking_a_global_allocator/](https://www.reddit.com/r/rust/comments/1ifjzvv/picking_a_global_allocator/)  
11. Background · jemalloc/jemalloc Wiki - GitHub, accessed December 11, 2025, [https://github.com/jemalloc/jemalloc/wiki/Background](https://github.com/jemalloc/jemalloc/wiki/Background)  
12. How to trace the fragmentation? · Issue #2850 · jemalloc/jemalloc - GitHub, accessed December 11, 2025, [https://github.com/jemalloc/jemalloc/issues/2850](https://github.com/jemalloc/jemalloc/issues/2850)  
13. Jemalloc Memory Analysis - Apache Doris, accessed December 11, 2025, [https://doris.apache.org/docs/3.x/admin-manual/trouble-shooting/memory-management/memory-analysis/jemalloc-memory-analysis/](https://doris.apache.org/docs/3.x/admin-manual/trouble-shooting/memory-management/memory-analysis/jemalloc-memory-analysis/)  
14. 1656034 – Varnish is compiled without jemalloc. jemalloc is missing. - Red Hat Bugzilla, accessed December 11, 2025, [https://bugzilla.redhat.com/show_bug.cgi?id=1656034](https://bugzilla.redhat.com/show_bug.cgi?id=1656034)  
15. Varnish duplicate process 170 once - Unix & Linux Stack Exchange, accessed December 11, 2025, [https://unix.stackexchange.com/questions/632427/varnish-duplicate-process-170-once](https://unix.stackexchange.com/questions/632427/varnish-duplicate-process-170-once)  
16. Two-Minute Tech Tuesdays - Memory Governor - Resources - Varnish Software, accessed December 11, 2025, [https://info.varnish-software.com/blog/two-minute-tech-tuesdays-memory-governor](https://info.varnish-software.com/blog/two-minute-tech-tuesdays-memory-governor)  
17. Parameters — Varnish version 4.0.5 documentation, accessed December 11, 2025, [https://varnish-cache.org/docs/4.0/users-guide/params.html](https://varnish-cache.org/docs/4.0/users-guide/params.html)  
18. Storage backends — Varnish version trunk documentation, accessed December 11, 2025, [https://varnish-cache.org/docs/trunk/users-guide/storage-backends.html](https://varnish-cache.org/docs/trunk/users-guide/storage-backends.html)  
19. Storage backends - malloc - Varnish Cache, accessed December 11, 2025, [https://varnish-cache.org/docs/4.1/users-guide/storage-backends.html](https://varnish-cache.org/docs/4.1/users-guide/storage-backends.html)  
20. varnishd — Varnish version trunk documentation, accessed December 11, 2025, [https://varnish-cache.org/docs/trunk/reference/varnishd.html](https://varnish-cache.org/docs/trunk/reference/varnishd.html)  
21. varnish-counters — Varnish version trunk documentation, accessed December 11, 2025, [https://varnish-cache.org/docs/trunk/reference/varnish-counters.html](https://varnish-cache.org/docs/trunk/reference/varnish-counters.html)  
22. VSV00002 Data leak - '-sfile' Stevedore transient objects — Varnish HTTP Cache, accessed December 11, 2025, [https://varnish-cache.org/security/VSV00002.html](https://varnish-cache.org/security/VSV00002.html)  
23. Varnish crashes on bigger files - cache - Server Fault, accessed December 11, 2025, [https://serverfault.com/questions/1031656/varnish-crashes-on-bigger-files](https://serverfault.com/questions/1031656/varnish-crashes-on-bigger-files)  
24. Limiting memory for varnish process - caching - Stack Overflow, accessed December 11, 2025, [https://stackoverflow.com/questions/58909821/limiting-memory-for-varnish-process](https://stackoverflow.com/questions/58909821/limiting-memory-for-varnish-process)  
25. 90+ Knit Running Shoe Reviews - RunRepeat, accessed December 11, 2025, [https://runrepeat.com/catalog/knit-running-shoes](https://runrepeat.com/catalog/knit-running-shoes)  
26. Performance Boosting with Varnish Cache - maxcluster, accessed December 11, 2025, [https://maxcluster.de/en/knowledge/blog/article/performance-page-speed-boosting-varnish-cache](https://maxcluster.de/en/knowledge/blog/article/performance-page-speed-boosting-varnish-cache)  
27. Varnish monitoring - Varnish Developer Portal, accessed December 11, 2025, [https://www.varnish-software.com/developers/tutorials/varnish-monitoring/](https://www.varnish-software.com/developers/tutorials/varnish-monitoring/)  
28. Top Varnish performance metrics | Datadog, accessed December 11, 2025, [https://www.datadoghq.com/blog/top-varnish-performance-metrics/](https://www.datadoghq.com/blog/top-varnish-performance-metrics/)  
29. querystring.sort | Fastly Documentation, accessed December 11, 2025, [https://www.fastly.com/documentation/reference/vcl/functions/query-string/querystring-sort/](https://www.fastly.com/documentation/reference/vcl/functions/query-string/querystring-sort/)  
30. Vary — Varnish version 3.0.7 documentation, accessed December 11, 2025, [https://varnish-cache.org/docs/3.0/tutorial/vary.html](https://varnish-cache.org/docs/3.0/tutorial/vary.html)  
31. 5 Don'ts When Caching with Varnish - Resources, accessed December 11, 2025, [https://info.varnish-software.com/blog/5-varnish-donts](https://info.varnish-software.com/blog/5-varnish-donts)  
32. Varnish Using Significantly More Memory than Cache? - Stack Overflow, accessed December 11, 2025, [https://stackoverflow.com/questions/78379910/varnish-using-significantly-more-memory-than-cache](https://stackoverflow.com/questions/78379910/varnish-using-significantly-more-memory-than-cache)  
33. Varnish Cache extension — Dynatrace Docs, accessed December 11, 2025, [https://docs.dynatrace.com/docs/observe/infrastructure-observability/databases/extensions/varnish-cache-1](https://docs.dynatrace.com/docs/observe/infrastructure-observability/databases/extensions/varnish-cache-1)