https://g.co/gemini/share/6a13424eb95f

Инструкция для T1⁎ (Планирование миграции Stripe)

Эта инструкция описывает шаги, необходимые для планирования миграции и консолидации двух исходных аккаунтов Stripe (Source Accounts: US и International) в новый единый аккаунт Stripe US (Target Account). 
План включает определение шагов миграции (PAN copy), маппинг продуктов, цен, налогов, пробных периодов и метаданных, а также определение рисков, верификации и плана отката.

1. Аудит и Определение Объема Данных (Audit and Data Scoping)

1.1. Определить ограничения автоматической миграции данных.
Зафиксировать типы данных, которые могут и не могут быть автоматически скопированы между аккаунтами Stripe.

1.1.1. Данные, которые копируются: Объекты `Customer` и связанные с ними платежные данные (например, `Card` objects, `PaymentMethod` objects).

1.1.2. Данные, которые НЕ копируются: `Subscriptions`, `Products`, `Prices` (или `Plans`), `Coupons`, `Invoices`, `Charges`, `PaymentIntents`, `Events`, `Logs`.

Обоснование: Документация Stripe четко определяет границы автоматического копирования. Это понимание критически важно для определения объема работ по программному воссозданию логики биллинга.

Источник: Stripe Docs, "Copy PAN data across Stripe accounts":
> We only copy the raw Customer objects and associated payment data objects.
(Перевод: Мы копируем только сырые объекты Customer и связанные с ними объекты платежных данных.)
> We can't copy individual Charges, PaymentIntents, Invoices, Plans, Subscriptions, Coupons, Events, Logs [...] or any other Stripe objects.
(Перевод: Мы не можем копировать отдельные Charges, PaymentIntents, Invoices, Plans, Subscriptions, Coupons, Events, Logs [...] или любые другие объекты Stripe.)

1.2. Проанализировать используемые методы интеграции и версии API.

1.2.1. Определить, используют ли текущие интеграции устаревшие API (Charges API, Sources API) или современные (Payment Intents API, Payment Methods API).

Обоснование: Устаревшие интеграции могут иметь ограничения при миграции данных и усложнять соблюдение комплаенса. Например, интеграции на Charges API не готовы к Strong Customer Authentication (SCA) и могут привести к высокому уровню отклоненных платежей.

Источник: Stripe Docs, "Strong Customer Authentication readiness":
> Integrations that aren't SCA-ready, like those using the legacy Charges API, might see high rates of declines from banks that enforce SCA.
(Перевод: Интеграции, не готовые к SCA, например, использующие устаревший Charges API, могут столкнуться с высоким уровнем отказов со стороны банков, применяющих SCA.)

1.2.2. Проверить Default API version в настройках аккаунтов («Developers» → «API keys» → «API version»).

Обоснование: Поведение API может различаться в зависимости от версии. Скрипты миграции должны использовать консистентную версию API для корректного извлечения данных.

1.3. Идентифицировать используемые платежные методы (Payment Methods).

1.3.1. Определить, используются ли в International Source Account локальные платежные методы (Local Payment Methods, LPMs), такие как SEPA Direct Debit или Bacs Direct Debit.

1.3.2. В случае использования LPMs, определить, хранятся ли они как устаревшие `Source` объекты (`src_...`) или как современные `PaymentMethod` объекты (`pm_...`).

Обоснование: Стандартный инструмент копирования имеет ограничения. Некоторые LPMs, сохраненные как `Source` объекты, не могут быть скопированы.

Источник: Stripe Docs, "Copy PAN data across Stripe accounts":
> We can't copy Single Euro Payments Area (SEPA) stored as source objects, Bacs Direct Debit, or pre-authorized debit payments (PADs)...
(Перевод: Мы не можем копировать Single Euro Payments Area (SEPA), сохраненные как объекты source, Bacs Direct Debit или pre-authorized debit payments (PADs)...)

Если используются `Source` объекты для LPMs, необходимо запланировать предварительную миграцию на `PaymentMethod` объекты в Source Account.

