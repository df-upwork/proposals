# 0.
Сегодня 2025-10-16.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021978474008538239814

## 2.2. Title
Epic EHR Consultant for Referrals Guidance

## 2.3. Description
`PD` ≔ 
```text
We’re looking for a seasoned Epic EHR expert with deep, hands-on knowledge of Epic referral workflows to help our external clinic become a recognized referral destination within Epic.

We need someone who can guide us through the end-to-end process of enabling referrals to our organization — from understanding how referrals are initiated by clinicians to configuring our setup so that providers can easily refer patients to us.

Key responsibilities:
- Explain how Epic referrals work from both the clinician and IT perspectives.
- Identify which roles and permissions in Epic are required to create or manage referrals.
- Clarify the different types of referrals available in Epic and how each is configured (internal, external, work queue–based, etc.).
- Advise on what needs to happen within Epic (or at the health system level) for our clinic to be added as a referral destination.
- Help us navigate Epic’s support structure to find the right contacts or departments who can implement the necessary changes.
- Provide best practices for streamlining the referral process so that clinicians can easily send patients to our organization.

Ideal candidate:
- Extensive experience working with Epic EHR, especially with referral management, work queues, and inter-organization workflows.
- Familiarity with EpicCare Link, Care Everywhere, and EpicCare Ambulatory is a plus.
- Strong understanding of Epic configuration, user roles, and security permissions.
- Proven ability to work with or advise external clinics or partner organizations integrating with health systems using Epic.
- Excellent communication skills and comfort explaining technical details to non-Epic users.

If you’ve successfully helped organizations establish or optimize referral connectivity within Epic, we’d love to hear from you.
```

## 2.4. Tags
Strategy
Business Services
HIPAA
Epic Systems Medical Software
Medical Referrals
Tech & IT
Ehealth
Healthcare IT

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
Health & Fitness

### 5.2.2. Количество сотрудников
10-99

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Oct 15, 2025
### 5.3.2. Hire rate (%)
0
### 5.3.3. Количество опубликованных проектов (jobs posted)
1
### 5.3.4. Total spent (USD)
0
### 5.3.5. Количество оплаченных часов в почасовых проектах
0
### 5.3.6. Средняя почасовая ставка (USD)
0

# 6.
## 6.1.
`T1⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Explain how Epic referrals work from both the clinician and IT perspectives
~~~
```

## 6.2.
`T2⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Identify which roles and permissions in Epic are required to create or manage referrals
~~~
```

## 6.3.
`T3⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Clarify the different types of referrals available in Epic and how each is configured (internal, external, work queue–based, etc.)
~~~
```

## 6.4.
`T4⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Advise on what needs to happen within Epic (or at the health system level) for our clinic to be added as a referral destination
~~~
```

## 6.5.
`T5⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Help us navigate Epic’s support structure to find the right contacts or departments who can implement the necessary changes
~~~
```

## 6.6.
`T6⁎` ≔ 
```		
Подзадача из `PD`:
~~~
Provide best practices for streamlining the referral process so that clinicians can easily send patients to our organization
~~~
```

# 7. Контекст ситуации
Клиент (`ꆜ`) представляет собой внешнюю клинику (External Clinic), расположенную в США (`O.md`::§5.1).

## 7.1. Цель `ꆜ`
Стать «recognized referral destination within Epic» (`O.md`::§2.3). 
Это означает, что клиника стремится к тому, чтобы врачи из других медицинских организаций, использующих Epic EHR (далее — Целевые Организации), могли легко и систематически направлять (refer) пациентов в `ꆜ` непосредственно через свои рабочие процессы.

## 7.2. Ключевое предположение
Клиника `ꆜ`, вероятно, сама не использует Epic, но хочет интегрироваться в экосистему направлений Целевых Организаций.

# 8. Выявленные проблемы `ꆜ` на основе `PD`
## 8.1. `Prb1`
Отсутствие понимания механизмов работы направлений (Referral Workflows) в Epic как с клинической, так и с ИТ-перспективы (`T1⁎`).
## 8.2. `Prb2` 
Неопределенность относительно ролей и разрешений в Epic, необходимых для создания и управления направлениями (`T2⁎`).
## 8.3. `Prb3` 
Отсутствие ясности в отношении различных типов направлений (внутренние, внешние, основанные на очередях задач — Work Queues) и способов их конфигурации (`T3⁎`).
## 8.4. `Prb4` (Центральная техническая проблема)
Незнание технических и административных шагов, необходимых для добавления клиники `ꆜ` в качестве адресата направлений в системе Epic Целевой Организации (`T4⁎`).
## 8.5. `Prb5` (Центральная организационная проблема)
Трудности с идентификацией нужных контактов или отделов, которые могут реализовать необходимые изменения (`T5⁎`).
## 8. `Prb6` 
Опасение, что процесс направления будет сложным для врачей, и потребность в оптимизации этого процесса (`T6⁎`).

