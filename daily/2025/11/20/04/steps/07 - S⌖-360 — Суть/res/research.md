https://gemini.google.com/share/0bdc33707b72


## **1. Введение: Концептуальная парадигма и операционная сущность SoftPro 360**

### **1.1. Определение и роль в экосистеме PropTech**

SoftPro 360 (в технической документации часто обозначаемый как Sꕊ или S⌖-360) представляет собой высокоуровневую интеграционную платформу класса middleware, разработанную компанией SoftPro для обеспечения бесшовного, двунаправленного обмена данными между ядром системы управления недвижимостью (SoftPro Select, Standard, Enterprise) и распределенной сетью внешних поставщиков услуг.1 В современной архитектуре PropTech (Property Technology) данное решение выполняет функцию критического связующего звена, устраняя технологический разрыв между внутренними операционными процессами титульных компаний (Title Companies), эскроу-агентов (Escrow Agents) и внешними провайдерами сервисов, таких как андеррайтеры, государственные реестры, нотариусы и финансовые институты.1

Фундаментальная задача Sꕊ заключается в решении проблемы фрагментации данных. В традиционных моделях работы специалисты вынуждены вручную переносить данные из локальной системы (Order Management System) в веб-порталы поставщиков, что порождает высокий риск ошибок ввода (re-keying errors), дублирование информации и временные задержки. SoftPro 360 автоматизирует этот процесс, трансформируя локальные объекты данных заказа в структурированные запросы к API партнеров и обеспечивая автоматический прием и маппинг ответов (документов, метаданных, статусов) обратно в реестр SoftPro без участия оператора.1

### **1.2. Стратегическое позиционирование в продуктовой линейке**

Платформа SoftPro 360 не является автономным коммерческим продуктом, а позиционируется как инфраструктурный компонент, встроенный во все редакции программного обеспечения SoftPro. Это стратегическое решение позволяет стандартизировать протоколы взаимодействия независимо от масштаба бизнеса клиента:

* **SoftPro Select:** Флагманское решение для крупных предприятий, построенное на современной.NET архитектуре. Здесь Sꕊ демонстрирует максимальную гибкость, поддерживая глубокую автоматизацию через SDK и пользовательские скрипты.2  
* **SoftPro Standard и Enterprise:** В классических (legacy) версиях системы SoftPro 360 функционирует как внешний модуль, обеспечивая доступ к той же сети вендоров, но с некоторыми отличиями в механизме интеграции интерфейса.1  
* **SoftPro Hosted:** В облачной инфраструктуре Sꕊ работает в виртуализированной среде, обеспечивая доступ к интеграциям без необходимости локального развертывания серверов интеграции на стороне клиента.6

Доступ к платформе предоставляется бесплатно для пользователей SoftPro, что подчеркивает её роль как инструмента удержания клиентов и повышения ценности основной экосистемы. Монетизация осуществляется через транзакционные модели взаимодействия с вендорами.1

## **2. Технологическая архитектура и протоколы взаимодействия**

Анализ технической документации выявляет гибридную природу архитектуры SoftPro 360, которая вынуждена балансировать между поддержка унаследованных стандартов индустрии и внедрением современных веб-технологий.

### **2.1. Дихотомия протоколов: SOAP и REST**

Платформа поддерживает два основных архитектурных стиля веб-сервисов, выбор которых диктуется спецификой интегрируемого партнера и требованиями к безопасности.

#### **2.1.1. Доминирование SOAP и роль WSDL**

Исторически значительная часть интеграций в сфере страхования титула и взаимодействия с государственными органами базируется на протоколе **SOAP (Simple Object Access Protocol)**. Это обусловлено строгими требованиями к типизации данных и транзакционной надежности.

