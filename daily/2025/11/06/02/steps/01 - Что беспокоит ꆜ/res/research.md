

# **Аналитический Отчет: Диагностика и Устранение Системных Сбоев в Интеграции P⁎ и Google Merchant Center**

## **I. Диагностический Аудит: Идентификация и Систематизация Проблем ꆜ в Экосикосистеме P⁎**

Настоящий аудит выявляет три основных, взаимосвязанных "симптома", с которыми сталкивается ꆜ. Эти симптомы являются не отдельными сбоями, а проявлениями глубокого системного конфликта между архитектурой платформы P⁎ (Shopify) и строгими, асинхронными механизмами валидации Google.

### **A. Симптом 1: Кризис Синхронизации Данных в Google Merchant Center (GMC)**

Основная проблема, вызывающая наибольшее беспокойство, — это повторяющиеся и массовые ошибки "Mismatched value (page crawl) \[price\]" (Несоответствие значения (сканирование страницы) \[цена\]) в Google Merchant Center.1 Эта ошибка возникает, когда цена, указанная в фиде данных о товарах (product data feed), не совпадает с ценой, которую Googlebot обнаруживает на целевой странице.1 Критически важно, что Googlebot сверяет цену фида не только с видимым текстом на странице, но и с информацией, содержащейся в *структурированных данных* (разметке schema.org) этой страницы.3

Последствия этого несоответствия носят каскадный характер:

1. **Массовое отклонение товаров**, что приводит к остановке рекламных кампаний Shopping Ads.  
2. **Принудительное срабатывание "Automatic item updates"** (Автоматическое обновление информации о товарах).5

Как ни парадоксально, функция автоматического обновления, призванная помогать, усугубляет проблему. Анализ отчетов пользователей 7 показывает, что автоматические обновления, основанные на *медленном* и часто *устаревшем* сканировании сайта, начинают *неправильно* перезаписывать *корректные* и *мгновенные* обновления цен, которые ꆜ отправляет через Content API или фид данных.

Проблема обостряется при использовании цен со скидкой. Система требует идеальной и одновременной синхронизации атрибутов sale\_price \[цена\_со\_скидкой\] и sale\_price\_effective\_date \[срок\_действия\_цены\_со\_скидкой\]3 между тремя источниками: фидом GMC, видимым HTML-кодом страницы и разметкой schema.org.

Это создает для ꆜ "Ловушку-22", вызванную асинхронностью систем Google.

* **Сценарий A (AIU выключен):** ꆜ отключает автоматические обновления (AIU). Теперь, из\-за естественной задержки (до 24 часов 7) между обновлением фида и сканированием страницы Google, он получает массовые *отклонения* товаров за "Mismatched price".7  
* **Сценарий B (AIU включен):** ꆜ оставляет AIU включенным. Когда он обновляет цену через быстрый Content API (например, с 10$ до 15$), система AIU, опираясь на *старые* данные *медленного* сканирования (которое все еще видит 10$), "исправляет" *правильную* цену (15$) обратно на *неправильную* (10$).7

В обоих случаях ꆜ несет финансовые и операционные потери, становясь жертвой внутренней рассинхронизации между быстрыми и медленными системами валидации Google.

### **B. Симптом 2: Конфликт Источников Структурированных Данных на Платформе P⁎**

Этот симптом является *коренной причиной* Симптома 1\. При анализе страниц P⁎ (Shopify) с помощью инструментов валидации, таких как Rich Results Test 10 или Schema Markup Validator 12, обнаруживается наличие *нескольких* (дублирующихся) сущностей Product на одной и той же странице.13

Этот конфликт в P⁎ (Shopify) возникает из\-за его "многослойной" архитектуры:

1. **Разметка Темы (Theme):** Большинство современных тем Shopify (например, Dawn) по умолчанию внедряют собственный блок разметки Product. Это может быть современный JSON-LD 16 или, в старых темах, устаревший Microdata (с атрибутами itemscope, itemprop).17  
2. **Разметка Приложений (Apps):** ꆜ, по всей видимости, установил одно или несколько сторонних приложений (например, SEO-приложение 13 или приложение для отзывов 19) для "улучшения" SEO или добавления функционала. Эти приложения, не имея возможности *редактировать* разметку темы, *также* внедряют *свою собственную* разметку JSON-LD.20

В результате на странице возникает "загрязнение данных" (Data Pollution).13 В исходном коде одновременно существуют два или более блока \<script type="application/ld+json"\>, описывающих Product. Зачастую они содержат *разную* информацию: например, разметка темы содержит только базовую цену, а разметка приложения — актуальную цену со скидкой, SKU и отзывы.

