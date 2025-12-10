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
Сегодня 2025-10-11.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021976761693152321024

## 2.2. Title
AWS Lightsail/Wordpress DevOps Enginee

## 2.3. Description
`PD` ≔ 
```text
We need an experienced DevOps / Systems Engineer to stabilize our AWS Lightsail WordPress production environment. 
The site has had intermittent downtime and performance issues, and we need someone who can quickly diagnose the root causes, implement durable fixes, and improve system reliability.

What you’ll do:
- Diagnose Apache, PHP, and MySQL issues (CPU, memory, OS-level).
- Recommend and apply configuration and security improvements.
- Implement monitoring, alerting, and log retention (CloudWatch, uptime probes).
- Document findings and provide a clear handoff plan.

Short-term engagement with possible extension for ongoing monitoring and telemetry setup.

# Deliverables
- A root cause analysis identifying the sources of recent server instability
- Configuration updates and documentation of all changes made
- Optimized server setup with monitoring and alerts in place
- Recommendations for ongoing maintenance and scaling
```

## 2.4. Tags
WordPress
DevOps
Apache HTTP Server
MySQL
Amazon Lightsail
Linux System Administration
System Monitoring
Amazon CloudWatch
NGINX
Datadog

## 2.5. Questions
### 2.5.1.
Have you diagnosed or stabilized a production WordPress instance running on AWS Lightsail or EC2 before? 
Briefly describe what you found and how you fixed it.

### 2.5.2.
What monitoring and alerting stack do you typically recommend for small production environments?

### 2.5.3.
What’s your approach to finding the root cause of recurring Apache/MySQL downtime?

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Oct 11, 2025
### 5.3.2. Hire rate (%)
0
### 5.3.3. Количество опубликованных проектов (jobs posted)
1
### 5.3.4. Total spent (USD)
0
### 5.3.5. Количество оплаченных часов в почасовых проектах
STUB
### 5.3.6. Средняя почасовая ставка (USD)
0