* **Функция WSDL (Web Services Description Language):** В экосистеме Sꕊ файлы WSDL служат формальным контрактом между SoftPro и сервером вендора. WSDL — это XML-документ, который детерминировано описывает доступные методы (endpoints), структуру запросов и ответов, а также типы данных.8 Для разработчиков интеграций это означает, что любое взаимодействие строго регламентировано: если схема требует передачи LoanAmount как типа decimal, отклонение от этого формата приведет к отказу в обслуживании на уровне валидации XML.10  
* **Безопасность и WS-Security:** Использование SOAP оправдано встроенной поддержкой стандартов WS-Security. Это позволяет реализовать шифрование на уровне сообщения (message-level security), что критически важно при передаче персональных данных (PII) и финансовой информации через публичные сети. В отличие от транспортного шифрования (HTTPS), которое защищает канал, WS-Security защищает сами данные на всем пути следования, даже при прохождении через промежуточные узлы.11

#### **2.1.2. Миграция на REST API**

Для интеграции с современными SaaS-платформами (например, сервисы удаленного нотариата Proof, платформы eRecording) SoftPro 360 активно внедряет **REST (Representational State Transfer)**.

* **Преимущества реализации:** REST API в SoftPro 360 используют формат JSON, который значительно легче XML, что снижает нагрузку на сеть и ускоряет парсинг данных. Архитектура REST является stateless (без сохранения состояния), что упрощает масштабирование и обработку пиковых нагрузок при массовом закрытии сделок в конце месяца.13  
* **Гибкость endpoints:** В отличие от жестких контрактов WSDL, REST-архитектура позволяет более гибко управлять версионированием API и добавлять новые поля данных без нарушения работы существующих клиентов.1

### **2.2. Механизмы аутентификации и управления доступом**

Безопасность доступа к Sꕊ реализована через многоуровневую систему аутентификации, адаптирующуюся под конкретного партнера.

#### **2.2.1. Управление идентификацией пользователя**

Доступ к самому порталу SoftPro 360 осуществляется через единые учетные данные экосистемы SoftPro (mySoftPro или SoftPro LIVE).

* **Процесс первичной регистрации:** Если у пользователя отсутствуют учетные данные, процесс предусматривает регистрацию непосредственно через экран входа в SoftPro 360. Система генерирует временный пароль, отправляемый на верифицированный email, который подлежит обязательной смене при первом входе. Реализована функция "Remember Me", сохраняющая токен сессии для минимизации повторных входов в течение рабочего дня.1

#### **2.2.2. Аутентификация API и ключи доступа (Case Studies)**

Для взаимодействия "System-to-System" используются более сложные механизмы, чем простая пара логин/пароль.

* **Интеграция с Proof (ранее Notarize):** Здесь применяется механизм **API Key**.  
  * Пользователь (или администратор) генерирует полноправный (full-access) API-ключ в личном кабинете Proof.  
  * Этот ключ вводится в настройки сервиса внутри SoftPro 360 (360 > Services > Proof).  
  * *Архитектурная особенность:* Один API-ключ может использоваться всей организацией, так как он идентифицирует корпоративный аккаунт, а не конкретного оператора. Однако поддерживается и гранулярная настройка с индивидуальными ключами для повышения безопасности аудита.16  
  * *Работа с филиалами:* Важным нюансом является поддержка дочерних организаций (Child Organizations). Архитектура не допускает транзитной маршрутизации через родительский ключ; для каждого дочернего подразделения требуется генерация и ввод уникального API-ключа.16  
* **Интеграция с First American AgentNet:** Используется проприетарный механизм **User Access Key**.  
  * Вместо передачи пароля, который может быть скомпрометирован или изменен, пользователь генерирует специальный ключ доступа в профиле AgentNet.  
  * Этот ключ копируется и вставляется в поле конфигурации SoftPro 360. Это обеспечивает изоляцию учетных данных: смена пароля пользователем на портале AgentNet не нарушает настроенную интеграцию в SoftPro.17

### **2.3. Инструментарий разработки (SDK) и расширяемость**

