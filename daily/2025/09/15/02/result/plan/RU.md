-------------------
The migration plan
-------------------

# 1. Audit and Data Scoping
## 1.1. Определить ограничения автоматической миграции данных
Зафиксировать типы данных, которые могут и не могут быть автоматически скопированы между аккаунтами Stripe.
### 1.1.1. Данные, которые копируются
Объекты `Customer` и связанные с ними платежные данные (например, `Card` objects, `PaymentMethod` objects).

### 1.1.2. Данные, которые yt копируются
`Subscriptions`, `Products`, `Prices` (или `Plans`), `Coupons`, `Invoices`, `Charges`, `PaymentIntents`, `Events`, `Logs`.

### 1.1.3. Обоснование
Документация Stripe четко определяет границы автоматического копирования. 
Это понимание критически важно для определения объема работ по программному воссозданию логики биллинга.
Источник: Stripe Docs, «**Copy PAN data across Stripe accounts**»:
> We only copy the raw `Customer` objects and associated payment data objects.
> [...]
> We can't copy individual `Charges`, `PaymentIntents`, `Invoices`, `Plans`, `Subscriptions`, `Coupons`, `Events`, `Logs` [...] or any other Stripe objects.
https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve?copy-method=full#data-considerations

## 1.2. Проанализировать используемые методы интеграции и версии API
### 1.2.1. 
Определить, используют ли текущие интеграции устаревшие API (Charges API, Sources API) или современные (Payment Intents API, Payment Methods API).
#### Обоснование 
Устаревшие интеграции могут иметь ограничения при миграции данных и усложнять соблюдение комплаенса. 
Например, интеграции на Charges API не готовы к Strong Customer Authentication (SCA) и могут привести к высокому уровню отклоненных платежей.

Источник: Stripe Docs, «**Strong Customer Authentication readiness**»:
> Integrations that aren't SCA-ready, like those using the legacy Charges API, might see high rates of declines from banks that enforce SCA.
https://docs.stripe.com/strong-customer-authentication#preparing

### 1.2.2.
Проверить Default API version в настройках аккаунтов («Developers» → «API keys» → «API version»).
#### Обоснование 
Поведение API может различаться в зависимости от версии. 
Скрипты миграции должны использовать консистентную версию API для корректного извлечения данных.

## 1.3. Идентифицировать используемые Payment Methods
### 1.3.1. 
Определить, используются ли в International Source Account локальные платежные методы (**Local Payment Methods**, **LPMs**), такие как SEPA Direct Debit или Bacs Direct Debit.
### 1.3.2. 
В случае использования LPMs, определить, хранятся ли они как устаревшие `Source` объекты (`src_...`) или как современные `PaymentMethod` объекты (`pm_...`).
#### Обоснование
Стандартный инструмент копирования имеет ограничения. 
Некоторые LPMs, сохраненные как `Source` объекты, не могут быть скопированы.
Источник: Stripe Docs, «**Copy PAN data across Stripe accounts**»:
> We can't copy Single Euro Payments Area (SEPA) stored as source objects, Bacs Direct Debit, or pre-authorized debit payments (PADs)...
https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve?copy-method=full#data-considerations

Если используются `Source` объекты для LPMs, необходимо запланировать предварительную миграцию на `PaymentMethod` объекты в Source Account.

## 1.4. Провести аудит международного комплаенса (SCA)
### 1.4.1. 
Определить долю подписчиков из European Economic Area (EEA) в международном аккаунте.
### 1.4.2. 
Проверить наличие сохраненных Mandates и готовность интеграции к обработке Merchant-Initiated Transactions (MIT).
#### Обоснование
При миграции клиентов из EEA необходимо соблюдать требования SCA. 
Если доказательства аутентификации не будут корректно обработаны, клиентам может потребоваться повторная 3D Secure аутентификация, что приведет к увеличению оттока (churn).

Источник: Stripe Docs, «**SCA migration guide for Billing**»: https://docs.stripe.com/billing/migration/strong-customer-authentication

