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
```
▶ A
```
означает, что в описываемой мной ситуации я использую `A`.



~~~~~~

# 3. `O.md`
~~~~~~markdown
# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`C` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `C` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021958492453546725282

## 2.2. Title
Stripe Billing Consultant for SAAS — Trial-to-Paid & Failed Payment Recovery

## 2.3. Description
### 2.3.1. `PD`
`PD` ≔ 
```text
A senior payments engineer who has deep, hands-on Stripe Billing API experience and has previously integrated Stripe with HighLevel (GoHighLevel) at the API level (not just no-code).

You’re fluent with PaymentIntents/SetupIntents, Checkout Sessions, Subscriptions, webhooks, idempotency, and dunning flows, and you can trace issues across three different checkout paths (HighLevel pages, Stripe Checkout, custom Stripe API).

The FULL scope of the project is laid out in this loom video here: https://www.loom.com/share/baa04ab1914d434686529e7baa389e64?sid=7c52c873-b6b1-4636-9f63-dbbe2c193be0

Project overview (what’s going wrong):

We run 30-day free trials. For trials started outside native HighLevel checkout (i.e., via Stripe API / custom checkout), our trial→paid conversion is failing ~25% of the time (≈ 9–10× higher past-due rate than HighLevel-native checkouts).

Symptoms include:

- Subscriptions created via Stripe don’t appear in HighLevel’s Payments › Subscriptions.
- HighLevel shows “please update billing” even though Stripe shows a card on file.
- Occasional API errors like “Invalid value for confirm card payment – client_secret is null.”
- ProfitWell embed throwing an origin not allowed (CORS) error (easy win).

We need a root-cause audit and a production-ready fix.
```