Для обеспечения глубокой кастомизации SoftPro Select предоставляет разработчикам доступ к Software Development Kits (SDK) через репозиторий NuGet. Это позволяет внутренним IT-командам и партнерам создавать собственные модули, взаимодействующие с ядром системы и SoftPro 360.

| Пакет SDK | Назначение и функциональность | Зависимости |
| :---- | :---- | :---- |
| **SoftPro.Select.Core.Sdk** | Базовый фундамент разработки. Содержит основные библиотеки для взаимодействия с объектной моделью данных SoftPro (Order Object Model). Необходим для создания любых типов приложений (консольных, серверных, клиентских). Ориентирован на.NET Framework 4.6+.4 | Нет |
| **SoftPro.Select.Shell.Sdk** | Инструментарий для модификации клиентского интерфейса (Select Client). Позволяет создавать новые экраны, меню, кнопки, панели инструментов и интегрировать их в визуальную оболочку (Shell). Используется для создания пользовательских интерфейсов вызова сервисов 360.4 | Зависит от Core.Sdk |
| **SoftPro.Select.Server.Sdk** | Предназначен для разработки серверной логики, выполняемой на уровне приложений (mid-tier). Это критично для реализации фоновых процессов, валидации данных и интеграционных шлюзов, которые должны работать независимо от активности конкретного пользователя.4 | Зависит от Core.Sdk |

Использование этих SDK позволяет, например, написать скрипт на C#, который при сохранении заказа проверяет наличие определенных документов и, если они отсутствуют, автоматически инициирует запрос к API через SoftPro 360.

## **3. Детальный анализ экосистемы интеграций**

Функциональная мощь Sꕊ раскрывается через специализированные категории интеграций. Ниже приведен детальный анализ ключевых модулей с учетом специфики их работы и уникальных возможностей.

### **3.1. Андеррайтинг: CPL и Полисные Жакеты**

Автоматизация взаимодействия с андеррайтерами является ядром функциональности для титульных агентов.

* **Механизм работы:** При инициировании заказа CPL (Closing Protection Letter) данные извлекаются непосредственно из полей заказа SoftPro (информация о покупателе, продавце, кредиторе, сумме покрытия). Система формирует SOAP-запрос, соответствующий WSDL-схеме конкретного андеррайтера.  
* **Уникальные возможности партнеров:**  
  * **Westcor Land Title Insurance Company:** Реализована полная автоматизация заказа CPL и жакетов. Уникальной функцией является *Dual CPL Support* (одновременная генерация писем для разных бенефициаров) и *Update Jacket Feature* (обновление данных полиса без его перевыпуска). Также доступен специализированный экран эндорсментов (endorsement screen) с кодами и премиями.7  
  * **WFG National Title Insurance Company:** Позволяет не только генерировать документы, но и запрашивать "title evidence" (доказательства титула) и проводить поиск непосредственно из интерфейса.7  
  * **First National Title Insurance Company:** Интеграция поддерживает функции редактирования (Edit) и аннулирования (Void) выпущенных CPL и жакетов прямо из рабочего пространства SoftPro, что обновляет статус документа на стороне андеррайтера в реальном времени.20  
  * **Stewart Title Guaranty Company:** Обеспечивает возможность выбора агентства и локации (Agency Location selection) внутри интерфейса интеграции, что важно для мульти-офисных агентов.21

### **3.2. Титульный поиск и работа с данными (Title Search & Data)**

Интеграция в этом сегменте перешла от простого получения PDF-отчетов к передаче структурированных данных.