Хотя некоторые эксперты могут ошибочно полагать, что "Google выберет лучший" 19, это допущение опасно и неверно в контексте Google Merchant Center. Бот *Google Search* (для Rich Results) может быть достаточно "умен", чтобы объединить эти данные. Однако бот *GMC Crawler* (для валидации фида) работает по гораздо более строгим и примитивным правилам.3 Существуют прямые свидетельства 23, что "Google Merchant Center читает *только первую* структурированную дату".

Если *первой* в HTML-коде страницы загружается неполная или "сломанная" разметка Product от *темы*, бот GMC считывает *ее* (например, старую цену). Затем он сравнивает эту *неправильную* цену из разметки с *правильной* и актуальной ценой из фида.1 Результат — неизбежная ошибка "Mismatched value (page crawl) \[price\]".2

### **C. Симптом 3: Семантическая Неоднозначность и Ошибки в Словаре Schema.org**

Даже если бы на странице присутствовала *только одна* разметка, она, с высокой вероятностью, семантически некорректна, что усугубляет Симптомы 1 и 2\.

Ошибка 1: Некорректное использование AggregateOffer  
ꆜ (или приложение, которое он использует) использует тип AggregateOffer для отображения диапазона цен (lowPrice, highPrice) для вариантов товара (например, разные размеры).24 Это грубая семантическая ошибка. Документация Schema.org 25 и эксперты Google 24 четко указывают:

* AggregateOffer предназначен для *страниц-агрегаторов*, где *несколько разных продавцов* (merchants) предлагают один и тот же товар.  
* Он *не* предназначен для *одного продавца*, предлагающего *варианты* товара.

Использование AggregateOffer одним продавцом "может ограничить" функциональность 24, поскольку бот GMC не может найти *конкретное* предложение для *конкретного* SKU из фида.26

Ошибка 2: Некорректная реализация цены со скидкой (Sale Price)  
ꆜ, его тема или приложение не используют точную, недавно обновленную структуру, которую Google требует для отображения цен со скидкой.27

* **Неправильный (старый) метод:** Указание price (старая цена) и salePrice (новая цена).  
* **Правильный (рекомендованный Google) метод:** Google предоставил точные шаблоны.28 Активная (со скидкой) цена должна быть указана в свойстве price. Оригинальная (перечеркнутая) цена должна быть указана во вложенном объекте priceSpecification со свойством priceType: "https://schema.org/ListPrice" (или StrikethroughPrice).27

Эти семантические ошибки делают автоматическую валидацию цен ботом GMC *невозможной*. Когда бот приходит на страницу для проверки цены "10.00 USD" для SKU "L-123", он видит либо AggregateOffer с диапазоном "8.00-12.00" (не может найти точное совпадение 26), либо неправильно структурированное предложение о скидке, и не может понять, какая цена является активной. В любом случае, это приводит к фиксации несоответствия.

## **II. Анализ Обоснованности и Первопричин: Деконструкция Технического Стека P⁎ и Логики Google**

Анализ подтверждает, что все выявленные проблемы (Симптомы 1, 2 и 3\) *полностью обоснованы*. Они не являются результатом простой оплошности, а представляют собой прямое следствие системных конфликтов на стыке трех доменов: асинхронной логики GMC, архитектурных ограничений P⁎ (Shopify) и неверной интерпретации инструментов валидации.

### **A. Обоснованность Расхождений в GMC: Проблема Асинхронности Данных**

Жалобы ꆜ на "нелогичное" поведение GMC и "все портящие" автоматические обновления 7 *абсолютно обоснованы*. Причина кроется во "временном лаге" (Time Lag) между двумя системами обновления Google.

1. **Система 1 (Быстрая):** Content API и фиды данных. ꆜ обновляет цену, и GMC видит это "в течение нескольких минут".7  
2. **Система 2 (Медленная):** Googlebot (Page Crawl), который сканирует целевые страницы для верификации. Этот процесс занимает "несколько часов или дней" 3 или "до 24 часов".7

Между моментом обновления фида (Система 1\) и моментом сканирования страницы (Система 2\) *гарантированно* существует "окно уязвимости".9 В этот период данные в фиде и данные на (еще не просканированной) странице *объективно* не совпадают. Бот, сканирующий в это окно, *обязан* зафиксировать ошибку "Mismatched price".1

Как уже отмечалось, парадокс "Automatic item updates" (AIU) 5 заключается в том, что эта функция также опирается на *медленную* Систему 2\. Если фид обновлен (цена 15$), а *последнее сканирование* (час назад) видело цену 10$, AIU "исправит" *правильную* цену фида (15$) на *устаревшую* цену сканирования (10$).7