1.4. Провести аудит международного комплаенса (SCA).

1.4.1. Определить долю подписчиков из European Economic Area (EEA) в международном аккаунте.

1.4.2. Проверить наличие сохраненных мандатов (Mandates) и готовность интеграции к обработке Merchant-Initiated Transactions (MIT).

Обоснование: При миграции клиентов из EEA необходимо соблюдать требования SCA. Если доказательства аутентификации не будут корректно обработаны, клиентам может потребоваться повторная 3D Secure аутентификация, что приведет к увеличению оттока (churn).

Источник: Stripe Docs, "SCA migration guide for Billing".

1.5. Проанализировать использование `metadata`.
Определить, какие ключевые данные хранятся в `metadata` объектов `Customer`, `PaymentMethod` и `Subscription` (например, идентификаторы Kajabi).

Обоснование: `Metadata` объектов `Customer` и `PaymentMethod` копируются вместе с объектами. `Metadata` объектов `Subscription` необходимо извлечь и перенести при воссоздании подписок.

Источник: Stripe Support, "Data that can be copied between Stripe accounts":
> You can copy the following data types... Metadata associated with the Stripe customer object... Metadata associated with the Stripe object for a particular payment type...
(Перевод: Вы можете скопировать следующие типы данных... Метаданные, связанные с объектом клиента Stripe... Метаданные, связанные с объектом Stripe для определенного типа платежа...)

2. Стратегия Консолидации и Конфигурация Целевого Аккаунта

2.1. Оценить стратегические риски консолидации в США.
Оценить потенциальное влияние консолидации глобальных операций в едином аккаунте США на уровень авторизации из-за кросс-граничного эквайринга (cross-border acquiring).

Обоснование: Обработка международных карт через эквайринг США часто приводит к более низкому уровню авторизации по сравнению с использованием локального эквайринга (например, европейского аккаунта).

Источник: Stripe Guide, "Optimising authorization rates":
> Using locally optimised acquiring services helps you maximise acceptance rates (because banks are often more likely to approve domestic payments)...
(Перевод: Использование локально оптимизированных услуг эквайринга помогает максимизировать уровень одобрения (потому что банки часто более склонны одобрять внутренние платежи)...)

В качестве альтернативы рассмотреть использование Stripe Organizations для централизованного управления при сохранении отдельных локальных аккаунтов (США и ЕС).

2.2. Подготовить Target Account.

2.2.1. Убедиться, что Target Account активирован (Activated).

Обоснование: Копирование данных возможно только в активированный аккаунт.
Источник: Stripe Docs, "Copy PAN data across Stripe accounts":
> The recipient account must be an activated account.
(Перевод: Аккаунт-получатель должен быть активированным аккаунтом.)

2.2.2. Настроить параметры Stripe Billing, включая Smart Retries, Card Account Updater (CAU) и Network Tokens.

Обоснование: После миграции ожидается временное снижение Authorization Rate. Эти инструменты критически важны для минимизации потерь дохода и снижения недобровольного оттока (involuntary churn). Smart Retries используют машинное обучение для оптимизации времени повторных попыток оплаты.

Источник: Stripe Guide, "Optimizing authorization rates".

2.3. Определить стратегию налогового комплаенса.
Разработать стратегию управления глобальными налогами (VAT, GST, Sales Tax). Рассмотреть активацию и настройку Stripe Tax в Target Account для автоматизации.

Обоснование: Консолидация международных операций требует унифицированного подхода к соблюдению налогового законодательства в разных юрисдикциях. (Источник: Stripe Docs, "Get started with Stripe Tax").

3. Стратегия Маппинга Продуктов и Цен (Product and Price Mapping)

3.1. Определить стратегию идентификации.

3.1.1. Для объектов `Product` и устаревших `Plan` (если используются): стремиться использовать те же идентификаторы (IDs) в Target Account, что и в Source Accounts.

