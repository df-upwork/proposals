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
https://www.upwork.com/jobs/~021993559314159411838

## 2.2. Title
Zoom API/Developer Needed to Solve Notetaker + Registration Conflict

## 2.3. Description
`PD` ≔ 
```text
# About Us
We run a business coaching and education company that helps trades business owners (plumbing, electrical, HVAC, construction) grow profit, regain time, and systemize their operations. 
We have hundreds of active members in coaching programs and want to better understand how they feel about our experience, what’s working, what’s valuable and where we can improve.

# The Project
##
We currently use Zoom Meetings with registration enabled because we need to capture attendee emails for tracking member engagement. 

##
However, when registration is turned on:
- Our AI notetaker tool (Fathom) is blocked from joining the meeting, even when added as an alternative host or invited attendee.
- Disabling registration allows Fathom to join but then we lose email collection, which we must have for reporting.

##
Zoom live chat support confirmed this is considered a developer/API issue and pointed us toward the Zoom Meeting API as a possible workaround.

##
We need a developer who can come up with a solutions that:
- Ensures our notetaker (Fathom) can join meetings AND
- Keep registration on or capture attendee emails another way

# Requirements:
- Proven experience with Zoom Developer Platform & Zoom API
- Experience with OAuth, webhook events and automated meeting workflows
- Ability to advise on feasibility before implementation
- Clear communication and documentation on any setup needed
- (Bonus) Familiarity with AI notetakers like Fathom.

# Please include in your proposal:
- A short explanation of similar Zoom API works you’ve done
- Your recommended initial approach
- Estimated timeline
- Any questions you need answered before starting

# Deliverables
- Implement the chosen solution OR document a recommended alternative
- Provide step-by-step instructions for our internal team to maintain the setup
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
New Zealand
Hamilton

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
неизвестно

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Oct 16, 2017
### 5.3.2. Hire rate (%)
100
### 5.3.3. Количество опубликованных проектов (jobs posted)
24
### 5.3.4. Total spent (USD)
44K
### 5.3.5. Количество оплаченных часов в почасовых проектах
1145
### 5.3.6. Средняя почасовая ставка (USD)
18.32 

# 6. Другие проекты `ꆜ` на `UW`
## 6.1. `P1⁎`

### 6.1.1. URL
https://www.upwork.com/jobs/~021938456368146305758

### 6.1.2. Title
Wix Velo Developer Needed to Show Dynamic Booking Link by Logged-In User

### 6.1.3. Description
`P1D` ≔ 
```text
We’re looking for an experienced Wix Velo developer to implement a filtered booking system on our members-only site.

Project Overview:
Each of our members is assigned a coach. Each coach has their own booking calendar. We want to ensure that when a member logs in and visits the “Office Hours” page, they see only their own coach’s booking link or embedded calendar—no dropdowns, no access to other coaches.

What We Need:

Detect the logged-in user

Retrieve their assigned coach from the Members collection (already stored)

Look up that coach’s booking link from a separate Coaches collection

Display the correct booking link or embed for that coach only


Deliverables:

Fully functional Velo code to perform the lookup and conditional display

Clean, user-friendly interface showing only relevant booking link and sessions

Basic error handling if data is missing or misconfigured

Ideal Candidate:

Strong experience with Wix Velo and Wix CMS

Confident working with reference fields and dynamic user-based content

Able to deliver a reliable, maintainable solution within a few days
```

### 6.1.4. Publication Date
2 quarters ago

## 6.2. `P2⁎`

### 6.2.1. URL
https://www.upwork.com/jobs/~021837369588669795041

### 6.2.3. Title
Admin Needed for Data Entry & File Management

### 6.2.3. Description
`P2D` ≔ 
```text
We are seeking a detail-oriented Data Entry Specialist to transfer workbook data from our old membership site to our new Wix platform, ensuring each workbook is correctly linked to its corresponding video and identifying any content gaps.

Key Responsibilities:
Input workbook data from the old membership site into the corresponding video sections on Wix.
Ensure each workbook is accurately linked to its respective video.
Organize workbooks and videos into designated categories on Wix.
Identify any missing workbooks and create a list of these gaps.
Maintain high accuracy in data labeling and storage for easy accessibility and management.