# 6.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
The site has had intermittent downtime and performance issues
~~~
```

# 7.
## 7.1.
`Q2⁎` ≔ (Вопрос `ꆜ` §2.5.2)

## 7.2.
`Q3⁎` ≔ (Вопрос `ꆜ` §2.5.3)

# 8
## 8.1.
`Cᛘ⠿` ≔ ⠿~ (Возможные причины `P†`)

## 8.2.
`Cᛘᵢ` : `Cᛘ⠿`

## 8.3.
? `Cᛘᵢ`

# 9.  Анализ `Cᛘ⠿` 

## 9.1. Cᛘ₁: Исчерпание квоты производительности ЦП (CPU Burst Capacity)

### Суть
Инстансы AWS Lightsail функционируют на основе модели взрывной производительности (Burstable Performance).
Эта модель предоставляет низкий базовый уровень производительности ЦП с возможностью временного его превышения за счет накопленных кредитов (CPU Burst Capacity).
Если нагрузка на ЦП превышает базовый уровень, кредиты расходуются.
Когда кредиты исчерпаны, производительность ЦП принудительно ограничивается базовым уровнем (например, 10-30% от полной мощности vCPU).
Это ограничение (throttling) приводит к резкому замедлению обработки запросов или полной недоступности сайта.

### Оценка
90

### Доводы за
Характер проблемы, описанный как «периодический» (intermittent), идеально соответствует циклу исчерпания кредитов под нагрузкой и их медленного восстановления в простое.
Это самая распространенная причина внезапного падения производительности на инстансах Lightsail и EC2 T-серии.
Документация AWS подтверждает, что исчерпание кредитов приводит к деградации производительности (Source 2.2).
Базового уровня производительности часто недостаточно для обслуживания производственного сайта WordPress под нагрузкой, особенно при выполнении фоновых задач или обработке пикового трафика.

### Доводы против
Исчерпание кредитов является симптомом высокого использования ЦП, а не его первопричиной, которая может заключаться в неэффективном коде или внешних атаках.
Если фактическое использование ЦП сайтом всегда ниже базового порога, эта гипотеза неверна.

## 9.2. Cᛘ₂: Нехватка оперативной памяти и активация OOM Killer

### Суть
Стек приложений (Apache, MySQL, PHP) потребляет оперативную память (RAM) для своей работы и обработки запросов.
Если совокупное потребление памяти превышает доступный объем физической RAM, операционная система начинает использовать дисковое пространство подкачки (Swap).
Интенсивное использование Swap (thrashing) резко снижает производительность из-за медленных операций дискового ввода-вывода.
Если физическая память и Swap исчерпаны, ядро Linux активирует механизм OOM (Out-Of-Memory) Killer.
OOM Killer принудительно завершает критические процессы (часто MySQL или Apache) для освобождения памяти, вызывая полный простой сайта (Source 1.3).

### Оценка
85

### Доводы за
Инстансы Lightsail, особенно на младших тарифах, имеют ограниченный объем RAM (например, 1GB или 2GB), которого часто недостаточно для стека LAMP под нагрузкой (Source 1.2, 1.3).
WordPress, особенно с большим количеством плагинов, может потреблять значительный объем памяти (Source 1.4).
Нехватка памяти является типичной причиной сбоев, таких как ошибка подключения к базе данных, когда процесс MySQL завершается (Source 1.1).
Клиент прямо указал на необходимость диагностики проблем с памятью на уровне ОС.

### Доводы против
Если бы памяти было критически недостаточно для базовой работы, проблемы могли бы быть постоянными, а не периодическими.
Периодический характер может указывать на то, что нехватка памяти возникает только во время пиков активности или из-за утечек памяти в приложениях.

## 9.3. Cᛘ₃: Неоптимальная конфигурация веб-сервера (Apache/PHP)

### Суть
Настройки веб-сервера Apache, управляющие количеством одновременных процессов, не соответствуют доступным ресурсам сервера.
Если параметр `MaxRequestWorkers` (или `MaxClients`) установлен слишком высоко, сервер может создать слишком много дочерних процессов под нагрузкой (Source 4.2).
Избыточное количество процессов приводит к чрезмерному потреблению оперативной памяти, усугубляя Cᛘ₂.
Если параметр установлен слишком низко, сервер не сможет обработать входящий трафик, что приведет к отказу в обслуживании.

### Оценка
80

### Доводы за
Стандартные конфигурации Apache (особенно с `mod_php`) часто потребляют слишком много памяти для небольших серверов и могут быстро привести к OOM ошибкам (Source 4.3).
Настройка баланса между параллелизмом и потреблением памяти критически важна на серверах с ограниченными ресурсами (Source 4.1).
Если сервер начинает использовать Swap из-за слишком высокого `MaxRequestWorkers`, это убивает производительность (Source 4.1).
Клиент прямо указал диагностику Apache и PHP как одну из задач.

### Доводы против
Эта проблема чаще является фактором, способствующим исчерпанию ресурсов (Cᛘ₂), чем самостоятельной первопричиной.
Стандартные образы в Lightsail (например, от Bitnami) обычно имеют предварительно настроенную конфигурацию, хотя она может быть не идеальной для конкретного сайта.

## 9.4. Cᛘ₄: Вредоносный трафик и боты (Brute-Force, XML-RPC, DDoS)

### Суть
Автоматизированные атаки и агрессивные боты создают чрезмерную нагрузку на сервер, потребляя ресурсы CPU и памяти и вызывая отказ в обслуживании.
Основные векторы атак на WordPress включают попытки подбора паролей к `wp-login.php` и атаки через интерфейс `xmlrpc.php`.

### Оценка
75

### Доводы за
WordPress является частой целью для автоматизированных атак.
Атаки на `xmlrpc.php` позволяют использовать функцию `system.multicall` для проверки сотен паролей в одном HTTP-запросе, что значительно увеличивает нагрузку и эффективность атаки (Source 5.2).
Атаки могут использовать функцию Pingback для проведения DDoS-атак, перегружая сервер запросами (Source 5.2, 5.3).
Периодический характер проблемы хорошо соответствует паттернам атак или активности ботов.
Даже не очень интенсивные атаки могут перегрузить небольшой инстанс Lightsail.

### Доводы против
Использование эффективных плагинов безопасности или внешнего WAF (например, Cloudflare) может блокировать большинство таких атак.
Проблема может быть вызвана легитимным трафиком, который сервер не в состоянии обработать.

## 9.5. Cᛘ₅: Отсутствие или неправильная настройка кэширования

### Суть
WordPress динамически генерирует страницы при каждом посещении, что требует выполнения PHP-кода и запросов к базе данных.
Отсутствие эффективных механизмов кэширования (кэширование страниц, объектов) приводит к тому, что сервер выполняет избыточную работу для обслуживания идентичного контента (Source 6.1).
Это значительно увеличивает потребление CPU и RAM на каждый запрос и снижает максимальную пропускную способность сайта.

### Оценка
70

### Доводы за
Правильное кэширование страниц значительно снижает нагрузку на бэкенд (PHP и MySQL) и уменьшает время загрузки (Source 6.1).
Кэширование снижает нагрузку на сервер, так как ему не нужно обрабатывать каждый запрос индивидуально (Source 6.2).
Высокая нагрузка из-за отсутствия кэширования может быстро привести к исчерпанию кредитов CPU (Cᛘ₁) или памяти (Cᛘ₂).

### Доводы против
Кэширование страниц не помогает, если узким местом является обработка некэшируемых запросов (например, панель администратора, оформление заказа в электронной коммерции).
Кэширование может маскировать основные проблемы неэффективности кода, не устраняя их.

## 9.6. Cᛘ₆: Неэффективность на уровне базы данных (MySQL)

### Суть
Неоптимальная конфигурация MySQL (например, слишком маленький размер буферного пула `innodb_buffer_pool_size`) приводит к частым операциям чтения с диска вместо оперативной памяти.
Плохо закодированные или ресурсоемкие плагины могут генерировать медленные SQL-запросы.
Медленные запросы потребляют ресурсы CPU, могут вызывать блокировки таблиц и приводить к накоплению очереди запросов на веб-сервере.

### Оценка
65

### Доводы за
Сложные плагины WordPress часто генерируют тяжелые SQL-запросы, которые могут потреблять много RAM (Source 1.4).
Конфигурация MySQL по умолчанию может не подходить для производственной нагрузки и требовать настройки для работы с ограниченной памятью.
Фоновые задачи (WP-Cron), выполняемые плагинами, могут создавать интенсивную периодическую нагрузку на базу данных.
Клиент прямо указал диагностику MySQL как одну из задач.

### Доводы против
Проблемы с базой данных чаще проявляются в виде медленной загрузки страниц, а не в виде полного простоя всего сервера.
Сбой MySQL часто является следствием общей нехватки памяти (Cᛘ₂), а не первопричиной.

## 9.7. Вердикт

Проблема (`P†`) с высокой вероятностью вызвана фундаментальной нехваткой ресурсов на инстансе AWS Lightsail для обработки возникающей нагрузки.

Наиболее вероятными механизмами отказа являются ограничения инфраструктуры AWS, специфичные для Lightsail.

Это проявляется через исчерпание квоты производительности ЦП (Cᛘ₁) и нехватку оперативной памяти (Cᛘ₂).

Периодические простои возникают, когда нагрузка (легитимный трафик, фоновые задачи или атаки) превышает возможности сервера.

Это приводит либо к дросселированию ЦП после исчерпания кредитов (Cᛘ₁), либо к активации OOM Killer из-за исчерпания памяти (Cᛘ₂).

Эти базовые ограничения усугубляются неоптимальной конфигурацией веб-сервера (Cᛘ₃), которая может позволять создавать слишком много процессов, ускоряя исчерпание памяти.

Внешние факторы (Cᛘ₄) и отсутствие оптимизации, такой как кэширование (Cᛘ₅) или настройка базы данных (Cᛘ₆), увеличивают базовую нагрузку и провоцируют достижение лимитов ресурсов.

Для определения точной причины необходимо начать с мониторинга метрик CPU Burst Capacity, использования RAM и Swap, а также анализа конфигурации Apache/MySQL и логов доступа.


 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1.
## 1.1.
`Aᨀ` ≔ (мой ответ `ꆜ`)

## 1.2.
Содержание `Aᨀ`:
~~~markdown
I. Most likely causes of your problem:
1) CPU Burst Capacity
1.1) Essence
AWS Lightsail instances operate on the Burstable Performance model.
This model provides a low baseline of CPU performance with the ability to temporarily exceed it by consuming the accumulated CPU Burst Capacity.
If the CPU load exceeds the baseline level, these credits are consumed.
When the credits are depleted, the CPU performance is forcibly limited to the baseline level (e.g., 5-40% of a full vCPU's power, depending on the instance plan).
This limitation (throttling) leads to a sharp slowdown in request processing or the complete unavailability of the website.
1.2) Rationale
The nature of the problem, described as «intermittent», perfectly matches the cycle of credit exhaustion under load and their slow recovery during idle time.
This is the most common reason for sudden performance degradation on Lightsail and EC2 T-series instances.
The baseline performance is often insufficient to serve a production WordPress website under load, especially when running background tasks or handling peak traffic.
2) RAM shortage and OOM Killer activation
2.1) Essence
The application stack (Apache, MySQL, PHP) consumes Random Access Memory (RAM) for its operation and to process requests.
The Linux kernel manages memory utilization by moving less frequently used memory pages from RAM to swap space when memory pressure increases.
This process can begin well before physical RAM is exhausted, depending on the configuration of the `vm.swappiness` parameter.
Intensive swap usage (thrashing), whether caused by aggressive swapping settings or actual memory exhaustion, drastically reduces performance due to slow disk input/output operations.
If physical memory and swap space are exhausted, the Linux kernel activates the Out-of-Memory (OOM) Killer mechanism.
The OOM Killer forcibly terminates critical processes (often MySQL or Apache) to free up memory, causing a complete website outage.
2.2) Rationale
Lightsail instances, especially on lower-tier plans, have a limited amount of RAM (e.g., 1GB or 2GB), which is often insufficient for a LAMP stack under load.
WordPress, especially with a large number of plugins, can consume a significant amount of memory.
A memory shortage is a typical cause of failures, such as a database connection error when the MySQL process is terminated.
3) Suboptimal stack configuration (Apache/PHP-FPM)
3.1) Essence
The settings that control the number of concurrent processes in the application stack do not match the available server resources.
Standard Lightsail WordPress blueprints (e.g., Bitnami) use PHP-FPM (FastCGI Process Manager) to execute PHP code.
If the PHP-FPM configuration (e.g., the `pm.max_children` parameter) is set too high, the server can create too many PHP processes under load.
An excessive number of processes leads to excessive consumption of RAM, exacerbating the problem from point 2.
If the parameter is set too low, the server will not be able to handle the incoming traffic, which will lead to a denial of service.
3.2) Rationale
While Lightsail uses the more efficient PHP-FPM rather than the older `mod_php`, the default configurations may still be suboptimal for the specific workload and instance size.
Bitnami automatically tunes PHP-FPM settings based on instance memory, but this automated tuning might overestimate the available resources, especially if MySQL or other services consume significant memory.
Tuning the balance between parallelism (number of PHP-FPM children) and memory consumption is critically important on resource-constrained servers.
If the server begins to use Swap due to a `pm.max_children` value that is too high, it severely degrades performance.
4) Malicious traffic and bots (Brute-Force, XML-RPC, DDoS)
4.1) Essence
Automated attacks and aggressive bots create excessive load on the server, consuming CPU and memory resources and causing a denial of service.
The main attack vectors on WordPress include brute-force password attacks on `wp-login.php` and attacks via the `xmlrpc.php` interface.
4.2) Rationale
WordPress is a frequent target for automated attacks.
Attacks on `xmlrpc.php` leverage the `system.multicall` function to check hundreds of passwords in a single HTTP request, which significantly increases the load and the effectiveness of the attack.
Attacks can utilize the Pingback feature to conduct DDoS attacks, overwhelming the server with requests.
The intermittent nature of the problem corresponds well with the patterns of attacks or bot activity.
Even low-intensity attacks can overload a small Lightsail instance.

II. What monitoring and alerting stack do you typically recommend for small production environments?
1) Native AWS Stack (Lightsail Metrics + CloudWatch Agent)
1.1) Essence
This approach uses exclusively Amazon Web Services.
Built-in Lightsail metrics automatically collect hypervisor-level data (CPU utilization, network, CPU Burst Capacity).
Collecting operating system-level metrics (memory, disk) and application logs (Apache, MySQL) requires the installation of the CloudWatch Agent on the instance.
Data is centralized in Amazon CloudWatch for visualization, alerting (CloudWatch Alarms), and log analysis (Logs Insights).
1.2) Advantages
This approach utilizes the native AWS monitoring capabilities (Lightsail Metrics and Amazon CloudWatch), which are the definitive source for tracking CPU Burst Capacity (I.1)—the most likely cause of your problem.
Third-party monitoring solutions can also integrate with AWS APIs (e.g., the Lightsail API) to retrieve this metric.
However, the native stack provides the most direct access to this hypervisor-level data.
1.3) Disadvantages
The standard granularity of built-in Lightsail metrics (5-minute intervals) and standard CloudWatch custom metrics (1-minute intervals) is insufficient for diagnosing the rapid, transient spikes that characterize resource exhaustion scenarios (I.2, I.3).
While CloudWatch offers high-resolution custom metrics (down to 1-second granularity), enabling them increases API usage costs due to more frequent data transmission.
Collecting custom metrics (memory, disk) and logs via the CloudWatch Agent incurs additional charges for metric storage and log ingestion/storage.
The configuration of the CloudWatch Agent, especially for log collection and custom application metrics, requires manual setup and maintenance compared to auto-discovering solutions.
There is a noticeable latency (seconds to minutes) between an event occurring and the corresponding metric or log appearing in CloudWatch, which complicates real-time troubleshooting.
2) High-granularity diagnostic monitoring (Netdata)
2.1) Essence
Netdata is an open-source tool for real-time system performance monitoring.
It is installed as a lightweight agent on the Lightsail instance.
The agent automatically discovers services (Apache, MySQL) and collects thousands of metrics with per-second granularity.
Data is available through a local web interface or the free Netdata Cloud service.
2.2) Advantages
The solution provides per-second granularity, which is invaluable for diagnosing the intermittent performance spikes characteristic of I.2 and I.3.
The agent is extremely lightweight, consuming minimal CPU and memory resources, which is critical for a resource-constrained server.
The installation is very simple and does not require configuration for standard LAMP stacks thanks to auto-detection.
The solution offers excellent, pre-configured visualization of all system components and application performance.
While optimized for real-time troubleshooting, its database engine (`dbengine`) also provides efficient long-term storage for historical trend analysis using a multi-tiered architecture.
The alerting capabilities are sophisticated, supporting complex logic, hysteresis, and dynamic thresholds
2.3) Disadvantages
The agent cannot directly monitor hypervisor-level metrics (such as AWS CPU Burst Capacity), as these are not visible from within the operating system.
Monitoring these metrics requires integrating data from the AWS API (e.g., by deploying a CloudWatch exporter), which adds complexity and latency.
It is not designed for centralized log management.
The alerting capabilities offer fewer integrations with the broader AWS ecosystem (e.g. for automated remediation actions) compared to CloudWatch Alarms.
The dashboard can be overwhelming due to the vast number of metrics presented.
3) Recommendation: Hybrid Approach (AWS Stack + Netdata)
3.1) Essence
For a comprehensive and cost-effective solution in a small production environment facing stability issues, I recommend a hybrid monitoring approach.
This strategy combines the strengths of the native AWS stack for infrastructure-level visibility and Netdata for high-granularity, real-time diagnostics.
3.2) Rationale
The two approaches are complementary, not mutually exclusive.
The AWS stack (II.1) is essential for monitoring hypervisor-level metrics, specifically CPU Burst Capacity.
Accurate tracking of this metric is critical for diagnosing the most probable cause of the issue (I.1), and it is not visible from within the operating system (and thus invisible to Netdata).
Netdata (II.2) is essential for diagnosing resource exhaustion at the OS and application levels (I.2, I.3).
Its per-second granularity, minimal overhead, and detailed visualization provide the necessary insights that the standard AWS stack lacks due to its lower resolution and latency.
This combination ensures complete coverage: AWS monitors the infrastructure constraints, while Netdata monitors how the application utilizes the resources within those constraints.
3.3) Implementation
Use built-in Lightsail metrics to monitor CPU Burst Capacity and set critical CloudWatch Alarms for low remaining capacity.
Install the Netdata agent for real-time performance troubleshooting and detailed analysis of memory, swap usage, disk I/O, Apache, MySQL, and PHP-FPM performance.
Optionally, if long-term centralized log management is required, deploy the CloudWatch Agent configured specifically for log collection (e.g. Apache `access.log`/`error.log`, MySQL `error.log`/`slow_query_log`), while being mindful of ingestion costs.

III. «What’s your approach to finding the root cause of recurring Apache/MySQL downtime?»
My approach is a structured, multi-phase diagnostic workflow.
It is designed to systematically identify the root cause, starting with the most probable (Section I) and least intrusive methods.
It moves from the infrastructure layer up to the application layer.

1) Phase 1: Non-Intrusive Data Collection and Configuration Review
This phase focuses on analyzing existing data (metrics, logs, and configuration files) to quickly understand the failure mechanism and identify immediate triggers related to resource exhaustion, high load, or misconfiguration.

1.1) Basic Infrastructure Metrics Monitoring
1.1.1) Essence
This method uses the built-in AWS Lightsail monitoring tools to analyze the key performance metrics of the instance.
The main focus is on the CPU Utilization and remaining CPU Burst Capacity metrics.
1.1.2) Advantages
This method is critically important for diagnosing I.1, as CPU Burst Capacity exhaustion leads to CPU throttling on Lightsail instances.
The metrics provide objective data to confirm the hypothesis of performance degradation due to AWS infrastructure limitations.
The tools are built into the AWS platform and do not require configuration on the server itself.
Historical data analysis allows identifying CPU usage patterns and the frequency of quota exhaustion.
1.1.3) Disadvantages
Standard Lightsail metrics do not include monitoring of RAM and disk space usage, which is critical for diagnosing I.2.
The metrics show the fact of CPU resource exhaustion, but they do not indicate which specific processes caused this exhaustion.
The low granularity of the standard metrics can hide short load spikes.

1.2) System Log Analysis
1.2.1) Essence
This method involves examining the Linux kernel logs (`dmesg`, `/var/log/kern.log`) and system logs (`/var/log/syslog`, `journalctl`) to identify critical events at the operating system level.
The main focus is on finding messages from the OOM (Out-of-Memory) Killer mechanism and service startup errors.
1.2.2) Advantages
The method provides direct evidence of OOM Killer activation (point I.2).
The analysis makes it possible to precisely determine which process was terminated and when it occurred.
Collecting system logs has a minimal impact on server performance.
Timestamps in the logs help to establish an exact chronology of events.
1.2.3) Disadvantages
System logs record the failure mechanism (e.g., OOM) but not the root cause of memory exhaustion (e.g., a traffic spike).
Critical messages can be lost due to incorrect log rotation configuration or a kernel buffer overflow.

1.3) Application Log Analysis
1.3.1) Essence
This method involves a detailed analysis of existing web server logs (Apache `access.log` and `error.log`), database logs (MySQL `error.log` and, if available, `slow_query_log`), and PHP logs.
The goal is to understand traffic patterns, identify application errors, and determine inefficient database operations.
1.3.2) Advantages
Analysis of the `access.log` is critically important for identifying traffic spikes, bot activity, or DDoS attacks (I.4).
It allows identifying attacks on vulnerable WordPress endpoints (`xmlrpc.php`, `wp-login.php`) that create excessive load.
If available, MySQL slow query logs directly indicate inefficient SQL queries that consume excessive resources.
Apache and PHP error logs record script execution failures, such as reaching the PHP memory limit or timeouts.
1.3.3) Disadvantages
The volume of access logs can be very large, which makes manual analysis difficult without specialized aggregation tools.
Application logs do not provide direct information about the use of system resources (CPU, RAM) at the infrastructure level.
If MySQL slow query logging is disabled, this phase cannot identify specific slow queries.

1.4) Stack Configuration Audit
1.4.1) Essence
This method involves an audit of the Apache, MySQL, and PHP-FPM configurations against the available server resources (RAM and CPU).
In PHP-FPM, the Process Manager configuration is analyzed (I.3), focusing on the `pm` setting (e.g., dynamic, ondemand) and parameters controlling the number of child processes, primarily `pm.max_children`.
In Apache, the Multi-Processing Module (MPM) configuration (e.g., `mpm_event`) is reviewed to ensure efficient connection handling and integration with PHP-FPM.
In MySQL, parameters that affect memory consumption are checked, primarily the buffer pool size (`innodb_buffer_pool_size`).
1.4.2) Advantages
A suboptimal configuration is often a key factor in instability on resource-constrained servers.
The audit identifies potential configuration issues without requiring any changes or service restarts (non-intrusive).
It helps assess whether the PHP-FPM configuration might allow the creation of an excessive number of PHP processes leading to memory exhaustion (I.2).
It helps assess whether the MySQL configuration strikes an appropriate balance between database performance and overall system memory consumption.
1.4.3) Disadvantages
The optimal configuration is highly dependent on the workload characteristics, which are often unknown at the initial stage of diagnostics.
The audit identifies configuration settings but does not directly measure their performance impact without subsequent monitoring or load testing.

2) Phase 2: Active Diagnostics and Intervention
If Phase 1 is inconclusive or indicates a need for more detailed data, this phase involves active interventions, such as implementing granular monitoring or activating detailed diagnostic logging.

2.1) Advanced Resource Monitoring
2.1.1) Essence
This method is aimed at obtaining detailed metrics that are unavailable in the standard Lightsail monitoring, primarily the usage of Random Access Memory (RAM) and swap space.
This requires the installation of a monitoring agent, e.g. the AWS CloudWatch Agent, or the use of external systems.
2.1.2) Advantages
Monitoring RAM and Swap usage is absolutely essential to diagnose the conditions leading to OOM Killer activation (I.2).
The method also makes it possible to identify performance degradation due to intensive Swap usage (thrashing).
The method fills critical gaps in the basic Lightsail metrics, providing a complete picture of the server's resource status.
Historical data make it possible to analyze resource usage preceding the downtime and to identify trends such as memory leaks.
2.1.3) Disadvantages
This is an intrusive action as it requires installing software (the monitoring agent) on the production server.
Using advanced CloudWatch metrics or external services may incur additional costs.
Monitoring agents consume some server resources, although this overhead is typically minimal with modern solutions like the CloudWatch Agent or Netdata.

2.2) Diagnostic Configuration Activation
2.321) Essence
If critical diagnostic information was unavailable in Phase 1 (e.g., MySQL `slow_query_log` or detailed PHP error reporting was disabled), this step involves activating these features.
This provides the necessary data to correlate application behavior with resource consumption.
2.2.2) Advantages
Enabling the `slow_query_log` is essential for identifying database bottlenecks that may not be apparent through configuration audit alone.
Detailed logging provides concrete evidence of application inefficiencies.
2.2.3) Disadvantages
This is an intrusive action that requires modifying configurations and potentially restarting services (e.g., MySQL, PHP-FPM).
Intensive logging can have a minor performance impact, particularly on disk I/O.

3) Phase 3: Deep Application Profiling
This phase focuses on analyzing application efficiency at the code level and is necessary if instability persists after infrastructure, traffic, and configuration issues are resolved.
This is the most intrusive phase and therefore requires specific mitigation strategies to protect the production website.

3.0) Risk Mitigation: Staging Environment and Load Simulation
Because profiling tools generate significant overhead, performing Phase 3 diagnostics on the live production server risks exacerbating the existing instability.
Therefore, all activities in this phase must be carried out in a dedicated staging environment.
This environment must be an exact replica of the production setup (including Lightsail instance size, operating system, stack configuration, and website data).
Furthermore, realistic production load must be simulated in the staging environment (e.g., using load testing tools) to ensure the profiling captures relevant performance bottlenecks that occur under stress.

3.1) Application and Database Profiling
3.1.1) Essence
This method involves using specialized tools within the isolated staging environment (3.0) to analyze WordPress performance at the code and database query level.
Plugins (e.g., Query Monitor) or external Application Performance Monitoring (APM) services are used to identify slow PHP code and resource-intensive SQL queries under simulated load.
3.1.2) Advantages
Profiling precisely identifies the specific plugin, theme, or code fragment responsible for high resource consumption.
The method reveals the fundamental causes of the application's inefficiency.
Code and query optimization provides a long-term solution to the performance problem.
3.1.3) Disadvantages
Profiling tools add significant load to the server; however, conducting the analysis in the staging environment (3.0) mitigates the risk to production stability.
Creating, maintaining, and simulating load in an accurate staging environment requires additional effort and resources.
External APM solutions can be complex to configure and costly.
Profiling does not identify problems at the infrastructure level (I.1) or external attacks (I.4).
~~~

# 2.
# 2.1.
`Fⰳ(§p)` ≔ (Пункт `§p` из `Aᨀ`)

# 2.2.
`Fⰳ(§a-§b)` ≔ (Фрагмент `Aᨀ` с пункта `§a` по пункт `§b` включительно)

# 3.
`Fᨀ` ≔ `Fⰳ(III)`

# 4. `᛭T`
Проанализируй `Fᨀ`:
1) Есть ли там логические ошибки?
2) Есть ли там фактические ошибки?

# 5. Требования к твоему ответу
## 5.1.
Отвечай на русском языке.
## 5.2.
Мой вопрос не пересказывай.
## 5.3.
Уже сформулированную мной информацию не пересказывай.
## 5.4.
Писать свою версию `Fᨀ` не нужно: просто укажи свои замечания по пунктам.
## 5.5.
До и после списка замечаний ничего не пиши.
## 5.6.
Нумерация замечаний должна быть сквозной.
## 5.7.
Для каждого своего замечания указывай свою степень уверенности в нём по шкале от 0 до 100:
- 0 означает, что твоё замечание безосновательно (ошибочно).
- 100 означает, что ты полностью уверен в правоте своего замечания.

# 6. К чему не надо придираться
## 6.1.
Если большая часть `Fᨀ` — на русском языке, то не придирайся к смешению в `Fᨀ` русского и английского языков.
Это смешение — временное и будет устранено позже.
~~~~~~