### 2.3.2. `PDL`
`PDL` ≔ 
```
Расшифровка видеоролика loom.com, упоминаемого в `PD`:
~~~
Ниже представлена полная расшифровка видеоролика на языке оригинала, а также подробное описание показанных интерфейсов информационных систем с сопоставлением с речью спикера.

### 1. Полное содержание видеоролика (Язык оригинала: Английский)

[00:00:02] Okay, today I'm uh going through a job posting that we're doing for uh solving a problem with our payment integration between high level and Stripe.
[00:00:11] So right now, uh we have a substantial amount of payments that are doing a 30 day free trial and then are going into past due.
[00:00:24] Um, they are going into past due.
[00:00:30] Uh, and it's about 10 times higher than uh the amount of past due payments that it should be.
[00:00:40] Um, right now we have about um 25% of our payments of our subscriptions um that start a free trial,
[00:00:55] uh are going into a um when it's time to charge the card on file, it is not uh charging the card correctly.
[01:07:00] So this could be for a variety of reasons.
[01:10:00] Uh right now we kind of just need somebody to dig into it, diagnose exactly why it's not happening.
[01:16:00] But we do know that um it is some sort of disconnect between high level and between um Stripe, when we use non high level checkout pages.
[01:33:00] So, um we know that this is happening for we have three types of different ways that people um charge.
[01:46:00] Um, we need somebody to go into our Stripe logs and look at the failed payment intents and find out exactly why um when they are being charged that it's not saving the payment,
[02:04:00] um or why there's just a generic decline.
[02:09:00] Um, the deliverables would be uh to audit and and fix the problem,
[02:14:00] um to set up dunning automation,
[02:17:00] um and then have some sort of reporting to get us from about 25% free trial to uh paid conversion down to we're looking to be uh between five and 10%.
[02:38:00] Um, so as our technical background uh says right here,
[02:44:00] um we have a white label that we're using uh an agency for uh called Course Creator 360 on high level.
[02:50:00] We are using Stripe billing plus checkout and an API.
[02:54:00] Um, I currently am charging a with a custom checkout using the Stripe API.
[03:10:00] Um, and here are some of the requirements.
[03:13:00] We're looking for somebody who has experience using um the Stripe API and the high level API.
[03:22:00] Um, so some questions would be uh one, have you ever worked with recurring subscriptions with high level and Stripe?
[03:31:00] Um, what's your experience with failed payments?
[03:36:00] Um, and can you share some personal examples or projects that uh you have done?
[03:43:00] If you are able to do this and can send over the answers to those questions um and as well as your GitHub repository username, your GitHub repo name,
[04:03:00] um then that would be great.
[04:07:00] Uh so send over your, if you're made it to the end of this video, um include your GitHub username in the uh reply to this post.
[04:22:00] And then we will um continue the conversation from there.

### 2. Описание экранов интерфейса информационных систем

В видеоролике в основном демонстрируется один документ, однако в период с 01:39 по 01:47 происходит быстрое переключение между несколькими техническими интерфейсами.

#### Экран 1: Документ с описанием вакансии (Основной интерфейс)

**Таймкоды:** 00:00–01:38 и 01:48–04:26.

**Описание содержимого:**
Это основной экран видео, представляющий собой документ (вероятно, веб-страницу) с заголовком «Stripe + GoHighLevel API Integration Expert (Recurring Billing & Dunning)».

Документ подробно описывает вакансию по разделам:
*   **Project Overview (Обзор проекта):** Поиск разработчика для решения проблем интеграции Stripe и GoHighLevel (GHL) с рекуррентными платежами и взысканием задолженности (dunning) в кастомной («custom-coded») среде.
*   **Technical Environment (Техническая среда):** Стек включает платформу Course Creator 360 (white-label GHL), биллинг Stripe (API/Checkout), CRM GoHighLevel (API), бэкенд на AWS Lambda (Node/Python) с Webhooks, а также AWS и Cloudflare.
*   **Key Problems to Solve (Ключевые проблемы):** 1. Некорректная синхронизация неудачных платежей. 2. Настройка рабочего процесса Dunning/Recovery. 3. Обеспечение надежности API и вебхуков.
*   **Deliverables (Ожидаемые результаты):** Аудит и исправление ошибок, автоматизация Dunning, отчетность, документация.
*   **Requirements (Требования):** Опыт работы с API Stripe Billing и GHL, знание Node.js/Python/PHP.
*   **Questions for Applicants (Вопросы к кандидатам) и How to Apply (Как подать заявку).**

**Сопоставление с речью:**
Спикер следует структуре этого документа на протяжении всего видео.
*   [00:00:02] Спикер заявляет, что рассматривает объявление о вакансии («going through a job posting»).
*   [00:40:00] Он описывает основную проблему: 25% подписок после пробного периода переходят в статус просроченных, что соответствует разделу «Key Problems to Solve».
*   [02:09:00] Он перечисляет ожидаемые результаты («deliverables»), упоминая аудит, исправление [02:09:00] и автоматизацию взыскания («dunning automation») [02:14:00].
*   [02:38:00] Он ссылается на «technical background», упоминая «Course Creator 360» [02:44:00] и использование кастомного чекаута через Stripe API [02:54:00].
*   [03:22:00] Он зачитывает вопросы из раздела «Questions for Applicants».

#### Экран 2: Рабочий стол macOS с несколькими окнами (включая Stripe Dashboard)

**Таймкоды:** 01:39–01:40, 01:45–01:47.

**Описание содержимого:**
Вид рабочего стола macOS. Документ с вакансией открыт в окне браузера (вкладка показывает локальный файл `.../job_post_stripe_go_high_level_api_integration_expert.html`). Позади видны другие окна, включая браузер с вкладкой «dashboard.stripe.com». Справа частично видна панель, похожая на инспектор или терминал. В строке меню видна дата «Tue Aug 19 8:56 PM».

**Сопоставление с речью:**
Появляется во время переключения окон, когда спикер переходит к обсуждению необходимости анализа логов Stripe [01:46:00]. Видимость панели управления Stripe подтверждает технологии, о которых идет речь.

#### Экран 3: Интегрированная среда разработки (IDE)

**Таймкод:** 01:41.

**Описание содержимого:**
IDE в темной теме (вероятно, VS Code). Показан код на Python (файл `ingress_lambda.py`). Код относится к AWS Lambda: видны импорты `boto3` (AWS SDK), переменные окружения (например, `REGION`) и функции обработки событий (например, `get_customer_id_from_event`). В нижней части экрана видны логи выполнения в терминале.

**Сопоставление с речью:**
Этот экран иллюстрирует «custom-coded» бэкенд (упомянутый в Экране 1 и в речи спикера [02:54:00]), который, вероятно, участвует в обработке платежей.

#### Экран 4: Интерфейс ChatGPT

**Таймкод:** 01:42.

**Описание содержимого:**
Веб-интерфейс ChatGPT. Виден ответ модели со списком сгенерированных PNG-файлов (например, `test_run_modal.png`). В боковой панели видна история чатов, включая диалог «Stripe subscription sync issue» (Проблема синхронизации подписок Stripe).

**Сопоставление с речью:**
Появляется кратковременно. Название диалога «Stripe subscription sync issue» напрямую связано с проблемой, которую описывает спикер.

#### Экран 5: Инструменты разработчика браузера (Консоль)

**Таймкод:** 01:43–01:44.

**Описание содержимого:**
Консоль разработчика в браузере. Видны логи процесса разработки («[Fast Refresh] rebuilding») и критическая ошибка, выделенная красным: «Failed to load resource: the server responded with a status of 500 (Internal Server Error)», связанная с `localhost`.

**Сопоставление с речью:**
Появляется кратковременно. Ошибка сервера (500) иллюстрирует наличие технических проблем в системе, для решения которых ищут специалиста.
~~~
```