* **Property Insight (TitlePoint):** Одна из самых глубоких интеграций. Позволяет запускать сложные поисковые запросы (property, tax, name searches) и получать результаты не только в виде образов документов (Images), но и как метаданные, готовые к импорту. Реализована поддержка *Xpress Search* и *Legal & Vesting brief searches*.22  
* **Title Data, Inc. (TDI):** Для пользователей в Техасе и других регионах присутствия TDI реализована автоматизация открытия заказа. Система не только возвращает результаты поиска (run sheet) в папку вложений, но и автоматизирует обратную выгрузку — загрузку готовых обязательств (commitments) и полисов в цифровую библиотеку TDI (Starter Library) для участия в программе обмена данными (Starter Share Program).7  
* **MaestroX и Pippin Title:** Предоставляют сервисы поиска с возможностью трекинга статуса заказа в реальном времени, устраняя необходимость телефонных уточнений.7

### **3.3. Электронная регистрация (eRecording)**

Модуль eRecording трансформирует физический процесс подачи документов в цифровой поток.

* **Партнеры:** Ключевыми игроками являются **CSC** и **ePN (eRecording Partners Network)**, обеспечивающие покрытие тысяч округов США.  
* **Рабочий процесс:** Пользователь выбирает документы для регистрации, система валидирует их на соответствие требованиям конкретного округа (через API партнера) и отправляет пакет. После регистрации (recording) документ возвращается в SoftPro уже с проставленным штампом регистратора (recording stamp), а данные о фактических комиссиях (recording fees) автоматически обновляют бухгалтерский леджер заказа.7

### **3.4. Нотариат и цифровое закрытие (eClosing & RON)**

Этот сегмент демонстрирует наиболее активное внедрение REST API и современных сценариев взаимодействия.

* **Proof (ранее Notarize):**  
  * Помимо стандартного аутсорсинга нотариальных действий, интеграция поддерживает функцию **In-House Notaries (IHN)**. Это позволяет титульной компании использовать платформу Proof, но назначать транзакции своим собственным сотрудникам-нотариусам. В интерфейсе SoftPro выбирается опция "Review document package", и транзакция маршрутизируется во внутренний пул нотариусов. Если внутренние ресурсы заняты, можно использовать механизм переполнения (overflow) на сеть Proof.16  
* **SoftPro Sign:** Собственное решение компании, предлагающее бесшовный опыт eSign и RON. Документы отправляются на подпись, участники получают уведомления, а подписанные копии автоматически архивируются в деле.7  
* **Pre-Closing Docs (NextDeal):** Сервис **preDOCS** автоматизирует сбор предварительной информации от покупателей и продавцов через защищенные опросники, результаты которых (включая e-signed документы) возвращаются в файл SoftPro.7

### **3.5. Финансовые сервисы и Эскроу**

* **Deluxe Payment Exchange (DPX):** Революционизирует процесс выплат, заменяя бумажные чеки на цифровые (eChecks). Это позволяет отправлять средства мгновенно и с меньшими затратами, при этом сохраняя привычный процесс согласования и выписки чеков внутри интерфейса SoftPro.25  
* **TrustLink:** Сервис автоматической сверки (reconciliation) трастовых счетов. Интеграция обеспечивает ежедневную и ежемесячную передачу данных о транзакциях для внешнего аудита и сверки, снижая риски мошенничества и ошибок.7

## **4. Уникальная технология SoftPro Sync: B2B Экосистема**

Особняком в архитектуре SoftPro 360 стоит технология **SoftPro Sync**, которая позволяет пользователям SoftPro взаимодействовать друг с другом напрямую, создавая закрытую экосистему обмена данными.

### **4.1. Ролевая модель: Requestor и Provider**

В отличие от интеграции с внешним вендором, здесь обе стороны используют ПО SoftPro.

* **Requestor (Заказчик):** Обычно это титульный агент или эскроу-офицер. Он инициирует заказ услуги (например, абстракт титула или поиск).  
* **Provider (Поставщик):** Другой пользователь SoftPro (например, независимый абстрактор), который принимает заказ.26

### **4.2. Механизм синхронизации данных**

Техническая реализация Sync исключает необходимость ручного создания заказа на стороне Поставщика.