Вывод: Проблема ꆜ *обоснована* и *встроена* в архитектуру GMC. Его жалоба на то, что AIU саботирует его быстрые обновления через API, *валидна*.7

### **B. Обоснованность Конфликтов Разметки: Аудит Архитектуры P⁎ (Shopify)**

Проблема дублирующейся разметки *полностью обоснована* и является прямым следствием архитектуры P⁎ (Shopify).

1. Shopify использует систему шаблонов Liquid.29  
2. Основной шаблон товара (product.liquid 31 или, в современных темах, sections/main-product.liquid 16) по умолчанию включает *свою* разметку. Часто это делается через один Liquid-объект {{ product | structured\_data }} 18 или через статические теги Microdata (itemprop).18  
3. Сторонние приложения (для SEO, отзывов и т.д.) также внедряют свой код (часто JSON-LD).21  
4. Ключевая проблема: Приложения *не имеют* стандартного и безопасного способа *удалить* или *изменить* разметку, встроенную в *тему*. Они могут только *добавить* свою разметку *поверх* существующей.13

Вывод: Проблема ꆜ *обоснована*. Он столкнулся с *архитектурным недостатком* Shopify. В попытке "исправить" или "улучшить" неполную разметку своей темы 33, он установил приложение. Это приложение, не имея возможности *заменить* код, *продублировало* его. Это "загрязнение схемы" 13 является *прямым следствием* попытки ꆜ решить одну проблему, что непреднамеренно породило другую, более серьезную.

### **C. Обоснованность Семантических Ошибок: "Ложная Уверенность" от Инструментов Валидации**

Путаница ꆜ в отношении того, "что не так с моей разметкой", *полностью обоснована*. Он стал жертвой разной логики работы трех разных ботов Google, а его основной инструмент тестирования, вероятно, *скрывал* от него истинную проблему.

1. ꆜ (или его SEO-приложение 13) проверяет страницу в **Google Rich Results Test (RRT)**.10  
2. RRT видит две разметки: Product\_Theme (сломанную) и Product\_App (хорошую).  
3. RRT, чья цель — проверить *допустимость* для Rich Results 36, "по-умному" объединяет их или выбирает лучшую 19 и рапортует: "N valid item(s) detected" (Обнаружено N допустимых элементов).11  
4. ꆜ получает *ложное чувство безопасности*.  
5. *Однако*, **GMC Crawler** (бот Google Merchant Center) 3 — это *не* Rich Results Test. Он "глупее" и строже. Он видит Product\_Theme *первой* в коде 23, считывает ее *неправильную* цену, сравнивает с фидом и *отклоняет* товар.1

Проблема усугубляется тем, что ꆜ, вероятно, не использует *правильный* инструмент для этой задачи. **Schema Markup Validator (SMV)** 10 (бывший SDTT) — это единственный инструмент, чья цель — *общая валидация синтаксиса*, и он *показал* бы ꆜ наличие *двух* конфликтующих сущностей Product.

Этот конфликт инструментов является центральным в проблеме ꆜ:

**Таблица 1: Сравнительный Анализ Инструментов Валидации и их Влияния на ꆜ**

| Инструмент | Ссылка (Источник) | Основная Цель | Логика Обработки Дубликатов | Как это влияет на ꆜ |
| :---- | :---- | :---- | :---- | :---- |
| **Google Rich Results Test (RRT)** | 10 | Проверка *допустимости* для Google Rich Results (расширенных сниппетов). | *Скрывающая:* "Выбирает лучший" 19 или объединяет данные. | *Дает ложную уверенность.* Скрывает проблему дублирования. |
| **Schema Markup Validator (SMV)** | 10 | *Общая* валидация синтаксиса Schema.org. | *Выявляющая:* Показывает *все* обнаруженные сущности. | *Выявляет дубликаты* (но ꆜ, вероятно, им не пользуется). |
| **GMC Page Crawler (Бот GMC)** | 3 | *Строгая валидация* цены/наличия для фида GMC. | *Наказывающая:* Читает *первую* 23 или *не может* разрешить конфликт. | *Отклоняет товары*, вызывая Симптом 1\. |

## **III. Стратегический План Реконфигурации: Создание Единого Источника Истины (SSOT) для Данных P⁎**

Решение проблем ꆜ требует не "заплаток", а *полной реконфигурации* архитектуры данных на P⁎ (Shopify) для создания Единого Источника Истины (Single Source of Truth, SSOT). Этот план состоит из трех фаз.