## 2.4. Tags
Payment Gateway Integration
API Integration
Stripe API
Stripe
HighLevel

# 3. Информация о `C`
## 3.1. Местоположение
United States
St. George

## 3.2. Характеристики компании
### 3.2.1. Сектор экономики
Dec 29, 2021

### 3.2.2. Количество сотрудников
неизвестно

## 3.3. Характеристики учётной записи на `UW`
### 3.3.1. Member since
Dec 29, 2021
### 3.3.2. Hire rate (%)
0
### 3.3.3. Количество опубликованных проектов (jobs posted)
1
### 3.3.4. Total spent (USD)
0
### 3.3.5. Количество оплаченных часов в почасовых проектах
0

# 4.
`P†` ≔†
```
Проблема, о которой `C` пишет в `PD`:
~~~
For trials started outside native HighLevel checkout (i.e., via Stripe API / custom checkout), our trial→paid conversion is failing ~25% of the time (≈ 9–10× higher past-due rate than HighLevel-native checkouts).
~~~
```

# 5.
`H` ≔?
```
Возможная причина `P†`:
~~~
Вероятнее всего, текущая реализация использует PaymentIntent (возможно, с нулевой суммой или иным обходным путем), что не инициирует необходимый процесс аутентификации (например, 3D Secure) для авторизации будущих off-session списаний. 
Когда пробный период заканчивается и система пытается произвести первое списание, банк-эмитент, не имея должным образом оформленного мандата от первоначальной сессии, отклоняет транзакцию. 
Этот отказ, хотя технически может быть «мягким» (soft decline), в данном контексте является фактически «жестким» (hard decline) с кодом authentication_required, поскольку он требует вмешательства клиента для повторной аутентификации. 
Высокий процент отказов является прямым следствием выбора неверного инструмента API для поставленной задачи, что приводит к предсказуемым сбоям аутентификации в момент первого платежа.
~~~
```
 
~~~~~~

# 4. `T.md`
~~~~~~markdown
# 1.
## 1.1. 
`L_SOURCE` ≔ (Русский язык)

## 1.2. 
`L_TARGET` ≔ (English)

# 2.
## 2.1.
`D` ≔ (мой ответ `C`)

## 2.2.
Содержание `D`:
~~~markdown
Причина вашей проблемы очевидна для меня: использование неверного метода API Stripe: `PaymentIntent` вместо правильного `SetupIntent`.
1) Код отказа `authentication_required` является hard decline, который прямо указывает на то, что банк-эмитент требует аутентификации клиента (например, через 3D Secure) для проведения транзакции.
Такой отказ при попытке автоматического списания по окончании пробного периода однозначно свидетельствует об отсутствии предварительно полученного и валидированного мандата на списание средств в режиме off-session.
2) Системы автоматического повтора платежей Stripe (Smart Retries), предназначенные для борьбы с «мягкими» отказами, по своей архитектуре игнорируют «жесткие» отказы, включая `authentication_required`, что объясняет системный и неразрешимый характер проблемы без вмешательства в код.
3) Высокая доля таких отказов (~25%) является не показателем кредитного риска или нежелания клиентов платить, а прямым измерением архитектурного сбоя, при котором интеграция технически неспособна доказать банку наличие согласия клиента на рекуррентный платеж.
4) Высокая доля отказов при первой попытке списания средств после окончания пробного периода является прямым и ожидаемым следствием отсутствия надлежащей аутентификации Strong Customer Authentication (SCA) во время первоначальной сессии. 
Банки-эмитенты в соответствии с регуляторными требованиями, такими как PSD2 в Европе, отклоняют оффсессионные транзакции с кодом `authentication_required`, если продавец не получил явного согласия клиента на рекуррентные платежи через соответствующий механизм аутентификации.
5) Тот факт, что проблема возникает исключительно при использовании кастомного API-решения и отсутствует в нативном чекауте HighLevel, убедительно доказывает, что ошибка кроется именно в логике кастомного кода.
Нативные интеграции и готовые решения, такие как Stripe Checkout, по умолчанию реализуют корректную логику с `SetupIntent` для подписок, в то время как кастомная разработка допустила ошибку, неправильно реализовав этот поток.
6) Упомянутая вами ошибка «Invalid value for confirm card payment – client_secret is null» косвенно подтверждает гипотезу, указывая на запутанную и некорректную логику работы с интентами на стороне клиента. 
Такие ошибки часто возникают при попытке повторно подтвердить уже завершенный или просроченный интент, что вполне возможно в сценарии, где `PaymentIntent` ошибочно пытаются приспособить для создания подписки.