Обоснование: Stripe рекомендует по возможности использовать те же ID для упрощения маппинга.
Источник: Stripe Support, "Recreate subscriptions and plans after moving customer data to a new Stripe account":
> When recreating the plans, specify the same id for each plan as on your former account.
(Перевод: При воссоздании планов укажите тот же id для каждого плана, что и в вашем прежнем аккаунте.)

3.1.2. Для современных объектов `Price`: запланировать использование альтернативных методов маппинга, таких как `lookup_key` или `metadata`, для хранения старого идентификатора.

Обоснование: В отличие от Products API и Plans API, современный Prices API не позволяет указать `id` при создании объекта.

Источник: Stripe API Reference, "Create a product" (параметр `id` доступен); "Create a price" (параметр `id` недоступен).

3.2. Создать таблицу соответствия (Mapping Table).

3.2.1. Извлечь все `Product`, `Price`/`Plan`, `Tax Rate`, `Coupon` из обоих Source Accounts через API.

3.2.2. Структурировать данные в единую таблицу, включающую все параметры: `id`, `currency`, `unit_amount`, `recurring.interval`, `tax_behavior`, `metadata`.

3.2.3. Определить соответствие между объектами из разных Source Accounts (например, консолидация мультивалютных цен).

3.3. Определить процесс воссоздания объектов.
Разработать скрипт для создания всех необходимых объектов в Target Account на основе Mapping Table и заполнить таблицу новыми идентификаторами (если применимо).

4. Определение Процедуры Миграции Данных (PAN Copy Steps)

4.1. Выбрать метод копирования.
Использовать инструмент Self-serve copy migration в Stripe Dashboard.

Обоснование: Это рекомендуемый Stripe безопасный и соответствующий PCI-compliant способ переноса конфиденциальных платежных данных между аккаунтами.
Источник: Stripe Docs, "Migrate payment data":
> If you want to transfer data between two Stripe accounts, complete a self-serve copy migration.
(Перевод: Если вы хотите перенести данные между двумя аккаунтами Stripe, выполните миграцию методом self-serve copy.)

4.2. Оценить риски Card Account Updater (CAU).
Принять решение о временном отключении CAU в Target Account на время миграции, если необходимо избежать дополнительных комиссий за обновление истекших карт.

Обоснование: CAU может автоматически обновлять скопированные карты, что приводит к дополнительным расходам.

Источник: Stripe Docs, "Copy PAN data across Stripe accounts":
> This can result in additional CAU fees for the destination account.
(Перевод: Это может привести к дополнительным комиссиям CAU для целевого аккаунта.)

4.3. Определить последовательность действий для инициации копирования (Действия Sender).

4.3.1. В Source Account перейти в «Customers».
4.3.2. Нажать «Copy customers».
4.3.3. В поле «Copy Method» выбрать «Copy all customers».
4.3.4. Ввести идентификатор Target Account (`acct_xxxx`) и нажать «Continue».
4.3.5. Нажать «Confirm».

Обоснование: Стандартная процедура инициации копирования. (Источник: Stripe Docs, "Copy PAN data across Stripe accounts", раздел "Share customer data with the recipient").

4.4. Определить последовательность действий для авторизации копирования (Действия Recipient).

4.4.1. В Target Account перейти в «Customers».
4.4.2. Найти баннер с уведомлением о запросе.
4.4.3. Нажать «Authorize and Accept».

Обоснование: Копирование начнется только после авторизации получателем. (Источник: Stripe Docs, "Copy PAN data across Stripe accounts", раздел "Authorize and accept customer data from the sender").

4.5. Запланировать время выполнения.
Заложить до 72 часов на завершение процесса копирования после авторизации.

Источник: Stripe Docs, "Copy PAN data across Stripe accounts":
> Most data copies finish within 72 hours...
(Перевод: Большинство операций копирования данных завершаются в течение 72 часов...)

4.6. Определить процедуру получения и обработки файла соответствия (Mapping File).