### **A. Фаза 1: Очистка (Sanitization) Разметки на Платформе P⁎ (Shopify)**

**Цель:** Достичь "чистого листа" — полного отсутствия *конфликтующей* разметки Product, генерируемой темой, прежде чем внедрять новую "Мастер-Схему".

1. **Действие 1: Резервное копирование.** Создать полную резервную копию текущей темы Shopify.18  
2. **Действие 2: Идентификация и Удаление.** Разработчик должен проанализировать файлы темы (.liquid) и удалить *все* существующие реализации разметки Product.

**Таблица 2: План "Очистки" (Sanitization) Темы P⁎ (Shopify)**

| Тип Разметки | Ключевые слова для поиска | Вероятные Файлы | Безопасный Метод Устранения | Источник |
| :---- | :---- | :---- | :---- | :---- |
| **JSON-LD (Темы)** | application/ld+json, \`{{ product | structured\_data }}\` | sections/main-product.liquid, product.liquid, theme.liquid | Обернуть весь блок \<script\> в теги {% comment %}... {% endcomment %}. Это безопаснее, чем удаление. |
| **Microdata (Темы)** | itemscope, itemtype, itemprop | product.liquid, snippets/\*.liquid (например, product-price.liquid) | *Аккуратно* удалить *только* сами атрибуты (например, itemprop="price"), *не* HTML-теги, в которые они встроены. | 18 |
| **JSON-LD (Приложения)** | (Динамическое внедрение) | N/A (Управляется приложением) | *Отключить* функцию генерации разметки в настройках SEO-приложения *или* удалить само приложение, если оно не позволяет этого. | 13 |

3. **Действие 3: Валидация Очистки.** После выполнения Действия 2 необходимо проверить URL продукта в **Schema Markup Validator (SMV)**.12 Цель: SMV *не должен* обнаруживать *ни одной* сущности Product.

### **B. Фаза 2: Проектирование и Внедрение "Мастер-Схемы" (Master Schema) JSON-LD**

**Цель:** Внедрить *единый, полный и семантически точный* блок JSON-LD, который будет служить SSOT для *всех* ботов Google (RRT, SMV и GMC).

1. **Действие 1: Выбор Инструмента.** Рекомендуется использовать *одно* решение: либо кастомный скрипт JSON-LD, внедренный вручную в theme.liquid или product.liquid, либо высококачественное SEO-приложение, которое *гарантированно* отключает разметку темы и управляет SSOT. Формат JSON-LD является рекомендуемым Google.21  
2. **Действие 2: Проектирование "Мастер-Схемы".** Эта схема должна быть полной и решать все семантические проблемы (Симптом 3).  
   * **Консолидация:** Используйте @graph 41 для объединения *всех* сущностей (например, Product, BreadcrumbList, Organization) в *один* блок \<script\>. Это чистая практика, превосходящая несколько отдельных скриптов.42  
   * **Решение для Offer:**  
     * *Никогда* не использовать AggregateOffer.24  
     * Использовать один объект Offer.44  
     * Для вариантов товара 26: Offer должен *динамически* обновляться (с помощью JavaScript на стороне клиента) при выборе варианта, изменяя поля price, availability и, что *критически важно*, sku. Поле sku в JSON-LD *должно* точно соответствовать id в фиде GMC.26  
   * **Решение для Отзывов:** Внедрить данные об отзывах *внутрь* (nesting) объекта Product.46 Использовать aggregateRating для сводной информации 47 и массив review для отдельных отзывов 50, которые *физически* видны на странице.51  
   * **Решение для Цены со Скидкой:** Использовать *только* одобренный Google шаблон.27

**Таблица 3: Шаблоны JSON-LD для "Мастер-Схемы" (SSOT)**

| Сценарий | Рекомендуемый Шаблон JSON-LD |
| :---- | :---- |
| **Товар со Скидкой (Решение для GMC)** | json "offers": { "@type": "Offer", "url": "https://elewell.shop/products/liposomal-glutathione", "priceCurrency": "USD", "availability": "https://schema.org/InStock", "sku": "VARIANT-SKU-123", "price": "49.99", "priceSpecification": { "@type": "UnitPriceSpecification", "priceType": "https://schema.org/ListPrice", "price": "79.99", "priceCurrency": "USD" } } **Пояснение:** price: "49.99" — это *текущая цена со скидкой*.28 priceSpecification.price: "79.99" — это *оригинальная (перечеркнутая) цена*.27 sku *должен* соответствовать id из фида.26 |
| **Интеграция Отзывов и Консолидация @graph** | json \<script type="application/ld+json"\> { "@context": "https://schema.org", "@graph": }, { "@type": "BreadcrumbList",... } \] } \</script\> **Пояснение:** @graph 41 позволяет объединить все в один скрипт. aggregateRating 49 и review 50 вложены в Product. |

Внедрение этой "Мастер-Схемы" (SSOT) является "антидотом" к Симптомам 2 и 3\. Она устраняет *неоднозначность* данных. Теперь, когда "временной лаг" (Симптом 1\) проходит и бот GMC *наконец* сканирует страницу 3, он находит *идеальное, 1-в-1 совпадение* с данными фида. Он сравнивает price: "49.99" и sku: "VARIANT-SKU-123" в *схеме* с sale\_price: "49.99" и id: "VARIANT-SKU-123" в *фиде*. Ошибки "Mismatched value" исчезают.

### **C. Фаза 3: Гармонизация Фидов GMC и Данных Сканирования**

**Цель:** Синхронизировать *процессы* обновления данных, используя SSOT (из Фазы 2\) в качестве общего знаменателя.

1. **Действие 1: Приоритет Content API.** Использовать Content API для *мгновенных* обновлений price, sale\_price и availability.2 Это "быстрая" система.7  
2. **Действие 2: Корректное Использование Фида.** Убедиться, что id в фиде *точно* соответствует sku в "Мастер-Схеме".26 Убедиться, что price (базовая цена) и sale\_price (цена со скидкой) в фиде 8 *семантически* соответствуют priceSpecification.price и price в "Мастер-Схеме".28  
3. **Действие 3: Повторное Включение AIU (Automatic Item Updates).** После внедрения SSOT (Фаза 2\) и очистки (Фаза 1), *безопасно* снова включить "Automatic item updates".5 Теперь AIU (основанный на *сканировании*) становится *страховкой*, а не *проблемой*. Если фид *не* обновится, AIU *правильно* обновит цену, прочитав *идеально точную* "Мастер-Схему" (SSOT). Проблема из 7 (когда AIU перезаписывал правильные данные) *решена*, потому что теперь данные сканирования и данные фида *всегда идентичны по смыслу*.

## **IV. Заключительные Рекомендации и Процедуры Непрерывного Мониторинга**

Внедрение SSOT — это не разовое действие, а начало нового процесса. Архитектура P⁎ (Shopify) (обновления тем, добавление новых приложений) по своей природе склонна к рецидиву "загрязнения схемы".13

### **A. Регламент Мониторинга**

1. **Google Search Console (GSC):** Регулярно проверять отчеты "Enhancements" ("Улучшения").52 Любые новые ошибки или предупреждения в разделах "Merchant listings" (Товарные предложения) или "Product snippets" (Расширенные результаты о товарах) 52 являются индикатором того, что "Мастер-Схема" "сломалась" или тема снова начала внедрять дублирующую разметку.  
2. **Google Merchant Center (GMC):** Ежедневно отслеживать вкладку "Diagnostics" ("Диагностика").2 Появление новых ошибок "Mismatched value" 3 — это сигнал о рассинхронизации SSOT и фида.

### **B. Регламент Валидации Изменений (Обязательно)**

*Перед* публикацией *любых* изменений в "Мастер-Схеме" или *обновлением* темы Shopify:

1. **Тест Кода:** Скопировать *фрагмент кода* (snippet) "Мастер-Схемы" и протестировать его в **Schema Markup Validator (SMV)** 10 для проверки синтаксиса.  
2. **Тест Кода:** Скопировать *фрагмент кода* в **Rich Results Test (RRT)** 10 для проверки на допустимость.

*Сразу после* публикации изменений на *рабочем* сайте:

1. **Тест URL:** Протестировать *живой URL* в **Rich Results Test (RRT)** 35 для подтверждения, что Google видит разметку и считает ее допустимой.  
2. **Критический Тест URL:** Протестировать *живой URL* в **Schema Markup Validator (SMV)**.12 Цель — убедиться, что в результатах по-прежнему отображается *только одна* (1) сущность Product. Если их снова две, значит, обновление темы или новое приложение "сломало" SSOT, и Фазу 1 (Очистка) необходимо повторить.

#### **Works cited**

1. How to Fix Price Mismatch Error in Google Merchant Center? \- AdNabu Blog, accessed November 6, 2025, [https://blog.adnabu.com/google-merchant-center/google-merchant-center-price-mismatch/](https://blog.adnabu.com/google-merchant-center/google-merchant-center-price-mismatch/)  
2. How to Fix Mismatched Value (page crawl) \[price\] in the Merchant Center? \- DataFeedWatch, accessed November 6, 2025, [https://www.datafeedwatch.com/blog/mismatched-value-page-crawl-price](https://www.datafeedwatch.com/blog/mismatched-value-page-crawl-price)  
3. How to fix: Mismatched product price \- Google Merchant Center Help, accessed November 6, 2025, [https://support.google.com/merchants/answer/12159029?hl=en](https://support.google.com/merchants/answer/12159029?hl=en)  
4. Most Common Price Errors in Google Merchant Center \- \[How to Fix\] \- WebAppick, accessed November 6, 2025, [https://webappick.com/most-common-price-errors-in-google-merchant-center/](https://webappick.com/most-common-price-errors-in-google-merchant-center/)  
5. How to fix: Automatic updates: Mismatched price \- Google Merchant Center Help, accessed November 6, 2025, [https://support.google.com/merchants/answer/14916353?hl=en](https://support.google.com/merchants/answer/14916353?hl=en)  
6. How to fix: Mismatched value (page crawl): loyalty programme price \[loyalty\_program\_price\] \- Google Merchant Center Help, accessed November 6, 2025, [https://support.google.com/merchants/answer/15101263?hl=en-IE](https://support.google.com/merchants/answer/15101263?hl=en-IE)  
7. Google Merchant Center Auto Update overrides vs. mismatched price/availability disapprovals : r/PPC \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/PPC/comments/19f7oz6/google\_merchant\_center\_auto\_update\_overrides\_vs/](https://www.reddit.com/r/PPC/comments/19f7oz6/google_merchant_center_auto_update_overrides_vs/)  
8. Sale price \[sale\_price\] \- Google Merchant Center Help, accessed November 6, 2025, [https://support.google.com/merchants/answer/6324471?hl=en](https://support.google.com/merchants/answer/6324471?hl=en)  
9. Mismatched value (page crawl): \[price\] | Price Mismatch Error Fix | Google Merchant Center, accessed November 6, 2025, [https://www.youtube.com/watch?v=B9j52nPyao8](https://www.youtube.com/watch?v=B9j52nPyao8)  
10. Schema Markup Testing Tool | Google Search Central, accessed November 6, 2025, [https://developers.google.com/search/docs/appearance/structured-data](https://developers.google.com/search/docs/appearance/structured-data)  
11. Rich Results Test \- Search Console Help, accessed November 6, 2025, [https://support.google.com/webmasters/answer/7445569?hl=en](https://support.google.com/webmasters/answer/7445569?hl=en)  
12. Schema.org Markup Validator, accessed November 6, 2025, [https://schema.org/docs/validator.html](https://schema.org/docs/validator.html)  
13. Removing of duplicate schema \- Store Design \- Shopify Community, accessed November 6, 2025, [https://community.shopify.com/t/removing-of-duplicate-schema/359409](https://community.shopify.com/t/removing-of-duplicate-schema/359409)  
14. accessed November 6, 2025, [https://meetdomaine.com/studio/insights/technology/shopify-product-schema-for-seo/\#:\~:text=This%20issue%20occurs%20when%20multiple,and%20remove%20or%20consolidate%20them.](https://meetdomaine.com/studio/insights/technology/shopify-product-schema-for-seo/#:~:text=This%20issue%20occurs%20when%20multiple,and%20remove%20or%20consolidate%20them.)  
15. Schema Markup Duplication Issue After Setting up Avada SEO Suite. Theme Default Need to be Disabled. \- Shopify Community, accessed November 6, 2025, [https://community.shopify.com/t/schema-markup-duplication-issue-after-setting-up-avada-seo-suite-theme-default-need-to-be-disabled/409229](https://community.shopify.com/t/schema-markup-duplication-issue-after-setting-up-avada-seo-suite-theme-default-need-to-be-disabled/409229)  
16. Removing of duplicate schema \- \#2 by PaulNewton \- Shopify Community, accessed November 6, 2025, [https://community.shopify.com/c/online-store-and-theme/removing-of-duplicate-schema/m-p/2772391](https://community.shopify.com/c/online-store-and-theme/removing-of-duplicate-schema/m-p/2772391)  
17. Removing the invalid structured data from your Shopify theme \- microdata and JSON-LD, accessed November 6, 2025, [https://www.youtube.com/watch?v=aoVeQOzOPxI](https://www.youtube.com/watch?v=aoVeQOzOPxI)  
18. Remove invalid structured data from your Shopify theme \- Ilana Davis, accessed November 6, 2025, [https://www.ilanadavis.com/blogs/articles/removing-invalid-microdata-shopify-theme](https://www.ilanadavis.com/blogs/articles/removing-invalid-microdata-shopify-theme)  
19. Dawn Theme \- Duplicate Structured / Rich Data (Schema.org / JSON\_LD) with Shopify Review App, accessed November 6, 2025, [https://community.shopify.com/t/dawn-theme-duplicate-structured-rich-data-schema-org-json-ld-with-shopify-review-app/78809](https://community.shopify.com/t/dawn-theme-duplicate-structured-rich-data-schema-org-json-ld-with-shopify-review-app/78809)  
20. Multiple Product Schemas on Shopify Causing SEO Issues – Need Help\!, accessed November 6, 2025, [https://support.google.com/webmasters/thread/297971241/multiple-product-schemas-on-shopify-causing-seo-issues-%E2%80%93-need-help?hl=en](https://support.google.com/webmasters/thread/297971241/multiple-product-schemas-on-shopify-causing-seo-issues-%E2%80%93-need-help?hl=en)  
21. Intro to How Structured Data Markup Works | Google Search Central | Documentation, accessed November 6, 2025, [https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)  
22. The myth of duplicate structured data \- Ilana Davis, accessed November 6, 2025, [https://www.ilanadavis.com/blogs/articles/the-myth-of-duplicate-structured-data](https://www.ilanadavis.com/blogs/articles/the-myth-of-duplicate-structured-data)  
23. Removing the invalid structured data from Shopify theme – microdata and Turbo theme's JSON-LD, accessed November 6, 2025, [https://community.shopify.com/t/removing-the-invalid-structured-data-from-shopify-theme-microdata-and-turbo-themes-json-ld/35751](https://community.shopify.com/t/removing-the-invalid-structured-data-from-shopify-theme-microdata-and-turbo-themes-json-ld/35751)  
24. Product Schema \- Google Search Central Community, accessed November 6, 2025, [https://support.google.com/webmasters/thread/317394279/product-schema?hl=en](https://support.google.com/webmasters/thread/317394279/product-schema?hl=en)  
25. AggregateOffer \- Schema.org Type, accessed November 6, 2025, [https://schema.org/AggregateOffer](https://schema.org/AggregateOffer)  
26. How to fix Google Shop Mismatched value (page crawl) \[price\]? \- Shopify Community, accessed November 6, 2025, [https://community.shopify.com/t/how-to-fix-google-shop-mismatched-value-page-crawl-price/76637](https://community.shopify.com/t/how-to-fix-google-shop-mismatched-value-page-crawl-price/76637)  
27. Google adds support for sale pricing and priceType property \- Search Engine Land, accessed November 6, 2025, [https://searchengineland.com/google-adds-support-for-sale-pricing-and-pricetype-property-446910](https://searchengineland.com/google-adds-support-for-sale-pricing-and-pricetype-property-446910)  
28. How To Add Merchant Listing Structured Data | Google Search ..., accessed November 6, 2025, [https://developers.google.com/search/docs/appearance/structured-data/merchant-listing](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)  
29. Sections \- Shopify Dev Docs, accessed November 6, 2025, [https://shopify.dev/docs/storefronts/themes/architecture/sections](https://shopify.dev/docs/storefronts/themes/architecture/sections)  
30. Section schema \- Shopify Dev Docs, accessed November 6, 2025, [https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema)  
31. How to Remove Shopify Theme Schema.org Microdata, accessed November 6, 2025, [https://support.schemaapp.com/support/solutions/articles/33000265014-how-to-remove-shopify-theme-schema-org-microdata](https://support.schemaapp.com/support/solutions/articles/33000265014-how-to-remove-shopify-theme-schema-org-microdata)  
32. Does the .liquid file for product schema apply to ALL of my products? \- Shopify Community, accessed November 6, 2025, [https://community.shopify.com/t/does-the-liquid-file-for-product-schema-apply-to-all-of-my-products/567445](https://community.shopify.com/t/does-the-liquid-file-for-product-schema-apply-to-all-of-my-products/567445)  
33. What JSON-LD Schema Does for Your Shopify SEO | Analyzify, accessed November 6, 2025, [https://analyzify.com/hub/shopify-seo-json-ld-schema-guide](https://analyzify.com/hub/shopify-seo-json-ld-schema-guide)  
34. Does a custom theme affect rich snippets and structured data? \- Shopify Community, accessed November 6, 2025, [https://community.shopify.com/t/does-a-custom-theme-affect-rich-snippets-and-structured-data/304053](https://community.shopify.com/t/does-a-custom-theme-affect-rich-snippets-and-structured-data/304053)  
35. Rich Results Test \- Google Search Console, accessed November 6, 2025, [https://search.google.com/test/rich-results](https://search.google.com/test/rich-results)  
36. Introducing Rich Results and the Rich Results Testing Tool | Google Search Central Blog, accessed November 6, 2025, [https://developers.google.com/search/blog/2017/12/rich-results-tester](https://developers.google.com/search/blog/2017/12/rich-results-tester)  
37. What is the Schema Markup Validator (SMV), accessed November 6, 2025, [https://www.schemaapp.com/schema-app-news/what-is-smv-schema-org-markup-validator/](https://www.schemaapp.com/schema-app-news/what-is-smv-schema-org-markup-validator/)  
38. Microdata manual removal \- about elements which are identified by itemprop, accessed November 6, 2025, [https://community.shopify.com/t/microdata-manual-removal-about-elements-which-are-identified-by-itemprop/358140](https://community.shopify.com/t/microdata-manual-removal-about-elements-which-are-identified-by-itemprop/358140)  
39. How to remove product schema in Shopify \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/shopify/comments/1jltom8/how\_to\_remove\_product\_schema\_in\_shopify/](https://www.reddit.com/r/shopify/comments/1jltom8/how_to_remove_product_schema_in_shopify/)  
40. What Are The Main Differences Between JSON-LD and Microdata Schema in Shopify, accessed November 6, 2025, [https://storeseo.com/blog/differences-between-json-ld-and-microdata-schema/](https://storeseo.com/blog/differences-between-json-ld-and-microdata-schema/)  
41. How do you combine several JSON-LD markups? \- Stack Overflow, accessed November 6, 2025, [https://stackoverflow.com/questions/48294593/how-do-you-combine-several-json-ld-markups](https://stackoverflow.com/questions/48294593/how-do-you-combine-several-json-ld-markups)  
42. Best JSON-LD practices: using multiple  
43. Can we add multiple schema.org JSON-LD code blocks to the home page of a website?, accessed November 6, 2025, [https://webmasters.stackexchange.com/questions/122836/can-we-add-multiple-schema-org-json-ld-code-blocks-to-the-home-page-of-a-website](https://webmasters.stackexchange.com/questions/122836/can-we-add-multiple-schema-org-json-ld-code-blocks-to-the-home-page-of-a-website)  
44. Intro to Product Structured Data on Google | Google Search Central | Documentation, accessed November 6, 2025, [https://developers.google.com/search/docs/appearance/structured-data/product](https://developers.google.com/search/docs/appearance/structured-data/product)  
45. Set up structured data for Merchant Center \- Google Help, accessed November 6, 2025, [https://support.google.com/merchants/answer/7331077?hl=en](https://support.google.com/merchants/answer/7331077?hl=en)  
46. Review Schema: What It Is & How to Implement It At Scale \- seoClarity, accessed November 6, 2025, [https://www.seoclarity.net/blog/review-schema/](https://www.seoclarity.net/blog/review-schema/)  
47. Review Snippet (Review, AggregateRating) Structured Data | Google Search Central | Documentation, accessed November 6, 2025, [https://developers.google.com/search/docs/appearance/structured-data/review-snippet](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)  
48. The Easiest Way of Adding Aggregate Rating Schema using Coding \- SEO Hacker, accessed November 6, 2025, [https://seo-hacker.com/easiest-adding-aggregate-rating-schema-coding/](https://seo-hacker.com/easiest-adding-aggregate-rating-schema-coding/)  
49. AggregateRating \- Schema.org Type, accessed November 6, 2025, [https://schema.org/AggregateRating](https://schema.org/AggregateRating)  
50. How can I add multiple reviews to a product snippet? \- Stack Overflow, accessed November 6, 2025, [https://stackoverflow.com/questions/47586150/how-can-i-add-multiple-reviews-to-a-product-snippet](https://stackoverflow.com/questions/47586150/how-can-i-add-multiple-reviews-to-a-product-snippet)  
51. How many Reviews to include in JSON-LD schema markup? : r/TechSEO \- Reddit, accessed November 6, 2025, [https://www.reddit.com/r/TechSEO/comments/oxmexd/how\_many\_reviews\_to\_include\_in\_jsonld\_schema/](https://www.reddit.com/r/TechSEO/comments/oxmexd/how_many_reviews_to_include_in_jsonld_schema/)  
52. Rich result report overview \- Search Console Help, accessed November 6, 2025, [https://support.google.com/webmasters/answer/7552505?hl=en](https://support.google.com/webmasters/answer/7552505?hl=en)  
53. Schema Markup Validator, accessed November 6, 2025, [https://validator.schema.org/](https://validator.schema.org/)