~~~

# 3.
## 3.1.
`D2` ≔ (начальная часть `D`, переведённая с `L_SOURCE` на `L_TARGET`)

## 3.2.
Содержание `D2`:
~~~markdown
~~~

# 4.
## 4.1.
`F` ≔ (фрагмент `D`)

## 4.2.
Содержание `F`:
~~~markdown
Такие ошибки часто возникают при попытке повторно подтвердить уже завершенный или просроченный интент, что вполне возможно в сценарии, где `PaymentIntent` ошибочно пытаются приспособить для создания подписки.
~~~

# 5. `᛭T`
Переведи `F` на `L_TARGET`, с учётом:
- контекста `D`
- `D2`: уже переведённой части `D`
- `᛭O`

# 6. Правила перевода
## 6.1.
Переводи именно в той стилистике, как написано на `L_SOURCE`.
Не делай перевод более вежливым, чем оригинал.

## 6.2.
Те предложения, которые сейчас полностью на `L_TARGET` — оставь без изменения.

## 6.3.
### 6.3.1.
Не используй Markdown: только plain text.
### 6.3.2.
При этом можно и нужно использовать то форматирование, которое уже есть в оригинале: его не убирай.
### 6.3.3.
Не форматируй веб-ссылки посредством Markdown, если они не отформатированы так в оригинале. 
Например, не пиши так:
```
[https://www.eca.web.tr/eca-nita-esnek-uclu-eviye-bataryasi-beyaz-102118110-308](https://www.eca.web.tr/eca-nita-esnek-uclu-eviye-bataryasi-beyaz-102118110-308)
```
если в оригинале скобок `[]()` нет.

## 6.4.
Форматируй перевод в точности как оригинал. 
В частности:
*) каждый абзац должен содержать ровно одно предложение
*) между абзацами не должно оставаться пустых строк.
*) кавычки используй те же, что и в оригинале: «» и ``.

## 6.5.
Не используй сокращения типа «don't». Все подобные фразы пиши полностью: «do not».

## 6.6.
Не используй жаргон.
Вместо этого используй официальные термины.
### 6.6.1.
В частности, фразы в кавычках используй только в том случае, когда они являются точными цитатами.
Не используй фразы в кавычках для применения жаргонных фраз.
Например, следующий фрагмент текста недопустим, потому что там используется жаргонная фраза «пролетел»: 
```
Например, код, который пушит данные о покупке, подключён асинхронно и загружается с небольшой задержкой, а триггер уже «пролетел».
```

## 6.7.
При обсуждении программного обеспечения используй точные официальные термины на английском языке: именно в том виде, как они указаны в официальной англоязычной документации к этому программному обеспечению.

## 6.8.
Не используй «you need» и другие подобные обращённые к клиенту фразы, перекладывающие действия на него.
Помни: я пишу клиенту или потенциальному клиенту.
Делать в любом случае буду я, а не клиент.
Вместо «you need» используй 2 альтернативы:
### 6.8.1.
Нейтральные фразы типа «it is necessary».
### 6.8.2.
Глаголы в неопределённой форме.
Например, во фрагменте ниже использованы подобные глаголы «set up», «create»:
```
1.2) Set up the transfer of login events from WordPress to Power BI using Fabric / OneLake.
1.2.1) Set up a «Data Pipeline» from the WordPress database table that stores login events (see point 1.1) to Fabric / OneLake.
1.2.2) Set up a connection from Power BI to Fabric / OneLake to pass login events.
1.3) Create the data model in Power BI.
```
Обрати внимание, в этом фрагменте не говорится, кто именно будет выполнять описанные действия: ответственность не перекладывается на клиента, в отличие от «you need».

## 6.9.
Никогда не переводи понятие «сайт» / «веб-сайт» как «site». 
Вместо этого используй форму «website»: это является более профессиональным.

## 6.10.
Никогда не переводи понятие «пункт нумерованного списка» как «item».
Всегда переводи это как «point».

## 6.11.
Вместо «for example» используй «e.g.».
~~~~~~