# 9. Анализ обоснованности проблем §8
Все выявленные проблемы (`Prb1`-`Prb6`) являются высоко обоснованными. 
Интеграция внешней клиники в экосистему Epic — сложная задача из-за архитектурных особенностей системы и организационной структуры крупных систем здравоохранения.

## 9.1. Обоснованность Prb4 (Интеграция) и Prb5 (Навигация)
Это наиболее критичные проблемы. 
Их обоснованность чрезвычайно высока по следующим причинам:

### 9.1.1. Децентрализованная архитектура и зависимость от Целевой Организации
Epic не является централизованной облачной сетью. 
Каждая организация здравоохранения устанавливает и настраивает свой экземпляр Epic независимо. 
Не существует глобального каталога, где `ꆜ` могла бы зарегистрироваться.

Интеграция должна происходить по принципу "точка-точка" с **каждой** Целевой Организацией.
Техническая реализация осуществляется ИТ-специалистами Целевой Организации, а не клиникой `ꆜ` или корпорацией Epic.

### 9.1.2. Техническая конфигурация: SER Master File (Prb4)
Чтобы врач мог выбрать `ꆜ` при создании направления, информация о клинике должна быть внесена в базу данных Целевой Организации. 
Ключевым элементом является конфигурация **SER (Service Provider) Master File** — основного справочника поставщиков услуг.

Документация подтверждает, что в SER файле должны быть созданы записи для внешних поставщиков с указанием их статуса (Active/Inactive) и типа (Internal/External). 
Если `ꆜ` не внесена в SER файл как активный внешний поставщик с корректными данными (специальность, контактная информация), она не будет доступна для выбора в рабочих процессах.

### 9.1.3. Организационные барьеры и заблуждения (Prb5)
Формулировка клиента о навигации по «структуре поддержки Epic» (`O.md`::§6.5) является распространенным заблуждением. 
Необходимые изменения (например, обновление SER файла) реализуются **ИТ-отделами и администрацией Целевых Организаций**.

Крупные больничные системы имеют сложную структуру. 
Поиск нужных контактных лиц (ИТ-аналитиков Epic, менеджеров по интероперабельности, специалистов по связям с врачами — Physician Liaisons) является серьезным административным барьером. 
Исследования подтверждают, что организационная сложность и необходимость балансировать между стандартизацией и кастомизацией создают значительные трудности при внесении изменений в EHR.

## 9.2. Обоснованность Prb1, Prb3 (Процессы и типы) и Prb6 (Оптимизация)

Эти проблемы обоснованы сложностью и вариативностью настроек Epic, а также необходимостью обеспечения бесшовного процесса для врачей (Prb6).

### 9.2.1. Сложность и вариативность рабочих процессов (Prb1, Prb3)
Рабочие процессы направлений сильно зависят от конфигурации конкретной организации. 
Процесс включает использование очередей задач (Workqueues), сортировку (Triage), авторизацию и планирование визита. Без понимания того, как врач инициирует направление и как система его маршрутизирует, невозможно эффективно интегрироваться.

### 9.2.2. Механизмы интероперабельности (Prb3, Prb6)
Для реализации электронных направлений (ключ к оптимизации Prb6) необходимо использовать один из механизмов интероперабельности:

#### EpicCare Link (ECL)
Веб-портал, предоставляемый Целевой Организацией внешним партнёрам. 
Это распространенный способ для клиник без Epic управлять направлениями. 
Однако он требует заключения соглашений (например, Information Partnering Agreement) и назначения администратора сайта со стороны `ꆜ`.
#### Care Everywhere (CE)
Платформа обмена медицинской информацией (HIE), позволяющая обмениваться данными и электронными направлениями между организациями.
#### Direct Secure Messaging
Стандартный протокол безопасного обмена данными.

Если электронная интеграция не настроена, врачи вынуждены использовать факс или телефон, что снижает вероятность направления (явление известно как «Referral Leakage» — утечка направлений).

## 9.3. Обоснованность Prb2 (Роли и разрешения)
Проблема обоснована. 
Хотя `ꆜ` не будет настраивать роли внутри Epic Целевой Организации, им необходимо понимать, кто участвует в процессе:
1.  Кто инициирует направление (Врачи).
2.  Кто управляет процессом (Координаторы направлений).
3.  Кто отвечает за конфигурацию внешних поставщиков (ИТ-аналитики, администраторы SER файла).

Если `ꆜ` будет использовать EpicCare Link, им потребуются специфические типы доступа, которые должны быть настроены и одобрены Целевой Организацией.
 