## 1.5. Проанализировать использование `metadata`.
Определить, какие ключевые данные хранятся в `metadata` объектов `Customer`, `PaymentMethod` и `Subscription` (например, идентификаторы Kajabi).
### Обоснование
`Metadata` объектов `Customer` и `PaymentMethod` копируются вместе с объектами. 
`Metadata` объектов `Subscription` необходимо извлечь и перенести при воссоздании подписок.

Источник: Stripe Support, «**Data that can be copied between Stripe accounts**»:
> You can copy the following data types... Metadata associated with the Stripe customer object... Metadata associated with the Stripe object for a particular payment type...
https://support.stripe.com/questions/data-that-can-be-copied-between-stripe-accounts

# 2. Стратегия Консолидации и Конфигурация Целевого Аккаунта
### 2.1. Оценить стратегические риски консолидации в США
Оценить потенциальное влияние консолидации глобальных операций в едином аккаунте США на уровень авторизации из-за кросс-граничного эквайринга (cross-border acquiring).

#### Обоснование
Обработка международных карт через эквайринг США часто приводит к более низкому уровню авторизации по сравнению с использованием локального эквайринга (например, европейского аккаунта).

Источник: Stripe Guide, «**Optimising authorization rates**»:
> Using locally optimised acquiring services helps you maximise acceptance rates (because banks are often more likely to approve domestic payments)...
https://stripe.com/guides/optimizing-authorization-rates

В качестве альтернативы рассмотреть использование Stripe Organizations для централизованного управления при сохранении отдельных локальных аккаунтов (США и ЕС).

## 2.2. Подготовить Target Account
### 2.2.1. 
Убедиться, что Target Account is activated
Копирование данных возможно только в активированный аккаунт.
Источник: Stripe Docs, «**Copy PAN data across Stripe accounts**»:
> The recipient account must be an activated account.
https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve?copy-method=full#data-considerations

### 2.2.2. 
Настроить параметры Stripe Billing, включая Smart Retries, Card Account Updater (CAU) и Network Tokens.
#### Обоснование
После миграции ожидается временное снижение Authorization Rate. 
Эти инструменты критически важны для минимизации потерь дохода и снижения involuntary churn. 
Smart Retries используют машинное обучение для оптимизации времени повторных попыток оплаты.

Источник: Stripe Guide, «**Optimizing authorization rates**»: https://stripe.com/guides/optimizing-authorization-rates

## 2.3. Определить стратегию налогового комплаенса
Разработать стратегию управления глобальными налогами (VAT, GST, Sales Tax). 
Рассмотреть активацию и настройку Stripe Tax в Target Account для автоматизации.
Консолидация международных операций требует унифицированного подхода к соблюдению налогового законодательства в разных юрисдикциях.

# 3. Стратегия Product and Price Mapping
## 3.1. Определить стратегию идентификации
### 3.1.1. Для объектов `Product` и устаревших `Plan` (если используются)
Cтремиться использовать те же идентификаторы (IDs) в Target Account, что и в Source Accounts.
#### Обоснование
Stripe рекомендует по возможности использовать те же ID для упрощения маппинга.
Источник: Stripe Support, «**Recreate subscriptions and plans after moving customer data to a new Stripe account**»:
> When recreating the plans, specify the same `id` for each plan as on your former account.
https://support.stripe.com/questions/recreate-subscriptions-and-plans-after-moving-customer-data-to-a-new-stripe-account

### 3.1.2. Для современных объектов `Price`
Запланировать использование альтернативных методов маппинга, таких как `lookup_key` или `metadata`, для хранения старого идентификатора.
#### Обоснование
В отличие от Products API и Plans API, современный Prices API не позволяет указать `id` при создании объекта.
Источник: Stripe API Reference:
- «**Create a product**» (параметр `id` доступен): https://docs.stripe.com/api/products/create
- «**Create a price**» (параметр `id` недоступен): https://docs.stripe.com/api/prices/create

## 3.2. Создать Mapping Table
### 3.2.1. 
Извлечь все `Product`, `Price`/`Plan`, `Tax Rate`, `Coupon` из обоих Source Accounts через API.
### 3.2.2. 
Структурировать данные в единую таблицу, включающую все параметры: `id`, `currency`, `unit_amount`, `recurring.interval`, `tax_behavior`, `metadata`.
### 3.2.3. 
Определить соответствие между объектами из разных Source Accounts (например, консолидация мультивалютных цен).