4.6.1. После завершения копирования скачать CSV файл соответствия в разделе «Documents» Target Account.

4.6.2. Разработать механизм обработки этого файла скриптом миграции.

Обоснование: При копировании идентификаторы платежных методов (`PaymentMethod` IDs) изменяются. Файл соответствия содержит маппинг старых ID на новые ID. Идентификаторы `Customer` ID не изменяются.

Источник: Stripe Docs, "Copy PAN data across Stripe accounts":
> The copy process assigns new object IDs of the same payment type to payment data...
(Перевод: Процесс копирования назначает новые идентификаторы объектов того же типа платежным данным...)
> The copy operation doesn't change customer IDs...
(Перевод: Операция копирования не изменяет идентификаторы клиентов...)

5. Стратегия Воссоздания Подписок (Subscription Recreation Strategy)

5.1. Выбор инструмента миграции.
Для сложной консолидации рекомендуется разработка кастомного скрипта с использованием Stripe API, а не использование Stripe Billing Migration Toolkit (CSV-based).

Обоснование: Кастомный скрипт обеспечивает необходимую гибкость для обработки сложного маппинга данных из двух источников, управления ошибками и интеграции с Kajabi.

5.2. Обеспечение непрерывности цикла биллинга.
Спланировать использование параметра `billing_cycle_anchor` (или `trial_end`) при создании новой подписки через API. Значение должно быть равно дате следующего платежа (`current_period_end`) исходной подписки.

Обоснование: Это критически важно для предотвращения немедленного или двойного списания средств.

Источник: Stripe Support, "Recreate subscriptions and plans after moving customer data to a new Stripe account":
> If you want to use the same billing dates on the new account as you did on the old account, you can force the billing period of subscriptions on the new account by setting a custom trial end date when you create them.
(Перевод: Если вы хотите использовать те же даты биллинга в новом аккаунте, что и в старом, вы можете принудительно установить период биллинга для подписок в новом аккаунте, установив пользовательскую дату окончания пробного периода при их создании.)

5.3. Отключение прораций.
При создании новых подписок установить параметр `proration_behavior` в значение `none`.

Обоснование: Поскольку это миграция существующих обязательств, а не изменение плана в середине цикла, прорации рассчитываться не должны. (Источник: Stripe API Reference, "Create a subscription").

5.4. Обеспечение идемпотентности скриптов.
Спроектировать скрипты миграции с использованием `Idempotency Keys` при всех вызовах API, создающих объекты.

Обоснование: Это позволяет безопасно перезапускать скрипты в случае сбоев, не создавая дубликатов подписок или клиентов.

Источник: Stripe Docs, "Idempotent requests":
> The API supports idempotency for safely retrying requests without accidentally performing the same operation twice.
(Перевод: API поддерживает идемпотентность для безопасного повторения запросов без случайного выполнения одной и той же операции дважды.)

5.5. Определить стратегию синхронизации данных (Delta Synchronization).
Разработать механизм для отслеживания и миграции изменений, произошедших в Source Accounts между моментом запроса на PAN copy и фактическим переключением (Cutover).

Обоснование: Процесс PAN copy может занять до 72 часов (см. 4.5). Необходимо учесть новые подписки, отмены или обновления платежных методов, произошедшие в этот период. Это может потребовать использования Webhooks или инкрементального копирования. (Источник: Stripe Docs: "Migration checklist").

6. План Управления Рисками (Risk Management Plan)

6.1. Риск: Потеря дохода (MRR) из-за ошибок при воссоздании подписок (двойные списания, пропущенные платежи, некорректные суммы).

Смягчение: Провести многоэтапное тестирование.
1. Тестирование в Stripe Test Mode с использованием скопированных тестовых данных.
2. Выполнение Dry Run (режим симуляции) в Live Mode без внесения изменений.
3. Тестовая миграция на ограниченной выборке реальных клиентов.

Обоснование: Тестирование позволяет выявить ошибки в логике маппинга и использовании Stripe API (особенно `billing_cycle_anchor`) до воздействия на всех клиентов.