1. **Отправка:** Заказчик отправляет запрос через Sync.  
2. **Прием:** Поставщик получает уведомление и транзакцию в свою очередь 360 Queue. При принятии заказа система автоматически создает новый файл в SoftPro Поставщика, заполняя его данными из запроса (имена, адреса, суммы).  
3. **Исполнение и возврат:** Поставщик выполняет работу и отправляет результаты обратно.  
4. **Слияние данных (Data Merge):** Заказчик получает данные. Интерфейс Sync отображает сравнение: **Current Value** (текущее значение в поле) и **New Value** (значение, присланное Поставщиком). Заказчик может выборочно принять изменения, которые перезапишут текущие данные, или отклонить их. Это обеспечивает контроль целостности данных перед их импортом в живой заказ.26

## **5. Системные требования и параметры развертывания**

Для обеспечения стабильной работы интеграционного шлюза, особенно в условиях интенсивного обмена данными, инфраструктура клиента должна соответствовать определенным спецификациям. Важно отметить различие требований для локальных и облачных версий.

### **5.1. Аппаратные и программные требования (On-Premise)**

Ниже представлена сводная таблица требований для рабочей станции **SoftPro Select Client**, где происходит непосредственная работа с модулями 360.

| Компонент | Минимальные требования | Рекомендуемые требования | Комментарий архитектора |
| :---- | :---- | :---- | :---- |
| **Операционная система** | Windows 10 (64-bit) | Windows 10/11 (64-bit) | Поддержка 32-битных ОС прекращена для современных версий клиента. Требуется.NET Framework 4.6+.28 |
| **Оперативная память (RAM)** | 4 GB | **12 GB и выше** | Большой объем RAM критичен при одновременной работе с тяжелыми пакетами интеграции и открытыми документами Word.28 |
| **Процессор** | Dual Core | Quad Core | Обработка XML/JSON сериализации и рендеринг документов требуют вычислительной мощности.29 |
| **Дисковое пространство** | 2 GB (свободно) | SSD | Высокая скорость Disk I/O (IOPS) критична для производительности базы данных SQL Server.30 |
| **Офисный пакет** | Word 2013 | Word 2016/2019/365 | Необходим для работы движка слияния документов (Document Merge) и функционала Ready Docs.29 |

### **5.2. Сетевые требования и Hosted-специфика**

* **Доступ в Интернет:** Для работы SoftPro 360 необходим стабильный доступ к доменам softprocorp.com и API-endpoints конкретных вендоров по протоколу HTTPS (порт 443).  
* **SoftPro Hosted:** В этой конфигурации все вычислительные нагрузки переносятся на сервера SoftPro. От клиента требуется лишь надежное интернет-соединение и "тонкий" клиент (RDP/Citrix-подобный доступ), что снимает нагрузку с локального железа, но повышает требования к пропускной способности канала.6

## **6. Портал документов и обновлений (SoftPro Documents Portal)**

Отдельного внимания заслуживает новый механизм дистрибуции контента — **SoftPro Documents Portal** (docs.softprocorp.com). Это централизованный репозиторий, обеспечивающий compliance (соответствие нормативным требованиям).

* **Функциональность:** Портал служит библиотекой всех пакетов документов (штатные, федеральные, андеррайтерские формы).  
* **Интеграция с Select:** Пользователи SoftPro Select имеют преимущество автоматической интеграции. Они могут создавать персонализированные списки наблюдения ("Watchlist"). Когда андеррайтер обновляет форму полиса, система присылает уведомление, и пакет можно загрузить и инсталлировать в систему "на лету" без сложных процедур обновления ПО.  
* **Ограничение для Standard/Enterprise:** На текущий момент автоматическая загрузка через портал доступна только для Select; пользователи классических версий вынуждены использовать ручной режим загрузки обновлений.31

## **7. Экономическая эффективность и бизнес-модель**