## 3.3. Определить процесс воссоздания объектов
Разработать скрипт для создания всех необходимых объектов в Target Account на основе Mapping Table и заполнить таблицу новыми идентификаторами (если применимо).

# 4. Определение Процедуры Миграции Данных (PAN Copy Steps)
## 4.1. Выбрать метод копирования
Использовать инструмент «**Self-serve copy migration**» в Stripe Dashboard.
Это рекомендуемый Stripe безопасный и соответствующий PCI-compliant способ переноса конфиденциальных платежных данных между аккаунтами.
Источник: Stripe Docs, «**Migrate payment data**»:
> If you want to transfer data between two Stripe accounts, complete a self-serve copy migration.
https://docs.stripe.com/get-started/data-migrations/overview#copy-payment-data-between-stripe-accounts

## 4.2. Оценить риски Card Account Updater (CAU)
Принять решение о временном отключении CAU в Target Account на время миграции, если необходимо избежать дополнительных комиссий за обновление истекших карт.
CAU может автоматически обновлять скопированные карты, что приводит к дополнительным расходам.
Источник: Stripe Docs, «**Copy PAN data across Stripe accounts**»:
> This can result in additional CAU fees for the destination account.
https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve?copy-method=full#data-considerations

## 4.3. Определить последовательность действий для инициации копирования (Действия Sender)
- В Source Account перейти в «Customers».
- Нажать «Copy customers».
- В поле «Copy Method» выбрать «Copy all customers».
- Ввести идентификатор Target Account (`acct_xxxx`) и нажать «Continue».
- Нажать «Confirm».

https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve?copy-method=full#share-customer-data-with-the-recipient

## 4.4. Определить последовательность действий для авторизации копирования (Действия Recipient)
- В Target Account перейти в «Customers».
- Найти баннер с уведомлением о запросе.
- Нажать «Authorize and Accept».

Копирование начнется только после авторизации получателем.
https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve?copy-method=full#authorize-and-accept-customer-data-from-the-sender

## 4.5. Запланировать время выполнения
Заложить до 72 часов на завершение процесса копирования после авторизации.
Источник: Stripe Docs, «**Copy PAN data across Stripe accounts**»:
> Most data copies finish within 72 hours...
https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve?copy-method=full#the-copying-process-finishes

## 4.6. Определить процедуру получения и обработки файла соответствия (Mapping File)
### 4.6.1. 
После завершения копирования скачать CSV файл соответствия в разделе «Documents» Target Account.
### 4.6.2. 
Разработать механизм обработки этого файла скриптом миграции.
### Обоснование
При копировании идентификаторы платежных методов (`PaymentMethod` IDs) изменяются. 
Файл соответствия содержит маппинг старых ID на новые ID. 
Идентификаторы `Customer` ID не изменяются.
Источник: Stripe Docs, «**Copy PAN data across Stripe accounts**»:
> The copy process assigns new object IDs of the same payment type to payment data...
> [...]
> The copy operation doesn't change customer IDs...
https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve?copy-method=full#data-considerations

# 5. Subscription Recreation Strategy
## 5.1. Выбор инструмента миграции
Для сложной консолидации рекомендуется разработка кастомного скрипта с использованием Stripe API, а не использование Stripe Billing Migration Toolkit (CSV-based).
Кастомный скрипт обеспечивает необходимую гибкость для обработки сложного маппинга данных из двух источников, управления ошибками и интеграции с Kajabi.
## 5.2. Обеспечение непрерывности цикла биллинга
Спланировать использование параметра `billing_cycle_anchor` (или `trial_end`) при создании новой подписки через API. 
Значение должно быть равно дате следующего платежа (`current_period_end`) исходной подписки.
Это критически важно для предотвращения немедленного или двойного списания средств.
Источник: Stripe Support, «**Recreate subscriptions and plans after moving customer data to a new Stripe account**»:
> If you want to use the same billing dates on the new account as you did on the old account, you can force the billing period of subscriptions on the new account by setting a custom trial end date when you create them.
https://support.stripe.com/questions/recreate-subscriptions-and-plans-after-moving-customer-data-to-a-new-stripe-account