6.2. Риск: Снижение уровня авторизации платежей (Authorization Rate Decline) после миграции.

Обоснование: Смена аккаунта Stripe приводит к смене Merchant ID. Банки-эмитенты могут временно отклонять транзакции от нового ID.

Источник: Stripe Docs, "Migrate payment data":
> When you migrate credit card data to a new Stripe account, authorization rates for the migrated cards might temporarily decline.
(Перевод: Когда вы переносите данные кредитных карт в новый аккаунт Stripe, уровень авторизации для перенесенных карт может временно снизиться.)

Смягчение:
1. Активировать и настроить Smart Retries, CAU и Network Tokens в Target Account (см. шаг 2.2.2).
2. Отслеживать Authorization Rate и коды отказов (Decline Codes) сразу после миграции.

6.3. Риск: Нарушение комплаенса SCA для европейских клиентов, ведущее к массовым отказам платежей.

Обоснование: Если мандаты MIT не будут корректно перенесены или обработаны, может потребоваться повторная 3D Secure аутентификация. (Источник: Stripe Docs, "SCA migration guide for Billing").

Смягчение: При воссоздании подписок убедиться, что платежи (Payment Intents) корректно помечаются как внесессионные. При создании Payment Intents параметр `off_session` должен быть установлен в `true`, и используемые Payment Methods должны иметь соответствующие мандаты.

Источник: Stripe Docs, "SCA enforcement".

6.4. Риск: Потеря доступа к историческим данным биллинга (Invoices, Charges).

Обоснование: История транзакций не переносится между аккаунтами.

Смягчение: Сохранить доступ к Source Accounts после миграции для целей отчетности, поддержки клиентов и управления диспутами по старым платежам.

Источник: Stripe Docs, "Copy PAN data across Stripe accounts":
> Source account data remains intact. We recommend keeping the original source account as a backup for your data.
(Перевод: Данные исходного аккаунта остаются нетронутыми. Мы рекомендуем сохранить исходный аккаунт в качестве резервной копии ваших данных.)

7. Стратегия Верификации и Отката (Verification and Rollback Strategy)

7.1. Стратегия верификации (Verification Strategy).

7.1.1. Верификация PAN Copy: Сравнить количество объектов `Customer` и `PaymentMethod` в Target Account с количеством в Source Accounts. Проверить корректность Mapping File.

7.1.2. Верификация Subscription Recreation: Разработка автоматизированных скриптов сверки (Reconciliation Scripts).

7.1.2.1. Сравнить общее количество активных `Subscription` и общий MRR.

7.1.2.2. Провести детальную сверку параметров для статистически значимой выборки подписок. Проверить: `status`, `price_id`, `quantity`, `current_period_end` (дата следующего платежа), `default_payment_method`, `metadata`.

7.1.2.3. Сгенерировать предстоящие инвойсы (Upcoming Invoices) через API для выборки клиентов и сверить суммы и даты с ожидаемыми.

7.2. План Отката (Rollback Plan).

7.2.1. Определить Точку Невозврата (Point of No Return): Момент начала массового воссоздания подписок в Target Account и отключения биллинга/интеграций в Source Accounts.

7.2.2. Процедура отката до Точки Невозврата: В случае ошибок во время тестирования или Dry Run остановить процесс, исправить скрипты и перезапустить.

7.2.3. Процедура экстренного отката после Точки Невозврата:

7.2.3.1. Немедленно остановить скрипт миграции.
7.2.3.2. Переключить API Keys и Webhooks обратно на Source Accounts.
7.2.3.3. Отменить (Cancel) некорректно созданные подписки в Target Account через API.
7.2.3.4. Если были произведены некорректные списания, инициировать возврат средств (Refund) через API в Target Account.
7.2.3.5. Возобновить биллинг в Source Accounts (если применимо).
7.2.3.6. Провести детальный анализ причин сбоя (Postmortem).