Внедрение SoftPro 360 оказывает прямое влияние на операционную рентабельность бизнеса недвижимости.

### **7.1. Модель затрат**

* **Лицензирование:** Использование самой платформы SoftPro 360 предоставляется бесплатно всем клиентам SoftPro. Нет ежемесячной абонентской платы за доступ к порталу.1  
* **Транзакционные издержки:** Оплата производится только за фактически потребленные услуги (pay-per-use). Например, плата за eRecording взимается за каждый документ, плата за CPL — за каждое письмо.  
* **Партнерские программы:** Благодаря эффекту масштаба, SoftPro договаривается о специальных тарифах (preferred rates) с вендорами. Ярким примером является партнерство с **EC Purchasing**, которое дает пользователям SoftPro доступ к корпоративным скидкам на офисные товары, логистику (FedEx, UPS) и услуги связи, без членских взносов.1

### **7.2. ROI и операционные метрики**

Основная экономическая выгода формируется за счет снижения OPEX (операционных расходов):

1. **Устранение избыточного труда:** Автоматический перенос данных экономит от 15 до 30 минут на файл, которые ранее тратились на ручной ввод данных на сайтах вендоров.  
2. **Снижение рисков (Risk Mitigation):** Исключение ошибок ручного ввода (опечатки в суммах займа, именах) снижает риск отказов в регистрации, финансовых потерь и репутационных издержек. Точность данных (Data Integrity) гарантируется тем, что данные берутся непосредственно из первоисточника (системы SoftPro).2

## **8. Заключение**

Анализ архитектуры и функциональных возможностей SoftPro 360 (Sꕊ) позволяет сделать вывод, что данная платформа является не просто вспомогательным модулем, а **стратегическим активом** для любой компании, использующей экосистему SoftPro.

Технологическая зрелость решения, подтверждаемая поддержкой как надежных протоколов SOAP/WSDL для критических финансовых операций, так и гибких REST API для современных сервисов, обеспечивает долгосрочную актуальность платформы. Глубокая интеграция с ведущими игроками рынка (ClosingCorp, Proof, Westcor, TitlePoint) и уникальные возможности B2B-синхронизации (Sync) создают замкнутый цифровой контур, который невозможно воспроизвести при использовании разрозненных программных решений.

Для пользователей SoftPro отказ от использования возможностей 360 в пользу ручных процессов является экономически необоснованным, так как это игнорирует доступные инструменты повышения эффективности и снижения операционных рисков, предоставляемые в рамках уже оплаченной лицензии на основное ПО.

#### **Works cited**