## 5.3. Отключение прораций
При создании новых подписок установить параметр `proration_behavior` в значение `none`.
Поскольку это миграция существующих обязательств, а не изменение плана в середине цикла, прорации рассчитываться не должны. 
Источник: Stripe API Reference, «**Create a subscription**»: https://docs.stripe.com/api/subscriptions/create#create_subscription-proration_behavior

## 5.4. Обеспечение идемпотентности скриптов
Спроектировать скрипты миграции с использованием `Idempotency Keys` при всех вызовах API, создающих объекты.
Это позволяет безопасно перезапускать скрипты в случае сбоев, не создавая дубликатов подписок или клиентов.
Источник: Stripe Docs, «**Idempotent requests**»:
> The API supports idempotency for safely retrying requests without accidentally performing the same operation twice.
https://docs.stripe.com/api/idempotent_requests

## 5.5. Определить стратегию синхронизации данных (Delta Synchronization)
Разработать механизм для отслеживания и миграции изменений, произошедших в Source Accounts между моментом запроса на PAN copy и фактическим переключением (Cutover).
### Обоснование
Процесс PAN copy может занять до 72 часов (пункт 4.5 выше). 
Необходимо учесть новые подписки, отмены или обновления платежных методов, произошедшие в этот период. 
Это может потребовать использования Webhooks или инкрементального копирования. 

# 6. Risk Management Plan
## 6.1. 
### 6.1.1. Риск
Потеря дохода (MRR) из-за ошибок при воссоздании подписок (двойные списания, пропущенные платежи, некорректные суммы).
### 6.1.2. Смягчение
Провести многоэтапное тестирование:
1. Тестирование в Stripe Test Mode с использованием скопированных тестовых данных.
2. Выполнение Dry Run (режим симуляции) в Live Mode без внесения изменений.
3. Тестовая миграция на ограниченной выборке реальных клиентов.

Тестирование позволяет выявить ошибки в логике маппинга и использовании Stripe API (особенно `billing_cycle_anchor`) до воздействия на всех клиентов.

## 6.2. 
### 6.2.1. Риск
Снижение уровня авторизации платежей (Authorization Rate Decline) после миграции.
Смена аккаунта Stripe приводит к смене Merchant ID. 
Банки-эмитенты могут временно отклонять транзакции от нового ID.

### 6.2.2. Смягчение
1. Активировать и настроить Smart Retries, CAU и Network Tokens в Target Account (см. шаг 2.2.2).
2. Отслеживать Authorization Rate и коды отказов (Decline Codes) сразу после миграции.

## 6.3. 
### 6.3.1. Риск
Нарушение комплаенса SCA для европейских клиентов, ведущее к массовым отказам платежей.
Если мандаты MIT не будут корректно перенесены или обработаны, может потребоваться повторная 3D Secure аутентификация. 
Источник: Stripe Docs, «**SCA migration guide for Billing**»: https://docs.stripe.com/billing/migration/strong-customer-authentication
### 6.3.2. Смягчение
При воссоздании подписок убедиться, что платежи (`Payment Intents`) корректно помечаются как внесессионные. 
При создании `Payment Intents` параметр `off_session` должен быть установлен в `true`, и используемые Payment Methods должны иметь соответствующие мандаты.
Источник: Stripe Docs, «**SCA enforcement**»: https://docs.stripe.com/strong-customer-authentication/sca-enforcement

## 6.4. 
### 6.4.1. Риск
Потеря доступа к историческим данным биллинга (`Invoices`, `Charges`).
История транзакций не переносится между аккаунтами.
### Смягчение
Сохранить доступ к Source Accounts после миграции для целей отчетности, поддержки клиентов и управления диспутами по старым платежам.

Источник: Stripe Docs, "Copy PAN data across Stripe accounts":
> Source account data remains intact.
We recommend keeping the original source account as a backup for your data.
https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve?copy-method=full#data-considerations

# 7. Verification and Rollback Strategy
## 7.1. Verification Strategy

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