Looking for someone who can start asap
```

### 6.2.4. Publication Date
last year

## 6.3. `P3⁎`

### 6.3.1. URL
https://www.upwork.com/jobs/~021895182206338936619

### 6.3.2. Title
Call Review System Development with Fathom and GPT Integration

### 6.3.3. Description
`P3D` ≔ 
```text
We are looking for a skilled developer to create a call review system that integrates with Fathom to pull transcripts and uses GPT to evaluate calls based on a specific rubric. The ideal candidate will have experience with API integrations and AI models to ensure smooth operation and accurate evaluations. Responsibilities include setting up the Zapier automation and designing prompts for the GPT model to generate meaningful insights from the transcripts. Strong attention to detail and problem-solving skills are essential.
```

### 6.3.4. Publication Date
3 quarters ago

# 7.
## 7.1.
`POs` ≔⠿ {`P1⁎`, `P2⁎`, `P3⁎`}

## 7.2.
`Ps` ≔ (⠿{`P⁎`} ⋃ `POs`)

## 7.3.
`Pi` : `Ps`

# 8.
## 8.1.
`С⁎` ≔ 
```
Компания `ꆜ`:
~~~
a business coaching and education company that helps trades business owners (plumbing, electrical, HVAC, construction) grow profit, regain time, and systemize their operations
~~~
```

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`P†` ≔†
```
Проблема, о которой `ꆜ` пишет в `PD`:
~~~
- Our AI notetaker tool (Fathom) is blocked from joining the meeting, even when added as an alternative host or invited attendee.
- Disabling registration allows Fathom to join but then we lose email collection, which we must have for reporting.
~~~
```

# 10. Что беспокоит `ꆜ` (анализ №1, выполнен Gemini Deep Research)
https://gemini.google.com/share/fa774702ddb7

## **1. Введение и контекст исследования**

В современном ландшафте корпоративных коммуникаций наблюдается фундаментальный сдвиг в сторону автоматизации документирования встреч. Инструменты на базе искусственного интеллекта, такие как Fathom, трансформировали процесс сбора информации, превратив его из ручной рутины в автоматизированный поток данных. Однако внедрение подобных инструментов в устоявшиеся экосистемы видеоконференцсвязи, в частности Zoom, неизбежно сталкивается с техническими и архитектурными противоречиями. Для клиента ꆜ и проекта P⁎ эти противоречия вышли за рамки простых неудобств и переросли в критические блокирующие факторы, угрожающие целостности бизнес-процессов и качеству собираемых данных.

Настоящий отчет представляет собой всесторонний анализ технической обоснованности проблем, выявленных клиентом ꆜ. Мы детально рассмотрим конфликт между протоколами безопасности Zoom (требование регистрации, аутентификация пользователей) и операционной моделью "безголовых" (headless) ботов, используемых Fathom. Цель документа — не просто констатировать наличие сбоев, а вскрыть их корневые причины на уровне API, HTTP-протоколов и логики обработки данных, а также предложить технически выверенные стратегии решения, варьирующиеся от процессных обходных путей до сложных интеграционных архитектур.

Анализ базируется на детальном изучении документации Zoom API, механизмов работы Fathom, а также эмпирических данных, полученных из сообществ разработчиков и технической поддержки обеих платформ. Мы последовательно докажем, что проблемы клиента ꆜ являются не следствием некорректной настройки, а результатом фундаментальной несовместимости выбранных конфигураций безопасности Zoom с текущей архитектурой инструмента Fathom.

---

## **2. Архитектурный ландшафт и идентификация проблем клиента ꆜ**

Чтобы понять глубину конфликта, необходимо деконструировать архитектуру взаимодействия трех ключевых компонентов: платформы видеоконференцсвязи (Zoom), инструмента автоматизации (Fathom) и бизнес-требований клиента (сбор данных через регистрацию).

### **2.1. Анатомия проблемы: Трилемма "Безопасность — Автоматизация — Данные"**

Клиент ꆜ находится в ситуации, которую можно охарактеризовать как "интеграционная трилемма". В проекте P⁎ существуют три взаимоисключающих требования:

1. **Безопасность и контроль доступа:** Клиент стремится ограничить доступ к встречам, используя функции Require Registration (Требовать регистрацию) или Only Authenticated Users (Только аутентифицированные пользователи). Это стандартная практика для защиты от нежелательных вторжений ("Zoom-bombing") и контроля аудитории.  
2. **Целостность данных (CRM):** Критически важным требованием является сбор email-адресов участников для последующей аналитики и интеграции с CRM (например, Salesforce или HubSpot). Механизм регистрации Zoom является нативным способом сбора этих данных.  
3. **Автоматизация документирования:** Использование Fathom для автоматической записи, транскрибации и саммаризации встреч.

Анализ показывает, что одновременное выполнение всех трех условий невозможно в рамках текущей "коробочной" функциональности Fathom. Когда клиент включает регистрацию (требование 2), Zoom изменяет протокол входа, создавая барьер, который бот Fathom (требование 3) не может преодолеть.1 Если клиент отключает регистрацию, чтобы пропустить бота, он теряет данные об участниках (требование 2), так как Zoom API перестает возвращать email-адреса для "гостевых" подключений.3

### **2.2. Техническая природа "Бота-участника" (Participant Bot)**

Fathom, как и большинство аналогичных решений (Otter.ai, Fireflies.ai), функционирует по модели "бота-участника". Это означает, что технически Fathom не интегрируется с сервером Zoom на уровне бэкенда (через SIP-транки или RTMP-потоки в стандартном режиме). Вместо этого он эмулирует поведение обычного пользователя:

* **Сканирование календаря:** Бот получает доступ к календарю пользователя (Google/Outlook), находит событие и извлекает ссылку на встречу (поле Location или Description).4  
* **Инициализация headless-браузера:** В назначенное время Fathom запускает виртуальный браузер (обычно на базе Chromium) на своих серверах.  
* **Навигация и DOM-манипуляции:** Этот браузер переходит по извлеченной ссылке, взаимодействует с веб-интерфейсом Zoom (Web Client), вводит имя (например, "Fathom Notetaker") и нажимает кнопку "Join".  
* **Захват медиапотока:** После входа бот захватывает аудио и видео потоки непосредственно из DOM-элементов страницы (HTML5 <video>/<audio> теги) или через перехват WebRTC трафика.

Эта архитектура критически зависима от предсказуемости веб-интерфейса Zoom. Любое отклонение от стандартного сценария "нажал ссылку -> попал в лобби" ломает логику бота. Включение регистрации — это именно такое отклонение.

---

## **3. Глубокий анализ конфликта: Zoom API и механизмы регистрации**

В этом разделе мы детально разберем, почему именно механизм регистрации Zoom становится непреодолимым препятствием для Fathom, анализируя структуру URL, токены доступа и логику перенаправлений.

### **3.1. Феноменология сбоя: Регистрационная стена**

Когда организатор встречи включает опцию **"Required Registration"**, стандартная ссылка на встречу (формата https://zoom.us/j/123456789) перестает вести непосредственно в комнату ожидания или на встречу. Вместо этого сервер Zoom возвращает HTTP-ответ с кодом перенаправления (обычно 302), который отправляет клиента на веб-страницу с формой регистрации.

Технический анализ препятствия:  
Бот Fathom — это скрипт. Он ожидает, что по ссылке откроется интерфейс конференции. Вместо этого он получает HTML-страницу с полями ввода (First Name, Last Name, Email) и, что критично, часто с CAPTCHA.5

* **Отсутствие контекста:** Бот "не знает", какие данные вводить в форму. Он запускается от имени пользователя Fathom, но не обладает его полным профилем для заполнения произвольных форм.  
* **Проблема CAPTCHA:** Даже если бы бот мог заполнить поля, современные механизмы защиты от ботов (ReCAPTCHA или собственные алгоритмы Zoom) блокируют автоматизированные попытки регистрации, особенно если они исходят с IP-адресов дата-центров (AWS, Google Cloud), где хостятся серверы Fathom.6  
* **Результат:** Бот "застревает" на странице регистрации и не может попасть на встречу. В логах Fathom это, вероятно, отображается как тайм-аут или ошибка навигации.

Исследование подтверждает, что документация Fathom прямо указывает на невозможность работы с встречами, требующими регистрации: *"Fathom will still not be able to join unsupported calls, including calls that... Require registration"*.1 Это подтверждает техническую обоснованность беспокойства клиента: инструмент действительно несовместим с текущей конфигурацией безопасности.

### **3.2. Токенизация доступа: Параметр tk**

Для успешного входа на встречу с включенной регистрацией Zoom требует наличие специального токена.

**Механизм работы:**

1. Пользователь заполняет форму регистрации.  
2. Zoom создает запись в базе данных registrants.  
3. Zoom генерирует уникальную ссылку для входа (Join URL), которая выглядит следующим образом:  
   https://zoom.us/w/123456789?tk=IyRR7...&pwd=...  
   Здесь параметр tk (Token) является криптографическим идентификатором, связывающим конкретную сессию подключения с записью регистрации.7

Суть конфликта для проекта P⁎:  
Бот Fathom берет ссылку из календаря. В календаре организатора обычно сохраняется общая ссылка на встречу (без токена tk), так как организатору не нужно регистрироваться на собственную встречу. Бот, использующий эту общую ссылку, попадает на перенаправление к форме регистрации. Чтобы бот мог войти, он должен иметь ссылку, уже содержащую валидный tk токен. Однако механизма автоматического получения такого токена для бота в экосистеме Fathom не предусмотрено.  
Это подтверждается анализом Zoom API, который гласит, что join_url с токеном возвращается только в ответе на API-запрос POST /meetings/{meetingId}/registrants.9 Fathom не делает этот вызов, так как он позиционируется как пользовательское приложение, а не интегратор инфраструктуры Zoom.

### **3.3. Блокировка "Authenticated Users Only"**

Еще одной проблемой, выявленной клиентом, является конфликт с настройкой **"Only authenticated users can join"**.10

Техническая валидация:  
Эта настройка требует, чтобы любой участник (включая бота) был авторизован в аккаунте Zoom перед присоединением.

* **Проблема:** Бот Fathom — это анонимный агент. У него нет учетной записи Zoom, пароля или сессионных куки. Он пытается присоединиться как "Гость".  
* **Результат:** Zoom API или Web Client возвращает ошибку доступа (код 403 или специфическое сообщение "Sign In Required").11

Это ограничение является абсолютным для ботов типа "Web Scraper", к которым относится Fathom. Единственный способ обойти это — использовать ZAK (Zoom Access Key) токены, которые позволяют программно авторизовать веб-клиента.11 Однако Fathom не предоставляет пользователям возможность генерировать и передавать ZAK токены своим ботам.

---

## **4. Проблема целостности данных: Zoom API и потеря Email-адресов**

Клиент ꆜ справедливо обеспокоен тем, что отключение регистрации (как способ починить Fathom) ломает сбор аналитики. Этот раздел анализирует поведение Zoom API при работе с анонимными пользователями.

### **4.1. Анализ Webhook participant_joined**

Для автоматизации бизнес-процессов (например, отметки посещаемости в CRM) разработчики часто используют вебхуки Zoom. Ключевым событием является meeting.participant_joined.

Поведение API при включенной регистрации:  
Объект participant содержит поля:

* user_name: Имя, введенное при регистрации.  
* user_email: Email, введенный при регистрации.  
* user_id: Уникальный ID.  
* registrant_id: Ссылка на запись регистрации.

Поведение API при ОТКЛЮЧЕННОЙ регистрации (Guest Join):  
Когда пользователь присоединяется к встрече без регистрации (через веб-клиент или десктопное приложение без входа в аккаунт), Zoom API намеренно ограничивает передачу персональных данных (PII).

* user_email: **Возвращается пустым (null/empty string)**.3  
* user_id: Генерируется временный ID, который невозможно сопоставить с реальным аккаунтом пользователя вне контекста этой конкретной встречи.

Анализ беспокойства клиента:  
Беспокойство клиента абсолютно обосновано. Если отключить регистрацию, чтобы Fathom мог работать, поле email в отчетах Zoom и вебхуках исчезнет для всех внешних участников. Это делает невозможным автоматическое сопоставление участника встречи с карточкой контакта в Salesforce или HubSpot, разрушая логику проекта P⁎.  
Исследование подтверждает, что даже если передать email в URL (например, через нестандартные параметры), Zoom Web SDK и Web Client часто игнорируют их для неавторизованных пользователей в целях безопасности.14

---

## **5. Сравнительный анализ альтернативных архитектурных решений**

Учитывая выявленные фундаментальные конфликты, необходимо рассмотреть, существуют ли на рынке решения, способные удовлетворить всем требованиям клиента ꆜ одновременно. Мы сравним текущее решение (Fathom) с альтернативными подходами.

### **5.1. Fathom vs. Recall.ai (API-подход)**

**Fathom (SaaS Application):**

* **Тип:** Готовое приложение для конечного пользователя.  
* **Метод:** Web Automation (Scraping).  
* **Ограничения:** Зависит от UI Zoom, блокируется капчей, регистрацией и требованиями авторизации.  
* **Вердикт:** Не гибкое решение. Не позволяет кастомизировать процесс входа.

**Recall.ai (Unified API for Meeting Bots):**

* **Тип:** Инфраструктурное API для разработчиков.  
* **Метод:** Позволяет программно создавать ботов для входа на встречи.  
* **Работа с регистрацией:** Документация Recall.ai прямо заявляет о поддержке встреч с регистрацией. Разработчик может передать meeting_url вместе с токеном tk или настроить бота на получение join_url через Zoom API.16  
* **Работа с авторизацией:** Поддерживает "Signed-in Bots" через передачу ZAK токенов, что позволяет обходить ограничение "Authenticated Users Only".11  
* **Стоимость:** Модель "Pay As You Go" ($0.70/час записи) или энтерпрайз контракты.18  
* **Вердикт:** Технически полностью решает проблему, но требует разработки собственного приложения (Build vs. Buy).

### **5.2. Нативные решения: Zoom AI Companion**

Zoom активно развивает собственный ИИ-инструмент — **AI Companion**.

* **Преимущество:** Работает "на сервере". Ему не нужно "присоединяться" к встрече как участнику. Он имеет доступ к потокам данных напрямую из ядра Zoom.  
* **Регистрация:** Не имеет значения. Инструмент доступен организатору независимо от настроек входа гостей.  
* **Конфликт:** LBL (Lawrence Berkeley National Lab) и другие организации блокируют сторонних ботов (Fathom, Otter) именно в пользу Zoom AI Companion из соображений безопасности.10  
* **Недостаток для клиента:** Может уступать Fathom в качестве саммаризации или интеграции с специфическими CRM, к которым привык клиент. Однако с точки зрения *доступа* это самое надежное решение.

---

## **6. Стратегии решения и технические обходные пути (Workarounds)**

На основе проведенного анализа мы предлагаем три стратегии решения проблемы для проекта P⁎. Они ранжированы от организационных изменений до сложных инженерных внедрений.

### **Стратегия А: "Разделение потоков" (Организационное решение)**

**Концепция:** Разделить процесс сбора данных (регистрацию) и процесс доступа к видеоконференции.

**Реализация:**

1. **Лендинг-пейдж:** Клиент создает внешнюю страницу регистрации (на Tilda, HubSpot, Unbounce или собственном сайте).  
2. **Сбор данных:** Пользователь заполняет форму на этом сайте. Данные (email, имя) сразу отправляются в CRM.  
3. **Доступ:** После успешной отправки формы пользователю показывается (или отправляется на email) **стандартная ссылка Zoom без требования регистрации** (https://zoom.us/j/12345...).  
4. **Настройка Zoom:** В самом Zoom регистрация **отключена**. Опция "Authenticated users only" **отключена** (или настроен Waiting Room).

**Анализ:**

* **Fathom:** Работает, так как Zoom-ссылка открытая и не требует регистрации.  
* **Данные:** Собираются на внешней форме.  
* **Риски:** Пользователи могут переслать прямую ссылку Zoom коллегам, минуя регистрацию. Это приведет к появлению "неучтенных" участников в CRM.  
* **Митигация рисков:** Использовать "Waiting Room" и скрипт, который сверяет имена в Зале ожидания со списком зарегистрированных на лендинге (сложно реализуемо вручную, но возможно).

### **Стратегия Б: "API-Middleware" (Инженерное решение)**

**Концепция:** Программная имитация регистрации для бота. Если клиент настаивает на использовании Require Registration в Zoom, необходимо "научить" Fathom проходить её. Поскольку Fathom закрытая система, мы должны действовать через Zoom API.

**Алгоритм реализации (Developer Workaround):**

1. **Триггер:** При создании встречи в календаре, скрипт-мидлварь (на Python/Node.js) обнаруживает событие.  
2. **Регистрация Бота:** Скрипт вызывает метод Zoom API POST /meetings/{id}/registrants.9  
   * Body: { "email": "bot@fathom.video", "first_name": "Fathom", "last_name": "Notetaker" }.  
3. **Получение Токена:** API возвращает JSON, содержащий поле join_url, в котором зашит уникальный токен tk.  
   * Пример: https://zoom.us/w/999?tk=Kpxg...&pwd=123.  
4. **Инъекция (Ручная):** К сожалению, Fathom API пока не позволяет программно "скормить" ему эту ссылку для предстоящей встречи. Единственный способ — использовать функцию "Add to Meeting" в десктопном приложении Fathom **в момент начала встречи**, вставив туда полученную уникальную ссылку.4

**Вердикт:** Это решение требует ручного вмешательства на каждой встрече (копипаст ссылки с токеном в Fathom), что убивает идею автоматизации. **Не рекомендуется**, но технически валидирует возможность прохода через регистрацию.

### **Стратегия В: "Пост-аналитическое обогащение данных" (Рекомендуемое решение)**

**Концепция:** Отключить регистрацию Zoom (чтобы пустить Fathom), но восстановить потерянные email-адреса, сопоставляя участников встречи с приглашениями в календаре.

**Техническая реализация:**

1. **Zoom:** Отключить Require Registration. Включить Waiting Room (Fathom рекомендует отключить, но это компромисс безопасности; бота придется пускать вручную).  
2. **Календарь:** Все участники должны быть приглашены через Google/Outlook Calendar. В событии календаря есть связь Name <-> Email.  
3. **Скрипт синхронизации (Post-Meeting):**  
   * После завершения встречи (Webhook meeting.ended), скрипт запрашивает список участников из Zoom (GET /past_meetings/{id}/participants).  
   * Скрипт получает список приглашенных из Google Calendar API для этого временного слота.  
   * **Алгоритм Fuzzy Matching:** Скрипт сопоставляет user_name из Zoom (например, "Ivan Petrov") с именами в календаре, чтобы восстановить email (ivan@company.com).  
   * Обогащенные данные отправляются в CRM.

**Преимущества:**

* Fathom работает стабильно (нет редиректа на регистрацию).  
* Данные восстанавливаются с высокой долей вероятности (для корпоративных встреч имена обычно совпадают).

---

## **7. Детальный анализ API и кодов ошибок для команды разработки**

Для технической команды проекта P⁎ приводим спецификацию ожидаемых ошибок и поведения API, подтверждающую выводы отчета.

### **7.1. Коды ошибок при попытке регистрации бота**

При попытке добавить регистрацию к встрече, где она не включена, или наоборот, API возвращает специфические коды:

* **Code 300:** "Registration has not been enabled for this meeting". Это подтверждает, что нельзя получить tk-токен для встречи без принудительной регистрации.19  
* **Code 403 / 405:** Ошибки доступа, возникающие при попытке получить данные участников "живой" встречи без соответствующих прав (Scope) OAuth приложения.20

### **7.2. Особенности поля join_url**

В документации Zoom четко разграничены типы ссылок:

| Тип ссылки | Формат | Доступность для Fathom |
| :---- | :---- | :---- |
| **Generic Join URL** | zoom.us/j/{id} | **Доступна** (если нет регистрации) |
| **Registrant Join URL** | zoom.us/w/{id}?tk={token} | **Недоступна** (Fathom не умеет извлекать токен) |
| **Web Client URL** | zoom.us/wc/{id}/join | Используется ботами, но блокируется CAPTCHA |

Исследование 7 подтверждает, что получить join_url с токеном можно *только* через API вызов создания регистранта. Не существует способа "сконструировать" его вручную, зная только email.

---

## **8. Итоговое заключение и рекомендации**

Проведенный анализ подтверждает высокую техническую обоснованность проблем, беспокоящих клиента ꆜ. Конфликт между Fathom и настройками безопасности Zoom носит системный характер и не может быть разрешен простой сменой конфигураций ("галочек") в настройках аккаунта.

**Ключевые выводы:**

1. **Fathom несовместим с Zoom Registration:** Инструмент технически неспособен преодолеть редирект на веб-форму регистрации и получить токен доступа tk.  
2. **Потеря данных неизбежна при стандартном подходе:** Отключение регистрации для допуска бота приводит к анонимизации участников в отчетах Zoom (отсутствие email).  
3. **Аутентификация блокирует ботов:** Настройка "Authenticated Users Only" полностью отсекает возможность использования внешних ботов-партисипантов.

**Рекомендуемый план действий для проекта P⁎:**

Вариант 1 (Минимальные затраты / "Strategy C"):  
Отказаться от нативной регистрации Zoom. Перенести сбор лидов на внешний лендинг, после чего выдавать открытую ссылку. Использовать скрипт пост-обработки для сопоставления имен участников с базой регистраций. Это позволит сохранить Fathom и получить данные, пожертвовав частью безопасности ссылки.  
Вариант 2 (Максимальная надежность / "Platform Shift"):  
Если бюджет позволяет, рассмотреть переход на разработку собственного бота на базе Recall.ai. Это снимет все ограничения: бот сможет регистрироваться, проходить аутентификацию и гарантированно записывать встречи, сохраняя при этом жесткие настройки безопасности Zoom. Это инвестиция в инфраструктуру, которая устранит зависимость от ограничений потребительских приложений вроде Fathom.  
Вариант 3 (Компромисс):  
Использовать нативный Zoom AI Companion для саммаризации (он игнорирует ограничения входа), а данные собирать через нативную регистрацию Zoom. Это требует отказа от Fathom, но является самым стабильным и безопасным решением в рамках экосистемы Zoom.  
Выбор конкретной стратегии зависит от того, что для клиента ꆜ является приоритетом: привычный интерфейс Fathom, строгость безопасности Zoom или бюджет на разработку кастомных интеграций.

---

### **Приложение: Таблица совместимости функций**

| Функция Zoom | Совместимость с Fathom | Влияние на сбор данных (Email) | Техническая причина сбоя |
| :---- | :---- | :---- | :---- |
| **Standard Meeting** | ✅ Полная | ⚠️ Частичная (только если юзер залогинен) | Нет. |
| **Require Registration** | ❌ Не работает | ✅ Полная (все email проверены) | Редирект на форму, отсутствие tk токена у бота.1 |
| **Auth. Users Only** | ❌ Не работает | ✅ Полная | Бот не имеет учетной записи Zoom (Guest).10 |
| **Waiting Room** | ⚠️ Частичная | Не влияет | Бот может "застрять", если хост не пустит его вручную.21 |

Для успешной реализации проекта P⁎ клиенту необходимо выбрать один из предложенных путей обхода, так как текущая конфигурация "Fathom + Registration" является технически неработоспособной.

#### **Works cited**

1. Adding Fathom to your Current Call - Fathom Help Center, accessed November 28, 2025, [https://help.fathom.video/en/articles/1977857](https://help.fathom.video/en/articles/1977857)  
2. Supported Zoom Call Types - Fathom Help Center, accessed November 28, 2025, [https://help.fathom.video/en/articles/2462209](https://help.fathom.video/en/articles/2462209)  
3. How to Track Meeting Participants' Emails Without Enabling "Required Registration" Using Zoom API, accessed November 28, 2025, [https://devforum.zoom.us/t/how-to-track-meeting-participants-emails-without-enabling-required-registration-using-zoom-api/135475](https://devforum.zoom.us/t/how-to-track-meeting-participants-emails-without-enabling-required-registration-using-zoom-api/135475)  
4. Using Fathom with Google Meet, accessed November 28, 2025, [https://help.fathom.video/en/articles/449472](https://help.fathom.video/en/articles/449472)  
5. Solved: Re: Block A.I. Tools - Zoom Community, accessed November 28, 2025, [https://community.zoom.com/t5/Zoom-AI-Companion/Block-A-I-Tools/m-p/163684](https://community.zoom.com/t5/Zoom-AI-Companion/Block-A-I-Tools/m-p/163684)  
6. Solved: Stopping users with Otter.ai from joining meeting - Zoom Community, accessed November 28, 2025, [https://community.zoom.com/t5/Zoom-Meetings/Stopping-users-with-Otter-ai-from-joining-meeting/m-p/106298](https://community.zoom.com/t5/Zoom-Meetings/Stopping-users-with-Otter-ai-from-joining-meeting/m-p/106298)  
7. Get Join_Url with Registration Token from API Call "Add a meeting registrant", accessed November 28, 2025, [https://devforum.zoom.us/t/get-join-url-with-registration-token-from-api-call-add-a-meeting-registrant/79979](https://devforum.zoom.us/t/get-join-url-with-registration-token-from-api-call-add-a-meeting-registrant/79979)  
8. I am able to join a meeting that requires registration without registering - API and Webhooks, accessed November 28, 2025, [https://devforum.zoom.us/t/i-am-able-to-join-a-meeting-that-requires-registration-without-registering/23671](https://devforum.zoom.us/t/i-am-able-to-join-a-meeting-that-requires-registration-without-registering/23671)  
9. Add meeting registrant returns 200 but blank response and no registrant is added - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/add-meeting-registrant-returns-200-but-blank-response-and-no-registrant-is-added/53012](https://devforum.zoom.us/t/add-meeting-registrant-returns-200-but-blank-response-and-no-registrant-is-added/53012)  
10. Zoom @ Berkeley Lab - FAQ, accessed November 28, 2025, [https://zoom.lbl.gov/faq](https://zoom.lbl.gov/faq)  
11. Zoom Signed-in Bots - Getting Started with Recall.ai, accessed November 28, 2025, [https://docs.recall.ai/docs/zoom-signed-in-bots](https://docs.recall.ai/docs/zoom-signed-in-bots)  
12. Getting email address for unregistered webinar participants - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/getting-email-address-for-unregistered-webinar-participants/76453](https://devforum.zoom.us/t/getting-email-address-for-unregistered-webinar-participants/76453)  
13. Webhook Partcipant joined event payload contains null value for participant id, accessed November 28, 2025, [https://devforum.zoom.us/t/webhook-partcipant-joined-event-payload-contains-null-value-for-participant-id/5184](https://devforum.zoom.us/t/webhook-partcipant-joined-event-payload-contains-null-value-for-participant-id/5184)  
14. Passing email in webinar join URL - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/passing-email-in-webinar-join-url/24532](https://devforum.zoom.us/t/passing-email-in-webinar-join-url/24532)  
15. Force username when entering meeting using browser Zoom app - Page 3 - Web, accessed November 28, 2025, [https://devforum.zoom.us/t/force-username-when-entering-meeting-using-browser-zoom-app/1102?page=3](https://devforum.zoom.us/t/force-username-when-entering-meeting-using-browser-zoom-app/1102?page=3)  
16. Zoom Webinars & Registration-Required Meetings - Getting Started with Recall.ai, accessed November 28, 2025, [https://docs.recall.ai/docs/zoom-webinars](https://docs.recall.ai/docs/zoom-webinars)  
17. Step 2: Create your first Zoom bot, accessed November 28, 2025, [https://docs.recall.ai/v1.10/docs/step-2-create-your-first-zoom-bot](https://docs.recall.ai/v1.10/docs/step-2-create-your-first-zoom-bot)  
18. Recall.ai Pricing, accessed November 28, 2025, [https://www.recall.ai/pricing](https://www.recall.ai/pricing)  
19. Registration has not been enabled for this meeting - Page 2 - API and Webhooks, accessed November 28, 2025, [https://devforum.zoom.us/t/registration-has-not-been-enabled-for-this-meeting/17226?page=2](https://devforum.zoom.us/t/registration-has-not-been-enabled-for-this-meeting/17226?page=2)  
20. REST API - Add a webinar registrant - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/rest-api-add-a-webinar-registrant/88898](https://devforum.zoom.us/t/rest-api-add-a-webinar-registrant/88898)  
21. Fathom AI can't join my meetings : r/Zoom - Reddit, accessed November 28, 2025, [https://www.reddit.com/r/Zoom/comments/1m83h7w/fathom_ai_cant_join_my_meetings/](https://www.reddit.com/r/Zoom/comments/1m83h7w/fathom_ai_cant_join_my_meetings/)

# 11. Что беспокоит `ꆜ` (анализ №1, выполнен Gemini Deep Research)
https://gemini.google.com/share/6701f4f585d9

## **1. Введение: Технологический дуализм в операционных процессах EdTech**

В современной экосистеме образовательного бизнеса (EdTech) и коучинга наблюдается фундаментальное противоречие между двумя критически важными операционными потоками: строгой атрибуцией пользователей для маркетинговой аналитики и автоматизацией документирования контента с помощью искусственного интеллекта. Рассматриваемый кейс компании ꆜ является хрестоматийным примером этого конфликта, где внедрение протоколов безопасности на уровне транспортного слоя видеоконференцсвязи (Zoom) непреднамеренно блокирует работу вспомогательных AI-сервисов (Fathom), создавая угрозу для целостности бизнес-данных.

Актуальность данной проблемы обусловлена не локальной ошибкой конфигурации, а глубинным архитектурным расхождением между моделями безопасности Zoom ("Gatekeeper Authentication") и моделями доступа современных AI-ботов ("Guest Participant Injection"). Для компании ꆜ, чей бизнес-модель строится на членстве и отслеживании вовлеченности ("tracking member engagement"), потеря любого из этих компонентов — будь то email-адреса участников для CRM или транскрипты встреч для контроля качества — несет прямые финансовые риски. В данном отчете проводится исчерпывающая деконструкция выявленных проблем, анализ их технической обоснованности и разработка многоуровневой стратегии решения, основанной на возможностях Zoom Developer Platform.

### **1.1. Профиль субъекта и контекст задачи**

Компания ꆜ представляет собой зрелый бизнес в сфере коучинга для владельцев торговых предприятий (сантехника, электрика, строительство), оперирующий сотнями активных участников. Анализ метаданных профиля на Upwork показывает высокую техническую зрелость заказчика: наличие проектов по интеграции Wix Velo, работе с GPT-моделями и сложной логике фильтрации контента указывает на существование развитой IT-инфраструктуры.

Задача, поставленная перед разработчиком, заключается не просто в "починке" настройки, а в разрешении логического парадокса:

1. **Требование А:** Сохранить механизм сбора PII (Personally Identifiable Information), в частности email-адресов, который в текущей архитектуре Zoom жестко привязан к функции "Meeting Registration".  
2. **Требование Б:** Обеспечить бесперебойную работу AI-ассистента Fathom, который архитектурно несовместим с механизмом регистрации Zoom.

Этот конфликт требует выхода за рамки стандартного администрирования Zoom и погружения в программные интерфейсы (API), вебхуки и альтернативные методы идентификации пользователей.

---

## **2. Деконструкция проблематики и валидация ограничений**

Для выработки валидного архитектурного решения необходимо детально проанализировать каждую из проблем, заявленных клиентом (ꆜ), и подтвердить их техническую обоснованность, опираясь на документацию платформ и эмпирические данные сообщества разработчиков.

### **2.1. Проблема №1: Блокировка AI-ассистента Fathom при включенной регистрации**

Клиент утверждает: *"Our AI notetaker tool (Fathom) is blocked from joining the meeting, even when added as an alternative host or invited attendee."*

#### **2.1.1. Технический анализ механизма блокировки**

Механизм "Zoom Meeting Registration" (параметр approval_type: 0 или 1 в объекте settings API) фундаментально меняет протокол присоединения к конференции. В стандартном режиме (без регистрации) для входа достаточно meetingId и password. Ссылка на встречу ведет непосредственно к запуску протокола zoommtg:// или веб-клиента.

При активации регистрации Zoom создает промежуточный шлюз (Gatekeeper). Ссылка вида https://zoom.us/meeting/register/... ведет на веб-форму. Только после успешной отправки формы сервер Zoom генерирует уникальный join_url, содержащий токен tk (token). Этот токен криптографически связывает сессию подключения с конкретной записью в базе данных регистрантов.

Анатомия отказа в обслуживании бота:  
AI-ассистент Fathom (как и большинство аналогичных "bot-based" решений, таких как Otter.ai или Fireflies) технически представляет собой виртуального участника. Он не является плагином, установленным на стороне клиента, а запускается как отдельная сущность на серверах провайдера.

1. **Отсутствие браузерного контекста:** Бот Fathom получает ссылку на встречу из календаря пользователя. Если это ссылка на регистрацию, бот, не обладая полноценным эвристическим движком для заполнения веб-форм (Headless Browser с логикой обхода CAPTCHA и валидации полей), не может пройти этап заполнения данных.  
2. **Отсутствие токена tk:** Пытаясь присоединиться к встрече по базовому meetingId без уникального токена tk, бот получает отказ от API Zoom с кодом ошибки, указывающим на необходимость регистрации.1  
3. **Неэффективность статуса "Alternative Host":** Клиент пытался добавить бота как альтернативного хоста. Это действие обречено на неудачу, так как статус "Alternative Host" требует, чтобы участник был авторизован под учетной записью Zoom (Licensed User), связанной с указанным email. Бот Fathom — это программный скрипт, не имеющий лицензированного аккаунта Zoom и не проходящий процедуру OAuth-авторизации как пользователь перед входом в медиа-канал.

#### **2.1.2. Валидация через источники**

Анализ базы знаний Fathom и форумов поддержки подтверждает абсолютную корректность наблюдения клиента. Официальная документация Fathom в разделе "Unsupported Calls" эксплицитно заявляет: *"Fathom does not currently support... meetings that require registration"*.2 Это жесткое ограничение (hard constraint) текущей версии продукта, связанное с архитектурой их бота. Более того, попытки обойти это через "Add to Meeting" в десктопном приложении также блокируются, если встреча требует регистрации.3

Таким образом, проблема является не следствием ошибки конфигурации на стороне ꆜ, а **системной несовместимостью** выбранных инструментов.

### **2.2. Проблема №2: Потеря атрибуции данных (Email Collection) при отключении регистрации**

Клиент утверждает: *"Disabling registration allows Fathom to join but then we lose email collection, which we must have for reporting."*

#### **2.2.1. Эволюция приватности Zoom API (Post-2022 Era)**

До 2020-2021 годов Zoom API позволял получать достаточно подробную информацию об участниках встреч. Однако, в ответ на критику касательно приватности (феномен "Zoom-bombing" и утечки данных), платформа радикально ужесточила политики. С 1 марта 2022 года Zoom внедрил изменения, скрывающие email-адреса пользователей, помеченных как "гости" (Guest Users), из всех отчетов и API-ответов.4

#### **2.2.2. Матрица доступности данных**

Для понимания глубины проблемы необходимо рассмотреть, как Zoom классифицирует участников и какие данные отдает:

| Тип входа участника | Статус регистрации | Наличие Email в API (user_email) | Причина / Механизм |
| :---- | :---- | :---- | :---- |
| **Через форму регистрации** | **Включена** | **Присутствует** | Пользователь явно передал PII через форму, создав связь registrant_id <-> email. API возвращает эти данные, так как есть согласие на обработку. 6 |
| **Гостевой вход (Guest)** | **Выключена** | **Скрыт / Пуст** | Если пользователь входит по прямой ссылке без авторизации в клиенте Zoom, он анонимен для системы. Поле email возвращается пустым строковым значением или маскируется. 7 |
| **Авторизованный вход (External)** | **Выключена** | **Скрыт (часто)** | Даже если пользователь залогинен в свой Zoom-аккаунт, но этот аккаунт не принадлежит домену организации хоста (ꆜ), Zoom часто скрывает email в целях защиты приватности, если не настроены специфические доверительные отношения. 8 |

#### **2.2.3. Влияние на бизнес-логику ꆜ**

Для коучинговой компании критически важно знать, *кто именно* присутствовал на занятии. Если регистрация отключена, в отчете API GET /past_meetings/{meetingId}/participants они увидят список имен (например, "Alex", "iPhone User", "Мария Иванова").

* Имена не уникальны.  
* Имена могут быть изменены пользователем произвольно.  
* Отсутствует уникальный идентификатор (Email), позволяющий связать участника с записью в CRM (Salesforce, HubSpot, Wix Database).

Следовательно, отключение регистрации разрушает аналитический контур компании. Проблема **валидна и критична**.

### **2.3. Проблема №3: Ограниченность стандартных методов аутентификации**

Существует гипотеза, что вместо "Регистрации" можно использовать "Требование аутентификации" (Require Authentication to Join).

#### **2.3.1. Анализ "Authentication Profiles"**

Zoom позволяет настроить профили безопасности, требующие, чтобы пользователь был залогинен в Zoom.

* *Плюс:* Это гарантирует, что userId участника стабилен.  
* *Минус 1:* Это не гарантирует передачу Email хосту, если пользователь из другой организации (зависит от настроек приватности профиля).  
* *Минус 2 (Фатальный):* AI-бот Fathom не имеет учетной записи Zoom. Если включить требование аутентификации, бот будет отсечен на этапе входа, так как не сможет предоставить валидный OAuth-токен или сессию.9

Существует механизм "Authentication Exceptions" (Исключения аутентификации), позволяющий добавить конкретных пользователей (по email/name) в белый список, отправляя им уникальную ссылку для входа.11 Однако:

* Email-адреса ботов Fathom динамически меняются или скрыты за инфраструктурой провайдера.  
* В документации Fathom нет упоминания о поддержке механизма "Authentication Exceptions" через предоставление статического email для белого списка.  
* Более того, добавление исключений требует ручной работы или сложной автоматизации для *каждой* встречи, что плохо масштабируется.

---

## **3. Архитектурный анализ экосистемы и технические ограничения**

Прежде чем переходить к решениям, необходимо систематизировать технические ограничения, накладываемые инфраструктурой Zoom и Fathom. Понимание этих границ позволит отсечь неработоспособные гипотезы.

### **3.1. Ограничения Zoom Meeting API и Webhooks**

API Zoom является мощным, но жестко регламентированным инструментом.

1. **Webhooks (participant_joined):** Этот вебхук срабатывает в реальном времени при входе участника. Однако полезная нагрузка (payload) строго следует правилам приватности. Если пользователь "Гость", поле email в объекте participant будет отсутствовать, даже если мы передадим его в URL-параметрах (об этом ниже).  
2. **URL Parameters (uname, confno):** Ранее существовала практика передачи имени пользователя через параметр uname в протоколе zoommtg://. Исследования показывают, что в версиях клиента Zoom 5.x и выше поддержка этого параметра стала нестабильной или была отключена для повышения безопасности, чтобы предотвратить спуфинг (подмену имени).12 Это означает, что мы не можем просто сгенерировать ссылку zoom.us/j/123?uname=ClientEmail и ожидать, что Zoom отобразит email вместо имени.

### **3.2. Специфика работы Fathom Bot**

Fathom, как и другие AI-notetakers, работает по принципу "Participant Injection".

* **Trigger:** Бот мониторит календарь пользователя (Google Calendar / Outlook).  
* **Action:** При наступлении времени встречи бот ищет ссылку на Zoom.  
* **Injection:** Бот запускает виртуальную машину (обычно на базе Linux с эмуляцией аудио/видео драйверов), которая стучится в конференцию как обычный участник.  
* **Identity:** Бот идентифицирует себя как "Fathom Notetaker" (имя настраивается 14), но не использует стандартный логин/пароль.

Ключевой инсайт из документации Fathom: **"Fathom works best when it knows your schedule."**.15 Это означает, что вся логика привязана к календарному событию. Если мы изменим ссылку в календаре на какую-то прокси-ссылку, мы рискуем сломать логику обнаружения встречи ботом.

### **3.3. Различие версий Fathom**

Важно отметить, что Fathom предлагает "Team Edition" с централизованным управлением. Однако даже в корпоративной версии ограничение на встречи с регистрацией сохраняется.2 Это подтверждает, что проблема лежит на уровне взаимодействия "Бот <-> Zoom", а не на уровне тарифного плана.

---

## **4. Комплексные стратегии решения (Solution Architectures)**

На основе проведенного анализа предлагаются три стратегии решения. Они ранжированы по степени сложности внедрения ("Effort") и уровню изменения текущих бизнес-процессов ("Impact").

### **Стратегия А: "Синхронная прокси-регистрация" (Рекомендуемое решение)**

Данная стратегия решает парадокс путем разделения потоков данных. Мы отключаем нативную регистрацию Zoom (удовлетворяя Fathom), но внедряем собственную систему регистрации, которая коррелирует данные в реальном времени.

#### **4.1. Концептуальная схема**

Идея заключается в создании "Промежуточного шлюза" (Middleware), который берет на себя функцию сбора email-адресов, а затем перенаправляет пользователя в "открытую" (для Zoom) конференцию, но с меткой, позволяющей идентифицировать его постфактум.

#### **4.2. Алгоритм реализации**

1. **Конфигурация Zoom:**  
   * В настройках встречи: **Registration Required = OFF**.  
   * **Waiting Room = OFF** (рекомендация Fathom для беспрепятственного входа 17).  
   * **Passcode = ON** (для базовой безопасности).  
2. **Разработка Custom Landing Page (Шлюз):**  
   * Вместо прямой ссылки Zoom, пользователям отправляется ссылка на веб-приложение клиента (например, coaching.com/join/{meeting_id}).  
   * Пользователь попадает на форму ввода: Имя, Email.  
   * Backend Logic: При отправке формы сервер:  
     a) Сохраняет запись в БД: { meeting_id, email, name, ip_address, timestamp, user_agent }.  
     b) Генерирует уникальный ID сессии или "Fingerprint".  
3. **Перенаправление (Redirection) и "Join Flow":**  
   * Сервер перенаправляет пользователя на протокол Zoom.  
   * *Критический нюанс:* Поскольку мы не можем надежно передать email в Zoom, мы должны заставить пользователя войти под **предсказуемым именем**.  
   * Формируется ссылка для веб-клиента или десктоп-клиента. Для веб-клиента можно использовать URL: https://zoom.us/wc/{meeting_id}/join?prefer=1&un={Base64_Encoded_Name}.  
   * Если используется десктоп-клиент, пользователю показывается инструкция: "Пожалуйста, убедитесь, что ваше имя в Zoom — [Имя, которое он ввел]".  
4. **Аналитика и Атрибуция (Reconciliation):**  
   * **Real-time:** Настраивается Zoom Webhook meeting.participant_joined.  
   * Когда участник входит, вебхук присылает JSON с user_name и user_id.  
   * Скрипт-обработчик (Webhook Handler) сравнивает user_name из вебхука с последними записями в БД регистраций для этой встречи.  
   * Используется алгоритм нечеткого поиска (Fuzzy Matching) и временнáя корреляция (Time Window Correlation): если "Ivan Petrov" зарегистрировался в 13:59 и "Ivan Petrov" вошел в Zoom в 14:00, с вероятностью 99% это один и тот же человек.  
   * Email из БД регистраций привязывается к user_id Zoom в CRM.

#### **4.3. Оценка**

* **Плюсы:** Fathom работает идеально (регистрация Zoom выключена). Сбор Email сохраняется (через свой лендинг).  
* **Минусы:** Требует разработки (Frontend + Backend). Вероятность ошибки при совпадении имен (коллизии). Зависимость от того, не сменит ли пользователь имя в процессе входа.

---

### **Стратегия Б: "Асинхронная аналитика" (Cloud Recording Pipeline)**

Если для клиента критична **абсолютная точность** email-адресов (которую дает только нативная регистрация Zoom) и допустима задержка в получении заметок, эта стратегия является наиболее надежной.

#### **4.1. Концептуальная схема**

Мы признаем, что "живой" бот Fathom несовместим с регистрацией. Поэтому мы убираем бота из уравнения в реальном времени, но используем возможности AI для пост-обработки.

#### **4.2. Алгоритм реализации**

1. **Конфигурация Zoom:**  
   * **Registration Required = ON**. (Email собираются штатно средствами Zoom).  
   * **Cloud Recording = Auto ON**. (Zoom сам пишет встречу).  
   * **Fathom Bot = Disabled/Kicked**.  
2. **Интеграционный слой (Automation):**  
   * Используется платформа автоматизации (Make.com / Zapier) или кастомный скрипт.  
   * **Trigger:** Webhook recording.completed (приходит, когда видео готово).  
   * **Action 1:** Скрипт скачивает аудио/видео файл через API Zoom (download_url).  
   * **Action 2:** Скрипт загружает файл в сервис транскрипции.  
     * *Вариант 1 (Fathom Upload):* Проверить текущий статус API Fathom на предмет загрузки файлов. Некоторые источники намекают на наличие Public API, но функционал загрузки часто ограничен Enterprise-планами.  
     * *Вариант 2 (Альтернативы):* Использовать API **OpenAI Whisper** (для транскрипции) + **GPT-4o** (для суммаризации по промптам, аналогичным Fathom). Или использовать API сервисов типа **AssemblyAI** / **Recall.ai** (async processing).  
3. **Доставка отчетов:**  
   * Сгенерированное саммари отправляется в CRM и привязывается к контактам, которые были выгружены из отчета о регистрации Zoom (GET /past_meetings/{id}/participants — здесь email'ы будут доступны, так как регистрация была включена).

#### **4.3. Оценка**

* **Плюсы:** 100% точность сбора Email. Отсутствие "раздражающего" бота в видеочате (многие коучи и клиенты предпочитают отсутствие лишних "слушателей" 18). Высокое качество записи (исходник Zoom лучше, чем стрим бота).  
* **Минусы:** Отсутствие мгновенных "хайлайтов" во время звонка. Задержка получения отчета (время встречи + время процессинга).

---

### **Стратегия В: "Инъекция авторизованного бота" (High-End Developer Solution)**

Если клиенту критически важны **и** нативная регистрация Zoom, **и** присутствие бота в реальном времени, единственным решением является использование специализированной инфраструктуры ботов, умеющей обходить барьер регистрации.

#### **4.1. Концептуальная схема**

Fathom как продукт не умеет регистрироваться. Но существуют платформы "Bot-as-a-Service" (например, **Recall.ai**), которые предоставляют API для запуска ботов, способных проходить аутентификацию.

#### **4.2. Алгоритм реализации**

1. **Замена Fathom на Custom Bot (Recall.ai):**  
   * Клиент отказывается от потребительской версии Fathom в пользу интеграции через Recall.ai API.19  
   * Recall.ai — это инфраструктура, на которой построен сам Fathom и многие его конкуренты.  
2. **Логика "Умного входа":**  
   * Перед началом встречи скрипт клиента (Backend) вызывает Zoom API POST /meetings/{id}/registrants и регистрирует самого бота (создает "фейкового" участника "AI Notetaker" с email bot+meeting123@client.com).  
   * Zoom возвращает уникальный join_url с токеном tk.20  
   * Скрипт передает этот join_url в API Recall.ai.  
   * Бот Recall.ai, получив ссылку с токеном, успешно входит во встречу, так как для Zoom он выглядит как легитимный зарегистрированный пользователь.  
3. **Обработка данных:**  
   * Бот стримит аудио/видео.  
   * Транскрипция и аналитика реализуются через подключение LLM (GPT-4) к потоку данных от Recall.ai.

#### **4.3. Оценка**

* **Плюсы:** Решает задачу бескомпромиссно. Работает нативная регистрация, работает бот.  
* **Минусы:** Высокая стоимость (лицензия Recall.ai + затраты на LLM). Высокая сложность разработки (нужно писать своего "мини-Fathom").

---

## **5. Сравнительный анализ данных в отчетах Zoom (Data Table)**

Для наглядности приведем таблицу, демонстрирующую доступность полей данных в зависимости от выбранной конфигурации. Это критически важно для понимания ограничений Стратегии А.

| Параметр API / Webhook | Native Registration ON | Registration OFF (Guest) | Registration OFF + Custom Gate (Стратегия А) |
| :---- | :---- | :---- | :---- |
| **participant.user_id** | Присутствует (Stable) | Присутствует (Session-based) | Присутствует (Session-based) |
| **participant.user_name** | Как в форме регистрации | Как ввел пользователь | Как ввел пользователь (Валидируется) |
| **participant.email** | **Присутствует** (Verified) | **Скрыт / Пуст** | **Скрыт**, но восстанавливается из БД Шлюза |
| **participant.registrant_id** | Присутствует | Отсутствует | Отсутствует |
| **Fathom Bot Access** | **Blocked** | **Allowed** | **Allowed** |
| **Data Reliability** | High | Low | Medium-High (зависит от логики матчинга) |

---

## **6. Рекомендации по внедрению и План действий**

На основе анализа профиля клиента (технически грамотный бизнес, использующий Wix Velo), я рекомендую **гибридный подход**, основанный на **Стратегии А (Синхронная прокси-регистрация)**, но с интеграцией в их существующую экосистему Wix.

### **6.1. Почему именно это решение?**

1. **Сохранение Fathom:** Клиент уже использует этот инструмент ("Our AI notetaker tool"). Переход на кастомного бота (Стратегия В) или асинхронную схему (Стратегия Б) потребует смены привычек команды, что вызовет сопротивление.  
2. **Интеграция с Wix:** У клиента уже есть опыт работы с Wix Velo (проекты P1, P2). Создание кастомной формы регистрации на Wix Velo — это задача, которая идеально ложится в их существующий стек технологий.  
3. **Гибкость:** Своя форма регистрации позволяет собирать дополнительные данные, которые Zoom Registration API может не поддерживать или поддерживать ограниченно.

### **6.2. Пошаговый план (Implementation Roadmap)**

#### **Фаза 1: Прототипирование (Week 1)**

* Создать тестовую страницу на Wix с формой регистрации.  
* Настроить отправку данных формы в коллекцию Wix Data.  
* Реализовать редирект на тестовую встречу Zoom (без регистрации, но с паролем).  
* Проверить, как Fathom присоединяется к такой встрече (должен успешно войти).

#### **Фаза 2: Разработка логики атрибуции (Week 2)**

* Настроить **Zoom Server-to-Server OAuth App**. Это необходимо для получения вебхуков.  
* Настроить endpoint на Wix (http-functions.js) для приема вебхука meeting.participant_joined.  
* Написать скрипт на Velo (JavaScript), который:  
  1. Получает payload от Zoom.  
  2. Ищет в коллекции Registrations запись, созданную за последние 10-15 минут, где IP_Address совпадает с IP из заголовков запроса (если доступно) или выполняет поиск по user_name (с нормализацией строк: lowercase, trim).  
  3. При нахождении совпадения, обновляет статус участника в базе ("Attended").

#### **Фаза 3: Тестирование и развертывание (Week 3)**

* Провести нагрузочное тестирование с участием реальных пользователей.  
* Проверить граничные случаи: пользователь с одинаковым именем, пользователь вошел с телефона (другой IP, чем при регистрации), переподключение.  
* Инструктаж команды: "Важно просить участников входить под тем именем, под которым они регистрировались".

### **6.3. Резервный план (Mitigation Plan)**

Если точность мэтчинга по имени окажется недостаточной (менее 90%), рекомендуется рассмотреть **Стратегию Б (Cloud Recording)**. Хотя она и лишает "живого" функционала, она гарантирует 100% точность данных, что может быть приоритетнее для маркетинговой отчетности.

---

## **7. Заключение**

Конфликт между Zoom Registration и Fathom Bot является системным и не может быть разрешен простым переключением настроек внутри Zoom. Решение лежит в плоскости архитектурной интеграции: вынос точки регистрации за пределы Zoom (на сторону клиента) позволяет удовлетворить требования Fathom к "открытости" встречи, в то время как программная корреляция данных на бэкенде восстанавливает аналитическую цепочку.

Для компании ꆜ это не просто технический патч, а возможность усилить контроль над данными, консолидировав процесс регистрации на собственной платформе (Wix), что стратегически более выгодно, чем зависимость от закрытой экосистемы регистрации Zoom. Предлагаемое решение полностью соответствует заявленным требованиям: оно обеспечивает работу Fathom и сохраняет сбор email-адресов альтернативным, но надежным способом.

#### **Works cited**

1. Zoom Webinars & Registration-Required Meetings - Getting Started with Recall.ai, accessed November 28, 2025, [https://docs.recall.ai/docs/zoom-webinars](https://docs.recall.ai/docs/zoom-webinars)  
2. Supported Zoom Call Types - Fathom Help Center, accessed November 28, 2025, [https://help.fathom.video/en/articles/2462209](https://help.fathom.video/en/articles/2462209)  
3. Adding Fathom to your Current Call, accessed November 28, 2025, [https://help.fathom.video/en/articles/1977857](https://help.fathom.video/en/articles/1977857)  
4. Not Receiving participant_user_id in Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/not-receiving-participant-user-id-in-webhooks/81568](https://devforum.zoom.us/t/not-receiving-participant-user-id-in-webhooks/81568)  
5. Want user's email address in the meeting participants list - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/want-users-email-address-in-the-meeting-participants-list/79955](https://devforum.zoom.us/t/want-users-email-address-in-the-meeting-participants-list/79955)  
6. Zoom API email address display rules - Zoom Developer Platform, accessed November 28, 2025, [https://developers.zoom.us/changelog/platform/zoom-api-email-address-display-rules/](https://developers.zoom.us/changelog/platform/zoom-api-email-address-display-rules/)  
7. After registering as a participant, the e-mail is omitted from the event webhook that processes entry and exit that occurs when joining a meeting with the participant's join url - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/after-registering-as-a-participant-the-e-mail-is-omitted-from-the-event-webhook-that-processes-entry-and-exit-that-occurs-when-joining-a-meeting-with-the-participants-join-url/39325](https://devforum.zoom.us/t/after-registering-as-a-participant-the-e-mail-is-omitted-from-the-event-webhook-that-processes-entry-and-exit-that-occurs-when-joining-a-meeting-with-the-participants-join-url/39325)  
8. Getting email of non-logged users - Meetings - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/getting-email-of-non-logged-users/80386](https://devforum.zoom.us/t/getting-email-of-non-logged-users/80386)  
9. Strategies to Block AI Bots from Zoom Sessions - Cornell University, accessed November 28, 2025, [https://it.cornell.edu/zoom/zoom-block-ai-bots](https://it.cornell.edu/zoom/zoom-block-ai-bots)  
10. Zoom Settings to Block Note-Taking Bots - CCA Portal - California College of the Arts, accessed November 28, 2025, [https://portal.cca.edu/knowledge-base/general/zoom-settings-to-block-note-taking-bots/](https://portal.cca.edu/knowledge-base/general/zoom-settings-to-block-note-taking-bots/)  
11. Requiring authentication to join a meeting or webinar - Zoom Support, accessed November 28, 2025, [https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0063837](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0063837)  
12. Set display name programmatically - Feature Requests - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/set-display-name-programmatically/53778](https://devforum.zoom.us/t/set-display-name-programmatically/53778)  
13. URL Scheme documentation and invite_links - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/url-scheme-documentation-and-invite-links/96064](https://devforum.zoom.us/t/url-scheme-documentation-and-invite-links/96064)  
14. Navigating the Organization Settings Page - Fathom Help Center, accessed November 28, 2025, [https://help.fathom.video/en/articles/3239681](https://help.fathom.video/en/articles/3239681)  
15. Here! Fathom Quick Start Guide, accessed November 28, 2025, [https://help.fathom.video/en/articles/276608](https://help.fathom.video/en/articles/276608)  
16. AI Notetaker by Fathom - Zoom App Marketplace, accessed November 28, 2025, [https://marketplace.zoom.us/apps/JgSwuY4ZSGim6_OPRZV0Ig](https://marketplace.zoom.us/apps/JgSwuY4ZSGim6_OPRZV0Ig)  
17. Fathom AI can't join my meetings : r/Zoom - Reddit, accessed November 28, 2025, [https://www.reddit.com/r/Zoom/comments/1m83h7w/fathom_ai_cant_join_my_meetings/](https://www.reddit.com/r/Zoom/comments/1m83h7w/fathom_ai_cant_join_my_meetings/)  
18. 10 Fathom AI Alternatives & Competitors [Updated September 2025] - Jamie - Your Personal AI Note Taker, accessed November 28, 2025, [https://www.meetjamie.ai/blog/fathom-ai-note-taker-review](https://www.meetjamie.ai/blog/fathom-ai-note-taker-review)  
19. How to build a Zoom notetaker - Recall.ai, accessed November 28, 2025, [https://www.recall.ai/blog/how-to-build-a-zoom-notetaker](https://www.recall.ai/blog/how-to-build-a-zoom-notetaker)  
20. Zoom registration and registrant join url - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/zoom-registration-and-registrant-join-url/53163](https://devforum.zoom.us/t/zoom-registration-and-registrant-join-url/53163)

# 12.
## 12.1.
`D𐊑⠿` ≔ ⠿~ (Заблуждения `ꆜ` относительно `P⁎`)

## 12.2.
`D𐊑ᵢ` : `D𐊑⠿`

## 12.3.
`Pⰳ(D𐊑ᵢ)` ≔
```
Правдоподобность `D𐊑ᵢ`.
Правдоподобность заблуждения `D𐊑ᵢ` означает оценку того, насколько утверждение `D𐊑ᵢ` действительно является заблуждением `ꆜ`. 
```

# 13. Анализ `D𐊑⠿` (выполнен Gemini Deep Think)
https://gemini.google.com/share/40f96decf114

## 1. Множество выявленных заблуждений `ꆜ` (`D𐊑⠿`)

Анализ описания проекта `P⁎` (`O.md`::§2.3) в контексте технического исследования (`O.md`::§10, §11) и внешней документации позволяет выявить следующие ключевые заблуждения клиента (`ꆜ`) относительно проблемы `P†`.

### 1.1. `D𐊑₁`

`D𐊑₁` ≔

```
Убеждение, что существует возможность разработать автоматизированное решение (вероятно, через Zoom API), которое заставит текущий инструмент Fathom автоматически присоединяться к конференциям с активированной нативной функцией регистрации Zoom («Require Registration»).
```

### 1.2. `D𐊑₂`

`D𐊑₂` ≔

```
Убеждение, что предоставление Fathom административных ролей (например, «Альтернативный организатор» — Alternative Host) или статуса приглашенного участника («invited attendee») должно позволить ему обойти требования регистрации.
```

### 1.3. `D𐊑₃`

`D𐊑₃` ≔

```
Неявное непонимание архитектуры Fathom, при котором он воспринимается как глубоко интегрированный сервис (на уровне сервера), а не как «бот-участник», использующий поверхностную веб-автоматизацию (Web Scraping).
```

### 1.4. `D𐊑₄`

`D𐊑₄` ≔

```
Недооценка сложности реализации альтернативного метода сбора email-адресов («capture attendee emails another way») из-за неосведомленности о строгих ограничениях конфиденциальности Zoom API в отношении гостевых пользователей.
```

## 2. Анализ и оценка заблуждений (`D𐊑⠿`)

### 2.1. Анализ `D𐊑₁` (Автоматизация доступа Fathom к встречам с регистрацией)

#### 2.1.1. Доводы за `Pⰳ(D𐊑₁)`

Это заблуждение, поскольку архитектура Fathom и ограничения его API делают автоматизацию невозможной в рамках существующих инструментов.

1.  **Фундаментальная несовместимость:** Активация регистрации Zoom создает «шлюз» (веб-форма, CAPTCHA), требующий для входа уникальный токен `tk` (`O.md`::§10.3.1). Fathom, будучи ботом на основе веб-автоматизации (`O.md`::§10.2.2), не может автоматически пройти этот барьер.
2.  **Подтверждение производителя:** Документация Fathom эксплицитно заявляет о несовместимости с встречами, требующими регистрации [1].
3.  **Проблема «последней мили» API:** Zoom API позволяет программно зарегистрировать участника через `POST /meetings/{meetingId}/registrants` [2] и получить `join_url` с токеном `tk`. Однако не существует способа *автоматически* передать этот уникальный URL боту Fathom перед встречей. Публичный API Fathom ориентирован на извлечение данных *после* встречи [3], а не на управление подключением бота. Fathom извлекает стандартные ссылки из календаря.
4.  **Отсутствие автоматизации:** Единственный способ использовать ссылку с токеном — ручное вмешательство в момент начала встречи (`O.md`::§10.6, Стратегия Б), что не является автоматизированным решением.

#### 2.1.2. Доводы против `Pⰳ(D𐊑₁)`

1.  **Рекомендация Zoom Support:** Клиент опирается на информацию от поддержки Zoom, которая указала на «Zoom Meeting API as a possible workaround» (`O.md`::§2.3). Это могло создать ложное впечатление, что API предлагает прямое решение для интеграции Fathom, тогда как речь идет о построении альтернативных архитектур.

#### 2.1.3. Вердикт

Ожидание, что разработчик может с помощью API преодолеть ограничения закрытой системы Fathom для автоматизации входа в зарегистрированные встречи, является заблуждением. Это технически невозможно из-за отсутствия механизма передачи уникального URL боту.

**Оценка `Pⰳ(D𐊑₁)`: 95/100**

### 2.2. Анализ `D𐊑₂` (Роли доступа как способ обхода безопасности)

#### 2.2.1. Доводы за `Pⰳ(D𐊑₂)`

Удивление клиента («even when», `O.md`::§2.3) подтверждает это заблуждение, основанное на неверном понимании модели аутентификации Zoom.

1.  **Требования к «Alternative Host»:** Чтобы воспользоваться правами альтернативного организатора, участник должен быть аутентифицирован (войти в свою учетную запись Zoom) и, как правило, иметь соответствующую лицензию [4] (`O.md`::§11.2.1.1).
2.  **Природа бота Fathom:** Бот Fathom — это автоматизированный скрипт, который присоединяется как анонимный гость. У него нет учетной записи Zoom, и он не проходит процедуру аутентификации (`O.md`::§10.3.3). Он технически не способен принять эту роль.
3.  **Статус приглашенного:** Приглашение через календарь лишь помогает Fathom обнаружить ссылку, но не отменяет требования безопасности самой встречи.

#### 2.2.2. Доводы против `Pⰳ(D𐊑₂)`

1.  **Интуитивная логика:** С точки зрения пользователя логично предположить, что назначение роли «организатора» должно предоставлять полный доступ. Клиент применил ментальную модель управления человеческими участниками к боту.

#### 2.2.3. Вердикт

Это абсолютное техническое заблуждение. Ожидания клиента фундаментально противоречат требованиям аутентификации платформы Zoom для активации административных ролей.

**Оценка `Pⰳ(D𐊑₂)`: 100/100**

### 2.3. Анализ `D𐊑₃` (Восприятие архитектуры Fathom)

#### 2.3.1. Доводы за `Pⰳ(D𐊑₃)`

Это фундаментальное непонимание лежит в основе заблуждений `D𐊑₁` и `D𐊑₂`.

1.  **Реальная архитектура:** Fathom использует поверхностную интеграцию — Web Scraping через headless-браузер (`O.md`::§10.2.2). Он взаимодействует с пользовательским интерфейсом (UI) Zoom, а не с его серверной инфраструктурой.
2.  **Источник ограничений:** Все проблемы клиента проистекают из этой архитектуры. Зависимость от UI делает бота уязвимым к любым барьерам в процессе входа (регистрация, CAPTCHA). Глубоко интегрированные решения (например, на базе Recall.ai) не имеют этих ограничений (`O.md`::§10.5).
3.  **Нереалистичные ожидания:** Ожидание, что API или изменение ролей может решить проблему, предполагает, что Fathom — это управляемая часть экосистемы, а не внешний агент, эмулирующий пользователя.

#### 2.3.2. Доводы против `Pⰳ(D𐊑₃)`

1.  **Опыт интеграции клиента:** Клиент реализовывал проект `P3⁎` (интеграция Fathom, GPT и Zapier, `O.md`::§6.3). Однако клиент может не различать уровни интеграции: доступ к данным *после* встречи (API) и механизм присоединения бота *к* встрече (Bot Join Mechanism).

#### 2.3.3. Вердикт

Критически важным является непонимание того, что механизм подключения Fathom основан на хрупком скрейпинге UI. Это непонимание является ключевым заблуждением, которое привело к нереалистичным ожиданиям относительно путей решения проблемы.

**Оценка `Pⰳ(D𐊑₃)`: 80/100**

### 2.4. Анализ `D𐊑₄` (Сложность альтернативного сбора email)

#### 2.4.1. Доводы за `Pⰳ(D𐊑₄)`

Клиент предлагает «capture attendee emails another way», вероятно, предполагая, что эти данные легко доступны через API, если регистрация отключена.

1.  **Политика конфиденциальности Zoom API:** Zoom активно скрывает персональные данные (PII) гостевых пользователей. Если регистрация отключена, Zoom API и вебхуки возвращают пустое значение для поля `user_email` (`O.md`::§10.4.1). Это подтверждается правилами отображения email-адресов Zoom API [5].
2.  **Сложность обходных путей:** Прямое извлечение email через API невозможно. «Другой способ» требует построения сложной инфраструктуры, например, «Синхронной прокси-регистрации» (`O.md`::§11.4, Стратегия А). Это включает разработку внешнего шлюза, корреляцию данных и алгоритмы нечеткого сопоставления (Fuzzy Matching), а не просто вызов API.

#### 2.4.2. Доводы против `Pⰳ(D𐊑₄)`

1.  **Техническая зрелость клиента:** Клиент обладает высокой технической компетенцией (`O.md`::§11.1.1) и понимает необходимость кастомной разработки, раз он ищет разработчика.

#### 2.4.3. Вердикт

Весьма вероятно, что клиент не осведомлен о специфических и строгих ограничениях Zoom API в отношении email-адресов гостей. Он может полагать, что задача сводится к написанию правильных запросов к API, тогда как на самом деле это требует построения целой архитектуры для обхода ограничений платформы.

**Оценка `Pⰳ(D𐊑₄)`: 70/100**

# 14. Анализ `D𐊑⠿` (выполнен Gemini Deep Research)
https://gemini.google.com/share/77b944f4fb2a

## **1. Введение: Эволюция идентификации в экосистеме видеоконференций**

В современной цифровой среде интеграция видеоконференций в корпоративные бизнес-процессы перестала быть простой задачей обеспечения связи и трансформировалась в сложную архитектурную проблему управления данными. Ключевым требованием для систем управления обучением (LMS), платформ управления взаимоотношениями с клиентами (CRM) и инструментов автоматизированного комплаенса является возможность сквозного отслеживания пользовательской идентичности. Задача заключается в том, чтобы связать действие пользователя на внешней платформе (например, нажатие кнопки «Присоединиться» в личном кабинете) с конкретной сессией в среде Zoom и последующими событиями, регистрируемыми через вебхуки.

Однако архитектура Zoom, исторически ориентированная на конфиденциальность и безопасность, создает существенные барьеры для передачи произвольных метаданных (таких как внешний user_id) через «воздушный зазор» между HTTP-запросом в браузере и запуском нативного десктопного клиента. Ситуация усложняется внедрением сторонних AI-ассистентов, таких как Fathom, которые имеют свои собственные жесткие ограничения по совместимости с механизмами безопасности Zoom.

Данный отчет представляет собой исчерпывающий анализ технических возможностей и ограничений передачи пользовательских идентификаторов (custom_tracking_id) в события вебхука meeting.participant_joined. Анализ базируется на детальном изучении документации Zoom API, обсуждений в сообществе разработчиков, спецификаций интеграции Fathom и возможностей платформы Recall.ai. Мы рассмотрим, почему стандартные методы манипуляции URL не работают, как изменения в политике конфиденциальности Zoom 2022 года разрушили традиционные методы отслеживания по email, и предложим архитектурные паттерны для решения конфликта между необходимостью строгой аутентификации и использованием AI-инструментов.

## **2. Архитектура идентификации Zoom и «Стена конфиденциальности»**

Для разработки надежного решения необходимо глубоко понимать, как Zoom управляет идентичностью участников и какие изменения претерпела эта модель за последние годы. Иллюзия простоты API часто приводит разработчиков к ошибочным архитектурным решениям, основанным на устаревших данных.

### **2.1 Иерархия идентификаторов участников**

В экосистеме Zoom не существует единого «идентификатора», который был бы универсально доступен во всех контекстах. Вместо этого система оперирует триадой идентификаторов, наличие которых зависит от способа входа пользователя во встречу. Понимание этой иерархии критически важно для интерпретации данных, получаемых через вебхуки.1

1. **Глобальный User ID (user_id):** Это уникальный, постоянный идентификатор учетной записи Zoom. Долгое время разработчики полагались на него как на «золотой стандарт» идентификации. Однако, согласно документации и многочисленным отчетам на форумах разработчиков, этот идентификатор присутствует в полезной нагрузке вебхука meeting.participant_joined *только* в том случае, если участник вошел в свой аккаунт Zoom перед присоединением к встрече.3 Для гостевых пользователей, которые составляют значительную часть аудитории внешних вебинаров и клиентских встреч, это поле часто остается пустым или содержит null. Это делает невозможным использование user_id для связывания с внешней базой данных для неавторизованных пользователей.  
2. **Идентификатор участника встречи (id в объекте participant):** Это поле является наиболее проблематичным из-за своей полиморфной природы. В зависимости от контекста, оно может содержать глобальный user_id (если пользователь залогинен), уникальный registrant_id (если использовалась регистрация) или быть пустым для анонимных гостей.5 Разработчики часто ошибочно принимают это поле за стабильный идентификатор, что приводит к сбоям в логике отслеживания, когда один и тот же пользователь входит в систему с разных устройств или в разном статусе авторизации.  
3. **UUID участника (participant_uuid):** Этот идентификатор уникален для конкретного соединения пользователя с конкретной сессией встречи. Он сохраняется, если пользователь отключается и подключается снова в рамках одной сессии.6 Хотя это полезно для склейки сессий (например, для подсчета общего времени присутствия), сам по себе UUID не несет никакой информации о внешней идентичности пользователя. Без механизма предварительного связывания UUID с внешним ID, этот идентификатор остается бесполезной строкой символов для целей CRM-интеграции.

### **2.2 Влияние обновлений конфиденциальности (PII) 2022 года**

Критический перелом в методологии отслеживания произошел в марте 2022 года, когда Zoom внедрил новые правила обработки персональных данных (PII). Ранее разработчики могли использовать поле email в вебхуке participant_joined для сопоставления участника с базой данных клиентов. Логика была простой: если email участника совпадает с email в CRM, значит, это тот самый клиент.

Однако анализ материалов сообщества показывает массовые сбои в работе интеграций после введения новых правил. Разработчики начали сообщать, что поле email возвращает пустую строку ("") для пользователей, классифицированных как «гости».7 Zoom подтвердил, что email отображается только в строго определенных сценариях: если пользователь зарегистрировался на встречу, если он является частью того же корпоративного аккаунта, или если используются специальные настройки исключений аутентификации.6

Это изменение сделало невозможным «наивное» отслеживание. Если LMS отправляет пользователя на встречу по общей ссылке, и пользователь не входит в свой аккаунт Zoom (или использует личный аккаунт вместо корпоративного), Zoom API намеренно скрывает его email от организатора в целях конфиденциальности. Следовательно, архитектура, полагающаяся на парсинг email из вебхуков для внешних пользователей, является фундаментально ненадежной в современных условиях.10

### **2.3 Проблема отсутствия настраиваемых метаданных**

Естественным решением проблемы отсутствия идентификации кажется передача метаданных через URL. В веб-разработке стандартной практикой является добавление GET-параметров (например, ?ref=uid_123), которые затем считываются сервером. Однако анализ поведения нативного клиента Zoom (Zoom Desktop Client) показывает, что эта модель здесь неприменима.

При клике на ссылку zoommtg:// или https://zoom.us/j/..., управление передается операционной системе, которая запускает приложение Zoom. Протокол запуска приложения строго регламентирован и принимает только определенный набор параметров: номер конференции, хешированный пароль, имя пользователя (в некоторых случаях) и токены шифрования.11

Многочисленные эксперименты разработчиков и официальные ответы сотрудников Zoom подтверждают: нативный клиент игнорирует любые нестандартные параметры запроса.13 Если вы добавите &custom_user_id=555 к ссылке присоединения, этот параметр будет просто отброшен на этапе хендшейка между браузером и приложением. Он не сохраняется в сессии встречи и, следовательно, никогда не попадает в полезную нагрузку вебхука participant_joined.

Существует распространенное заблуждение касательно параметра customer_key. В документации Web SDK и некоторых API отчетов этот параметр упоминается, что дает ложную надежду на возможность его использования для тегирования участников. Однако детальный анализ показывает, что для нативного клиента этот параметр не поддерживается при генерации ссылок присоединения.15 Он доступен только при использовании Web SDK (встраивании клиента в браузер), что влечет за собой ухудшение качества связи и пользовательского опыта, о чем будет сказано ниже.

Таким образом, мы приходим к выводу, что прямой «проброс» идентификатора через URL невозможен для стандартного сценария использования Zoom. Это вынуждает нас искать решения на уровне API регистрации.

## **3. Архитектурный паттерн «Тихая регистрация» (Silent Registration)**

Единственным официально поддерживаемым и надежным способом связать внешнего пользователя с участником встречи Zoom является использование механизма регистрации. Поскольку прямой ввод данных пользователем нежелателен (мы хотим автоматического входа), используется паттерн «Тихой регистрации» через REST API.

### **3.1 Механизм работы токенизированных ссылок**

Zoom API предоставляет возможность зарегистрировать участника на встречу программно, используя эндпоинт POST /meetings/{meetingId}/registrants.18 В ответ на этот запрос API возвращает уникальный объект, содержащий поле join_url.

Ключевой особенностью этого join_url является наличие параметра tk (токен).19 Этот токен представляет собой зашифрованный ключ, который уникально идентифицирует конкретную запись регистрации. Ссылка выглядит примерно так:  
https://zoom.us/w/123456789?tk=KpT...&pwd=...  
Когда пользователь переходит по этой ссылке, нативный клиент Zoom считывает параметр tk. В отличие от кастомных параметров, tk является частью протокола Zoom. Клиент передает этот токен на сервер Zoom при подключении. Сервер валидирует токен и автоматически ассоциирует входящего участника с созданной ранее записью регистрации.

### **3.2 Цепочка передачи данных (Data Lineage)**

Реализация этого паттерна позволяет построить неразрывную цепочку данных:

1. **Инициация:** Пользователь в LMS нажимает «Войти».  
2. **Регистрация:** Бэкенд LMS вызывает Zoom API, передавая имя пользователя и (опционально) email. Zoom возвращает уникальный registrant_id и ссылку с токеном tk.  
3. **Сохранение состояния:** Бэкенд LMS сохраняет связь: LMS_User_ID <-> Zoom_Registrant_ID.  
4. **Вход:** Пользователь перенаправляется по ссылке с tk.  
5. **Событие:** При входе пользователя Zoom генерирует вебхук meeting.participant_joined.  
6. **Идентификация:** В payload вебхука поле object.participant.id (или registrant_id) содержит тот самый ID, который был получен на шаге 2.5  
7. **Разрешение:** Бэкенд получает вебхук, извлекает registrant_id, находит соответствующий LMS_User_ID в своей базе и фиксирует присутствие.

Этот метод работает надежно, так как он опирается на внутреннюю логику Zoom. Токен tk переживает разрывы соединения и переподключения, обеспечивая стабильность идентификации.21

### **3.3 Ограничения метода регистрации**

Несмотря на надежность, этот метод имеет свои ограничения. Во-первых, ссылки с tk токеном часто привязываются к устройству или сессии. Если пользователь попытается открыть ссылку на другом устройстве, она может не сработать, если настройки встречи запрещают вход с нескольких устройств для одного регистранта.

Во-вторых, и это наиболее критично для текущей задачи, использование регистрации фундаментально меняет тип встречи. Встреча переходит из статуса «открытой» в статус «требующей регистрации». Это изменение имеет каскадный эффект на совместимость со сторонними приложениями, что подводит нас к главной проблеме интеграции.

## **4. Конфликт интеграции Fathom и дилемма регистрации**

В требованиях задачи указано использование AI-нотейкера Fathom. Анализ документации и материалов поддержки Fathom выявляет критическую несовместимость между паттерном «Тихой регистрации» и текущей архитектурой Fathom.

### **4.1 Блокировка ботов на встречах с регистрацией**

Согласно официальной базе знаний Fathom, сервис **не поддерживает** встречи Zoom, требующие регистрации.22 Это ограничение не является временным багом, а скорее следствием того, как работают потребительские боты-ассистенты.

Fathom подключается к встрече как гостевой участник (бот). Когда встреча требует регистрации, Zoom показывает промежуточную страницу или форму ввода данных (даже если пользователь идет по ссылке с токеном, бот Fathom, не имеющий этого токена, натыкается на стену). Для «Тихой регистрации» каждый участник должен иметь уникальную ссылку. Бот Fathom, присоединяющийся автоматически через календарь или по команде, обычно пытается использовать общую ссылку на встречу.

При попытке входа на встречу с обязательной регистрацией, бот Fathom сталкивается с требованием ввести email/имя или предоставить токен, которого у него нет. В результате он не может попасть в конференцию. Официальная рекомендация поддержки Fathom однозначна: «Отключите регистрацию для ваших встреч Zoom, чтобы использовать Fathom».22

### **4.2 Архитектурный тупик (Deadlock)**

Здесь возникает взаимоисключающая ситуация:

* **Требование А (Бизнес-логика):** Нам нужно отслеживать конкретных внешних пользователей и связывать их с ID в базе данных. Для этого, как доказано в разделе 3, *необходимо* включить регистрацию и использовать уникальные ссылки с tk.  
* **Требование Б (Инструментарий):** Нам нужно использовать Fathom для записи и транскрибации. Для этого, согласно документации, *необходимо* отключить регистрацию.

Одновременное выполнение этих требований в рамках стандартной интеграции Zoom + Fathom технически невозможно. Публичное API Fathom, упомянутое в материалах 24, предоставляет доступ к *результатам* встреч (получение списка встреч, резюме), но не дает инструментов для управления *процессом входа* бота в защищенные встречи. Оно не позволяет «вживить» боту токен регистрации tk или программно пройти процесс регистрации за бота.

Следовательно, для реализации поставленной задачи необходимо либо отказаться от точного отслеживания через API Zoom (перейдя на ручные методы или эвристику), либо сменить инструмент AI-протоколирования на более продвинутый, поддерживающий программное управление входом.

## **5. Решение уровня Enterprise: Инфраструктура Recall.ai**

Анализ рынка инструментов для разработчиков (API-first video tools) выделяет Recall.ai как решение, специально спроектированное для преодоления ограничений потребительских ботов типа Fathom. В отличие от Fathom, который является готовым продуктом (SaaS), Recall.ai представляет собой инфраструктурный API (PaaS), позволяющий создавать собственных ботов для встреч.

### **5.1 Механизм работы Headless-ботов**

Recall.ai позволяет разработчику программно отправить бота на любую встречу Zoom. Ключевое отличие заключается в уровне контроля над параметрами присоединения.

В API Recall.ai метод создания бота (Create Bot) принимает параметр meeting_url. Документация Recall прямо указывает, что платформа **поддерживает** встречи с обязательной регистрацией.19

* **Работа с токенами:** Разработчик может сгенерировать ссылку с токеном tk (используя Zoom API, как описано в разделе 3) специально для бота. Передав эту ссылку в API Recall, разработчик гарантирует, что бот пройдет аутентификацию Zoom как зарегистрированный участник.  
* **Работа без токенов:** В некоторых случаях Recall может автоматически обрабатывать формы регистрации, если ему предоставить соответствующие данные, хотя использование tk ссылок является более надежным методом.

### **5.2 Внедрение метаданных (Custom Metadata Injection)**

Recall.ai решает проблему передачи custom_tracking_id принципиально иным способом. Вместо того чтобы пытаться заставить Zoom передать эти данные, Recall позволяет привязать метаданные к самому объекту бота или сессии записи.25

Когда вы инициализируете бота через API Recall, вы можете передать объект metadata (например, external_user_id, crm_deal_id). Эти данные не отправляются в Zoom, они хранятся в инфраструктуре Recall.

* **Сценарий использования:**  
  1. LMS инициирует встречу.  
  2. LMS вызывает API Recall для отправки бота, передавая user_id организатора или контекст встречи в метаданных.  
  3. Бот присоединяется к встрече, записывает ее.  
  4. По окончании встречи Recall отправляет вебхук на сервер LMS.  
  5. Этот вебхук **содержит** переданные ранее метаданные.

Таким образом, цикл замыкается не через Zoom API, а через API Recall, что обеспечивает 100% сохранение контекста. Более того, Recall предоставляет доступ к событиям в реальном времени (кто говорит, кто присоединился), позволяя строить аналитику на стороне приложения, минуя ограничения вебхуков Zoom.

### **5.3 Экономика и сложность внедрения**

Переход на Recall.ai требует пересмотра бюджета и сроков разработки.

* **Стоимость:** Recall.ai использует модель оплаты за использование (pay-as-you-go), например, $0.70 за час записи.26 Это отличается от условно-бесплатных или тарифных моделей пользовательских приложений. Для стартапов предусмотрены скидки и бесплатные кредиты.27  
* **Разработка:** Это решение требует написания кода. Необходимо реализовать бэкенд для управления ботами, обработки вебхуков и хранения токенов. Это значительно сложнее, чем просто «установить приложение Fathom». Однако, это единственное решение, обеспечивающее промышленный уровень надежности и гибкости.

## **6. Альтернатива: Zoom Web SDK и управление состоянием на клиенте**

Если использование сторонних инфраструктурных решений (Recall) невозможно по бюджетным или иным причинам, существует альтернативный путь, требующий отказа от нативного клиента Zoom в пользу веб-интерфейса.

### **6.1 Технические особенности Web SDK**

Zoom Web SDK позволяет встроить интерфейс видеоконференции непосредственно в веб-страницу вашего приложения (LMS/CRM).29 В этом сценарии пользователь не покидает ваш домен.

* **Управление состоянием:** Поскольку страница с видеоокном находится под вашим полным контролем, вам не нужно передавать user_id в Zoom. Вы уже знаете, кто находится на странице. Вы можете сопоставить событие «пользователь открыл страницу встречи» с его сессией в вашем приложении.  
* **Параметр customer_key:** В функции ZoomMtg.join(), используемой в Web SDK, действительно можно передать customer_key.17 Хотя его отображение в отчетах может варьироваться, основной контроль осуществляется за счет того, что JavaScript-код инициализации встречи генерируется вашим бэкендом динамически для каждого пользователя.

### **6.2 Компромиссы качества и функциональности**

Выбор Web SDK сопряжен с серьезными компромиссами:

* **Качество AV:** Web SDK использует WebAssembly и WebRTC, но исторически обеспечивает худшее качество видео и аудио по сравнению с нативным приложением. Часто отсутствуют продвинутые функции шумоподавления и виртуальных фонов.30  
* **Ограничения Gallery View:** В веб-версии часто ограничено количество одновременно отображаемых видеопотоков.  
* **Мобильные браузеры:** Поддержка мобильных браузеров в Web SDK значительно уступает нативным мобильным приложениям Zoom.

Если для бизнес-задачи критично высокое качество связи (например, для продаж или терапии), Web SDK может оказаться неприемлемым решением, несмотря на удобство отслеживания.

## **7. Глубокий анализ вебхуков Zoom: Структура и безопасность**

Для реализации любого из описанных решений необходимо четкое понимание структуры данных, получаемых от Zoom. Ошибки в парсинге вебхуков являются частой причиной потери данных об участниках.

### **7.1 Анатомия Payload participant_joined**

Типичная структура JSON-пакета для события присоединения выглядит следующим образом 1:

JSON

{  
  "event": "meeting.participant_joined",  
  "payload": {  
    "account_id": "kBd...",  
    "object": {  
      "id": "1234567890", // ID встречи  
      "uuid": "U4...",    // UUID встречи  
      "participant": {  
        "user_id": "16778240", // Глобальный ID (если есть)  
        "user_name": "Иван Иванов",  
        "id": "B07...",  // <--- Критически важное поле (Registrant ID)  
        "join_time": "2023-11-01T10:00:00Z",  
        "email": "",     // Пусто для гостей!  
        "participant_user_id": ""  
      }  
    }  
  }  
}

### **7.2 Полиморфизм поля id**

Поле payload.object.participant.id является контекстно-зависимым.

* **Сценарий А (Авторизованный пользователь):** Поле содержит глобальный Zoom User ID.  
* **Сценарий Б (Гость с регистрацией):** Поле содержит registrant_id, который совпадает с тем, что вернул API при создании регистранта. Это и есть наш «крючок» для отслеживания.  
* **Сценарий В (Простой гость):** Поле может быть пустым или содержать временный идентификатор, бесполезный для долговременного отслеживания.

Логика обработки вебхука на сервере должна учитывать этот полиморфизм. Алгоритм должен сначала проверять наличие id в таблице активных регистраций. Если совпадение найдено — пользователь идентифицирован. Если нет — проверяется user_id (на случай, если сотрудник зашел под корпоративным аккаунтом).

### **7.3 Верификация безопасности (HMAC)**

Крайне важно реализовать проверку подлинности вебхуков. Zoom передает заголовок x-zm-signature, содержащий HMAC-SHA256 хеш тела запроса, подписанный вашим секретным токеном (Secret Token) приложения.2 Игнорирование этой проверки открывает систему для атак типа «спуфинг», когда злоумышленник может отправить поддельный вебхук, сымитировав присутствие пользователя на встрече.

Для приложений, работающих с чувствительными данными (образование, медицина), валидация заголовка x-zm-request-timestamp также обязательна для защиты от атак повторного воспроизведения (replay attacks).

## **8. Детальный обзор обходных путей (Workarounds) и их несостоятельность**

В ходе исследования были рассмотрены и другие потенциальные методы решения задачи, которые часто предлагаются на форумах, но при детальном анализе оказываются несостоятельными.

### **8.1 Использование Tracking Fields (Полей отслеживания)**

Zoom предоставляет функцию «Tracking Fields» 31, которая позволяет добавлять метаданные к самой встрече (например, код отдела или проекта). Эти поля возвращаются в вебхуках и отчетах.

* **Почему это не работает для участников:** Tracking Fields задаются на уровне *встречи*, а не на уровне *участника*. Вы можете пометить встречу как «Проект Х», но вы не можете пометить конкретного Ивана Иванова как «Клиент Y» с помощью этого механизма. Это инструмент для классификации ресурсов, а не людей.

### **8.2 Использование опросов (Polls) и чатов**

Существует теоретическая возможность идентифицировать пользователя, попросив его ответить на уникальный опрос или написать кодовое слово в чат.

* **API Чата:** Zoom API позволяет получать сообщения чата (через вебхуки или архивацию), но сопоставление имени в чате с реальным пользователем остается ненадежным, так как пользователь может изменить свое отображаемое имя в любой момент.32  
* **UX-трение:** Требовать от пользователя ручных действий для подтверждения присутствия — это плохой пользовательский опыт (UX), который приводит к ошибкам и неполным данным.

### **8.3 Манипуляции с «Breakout Rooms»**

Некоторые разработчики пытаются использовать предварительное назначение в сессионные залы (Breakout Rooms) как способ идентификации. Хотя API позволяет назначать участников в комнаты по email, это возвращает нас к проблеме скрытия email для гостевых пользователей и необходимости регистрации, что снова конфликтует с Fathom.

## **9. Стратегические рекомендации по внедрению**

На основе проведенного анализа, мы предлагаем три архитектурные стратегии, ранжированные по сложности реализации и функциональным возможностям.

### **Стратегия 1: «Чистая» интеграция Zoom (без Fathom)**

*Приоритет: Точность отслеживания, Безопасность, Использование нативного клиента.*

Если требование точного отслеживания user_id является доминирующим, а использование именно Fathom не является жестким требованием (или может быть заменено ручной обработкой/другими инструментами):

1. **Включить обязательную регистрацию** для всех встреч.  
2. Реализовать **паттерн «Тихой регистрации»** на бэкенде.  
3. Использовать вебхук meeting.participant_joined и сопоставление по registrant_id.  
4. Отказаться от Fathom в пользу встроенной записи Zoom (Cloud Recording) с последующей обработкой транскрипта через Zoom AI Companion (который становится все более мощным, см. 33) или выгрузкой записи через API для анализа внешними LLM.

### **Стратегия 2: Инфраструктура Recall.ai (Максимальная функциональность)**

*Приоритет: Совместимость требований, Автоматизация, Аналитика.*

Если необходимо и отслеживать пользователей, и получать качественные AI-саммари (аналогичные Fathom), и сохранять нативный опыт Zoom:

1. Интегрировать **Recall.ai API**.  
2. При создании встречи в LMS, генерировать команду для бота Recall.  
3. Передавать custom_user_id в метаданные бота.  
4. Использовать вебхуки Recall для получения статусов участия и готовых аналитических данных.  
   Это наиболее профессиональное и масштабируемое решение, снимающее зависимость от причуд Zoom API.

### **Стратегия 3: Компромиссная (Веб-клиент)**

*Приоритет: Скорость внедрения, Дешевизна.*

Если бюджет на Recall.ai отсутствует, а Fathom не критичен:

1. Использовать **Zoom Web SDK**.  
2. Встраивать встречу в защищенный раздел личного кабинета пользователя.  
3. Фиксировать участие на уровне загрузки страницы и JavaScript-событий SDK.  
4. Мириться с пониженным качеством связи.

## **10. Заключение**

Задача передачи пользовательского идентификатора через цепочку «URL -> Клиент -> Вебхук» в экосистеме Zoom не имеет прямого решения методом "простой подстановки параметров" из-за архитектурных особенностей безопасности нативного клиента. Попытки обойти это через манипуляции с URL обречены на провал.

Единственным легитимным путем для нативного клиента является использование **Registrant ID**, получаемого через API регистрации. Однако этот путь находится в прямом конфликте с текущими возможностями популярных AI-нотейкеров, таких как Fathom, которые требуют открытого доступа к встречам.

Для построения надежной системы корпоративного уровня рекомендуется переход от использования потребительских плагинов к использованию специализированных API-платформ видеоконференцсвязи (Recall.ai, Zoom Video SDK), которые позволяют разработчику полностью контролировать контекст встречи и потоки данных. Это требует больших начальных инвестиций в разработку, но обеспечивает стабильность, недостижимую при попытках связать несовместимые коробочные решения.

### **Справочные таблицы**

**Таблица 1. Сравнение методов передачи ID**

| Метод | Поддержка Native Client | Поддержка Web SDK | Персистентность ID | Совместимость с Fathom | Сложность |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **URL Query Params** | ❌ Нет | ⚠️ Частично | ❌ Нет | ✅ Да | Низкая |
| **Silent Registration** | ✅ Да | ✅ Да | ✅ Высокая (tk token) | ❌ Нет | Средняя |
| **Recall.ai Bot** | ✅ Да (через бота) | ✅ Да | ✅ Высокая (Metadata) | ⚠️ (Замена Fathom) | Высокая |
| **Zoom Tracking Fields** | ❌ Нет (уровень встречи) | ❌ Нет | ❌ Нет | ✅ Да | Низкая |

**Таблица 2. Поля идентификации в вебхуке (Guest User)**

| Поле | Значение (Без регистрации) | Значение (С регистрацией) | Примечание |
| :---- | :---- | :---- | :---- |
| user_id | 16778240 (или пусто) | 16778240 (или пусто) | Глобальный ID аккаунта |
| id (в participant) | Пусто / Временный ID | **registrant_id** | **Основной ключ для трекинга** |
| email | "" (Пустая строка) | user@example.com (редко) | Скрыто по Privacy Policy |
| user_name | "Ivan" (введено юзером) | "Ivan" (из API) | Ненадежно (можно сменить) |

---

*Конец отчета.*

#### **Works cited**

1. Meetings Webhooks - Zoom Developer Platform, accessed November 28, 2025, [https://developers.zoom.us/docs/api/meetings/events/](https://developers.zoom.us/docs/api/meetings/events/)  
2. Using webhooks - Zoom Developer Platform, accessed November 28, 2025, [https://developers.zoom.us/docs/api/webhooks/](https://developers.zoom.us/docs/api/webhooks/)  
3. Participants with an id, but no email, or an email, but no id - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/participants-with-an-id-but-no-email-or-an-email-but-no-id/50521](https://devforum.zoom.us/t/participants-with-an-id-but-no-email-or-an-email-but-no-id/50521)  
4. Tracking guest participants - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/tracking-guest-participants/68746](https://devforum.zoom.us/t/tracking-guest-participants/68746)  
5. Participant Joined Webhook – Mapping user_id to registrant_id - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/participant-joined-webhook-mapping-user-id-to-registrant-id/13006](https://devforum.zoom.us/t/participant-joined-webhook-mapping-user-id-to-registrant-id/13006)  
6. Not Receiving participant_user_id in Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/not-receiving-participant-user-id-in-webhooks/81568](https://devforum.zoom.us/t/not-receiving-participant-user-id-in-webhooks/81568)  
7. Email is empty string for meeting.participant_left and meeting.participant_joined events - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/email-is-empty-string-for-meeting-participant-left-and-meeting-participant-joined-events/79408](https://devforum.zoom.us/t/email-is-empty-string-for-meeting-participant-left-and-meeting-participant-joined-events/79408)  
8. Email passed when participant joins a meeting is now blank since yesterday - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/email-passed-when-participant-joins-a-meeting-is-now-blank-since-yesterday/65066](https://devforum.zoom.us/t/email-passed-when-participant-joins-a-meeting-is-now-blank-since-yesterday/65066)  
9. Using Zoom APIs - Zoom Developer Platform, accessed November 28, 2025, [https://developers.zoom.us/docs/api/using-zoom-apis/](https://developers.zoom.us/docs/api/using-zoom-apis/)  
10. Missing User email and id in Zoom Webhook Notifications, accessed November 28, 2025, [https://community.zoom.com/t5/Zoom-App-Marketplace/Missing-User-email-and-id-in-Zoom-Webhook-Notifications/m-p/171467](https://community.zoom.com/t5/Zoom-App-Marketplace/Missing-User-email-and-id-in-Zoom-Webhook-Notifications/m-p/171467)  
11. Participant Id in Zoom Join URl - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/participant-id-in-zoom-join-url/63685](https://devforum.zoom.us/t/participant-id-in-zoom-join-url/63685)  
12. Webhook payload for meeting.participant_joined event contains empty participant user_name - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/webhook-payload-for-meeting-participant-joined-event-contains-empty-participant-user-name/51001](https://devforum.zoom.us/t/webhook-payload-for-meeting-participant-joined-event-contains-empty-participant-user-name/51001)  
13. Appending Custom Parameter to Zoom Join_URL? - API and Webhooks, accessed November 28, 2025, [https://devforum.zoom.us/t/appending-custom-parameter-to-zoom-join-url/15117](https://devforum.zoom.us/t/appending-custom-parameter-to-zoom-join-url/15117)  
14. Appending Custom Parameter to Zoom Join_URL? continued - API and Webhooks, accessed November 28, 2025, [https://devforum.zoom.us/t/appending-custom-parameter-to-zoom-join-url-continued/34590](https://devforum.zoom.us/t/appending-custom-parameter-to-zoom-join-url-continued/34590)  
15. How to use `customer_key` in meeting participants report? - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/how-to-use-customer-key-in-meeting-participants-report/51344](https://devforum.zoom.us/t/how-to-use-customer-key-in-meeting-participants-report/51344)  
16. How to use `customer_key` in meeting participants report? - #15 by MaxM - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/how-to-use-customer-key-in-meeting-participants-report/51344/15](https://devforum.zoom.us/t/how-to-use-customer-key-in-meeting-participants-report/51344/15)  
17. Add customer_key property to ZoomMtg.join() and webhook notifications - Feature Requests, accessed November 28, 2025, [https://devforum.zoom.us/t/add-customer-key-property-to-zoommtg-join-and-webhook-notifications/56427](https://devforum.zoom.us/t/add-customer-key-property-to-zoommtg-join-and-webhook-notifications/56427)  
18. Zoom Meeting API - Zoom Developer Platform, accessed November 28, 2025, [https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/)  
19. Step 2: Create your first Zoom bot, accessed November 28, 2025, [https://docs.recall.ai/v1.10/docs/step-2-create-your-first-zoom-bot](https://docs.recall.ai/v1.10/docs/step-2-create-your-first-zoom-bot)  
20. Zoom Webinars & Registration-Required Meetings - Getting Started with Recall.ai, accessed November 28, 2025, [https://docs.recall.ai/docs/zoom-webinars](https://docs.recall.ai/docs/zoom-webinars)  
21. Appending Custom Parameter to Zoom Join_URL? continued II - API and Webhooks, accessed November 28, 2025, [https://devforum.zoom.us/t/appending-custom-parameter-to-zoom-join-url-continued-ii/42009](https://devforum.zoom.us/t/appending-custom-parameter-to-zoom-join-url-continued-ii/42009)  
22. Solved: Re: Fathom Does Not Work For Some Of My Meetings - Zoom Community, accessed November 28, 2025, [https://community.zoom.com/t5/Zoom-Meetings/Fathom-Does-Not-Work-For-Some-Of-My-Meetings/m-p/143291](https://community.zoom.com/t5/Zoom-Meetings/Fathom-Does-Not-Work-For-Some-Of-My-Meetings/m-p/143291)  
23. Supported Zoom Call Types - Fathom Help Center, accessed November 28, 2025, [https://help.fathom.video/en/articles/2462209](https://help.fathom.video/en/articles/2462209)  
24. Public API - Fathom Help Center, accessed November 28, 2025, [https://help.fathom.video/en/articles/8368641](https://help.fathom.video/en/articles/8368641)  
25. Receive Call Events, accessed November 28, 2025, [https://docs.recall.ai/v1.10/docs/call-events](https://docs.recall.ai/v1.10/docs/call-events)  
26. Recall.ai Pricing, accessed November 28, 2025, [https://www.recall.ai/pricing](https://www.recall.ai/pricing)  
27. Recall Pricing, accessed November 28, 2025, [https://www.getrecall.ai/pricing](https://www.getrecall.ai/pricing)  
28. Recall - Summarize Anything, Forget Nothing., accessed November 28, 2025, [https://www.getrecall.ai/](https://www.getrecall.ai/)  
29. Zoom Meeting SDK for web, accessed November 28, 2025, [https://developers.zoom.us/docs/meeting-sdk/web/](https://developers.zoom.us/docs/meeting-sdk/web/)  
30. A technical guide to the Zoom Web SDK - Daily.co, accessed November 28, 2025, [https://www.daily.co/blog/zoom-web-sdk-technical-notes/](https://www.daily.co/blog/zoom-web-sdk-technical-notes/)  
31. Managing scheduling tracking fields - Zoom Support, accessed November 28, 2025, [https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067020](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067020)  
32. Participation tracking - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/participation-tracking/97319](https://devforum.zoom.us/t/participation-tracking/97319)  
33. What's New at Zoom, accessed November 28, 2025, [https://www.zoom.com/en/products/whats-new/](https://www.zoom.com/en/products/whats-new/)

# 15.
## 15.1.
`T༄` ≔ `T⁎`

## 15.2.
`Aᚖ⠿` ≔ ⠿~ (Альтернативные `T༄` способы решения выявленных источников беспокойства `ꆜ` (`O.md::§10`, `O.md::§11`))

## 15.3.
`Aᚖᵢ` : `Aᚖ⠿`

# 16. Анализ `Aᚖ⠿` (выполнен Gemini Deep Think)
https://gemini.google.com/share/ab7f91424197

## Aᚖ₁: Внешняя прокси-регистрация (Синхронная прокси-регистрация)

### Суть
Этот подход реализует паттерн, описанный в `O.md`::§11.4 (Стратегия А), разделяя сбор данных и доступ к конференции.
Нативная регистрация в Zoom отключается, что устраняет технический барьер для присоединения Fathom.
Сбор email-адресов переносится на внешний шлюз (Middleware), например, на целевую страницу, разработанную на Wix Velo, с которым клиент уже знаком (`O.md`::§6.1).
Пользователи вводят свои данные на этой странице, после чего перенаправляются на открытую встречу Zoom.
Бэкенд-система сопоставляет данные из базы регистраций шлюза с данными участников, полученными через Zoom Webhooks (например, `meeting.participant_joined`).
Сопоставление использует алгоритмы нечеткого поиска (Fuzzy Matching) по имени (`user_name`) и временную корреляцию входа (`O.md`::§11.4.2).

### Оценка
75/100

### Достоинства
Fathom работает стабильно и в реальном времени, так как для него встреча является открытой.
Решение интегрируется в существующую техническую экосистему клиента (Wix), что упрощает разработку (`O.md`::§11.6.1).
Клиент получает полный контроль над процессом регистрации и может собирать любые необходимые дополнительные данные.
Сохраняется привычный для команды инструмент (Fathom) и его функции реального времени.

### Недостатки
Точность данных не гарантирована на 100% из-за ограничений Fuzzy Matching.
Возможны ошибки при совпадении имен или если пользователь изменит свое имя при входе в Zoom.
Существует риск безопасности: пользователи могут делиться прямой ссылкой на Zoom, минуя шлюз регистрации (`O.md`::§10.6, Стратегия А).
Требуется разработка фронтенда (страница регистрации) и бэкенда (логика сопоставления, обработка вебхуков).
Использование данных, полученных с помощью нечеткого сопоставления, может не соответствовать требованиям законодательства Новой Зеландии о точности персональной информации.
В частности, это может нарушить Принцип 8 Закона о конфиденциальности 2020 года (Privacy Act 2020, Section 24), который гласит: "An agency that holds personal information must not use or disclose that information without taking any steps that are, in the circumstances, reasonable to ensure that the information is accurate, up to date, complete, relevant, and not misleading." («Агентство, хранящее персональную информацию, не должно использовать или раскрывать эту информацию, не предприняв шагов, которые в данных обстоятельствах являются разумными для обеспечения того, чтобы информация была точной, актуальной, полной, релевантной и не вводящей в заблуждение».)
Зависимость от Fuzzy Matching для отслеживания вовлеченности участников может не считаться «разумным шагом» для обеспечения точности, если частота ошибок высока.

## Aᚖ₂: Асинхронная аналитика (Cloud Recording Pipeline)

### Суть
Этот подход признает несовместимость живого бота Fathom с регистрацией Zoom и фокусируется на пост-обработке (`O.md`::§11.4, Стратегия Б).
Нативная регистрация Zoom включается, обеспечивая точный сбор email.
Бот Fathom не присоединяется к встрече в реальном времени.
В настройках Zoom активируется автоматическая запись в облако (Cloud Recording).
После завершения встречи и обработки записи срабатывает вебхук Zoom (`recording.completed`).
Автоматизированный конвейер (скрипт или платформа типа Zapier/Make) скачивает видео/аудио файл через Zoom API.
Затем файл загружается в Fathom (вручную или через API, если доступно) или в альтернативный AI-сервис (например, OpenAI Whisper + GPT) для транскрипции и анализа.

### Оценка
80/100

### Достоинства
Гарантируется 100% точность сбора email через нативную регистрацию Zoom.
Качество записи выше, так как она ведется на стороне сервера Zoom, а не через перехват потока ботом (`O.md`::§11.4.3).
Участники не видят "бота" в списке присутствующих, что может быть предпочтительнее для коучинговых сессий.
Решение надежно и не зависит от ограничений Fathom на вход во встречу.

### Недостатки
Клиент теряет доступ к функциям Fathom в реальном времени (например, создание закладок и выделение моментов во время звонка).
Существует задержка между окончанием встречи и получением результатов анализа (время обработки записи).
Требуется разработка конвейера автоматизации для скачивания и загрузки файлов.
Необходимо проверить возможности API Fathom по программной загрузке внешних записей и соответствующие тарифные планы (`O.md`::§11.4.2).
Возможны дополнительные расходы на облачное хранилище Zoom или API альтернативных AI-сервисов.

## Aᚖ₃: Инфраструктура кастомных ботов (например, Recall.ai)

### Суть
Этот подход предполагает отказ от Fathom как готового продукта (SaaS) в пользу использования инфраструктурной платформы для ботов (PaaS), такой как Recall.ai (`O.md`::§11.4, Стратегия В).
Recall.ai предоставляет API для программного управления ботами, которые спроектированы для обхода ограничений регистрации Zoom (`O.md`::§14.5).
Нативная регистрация Zoom остается включенной.
Бэкенд клиента автоматически регистрирует бота через Zoom API, получая токен `tk`.
Этот токен передается в API Recall.ai при запуске бота.
Бот Recall.ai успешно присоединяется к защищенной встрече как легитимный зарегистрированный участник (`O.md`::§14.5.1).
Транскрипция и AI-анализ реализуются путем интеграции с внешними LLM (например, GPT-4) или использования встроенных возможностей платформы.

### Оценка
90/100

### Достоинства
Решение бескомпромиссно удовлетворяет всем требованиям: точный сбор email (нативная регистрация) и автоматическая работа бота в реальном времени.
Высокая надежность, масштабируемость и гибкость на уровне Enterprise-инфраструктуры.
Снимается зависимость от ограничений потребительских приложений вроде Fathom (`O.md`::§10.6).
Предоставляет расширенные возможности для интеграции метаданных и аналитики (`O.md`::§14.5.2).

### Недостатки
Высокая стоимость внедрения и сложность разработки, так как требуется создать собственное приложение ("мини-Fathom").
Значительные операционные расходы на использование инфраструктуры (например, $0.70 за час записи на Recall.ai) и LLM (`O.md`::§14.5.3).
Требуется полный отказ от привычного интерфейса и экосистемы Fathom и переобучение команды.
Возникает зависимость от нового поставщика инфраструктуры (Recall.ai).

## Aᚖ₄: Использование нативного Zoom AI Companion

### Суть
Этот подход предполагает отказ от Fathom и переход на встроенный инструмент искусственного интеллекта Zoom — AI Companion.
Нативная регистрация Zoom остается включенной для сбора данных участников.
Zoom AI Companion работает на серверном уровне и имеет прямой доступ к медиапотокам; ему не нужно «присоединяться» как участнику (`O.md`::§10.5.2).
Следовательно, настройки регистрации или аутентификации не влияют на его работу.
Организатор использует функции AI Companion для суммаризации встречи и генерации заметок.

### Оценка
85/100

### Достоинства
Это самое стабильное, простое и безопасное решение в рамках экосистемы Zoom.
Интеграция является нативной и не требует разработки сложных обходных путей или интеграций.
Отсутствуют конфликты с любыми настройками безопасности Zoom.
Обычно не требует значительных дополнительных затрат, так как AI Companion часто включен в платные тарифы Zoom.
Обеспечивается 100% точность сбора email-адресов.

### Недостатки
Требуется полный отказ от Fathom и адаптация бизнес-процессов к новому инструменту.
Функциональность, качество суммаризации и доступные интеграции Zoom AI Companion могут отличаться от Fathom (`O.md`::§10.5.2).
Клиент становится зависимым от темпов развития и ограничений AI-функций внутри Zoom.

## Aᚖ₅: Пост-аналитическое обогащение данных (Сопоставление с календарем)

### Суть
Этот подход, описанный в `O.md`::§10.6 (Стратегия В), также предполагает отключение регистрации в Zoom для обеспечения работы Fathom.
Вместо создания внешнего шлюза регистрации (как в Aᚖ₁), метод опирается на существующие данные о приглашенных участниках из внешних систем (например, Google Calendar или Outlook).
Предполагается, что все участники приглашены через эти системы и их email известны заранее.
После завершения встречи скрипт получает список фактических участников из Zoom API (только имена).
Затем скрипт получает список приглашенных из API соответствующего календаря (имена и email).
Алгоритм Fuzzy Matching используется для сопоставления имен из Zoom с именами в календаре, чтобы восстановить email-адреса.

### Оценка
45/100

### Достоинства
Fathom работает бесперебойно в реальном времени.
Не требуется разработка инфраструктуры для предварительной регистрации пользователей (в отличие от Aᚖ₁).
Реализация требует меньше усилий, так как фокусируется только на скрипте постобработки и интеграции с Calendar API.

### Недостатки
Надежность сопоставления данных критически низкая.
Метод не сработает, если имя участника в Zoom значительно отличается от имени в календаре (например, вход под никнеймом или с общего устройства).
Система не сможет идентифицировать участников, которые присоединились к встрече, не будучи явно приглашенными через этот календарь.
Решение плохо масштабируется для больших встреч с частыми коллизиями имен.
Существуют значительные юридические риски, связанные с точностью данных (Privacy Act 2020, Section 24, Principle 8), аналогичные Aᚖ₁, но с более высокой вероятностью ошибок.
Использование данных календаря для отслеживания посещаемости Zoom может нарушить ожидания пользователей относительно конфиденциальности и потребовать явного уведомления (Privacy Act 2020, Section 19, Principle 3).
Также это может рассматриваться как использование информации для цели, отличной от той, для которой она была собрана (Privacy Act 2020, Section 26, Principle 10), если только не будет доказано, что отслеживание посещаемости «напрямую связано» ("directly related") с организацией встречи.

## Aᚖ₆: Ручная инъекция токена (API-Middleware + Ручной шаг)

### Суть
Этот подход сохраняет нативную регистрацию Zoom, но требует ручного вмешательства для подключения Fathom (`O.md`::§10.6, Стратегия Б).
Перед встречей используется скрипт (Middleware), который через Zoom API (`POST /meetings/{id}/registrants`) программно регистрирует бота как участника.
Zoom API возвращает уникальную ссылку для входа (`join_url`), содержащую токен `tk` (`O.md`::§14.3.1).
В момент начала встречи сотрудник клиента должен вручную скопировать эту уникальную ссылку.
Затем он использует функцию "Add to Meeting" в десктопном приложении Fathom и вставляет эту ссылку.
Fathom, используя ссылку с токеном, может обойти требование регистрации и присоединиться к встрече.

### Оценка
20/100

### Достоинства
Сохраняется нативная регистрация Zoom, что гарантирует 100% точность сбора email-адресов участников.
Fathom используется для записи встречи в реальном времени.
Требует минимальной разработки (только скрипт для получения токена).

### Недостатки
Решение полностью уничтожает автоматизацию процесса подключения Fathom.
Требуется ручное вмешательство для каждой отдельной встречи.
Действие необходимо выполнить точно в момент начала встречи, что создает высокие операционные издержки.
Существует высокий риск человеческой ошибки (забыли добавить бота, использовали неверную ссылку, опоздали).
Подход абсолютно не масштабируется для компании с «сотнями активных членов» (`O.md`::§2.3).

## Итоговый вердикт

Анализ альтернативных решений (`Aᚖ⠿`) подтверждает выводы, сделанные в `O.md`::§13: исходный подход клиента (`T༄`), заключающийся в ожидании, что разработчик сможет с помощью Zoom API заставить текущую версию Fathom автоматически присоединяться к встречам с нативной регистрацией, является технически невозможным.
Это связано с фундаментальной несовместимостью архитектуры Fathom (бот-скрейпер) с механизмами безопасности Zoom (токен `tk`) и отсутствием у Fathom API для управления процессом входа (`O.md`::§13.2.1).
Следовательно, для решения проблемы `P†` необходимо использовать одну из жизнеспособных альтернатив `Aᚖᵢ`, отказавшись от `T༄`.

Выбор оптимальной стратегии зависит от критических приоритетов клиента:

### Приоритет на простоте, надежности и экономии
Если главным приоритетом является быстрое, надежное и экономичное решение, наилучшим выбором является **Aᚖ₄ (Zoom AI Companion)**.
Он решает обе задачи (точный сбор email и AI-анализ) без разработки, но требует смены инструмента.

### Приоритет на максимальной функциональности (при наличии бюджета)
Если клиент готов инвестировать в идеальное техническое решение, обеспечивающее и точность данных, и работу AI-бота в реальном времени, следует выбрать **Aᚖ₃ (Recall.ai)**.
Это решение требует значительных вложений в разработку и смены платформы, но обеспечивает максимальную надежность и гибкость на уровне Enterprise.

### Приоритет на сохранении Fathom
Если отказ от Fathom неприемлем, клиенту придется выбирать между точностью данных и функциями реального времени.
1. Если приоритетна точность данных, следует использовать **Aᚖ₂ (Асинхронная аналитика)**. Это надежное решение, но оно предполагает получение заметок с задержкой и отказ от функций реального времени.
2. Если критичны функции реального времени, следует использовать **Aᚖ₁ (Внешняя прокси-регистрация)**. Это решение позволяет сохранить Fathom в работе, но требует разработки и несет риски неточности данных из-за Fuzzy Matching, а также потенциальные юридические риски, связанные с точностью данных (Privacy Act 2020). Учитывая опыт клиента с Wix Velo, это реалистичный компромисс.

### Нежизнеспособные варианты
Aᚖ₅ (Сопоставление с календарем) и Aᚖ₆ (Ручная инъекция) не рекомендуются из-за крайне низкой надежности данных или отсутствия автоматизации соответственно.

# 17. Анализ `Aᚖ⠿` (выполнен Gemini Deep Research)
https://gemini.google.com/share/fbfbc0ba29a9

## **1. Декомпозиция проблематики и профилирование контекста**

Анализ текущей ситуации клиента ꆜ выявляет классический архитектурный конфликт между механизмами безопасности корпоративного уровня, реализованными в платформе Zoom, и моделями работы современных AI-инструментов, таких как Fathom, которые эмулируют поведение обычных пользователей.1  
Проблема, обозначенная как P†, заключается в том, что принудительное включение функции регистрации («Registration Required») создает непреодолимый барьер для автоматизированных агентов (ботов), поскольку процесс регистрации требует человеческого взаимодействия — ввода капчи, подтверждения email или уникального токена, который бот не может получить самостоятельно.2  
В то же время, отключение регистрации, хотя и открывает шлюзы для AI-ассистентов, приводит к потере критически важных маркетинговых данных — адресов электронной почты участников, что делает невозможным дальнейший трекинг вовлеченности членов коучинговых программ.3  
Анализ истории проектов клиента на Upwork (P1⁎, P2⁎, P3⁎) указывает на высокую степень цифровой зрелости компании: они используют Wix Velo для сложной кастомизации, интегрируют GPT-модели для оценки звонков и активно работают с данными.4  
Это свидетельствует о том, что клиент ищет не просто временный «пластырь», а системное решение, которое интегрируется в их существующий стек (Zoom + Wix + CRM) и обеспечит масштабируемость бизнес-процессов.6  
Заблуждение клиента (D𐊑⠿) состоит в уверенности, что проблема решается исключительно через разработку кастомного API-интеграции, однако глубокое исследование документации Zoom показывает, что API имеет строгие ограничения на выдачу персональных данных (PII) неавторизованных пользователей, что может сделать разработку бессмысленной без изменения настроек безопасности.7  
Таким образом, задача сводится не к написанию кода, а к реархитектуре процесса доступа к встречам, где необходимо сбалансировать три вектора: безопасность (защита от нежелательных гостей), аналитику (сбор email) и автоматизацию (доступ AI).9

## **2. Юридический ландшафт и ограничения Zoom API**

### **Анализ нормативной базы (GDPR/CCPA)**

При рассмотрении альтернативных решений (Aᚖ⠿) необходимо учитывать жесткие юридические рамки, в которых функционирует сбор данных об участниках.10  
Согласно Общему регламенту по защите данных (GDPR), сбор email-адресов и имен участников требует наличия законного основания (Legal Basis), которым в данном случае может выступать либо «Согласие» (Consent), либо «Законный интерес» (Legitimate Interest).11  
Использование ботов для записи встреч и последующей идентификации спикеров также подпадает под регулирование биометрических данных (в случае голосовой идентификации) и требует явного уведомления всех участников.12  
Калифорнийский закон о защите прав потребителей (CCPA) также накладывает обязательства по прозрачности сбора данных, что делает скрытый трекинг (например, через цифровые отпечатки браузера) юридически рискованным.10  
Это означает, что любое решение, которое пытается «обойти» регистрацию и идентифицировать пользователя скрытно, может поставить компанию ꆜ под удар регуляторов.14

### **Технические ограничения Zoom API в отношении PII**

Критически важным аспектом, выявленным в ходе исследования, является политика Zoom по минимизации данных: API endpoints, такие как Get Past Meeting Participants, намеренно возвращают пустые значения в полях email и user_name для пользователей, которые присоединились к встрече как «Гости» (без входа в аккаунт Zoom), если встреча не настроена на принудительную аутентификацию.7  
Сниппеты с форума разработчиков Zoom подтверждают, что даже при наличии платного аккаунта, данные user_id и email отсутствуют для внешних участников в целях соблюдения конфиденциальности.8  
Это фундаментальное ограничение разрушает гипотезу клиента о том, что разработчик может просто «вытащить» данные через API: если данные не были собраны на этапе входа (через регистрацию или аутентификацию), их технически не существует в базе данных встречи для выдачи через API.16  
Следовательно, любое альтернативное решение (Aᚖᵢ) должно обеспечивать сбор данных до или во время входа, а не полагаться на пост-фактум анализ API.3

## **3. Анализ архитектурных подходов AI-ноутейкеров**

Рынок AI-ассистентов делится на две принципиально разные архитектуры: «Bot-based» (на основе ботов, как Fathom) и «Client-side» (на стороне клиента, как Granola/Tactiq).9  
Инструменты на базе ботов (Fathom, Otter, Fireflies) функционируют как виртуальные участники, подключающиеся к SIP-транку конференции; они видят и слышат то же, что и обычный пользователь, но требуют прав на вход, что и вызывает конфликт с регистрацией.18  
Инструменты на стороне клиента (Granola, Bluedot, Tactiq) работают локально на машине пользователя, перехватывая аудиопоток операционной системы или данные браузера; они невидимы для сервера Zoom и, следовательно, игнорируют любые настройки входа, такие как Waiting Room или Registration.9  
Переход на Client-side архитектуру является наиболее очевидным техническим решением проблемы блокировки, однако он перекладывает ответственность за сбор email на другие механизмы, так как локальный рекордер не имеет доступа к списку участников на сервере.20  
Далее мы подробно проанализируем каждую альтернативу (Aᚖᵢ), оценивая её способность решить обе части уравнения: доступ к записи и сбор email.

## **4. Детальный анализ альтернативных решений (Aᚖ⠿)**

### **4.1. Aᚖ₁-S: Granola (Локальный клиентский AI-ассистент)**

#### **4.1.1) Суть**

Granola представляет собой нативное приложение для macOS, которое перехватывает аудиопотоки на уровне ядра операционной системы (CoreAudio), объединяя входящий звук конференции и исходящий звук микрофона пользователя для локальной обработки и транскрипции.9  
Архитектура приложения полностью исключает взаимодействие с серверами Zoom в качестве участника встречи, что делает Granola невидимой для механизмов контроля доступа, таких как "Waiting Room" или "Registration Required".9  
Вместо создания виртуального пользователя-бота, Granola полагается на то, что человек-хост уже прошел все процедуры аутентификации и имеет доступ к аудиопотоку, который приложение просто «слушает» в фоновом режиме.9  
Приложение использует локальные модели машинного обучения для первичной обработки или отправляет зашифрованные данные на серверы OpenAI/Anthropic для генерации структурированных заметок, что обеспечивает высокую точность саммари без риска блокировки.17  
Интеграция с Zapier, реализованная в последних версиях, позволяет настраивать триггеры на создание новых заметок, что теоретически дает возможность отправлять итоги встреч в CRM, но не решает проблему автоматического сопоставления заметки с контактом, если email не был введен вручную.22  
Для идентификации спикеров Granola использует алгоритмы диаризации аудиопотока, пытаясь различить голоса по их спектральным характеристикам, однако, не имея доступа к метаданным Zoom API, приложение не может точно присвоить имена (например, "Иван Иванов") новым спикерам без ручной разметки пользователя.21  
В контексте задачи T, Granola позволяет клиенту ꆜ включить самую строгую регистрацию в Zoom (для сбора email), так как это никак не помешает работе ассистента, запущенного на компьютере коуча.9  
Таким образом, Granola решает конфликт путем разделения плоскостей: Zoom занимается безопасностью и сбором лидов, а Granola — локальной записью контента.24  
Однако это решение требует смены привычного инструмента (Fathom) и перехода на новую платформу, что влечет за собой необходимость обучения персонала и проверки совместимости оборудования (требуется Mac для лучшей работы).25  
Кроме того, отсутствие видеозаписи в Granola ограничивает возможности для анализа невербального поведения клиентов, что может быть критично для глубокого коучинга.1

#### **4.1.2) Оценка**

82

#### **4.1.3) Достоинства**

Абсолютная независимость от настроек безопасности Zoom гарантирует стабильную работу записи даже при самых строгих политиках регистрации, что полностью устраняет технический конфликт, описанный в P†.9  
Высокое качество структурированных заметок, генерируемых моделями уровня GPT-4, превосходит стандартные транскрипты, предоставляя коучам готовые инсайты и списки задач.17  
Локальная запись обеспечивает конфиденциальность разговоров, так как бот не «висит» в списке участников, создавая более доверительную атмосферу для клиентов, которые могут опасаться записи третьими лицами.18  
Отсутствие необходимости в администрировании прав доступа Zoom (OAuth scopes) упрощает внедрение, так как не требуется прохождение сложных процедур верификации приложения в Zoom Marketplace.9  
Интерфейс, ориентированный на человека, позволяет коучу делать пометки в процессе встречи, которые AI затем интегрирует в общий контекст, повышая релевантность итогового отчета.24  
Широкие возможности интеграции через Zapier (8000+ приложений) позволяют настроить автоматическую отправку отчетов в HubSpot или Salesforce, встраивая Granola в существующий рабочий процесс.22  
Поддержка шаблонов заметок позволяет адаптировать выходные данные под специфику коучинговых сессий, выделяя ключевые инсайты, проблемы и обязательства клиента.26  
Модель "Set and Forget" (Установил и забыл) снижает когнитивную нагрузку на коуча, так как приложение может запускаться автоматически при обнаружении встречи в календаре.17

#### **4.1.4) Недостатки**

Фундаментальная неспособность автоматически извлекать email-адреса участников из встречи означает, что процесс связывания записи с карточкой клиента в CRM требует ручного вмешательства или сложной логики сопоставления по имени.20  
Ограниченная поддержка платформ (преимущественно macOS) может стать блокирующим фактором, если парк техники компании ꆜ состоит из Windows-устройств, хотя веб-версии и развиваются.25  
Локальная обработка аудио потребляет ресурсы процессора и батареи, что может быть критично для длительных сессий на ноутбуках, в отличие от облачных ботов, которые не нагружают машину пользователя.27  
Отсутствие видеозаписи лишает коучей возможности пересматривать реакции клиентов, что снижает ценность инструмента для обучения и супервизии.1  
Риск потери данных при сбое локального компьютера или приложения выше, чем при использовании облачных сервисов, которые пишут поток на сервере.27  
Идентификация спикеров менее точна и требует "обучения" системы или ручной правки, так как у приложения нет доступа к списку участников Zoom с их именами.28  
Необходимость установки ПО на компьютер каждого сотрудника усложняет администрирование и обновление парка софта по сравнению с централизованно управляемыми облачными ботами.17

### **4.2. Aᚖ₂-S: Bluedot (Браузерное расширение для записи)**

#### **4.2.1) Суть**

Bluedot реализует подход "Browser-based capture" (Захват через браузер), используя расширение для Chrome, которое внедряется в DOM-дерево веб-интерфейса Zoom или захватывает медиапоток вкладки/окна.19  
В отличие от нативных приложений, Bluedot работает внутри среды браузера, что позволяет ему захватывать не только звук, но и видеоизображение экрана, включая демонстрации презентаций и видеопотоки участников.29  
Механизм работы строится на использовании API getDisplayMedia и MediaRecorder, которые позволяют записывать содержимое экрана без необходимости подключения бота к серверу конференции.30  
Это решение полностью обходит проблему блокировки ботов регистрацией, так как для Zoom запись выглядит как обычная активность пользователя в браузере.31  
После завершения записи файл автоматически загружается в облачное хранилище Bluedot, где происходит асинхронная обработка: транскрибация, диаризация и генерация AI-саммари.29  
Bluedot позиционирует себя как комплексное решение для документирования встреч, предлагая функции видеоредактирования, создания клипов и шеринга коллекций видео, что сближает его с функционалом Loom, но с фокусом на встречи.32  
В контексте интеграции с CRM, Bluedot может отправлять данные в Slack, Notion или CRM, но, как и Granola, сталкивается с проблемой отсутствия доступа к скрытым метаданным встречи (email участников), если они не отображены явно на экране.33  
Для компании ꆜ переход на Bluedot потребует изменения привычек коучей: им придется проводить встречи через веб-версию Zoom или запускать захват окна десктопного приложения, что может быть менее удобно, чем полностью автоматический Fathom.19  
Однако это решение сохраняет визуальный контекст, что выгодно отличает его от Granola.29  
Важно отметить, что Bluedot хранит данные в зашифрованном виде и соответствует стандартам GDPR, что позволяет использовать его для работы с персональными данными клиентов.19

#### **4.2.2) Оценка**

78

#### **4.2.3) Достоинства**

Гарантированный обход любых ограничений на вход ботов (Registration, Waiting Room, Passcode), так как запись инициируется авторизованным пользователем локально.31  
Запись видео высокого качества (до 1080p) сохраняет визуальную информацию, мимику и демонстрацию экрана, что критически важно для качественного разбора коучинговых сессий.27  
Автоматическая загрузка в облако сразу после встречи обеспечивает сохранность данных и мгновенный доступ для шеринга с командой или клиентом.19  
Встроенные инструменты видеомонтажа позволяют быстро вырезать нежелательные фрагменты или создавать короткие хайлайты для отправки клиенту в качестве резюме.32  
Работает на любой операционной системе, где есть браузер Chrome (Windows, macOS, Linux), что обеспечивает универсальность внедрения в разнородной IT-среде.25  
Фоновая запись позволяет пользователю переключаться между вкладками, при этом рекордер может продолжать писать только окно Zoom, не захватывая лишнего.19  
Интеграция с Google Calendar позволяет автоматически предлагать запись для запланированных встреч, снижая риск того, что коуч забудет включить запись.33  
Отсутствие "бота-наблюдателя" в списке участников снижает психологическое напряжение у клиентов, делая общение более естественным.30

#### **4.2.4) Недостатки**

Критическая зависимость от производительности браузера и компьютера: процесс кодирования видео в реальном времени потребляет значительные ресурсы CPU/RAM, что может вызывать тормоза на слабых ноутбуках.27  
Невозможность автоматического извлечения email-адресов участников из Zoom API, так как расширение работает поверх интерфейса и не имеет доступа к бэкенду регистрации.30  
Требование к ручному запуску записи (или подтверждению автозапуска) для каждой встречи может привести к человеческим ошибкам и потере данных.30  
Ограниченная точность идентификации спикеров по сравнению с нативными ботами, которые получают отдельные аудиодорожки для каждого участника через Zoom API.34  
Необходимость держать браузер открытым и активным (если используется веб-версия Zoom) ограничивает многозадачность пользователя во время звонка.19  
Риск потери записи при внезапном закрытии браузера или крахе расширения, хотя локальное кэширование пытается минимизировать этот риск.27  
Юридическая серая зона: пользователь должен сам помнить о необходимости устного предупреждения о записи, так как автоматическое аудио-уведомление Zoom ("Recording in progress") при локальном захвате не воспроизводится.30

### **4.3. Aᚖ₃-S: Tactiq (Транскрибация субтитров в реальном времени)**

#### **4.3.1) Суть**

Tactiq использует принципиально иной подход к захвату информации, базирующийся на перехвате текстового потока субтитров (Closed Captions), которые генерируются серверами Zoom или Google Meet.18  
Вместо того чтобы обрабатывать тяжелые аудиофайлы, Tactiq считывает уже готовый текст, который отображается в интерфейсе видеоконференции, и сохраняет его в структурированный документ в реальном времени.35  
Этот метод делает Tactiq самым легковесным решением, так как оно практически не потребляет ресурсы процессора пользователя, перекладывая задачу распознавания речи на мощные серверы Zoom.36  
Для работы Tactiq не требуется ни бот, ни локальная запись звука, что автоматически решает проблему конфликта с регистрацией: расширение просто "читает" то, что видит пользователь на экране.36  
Однако для функционирования этого метода необходимо, чтобы в настройках встречи Zoom была включена опция "Automated Captions" (Автоматические субтитры), иначе источнику данных просто неоткуда взяться.36  
Tactiq интегрируется с GPT-4 для анализа полученного текста "на лету", предлагая пользователю саммари, выделение главных мыслей и задач прямо в боковой панели браузера во время встречи.37  
С точки зрения идентификации, Tactiq использует имена, привязанные к субтитрам в интерфейсе Zoom, что позволяет достаточно точно определять спикеров, если они корректно подписаны.38  
В вопросе сбора email Tactiq не предлагает решения: он видит только те данные, которые отображаются в UI (обычно только имя), и не имеет доступа к скрытым полям профиля участника.39  
Для компании ꆜ Tactiq может стать отличным дополнением, если основная цель — текстовые заметки, но он полностью лишен аудио/видео составляющей.37

#### **4.3.2) Оценка**

72

#### **4.3.3) Достоинства**

Нулевая нагрузка на систему пользователя, так как не производится кодирование аудио или видео, что делает решение идеальным для старых компьютеров.35  
Мгновенная готовность транскрипта сразу после окончания встречи, так как текст формируется в реальном времени, без задержки на пост-процессинг.35  
Высокая точность идентификации спикеров, базирующаяся на метаданных Zoom Captions, что часто надежнее, чем аудио-диаризация сторонних сервисов.38  
Полная невидимость и ненавязчивость: расширение работает тихо, не требуя добавления ботов и не меняя интерфейс Zoom для других участников.18  
Возможность поиска по тексту и выделения хайлайтов прямо во время разговора позволяет коучу оперативно фиксировать важные моменты.37  
Поддержка множества языков (в зависимости от возможностей движка субтитров Zoom), что обеспечивает гибкость в международных коммуникациях.40  
Автоматическое сохранение истории чата встречи вместе с транскриптом, что позволяет не терять ссылки и контакты, сброшенные в чат.19  
Низкая стоимость и простота внедрения (достаточно установить расширение в браузер).37

#### **4.3.4) Недостатки**

Критическая зависимость от настроек хоста: если "Closed Captions" отключены организатором или администратором аккаунта, Tactiq становится бесполезным.36  
Отсутствие аудиозаписи для верификации: если транскриптор ошибся, у пользователя нет возможности переслушать оригинальный фрагмент внутри инструмента.35  
Качество текста полностью определяется движком распознавания Zoom, который может уступать специализированным моделям Whisper, используемым в Granola или Bluedot.41  
Отсутствие видео-контекста делает невозможным анализ визуальной информации, презентаций и эмоций участников.37  
Необходимость использования веб-версии Zoom для корректной работы расширения (или сложной настройки интеграции с десктопным приложением) снижает удобство.40  
Не решает задачу сбора email, так как не имеет доступа к данным регистрации и видит только отображаемые имена.39  
Риск потери данных при нестабильном интернете, если поток субтитров прервется или браузер зависнет.35

### **4.4. Aᚖ₄-S: Zoom "Require Authentication" (Нативная конфигурация)**

#### **4.4.1) Суть**

Данное решение (Aᚖ₄) представляет собой не внедрение нового программного обеспечения, а стратегическое изменение конфигурации безопасности самого Zoom, устраняющее первопричину конфликта.2  
Вместо использования функции «Registration» (которая создает уникальные ссылки и блокирует ботов), предлагается использовать настройку «Require Authentication to Join» (Требовать аутентификацию для входа).2  
В этом сценарии ссылка на встречу остается статической (или обычной динамической), что позволяет ботам Fathom (которые, как правило, имеют собственные авторизованные аккаунты Zoom) успешно присоединяться к встрече.42  
В то же время, требование аутентификации обязывает каждого живого участника войти в свой аккаунт Zoom перед присоединением, что автоматически передает хосту его верифицированные данные: Имя и Email, привязанные к аккаунту.43  
Эти данные становятся доступны в стандартных отчетах Zoom ("Active Host Reports" или "Usage Reports") и могут быть выгружены через API или вручную после встречи.39  
Таким образом, цель P† (сбор email) достигается за счет использования данных профиля Zoom, а цель доступа бота — за счет снятия барьера уникальной регистрации.3  
Если бот Fathom все же блокируется настройкой аутентификации (например, если включено ограничение "Only users in my account"), можно добавить исключение ("Authentication Exception") для конкретных адресов ботов или разрешить вход любым авторизованным в Zoom пользователям.44  
Это решение является наиболее элегантным с архитектурной точки зрения, так как использует нативные механизмы платформы без "костылей".2

#### **4.4.2) Оценка**

92

#### **4.4.3) Достоинства**

Позволяет сохранить использование любимого инструмента Fathom, не заставляя команду переучиваться на новый софт, что экономит время и деньги.2  
Обеспечивает сбор 100% валидных email-адресов, так как данные берутся из верифицированных аккаунтов Zoom, исключая опечатки и фейковые адреса, частые при ручной регистрации.3  
Устраняет необходимость в сложной API-разработке, так как данные уже доступны в стандартных отчетах Zoom, которые можно легко экспортировать.39  
Повышает общую безопасность встреч, исключая возможность анонимного входа и "Зум-бомбинга", так как каждый участник идентифицирован.45  
Гибкость настройки: можно разрешить вход любым пользователям Zoom или ограничить определенными доменами, сохраняя при этом доступ для бота через исключения.44  
Автоматическая генерация отчетов о посещаемости с точным временем входа/выхода, что полезно для аналитики вовлеченности.39  
Отсутствие дополнительных расходов на лицензии стороннего ПО (в отличие от BlueSky или Virtually).2

#### **4.4.4) Недостатки**

Создает барьер для клиентов, у которых нет аккаунта Zoom: им придется зарегистрироваться перед входом, что может вызвать раздражение или снижение конверсии в посещение (drop-off).46  
Собирает email-адреса, на которые зарегистрирован Zoom-аккаунт (часто личные gmail/yahoo), которые могут отличаться от рабочих адресов, необходимых для CRM.3  
Не позволяет задавать кастомные вопросы перед встречей (например, "Ваш уровень опыта", "Цель звонка"), что возможно в стандартной форме регистрации Zoom.47  
Требует тщательной настройки исключений для ботов, если политики безопасности организации настроены слишком агрессивно.48  
Может вызвать путаницу у пользователей, если они привыкли заходить по клику без пароля и логина.46  
Если клиент заходит с чужого аккаунта (например, жены или коллеги), данные в отчете будут некорректными.3  
Не решает проблему, если бот Fathom технически не поддерживает прохождение потока аутентификации (хотя большинство Enterprise-ботов это умеют).42

### **4.5. Aᚖ₅-S: External Attendance Trackers (BlueSky / Virtually)**

#### **4.5.1) Суть**

Решение предполагает делегирование функции трекинга посещаемости специализированным приложениям из Zoom App Marketplace, таким как BlueSky Apps или Virtually, которые работают параллельно с Fathom.49  
Эти приложения используют Zoom API и Webhooks для мониторинга событий participant_joined в реальном времени, фиксируя каждого вошедшего пользователя.50  
Ключевая особенность заключается в том, что некоторые из них (например, BlueSky Attendance Taker) предлагают собственные механизмы идентификации: если пользователь не распознан, приложение может отправить ему личное сообщение в чат или показать всплывающее окно (Zoom App) с просьбой ввести email.51  
Это позволяет полностью отключить нативную регистрацию Zoom (открыв вход для Fathom), но при этом обеспечить жесткий контроль посещаемости через сторонний слой логики.52  
Virtually, в частности, интегрируется глубоко в образовательный процесс, позволяя не просто трекать вход, но и связывать его с базой студентов, автоматически обновляя статусы в CRM или LMS.49  
Такой подход превращает Zoom просто в канал связи, а всю логику управления аудиторией выносит во внешний сервис, который специально заточен под эти задачи.53  
Это решение особенно актуально для коучинговых программ, где важна не просто фиксация email, а аналитика посещаемости курса во времени.54

#### **4.5.2) Оценка**

68

#### **4.5.3) Достоинства**

Позволяет снять блокирующую регистрацию Zoom, обеспечивая беспрепятственный доступ для Fathom и других инструментов.51  
Предоставляет значительно более глубокую и удобную аналитику посещаемости, чем нативные отчеты Zoom (графики, тренды, авто-рассылка отчетов).51  
Автоматизирует коммуникацию с прогульщиками: Virtually может сам отправить письмо тем, кто не пришел на занятие.52  
Решает проблему идентификации гостей через интерактивные запросы данных внутри встречи (через чат или Zoom Apps), что невозможно стандартными средствами.55  
Интеграция с LMS и CRM "из коробки" экономит время на ручной перенос данных.49  
Поддерживает сценарии гибридного обучения и сложных расписаний, что актуально для коучингового бизнеса ꆜ.56  
Снижает нагрузку на администраторов за счет автоматизации рутинных задач по сверке списков.54

#### **4.5.4) Недостатки**

Вводит дополнительные расходы: качественные трекеры стоят денег (подписка), что увеличивает бюджет проекта.57  
Требует установки дополнительных приложений в аккаунт Zoom и, возможно, действий со стороны участников (установка App), что усложняет UX.58  
Технический риск: если API Zoom изменится или webhook не сработает, данные о посещаемости могут быть безвозвратно утеряны.59  
Проблема "пустых полей": если приложение полагается только на API без активного опроса пользователя, оно также получит пустой email для гостя, как и самописный скрипт.8  
Навязчивость: автоматические сообщения в чат или попапы с просьбой представиться могут раздражать клиентов во время платного коучинга.51  
Усложнение IT-ландшафта: появление еще одной сущности (BlueSky/Virtually), которую нужно администрировать и оплачивать.60  
Зависимость от стороннего вендора: если сервис закроется или изменит условия, бизнес-процесс сломается.60

### **4.6. Aᚖ₆-S: LTI Pro / LMS Integration (Интеграция через контекст обучения)**

#### **4.6.1) Суть**

Если компания ꆜ использует платформу обучения (LMS) или сайт на Wix с личными кабинетами, можно применить протокол LTI (Learning Tools Interoperability) или кастомную интеграцию для запуска встреч.61  
Идея заключается в том, что пользователь сначала авторизуется на сайте компании (где его email уже известен), а затем нажимает кнопку "Присоединиться", которая через LTI Pro или API генерирует ссылку на вход с уже "вшитыми" параметрами идентификации.48  
Zoom LTI Pro позволяет автоматически создавать аккаунты или матчить пользователей при входе из LMS (Canvas, Moodle и др.), передавая их данные в отчеты Zoom как "доверенных".62  
В случае с Wix Velo (упомянутым в проекте P1⁎), можно написать скрипт, который при клике на кнопку генерирует уникальную join_url для конкретного пользователя или регистрирует его в Zoom "на лету" через API, а затем редиректит во встречу.5  
Это позволяет отключить публичную регистрацию (открыв дверь для Fathom по общей ссылке, если настроить права), но для клиентов сделать вход строго через портал, где они де-факто "зарегистрированы".63  
Таким образом, Fathom заходит как обычный участник (или через отдельную ссылку для хоста), а студенты — как идентифицированные пользователи из LMS.62

#### **4.6.2) Оценка**

74

#### **4.6.3) Достоинства**

Обеспечивает "бесшовный" пользовательский опыт: клиентам не нужно регистрироваться в Zoom каждый раз, они используют единый логин от портала обучения.63  
Гарантирует 100% точность привязки посещаемости к конкретному студенту в базе данных компании, исключая ошибки ручного ввода.62  
Позволяет автоматически передавать данные о присутствии (оценки, часы) обратно в LMS, замыкая контур обучения.64  
Снимает необходимость в "Registration Required" на стороне Zoom, так как контроль доступа осуществляется на уровне портала (ссылка на встречу не публикуется открыто).62  
Позволяет реализовать сложную логику доступа (например, пускать только тех, кто оплатил курс), которую невозможно настроить в стандартном Zoom.5  
Данные остаются под полным контролем компании, а не третьих сторон.5  
Использует стандартные протоколы (LTI), поддерживаемые большинством современных образовательных платформ.61

#### **4.6.4) Недостатки**

Высокая стоимость и сложность внедрения: требует квалифицированных разработчиков (Velo/LTI) для настройки и поддержки интеграции.5  
Если у компании нет полноценной LMS, а только набор лендингов, внедрение LTI будет избыточным и дорогим ("стрельба из пушки по воробьям").61  
Бот Fathom может столкнуться с трудностями доступа, если встреча скрыта внутри LMS и требует авторизации на портале для получения ссылки (боту нужно дать прямую ссылку).62  
Возможны проблемы с LTI Pro, такие как ошибки авто-провижнинга пользователей или дублирование аккаунтов, требующие техподдержки.65  
Зависимость от работоспособности сайта/LMS: если портал упадет, клиенты не смогут попасть на урок.66  
Необходимость постоянного обновления интеграции при изменении API Zoom или LMS.5  
Сложности с "гостевыми" лекциями: если нужно пригласить человека не из базы LMS, придется придумывать обходные пути.65

## **5. Сравнительный анализ альтернатив**

Для наглядности сравним ключевые характеристики предложенных решений.

| Характеристика | Aᚖ₁ (Granola) | Aᚖ₂ (Bluedot) | Aᚖ₃ (Tactiq) | Aᚖ₄ (Zoom Auth) | Aᚖ₅ (Apps) | Aᚖ₆ (LMS) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Решает проблему блокировки Fathom** | ✅ (Замена) | ✅ (Замена) | ✅ (Замена) | ✅ (Совместим) | ✅ (Обход) | ✅ (Обход) |
| **Сбор Email участников** | ❌ (Нет) | ❌ (Нет) | ❌ (Нет) | ✅ (Авто) | ✅ (API/Чат) | ✅ (Системно) |
| **Качество транскрипции** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | N/A | N/A |
| **Видеозапись** | ❌ | ✅ | ❌ | ✅ (Fathom) | ✅ (Fathom) | ✅ (Fathom) |
| **Сложность внедрения** | Низкая | Низкая | Низкая | Средняя | Средняя | Высокая |
| **Стоимость** | $$ | $$ | $ | $0 | $$ | $$$ |
| **Влияние на UX клиента** | Нейтральное | Нейтральное | Нейтральное | Негативное | Смешанное | Позитивное |

## **6. Итоговый вердикт и рекомендация**

### **6.1. Синтез решения**

Проведенный Deep Research подтверждает, что первоначальный запрос клиента на "Zoom API Developer" базируется на ложной предпосылке (D𐊑⠿), что проблему можно решить кодом без изменения процессов.  
Технические ограничения Zoom API (пустые поля PII для гостей) делают разработку кастомного скрипта неэффективной.  
Оптимальным путем является не борьба с ветряными мельницами API, а архитектурная перестройка доступа.

### **6.2. Рекомендация**

Я рекомендую Aᚖ₄: Zoom Require Authentication как основное решение.  
Это единственный вариант, который позволяет:

1. **Сохранить Fathom** (инструмент, который нравится клиенту).  
2. **Гарантировать сбор Email** (через профиль Zoom).  
3. **Не тратить бюджет на разработку** (только настройка).

Если клиент категорически не готов требовать от пользователей аккаунта Zoom, то **вторым выбором** является **Aᚖ₁: Granola** — переход на локальную запись, что пожертвует автоматическим сбором email внутри инструмента (придется сверять вручную или использовать формы), но даст качественные заметки без блокировок.

### **6.3. Дорожная карта (Next Steps)**

1. **Тест Aᚖ₄:** Провести одну тестовую встречу с включенным "Require Authentication" вместо "Registration". Проверить, заходит ли Fathom и попадают ли данные в отчеты.  
2. **Аудит Fathom:** Проверить настройки бота Fathom в дашборде — разрешен ли ему вход в авторизованные встречи.  
3. **Настройка исключений:** Если нужно, добавить домены ботов в исключения аутентификации Zoom.  
4. **Резервный план:** Если Aᚖ₄ неприемлем для маркетинга, начать пилотное внедрение Granola для коучей.

#### **Works cited**

1. A side-by-side comparison of 22 AI notetakers for sales - Arrows, accessed November 28, 2025, [https://arrows.to/guide/top-ai-notetakers/a-side-by-side-comparison-of-22-ai-notetakers-for-sales](https://arrows.to/guide/top-ai-notetakers/a-side-by-side-comparison-of-22-ai-notetakers-for-sales)  
2. Re: How can I require guests to provide email address before joining a meeting?, accessed November 28, 2025, [https://community.zoom.com/t5/Zoom-Meetings/How-can-I-require-guests-to-provide-email-address-before-joining/m-p/134774](https://community.zoom.com/t5/Zoom-Meetings/How-can-I-require-guests-to-provide-email-address-before-joining/m-p/134774)  
3. How can I require guests to provide email address before joining a meeting?, accessed November 28, 2025, [https://community.zoom.com/t5/Zoom-Meetings/How-can-I-require-guests-to-provide-email-address-before-joining/td-p/39305](https://community.zoom.com/t5/Zoom-Meetings/How-can-I-require-guests-to-provide-email-address-before-joining/td-p/39305)  
4. Identify Zoom users and accounts - Zoom Developer Platform, accessed November 28, 2025, [https://developers.zoom.us/docs/contact-center/apps/identify-users-and-accounts/](https://developers.zoom.us/docs/contact-center/apps/identify-users-and-accounts/)  
5. Zoom Integration, accessed November 28, 2025, [https://dev.wix.com/docs/velo/articles/velo-package-readmes/zoom-integration](https://dev.wix.com/docs/velo/articles/velo-package-readmes/zoom-integration)  
6. Hubspot and Zoom Webinar Integration (I haven't COMPLETELY lost my mind yet, but I'm close :) - Reddit, accessed November 28, 2025, [https://www.reddit.com/r/hubspot/comments/1onnwcr/hubspot_and_zoom_webinar_integration_i_havent/](https://www.reddit.com/r/hubspot/comments/1onnwcr/hubspot_and_zoom_webinar_integration_i_havent/)  
7. Announcements - Zoom Developer Platform, accessed November 28, 2025, [https://developers.zoom.us/docs/platform/announcements/](https://developers.zoom.us/docs/platform/announcements/)  
8. Zoom participant api not returning participant emails - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/zoom-participant-api-not-returning-participant-emails/65028](https://devforum.zoom.us/t/zoom-participant-api-not-returning-participant-emails/65028)  
9. Granola — The AI notepad for people in back-to-back meetings, accessed November 28, 2025, [https://www.granola.ai/](https://www.granola.ai/)  
10. California Consumer Privacy Act (CCPA) | State of California - Department of Justice - Office of the Attorney General, accessed November 28, 2025, [https://oag.ca.gov/privacy/ccpa](https://oag.ca.gov/privacy/ccpa)  
11. What is the 'legitimate interests' basis? | ICO, accessed November 28, 2025, [https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/legitimate-interests/what-is-the-legitimate-interests-basis/](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/legitimate-interests/what-is-the-legitimate-interests-basis/)  
12. Zoom Privacy Policy and Conditions of Use - German Council on Foreign Relations (DGAP), accessed November 28, 2025, [https://dgap.org/en/zoom](https://dgap.org/en/zoom)  
13. Digital Trackers & Data Protection: How the CPRA Closes CCPA Gaps in Addressing Cross-Contextual Behavioral Tracking - California Lawyers Association, accessed November 28, 2025, [https://calawyers.org/business-law/digital-trackers-data-protection-how-the-cpra-closes-ccpa-gaps-in-addressing-cross-contextual-behavioral-tracking/](https://calawyers.org/business-law/digital-trackers-data-protection-how-the-cpra-closes-ccpa-gaps-in-addressing-cross-contextual-behavioral-tracking/)  
14. Zoom GDPR: Is the Tool Compliant with Data Protection? - Zeeg, accessed November 28, 2025, [https://zeeg.me/en/blog/post/zoom-gdpr](https://zeeg.me/en/blog/post/zoom-gdpr)  
15. I'm not receiving participant_user_id when a call List meeting participants endpoint, accessed November 28, 2025, [https://devforum.zoom.us/t/im-not-receiving-participant-user-id-when-a-call-list-meeting-participants-endpoint/83884](https://devforum.zoom.us/t/im-not-receiving-participant-user-id-when-a-call-list-meeting-participants-endpoint/83884)  
16. Dashboard API List Meetings Participants returns blank user_name for users not logged in, accessed November 28, 2025, [https://devforum.zoom.us/t/dashboard-api-list-meetings-participants-returns-blank-user-name-for-users-not-logged-in/47961](https://devforum.zoom.us/t/dashboard-api-list-meetings-participants-returns-blank-user-name-for-users-not-logged-in/47961)  
17. Granola vs Zoom - Sacra, accessed November 28, 2025, [https://sacra.com/research/granola-vs-zoom/](https://sacra.com/research/granola-vs-zoom/)  
18. 10 Best AI Meeting Note Takers That Do Not Use Bots To Join Video Calls, accessed November 28, 2025, [https://www.meetjamie.ai/blog/ai-meeting-note-takers-that-do-not-use-bots-to-join-video-calls](https://www.meetjamie.ai/blog/ai-meeting-note-takers-that-do-not-use-bots-to-join-video-calls)  
19. Zoom Meeting Recorder - Bluedot AI Note Taker, accessed November 28, 2025, [https://www.bluedothq.com/tools/zoom-meeting-recorder](https://www.bluedothq.com/tools/zoom-meeting-recorder)  
20. Granola Zoom Integration - Quick Connect - Zapier, accessed November 28, 2025, [https://zapier.com/apps/granola/integrations/zoom](https://zapier.com/apps/granola/integrations/zoom)  
21. How transcription works - Granola Help Center, accessed November 28, 2025, [https://help.granola.ai/article/transcription](https://help.granola.ai/article/transcription)  
22. Granola Integrations | Connect Your Apps with Zapier, accessed November 28, 2025, [https://zapier.com/apps/granola/integrations](https://zapier.com/apps/granola/integrations)  
23. Your meeting notes, now connected with 8,000+ apps - Granola, accessed November 28, 2025, [https://www.granola.ai/blog/your-meeting-notes-now-connected-with-8000-apps](https://www.granola.ai/blog/your-meeting-notes-now-connected-with-8000-apps)  
24. How to Get the Best Out of Granola: Your Ultimate Guide, accessed November 28, 2025, [https://www.granola.ai/blog/get-the-best-from-granola](https://www.granola.ai/blog/get-the-best-from-granola)  
25. Voicenotes: AI Notes and Meetings, accessed November 28, 2025, [https://voicenotes.com/](https://voicenotes.com/)  
26. What is Granola? The AI note taker everyone's talking about - Zapier, accessed November 28, 2025, [https://zapier.com/blog/granola-ai/](https://zapier.com/blog/granola-ai/)  
27. Recording settings explained | Bluedot Help Center, accessed November 28, 2025, [https://help.bluedothq.com/en/articles/11470421-recording-settings-explained](https://help.bluedothq.com/en/articles/11470421-recording-settings-explained)  
28. Granola AI Honest Review & the 7 Best Alternatives - Krisp, accessed November 28, 2025, [https://krisp.ai/blog/granola-ai-review-alternatives/](https://krisp.ai/blog/granola-ai-review-alternatives/)  
29. Zoom Meeting Recorder - YouTube, accessed November 28, 2025, [https://www.youtube.com/watch?v=jHo2bcsTtTs](https://www.youtube.com/watch?v=jHo2bcsTtTs)  
30. How To Record a Zoom Meeting Without Permission in 2025, accessed November 28, 2025, [https://www.bluedothq.com/blog/how-to-record-a-zoom-meeting](https://www.bluedothq.com/blog/how-to-record-a-zoom-meeting)  
31. Bluedot vs Zoom AI – Which meeting automation tool is right for you? - Circleback, accessed November 28, 2025, [https://circleback.ai/compare/bluedot-vs-zoom-ai](https://circleback.ai/compare/bluedot-vs-zoom-ai)  
32. Bluedot: AI notetaker & Meeting Recorder - Chrome Web Store, accessed November 28, 2025, [https://chromewebstore.google.com/detail/bluedot-ai-notetaker-meet/aeeninnnlhgaojlolnbpljadhbionlal](https://chromewebstore.google.com/detail/bluedot-ai-notetaker-meet/aeeninnnlhgaojlolnbpljadhbionlal)  
33. Inviting Bluedot Recorder into Your Zoom Meeting, accessed November 28, 2025, [https://help.bluedothq.com/en/articles/10697005-inviting-bluedot-recorder-into-your-zoom-meeting](https://help.bluedothq.com/en/articles/10697005-inviting-bluedot-recorder-into-your-zoom-meeting)  
34. The Best AI Note Takers of 2025 - YouTube, accessed November 28, 2025, [https://www.youtube.com/watch?v=xvxRJjdBCUk](https://www.youtube.com/watch?v=xvxRJjdBCUk)  
35. How to Use Zoom AI Transcription Tool - Tactiq, accessed November 28, 2025, [https://tactiq.io/learn/zoom-ai-transcription-tool](https://tactiq.io/learn/zoom-ai-transcription-tool)  
36. How to use Tactiq with Zoom, accessed November 28, 2025, [https://help.tactiq.io/en/articles/9530151-how-to-use-tactiq-with-zoom](https://help.tactiq.io/en/articles/9530151-how-to-use-tactiq-with-zoom)  
37. AI Meeting Assistant: Real-Time Zoom Transcriptions - Tactiq, accessed November 28, 2025, [https://tactiq.io/ai-tools/ai-meeting-assistant-for-zoom](https://tactiq.io/ai-tools/ai-meeting-assistant-for-zoom)  
38. Where to Find Zoom Recordings: Your Ultimate Guide - Tactiq, accessed November 28, 2025, [https://tactiq.io/learn/where-to-find-zoom-recordings](https://tactiq.io/learn/where-to-find-zoom-recordings)  
39. Zoom Attendance Report: Everything You Need to Know - Tactiq, accessed November 28, 2025, [https://tactiq.io/learn/zoom-attendance-report](https://tactiq.io/learn/zoom-attendance-report)  
40. Real-Time Zoom Transcription: Audio to Text - Tactiq, accessed November 28, 2025, [https://tactiq.io/transcribe/zoom](https://tactiq.io/transcribe/zoom)  
41. AI Meeting Note Taker | Free AI Transcription - Notta, accessed November 28, 2025, [https://www.notta.ai/en](https://www.notta.ai/en)  
42. Bluedot - Zoom App Marketplace, accessed November 28, 2025, [https://marketplace.zoom.us/apps/kteREsuHTAev4A2NJwB8AA](https://marketplace.zoom.us/apps/kteREsuHTAev4A2NJwB8AA)  
43. Changing user-level settings - Zoom Support, accessed November 28, 2025, [https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0061300](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0061300)  
44. Requiring authentication to join a meeting or webinar - Zoom Support, accessed November 28, 2025, [https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0063837](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0063837)  
45. Client Alert: Zoom-Users Beware! Reports of Significant Privacy and Data Security Flaws, accessed November 28, 2025, [https://www.whitefordlaw.com/news-events/client-alert-zoom-users-beware-reports-of-significant-privacy-and-data-security-flaws](https://www.whitefordlaw.com/news-events/client-alert-zoom-users-beware-reports-of-significant-privacy-and-data-security-flaws)  
46. Capturing Email addresses of Zoom Meeting Participants with a Zoom Pro Account, accessed November 28, 2025, [https://www.youtube.com/watch?v=Y_caAHcn8qY](https://www.youtube.com/watch?v=Y_caAHcn8qY)  
47. Synced fields for Salesforce for Lightning app - Zoom Support, accessed November 28, 2025, [https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0074461](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0074461)  
48. Configuring LTI Pro - Zoom Support, accessed November 28, 2025, [https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059624](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059624)  
49. Attendance Tracking by Virtually - Zoom App Marketplace, accessed November 28, 2025, [https://marketplace.zoom.us/apps/_Hh16NMURWi8byUcA8pxzg](https://marketplace.zoom.us/apps/_Hh16NMURWi8byUcA8pxzg)  
50. How to track participants during the meeting via the Zoom API - Recall.ai, accessed November 28, 2025, [https://www.recall.ai/blog/zoom-dev-forum-participant-tracking](https://www.recall.ai/blog/zoom-dev-forum-participant-tracking)  
51. Attendance Taker - Automatic Attendee Reports - Zoom App Marketplace, accessed November 28, 2025, [https://marketplace.zoom.us/apps/VFbMBZjDRh6cofA7CmN5bQ](https://marketplace.zoom.us/apps/VFbMBZjDRh6cofA7CmN5bQ)  
52. Virtually: Zoom Attendance Tracking Reports, accessed November 28, 2025, [https://www.tryvirtually.com/](https://www.tryvirtually.com/)  
53. Zoom Attendance Taker Documentation - Blue Sky Apps, accessed November 28, 2025, [https://blueskyapps.org/documentation/zoom-attendance-taker](https://blueskyapps.org/documentation/zoom-attendance-taker)  
54. Zoom Attendance Taker - How to Take Attendance in Zoom Automatically - YouTube, accessed November 28, 2025, [https://www.youtube.com/watch?v=BT2wHu0hG2E](https://www.youtube.com/watch?v=BT2wHu0hG2E)  
55. Identifying guests in the meeting/webinar - Zoom Support, accessed November 28, 2025, [https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066590](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066590)  
56. What is the Attendance Taker for Zoom? - BlueSky, accessed November 28, 2025, [https://help.blueskyapps.org/article/169-what-is-attendance-taker-for-zoom](https://help.blueskyapps.org/article/169-what-is-attendance-taker-for-zoom)  
57. Step-by-Step Guide to Setting Up a Zoom Meeting - Tactiq, accessed November 28, 2025, [https://tactiq.io/learn/setting-up-a-zoom-meeting](https://tactiq.io/learn/setting-up-a-zoom-meeting)  
58. How to Install Zoom Attendance App, accessed November 28, 2025, [https://blueskyapps.org/how-to-install-zoom-attendance-app](https://blueskyapps.org/how-to-install-zoom-attendance-app)  
59. User Name in zoom webhooks is empty, accessed November 28, 2025, [https://devforum.zoom.us/t/user-name-in-zoom-webhooks-is-empty/88171](https://devforum.zoom.us/t/user-name-in-zoom-webhooks-is-empty/88171)  
60. Attendance Tracking : r/Zoom - Reddit, accessed November 28, 2025, [https://www.reddit.com/r/Zoom/comments/1ar32ji/attendance_tracking/](https://www.reddit.com/r/Zoom/comments/1ar32ji/attendance_tracking/)  
61. Configuring LTI Pro 1.3 for Canvas - Zoom Support, accessed November 28, 2025, [https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059611](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0059611)  
62. Using Zoom LTI Pro without pre-provisioning - Instructure Community - 389853, accessed November 28, 2025, [https://community.canvaslms.com/t5/Archived-Questions/Using-Zoom-LTI-Pro-without-pre-provisioning/td-p/389853](https://community.canvaslms.com/t5/Archived-Questions/Using-Zoom-LTI-Pro-without-pre-provisioning/td-p/389853)  
63. FAQ: Zoom LTI Pro in Canvas - MIT Sloan Teaching & Learning Technologies, accessed November 28, 2025, [https://mitsloanedtech.mit.edu/support/faq-zoom-lti-pro/](https://mitsloanedtech.mit.edu/support/faq-zoom-lti-pro/)  
64. Configuring Zoom Events with the Salesforce Lightning app, accessed November 28, 2025, [https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0057644](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0057644)  
65. Configure email showing up for LTI Pro provisioned users - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/configure-email-showing-up-for-lti-pro-provisioned-users/20193](https://devforum.zoom.us/t/configure-email-showing-up-for-lti-pro-provisioned-users/20193)  
66. Wix Member to Member Zoom Meetings - API and Webhooks - Zoom Developer Forum, accessed November 28, 2025, [https://devforum.zoom.us/t/wix-member-to-member-zoom-meetings/21912](https://devforum.zoom.us/t/wix-member-to-member-zoom-meetings/21912)