1. Get Started with SoftPro 360, accessed November 24, 2025, [https://info.softprocorp.com/get-started-with-softpro-360](https://info.softprocorp.com/get-started-with-softpro-360)  
2. SoftPro Select - Real Estate Closing Software, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-select/](https://www.softprocorp.com/real-estate-software-solutions/softpro-select/)  
3. SoftPro 360: Your Free Vendor Portal - YouTube, accessed November 24, 2025, [https://www.youtube.com/watch?v=FSpxmD4UAzU](https://www.youtube.com/watch?v=FSpxmD4UAzU)  
4. SoftPro - NuGet Gallery, accessed November 24, 2025, [https://www.nuget.org/profiles/SoftPro](https://www.nuget.org/profiles/SoftPro)  
5. SoftPro Standard - Real Estate Software Package, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-standard/](https://www.softprocorp.com/real-estate-software-solutions/softpro-standard/)  
6. Real Estate Hosted Software Data - SoftPro, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-hosted-software/](https://www.softprocorp.com/real-estate-software-solutions/softpro-hosted-software/)  
7. SoftPro 360 Integrations, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/softpro-360-data-integration/](https://www.softprocorp.com/real-estate-software-solutions/softpro-360-data-integration/)  
8. What is WSDL? - HarmonyERP, accessed November 24, 2025, [https://www.harmonyerp.cloud/en/what-is-wsdl/](https://www.harmonyerp.cloud/en/what-is-wsdl/)  
9. Web Services Description Language - Wikipedia, accessed November 24, 2025, [https://en.wikipedia.org/wiki/Web_Services_Description_Language](https://en.wikipedia.org/wiki/Web_Services_Description_Language)  
10. ELI5 : What is WSDL and how exactly is it used? (Please include real world examples) : r/webdev - Reddit, accessed November 24, 2025, [https://www.reddit.com/r/webdev/comments/3buwmv/eli5_what_is_wsdl_and_how_exactly_is_it_used/](https://www.reddit.com/r/webdev/comments/3buwmv/eli5_what_is_wsdl_and_how_exactly_is_it_used/)  
11. REST vs. SOAP: What is the difference? - Document360, accessed November 24, 2025, [https://document360.com/blog/rest-vs-soap/](https://document360.com/blog/rest-vs-soap/)  
12. The difference between the Web Service - API, WSDL, SOAP, REST, Simply that the farmers understand :) - DEV Community, accessed November 24, 2025, [https://dev.to/mrgreenfz/the-difference-between-the-web-service-api-wsdl-soap-rest-simple-that-the-farmers-understand-7k4](https://dev.to/mrgreenfz/the-difference-between-the-web-service-api-wsdl-soap-rest-simple-that-the-farmers-understand-7k4)  
13. SOAP vs REST - Difference Between API Technologies - AWS, accessed November 24, 2025, [https://aws.amazon.com/compare/the-difference-between-soap-rest/](https://aws.amazon.com/compare/the-difference-between-soap-rest/)  
14. REST vs. SOAP - Red Hat, accessed November 24, 2025, [https://www.redhat.com/en/topics/integration/whats-the-difference-between-soap-rest](https://www.redhat.com/en/topics/integration/whats-the-difference-between-soap-rest)  
15. SOAP vs REST: What's the Difference? - SmartBear, accessed November 24, 2025, [https://smartbear.com/blog/soap-vs-rest-whats-the-difference/](https://smartbear.com/blog/soap-vs-rest-whats-the-difference/)  
16. SoftPro integration setup instructions - Proof Help Center, accessed November 24, 2025, [https://support.proof.com/hc/en-us/articles/6934762785175-SoftPro-integration-setup-instructions](https://support.proof.com/hc/en-us/articles/6934762785175-SoftPro-integration-setup-instructions)  
17. User Access Key Management for SoftPro 360 - First American, accessed November 24, 2025, [https://registration.firstam.com/EA/AgentNetIntegrationTraining/Content/SoftPro/useraccesskeymanagement.pdf?utm_source=sfmc&utm_medium=email&utm_campaign=AGN+-+SoftPro+Authentication_Jan2024+-+INT&utm_term=Refer+to+the+attached+guide+for+setup+instructions.&utm_id=155516&sfmc_id=4178232](https://registration.firstam.com/EA/AgentNetIntegrationTraining/Content/SoftPro/useraccesskeymanagement.pdf?utm_source=sfmc&utm_medium=email&utm_campaign=AGN+-+SoftPro+Authentication_Jan2024+-+INT&utm_term=Refer+to+the+attached+guide+for+setup+instructions.&utm_id=155516&sfmc_id=4178232)  
18. SoftPro.Select.Core 4.6.8 - NuGet, accessed November 24, 2025, [https://www.nuget.org/packages/SoftPro.Select.Core](https://www.nuget.org/packages/SoftPro.Select.Core)  
19. SoftPro.Select.Core.Sdk 4.5.5 - NuGet, accessed November 24, 2025, [https://www.nuget.org/packages/SoftPro.Select.Core.Sdk](https://www.nuget.org/packages/SoftPro.Select.Core.Sdk)  
20. First National User Guide (v1.0), accessed November 24, 2025, [https://fnti.com/wp-content/uploads/2020/06/First-National-Title-SoftPro360-User-Guide.pdf](https://fnti.com/wp-content/uploads/2020/06/First-National-Title-SoftPro360-User-Guide.pdf)  
21. Stewart 2.1 User Guide, accessed November 24, 2025, [https://www.stewart.com/content/dam/PI/Products/StewartAccess/StewartIntegrationSoftpro2_1.pdf](https://www.stewart.com/content/dam/PI/Products/StewartAccess/StewartIntegrationSoftpro2_1.pdf)  
22. Introducing TitlePoint Integration in SoftPro 360!, accessed November 24, 2025, [https://blog.softprocorp.com/introducing-titlepoint-integration-in-softpro-360](https://blog.softprocorp.com/introducing-titlepoint-integration-in-softpro-360)  
23. Integrations - SoftPro Blog, accessed November 24, 2025, [https://blog.softprocorp.com/topic/integrations](https://blog.softprocorp.com/topic/integrations)  
24. SoftPro - SoftPro Eclosings for Complete Transactions, accessed November 24, 2025, [https://www.softprocorp.com/real-estate-software-solutions/eclosings/](https://www.softprocorp.com/real-estate-software-solutions/eclosings/)  
25. Introducing the Deluxe Payment Exchange Integration in SoftPro Select, accessed November 24, 2025, [https://blog.softprocorp.com/introducing-deluxe-payment-exchange-integration-in-softpro-select](https://blog.softprocorp.com/introducing-deluxe-payment-exchange-integration-in-softpro-select)  
26. Resources for the SoftPro Sync integration in SoftPro 360, accessed November 24, 2025, [https://info.softprocorp.com/resources-for-softpro-sync-integration-in-softpro-360](https://info.softprocorp.com/resources-for-softpro-sync-integration-in-softpro-360)  
27. Sync User Guide for Sync User Guide for Title Providers Providers Providers V1.0 - SoftPro, accessed November 24, 2025, [https://info.softprocorp.com/hubfs/Sync%20User%20Guide%20-%20Title%20Provider%20v1.pdf?hsCtaTracking=f7db4a5b-524a-4a3f-9ceb-95b9c83d7d37%7C3f5b1268-55b1-4f1c-9eb8-2143f7f9faa8](https://info.softprocorp.com/hubfs/Sync%20User%20Guide%20-%20Title%20Provider%20v1.pdf?hsCtaTracking=f7db4a5b-524a-4a3f-9ceb-95b9c83d7d37%7C3f5b1268-55b1-4f1c-9eb8-2143f7f9faa8)  
28. SoftPro System Requirements – Hosted, accessed November 24, 2025, [https://www.softprocorp.com/softpro-system-requirements-hosted/](https://www.softprocorp.com/softpro-system-requirements-hosted/)  
29. SoftPro Select System Requirements, accessed November 24, 2025, [https://www.softprocorp.com/softpro-system-requirements-select/](https://www.softprocorp.com/softpro-system-requirements-select/)  
30. SoftPro System Requirements – Standard, accessed November 24, 2025, [https://www.softprocorp.com/softpro-system-requirements-standard/](https://www.softprocorp.com/softpro-system-requirements-standard/)  
31. SoftPro - Document and Report Downloads, accessed November 24, 2025, [https://www.softprocorp.com/resources/underwriting-documents/](https://www.softprocorp.com/resources/underwriting-documents/)  
32. SoftPro Documents Portal - Select, accessed November 24, 2025, [https://info.softprocorp.com/softpro-documents-portal-select](https://info.softprocorp.com/softpro-documents-portal-select)  
33. Introducing EC Purchasing Partnership in SoftPro 360!, accessed November 24, 2025, [https://blog.softprocorp.com/introducing-ec-purchasing-partnership-in-softpro-360](https://blog.softprocorp.com/introducing-ec-purchasing-partnership-in-softpro-360)