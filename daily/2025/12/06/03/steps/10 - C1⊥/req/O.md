# 0.
Сегодня 2025-12-06.

# 1.
## 1.1.
`UW` ≔ (Upwork: https://en.wikipedia.org/wiki/Upwork)

## 1.2.
`ꆜ` ≔ (Некий конкретный потенциальный клиент на `UW`)

## 1.3.
`P⁎` ≔ (Некий конкретный потенциальный проект, опубликованный `ꆜ` на `UW`)

# 2. Информация о `P⁎`
## 2.1. URL
https://www.upwork.com/jobs/~021996977273470295441

## 2.2. Title
GCP DevOps help needed

## 2.3. Description
`PD` ≔ 
```text
#
We need help with multiple items in GCP but to get started below is the first item we need help with:

# Project Summary
Google Datastream to MongoDB Atlas via PSC

# Objective
Establish a private connection between Google Cloud Datastream and MongoDB Atlas using Private Service Connect (PSC) to avoid public internet traversal.

# The Blockers
Datastream fails to connect with Connection Refused or Timeout. 

# Symptom
The error logs show Datastream attempting to connect to Atlas Public IPs instead of the PSC Private IPs 

# Root Cause Diagnosis
Split-Horizon DNS Failure. Datastream is ignoring the Private DNS Zone in the peered VPC and falling back to Public DNS (which resolves the Atlas Wildcard to public IPs).

# Infrastructure State (What is Configured)
## 1. Network & Connectivity:

### VPC
datastream-net (Project: internal-resources-corp).

### PSC Endpoints
2 Endpoints created targeting the Atlas Service Attachment.

### Private Service Access (PSA):
- Peering created with servicenetworking.googleapis.com.
- Crucial Config: export-custom-routes and import-custom-routes are set to TRUE on the peering connection.
- Reserved Range: [range]/24 for the service link.

## 2. DNS Configuration (Cloud DNS):

### Zone
mongo-psc-isolated (Private Zone).

### Visibility
Attached to datastream-net network.

### Records
We explicitly mapped the Canonical Atlas Hostnames (found via hello command) to the local PSC IPs.

## 3. Firewalls:
### GCP Ingress
Allow 0.0.0.0/0 (Temporary "Sledgehammer" rule for debugging).

### GCP Egress
Allow UDP:53 (DNS) to 0.0.0.0/0.

### MongoDB Atlas Access List
[range]/24 is whitelisted.

# Verification Results 
We deployed a DNS Verifier VM inside the datastream-net VPC to validate the infrastructure.

## ✅ VM DNS Test
nslookup on the VM correctly resolves the Atlas hostnames to Private IPs 

## ✅ VM Connectivity Test
mongosh on the VM connects successfully to the cluster using the Private IPs.

## ❌ Datastream Test
Datastream Connection Profile test fails. 
Configuring a dummy hostname (...mongodb.net-RESET) proves it resolves to Public IPs, meaning Datastream is not utilizing the Custom Routes exported via Peering.
```

# 5. Информация о `ꆜ`
## 5.1. Местоположение
United States
Coraopolis

## 5.2. Характеристики компании
### 5.2.1. Сектор экономики
неизвестно

### 5.2.2. Количество сотрудников
100-1,000

## 5.3. Характеристики учётной записи на `UW`
### 5.3.1. Member since
Nov 10, 2019
### 5.3.2. Hire rate (%)
79
### 5.3.3. Количество опубликованных проектов (jobs posted)
28
### 5.3.4. Total spent (USD)
239K
### 5.3.5. Количество оплаченных часов в почасовых проектах
3464
### 5.3.6. Средняя почасовая ставка (USD)
59.92

## 8.2.
⊤ (Все `Pi` касаются `С⁎`)

# 9.
`T⁎` ≔
```
Задача, о которой `ꆜ` пишет в `PD`:
~~~
Establish a private connection between Google Cloud Datastream and MongoDB Atlas using Private Service Connect (PSC) to avoid public internet traversal.
~~~
```

# 10.
`P†` ≔†
```
Проблема на пути к `T⁎`, о которой `ꆜ` пишет в `PD`:
~~~
```

# 11.
## 11.1.
`P1†` ≔ 
```		
Часть `P†`, описанная `PD` так:
~~~
The error logs show Datastream attempting to connect to Atlas Public IPs instead of the PSC Private IPs 
~~~
```

## 11.2.
`P2†` ≔ 
```		
Часть `P†`, описанная `PD` так:
~~~
Datastream is ignoring the Private DNS Zone in the peered VPC and falling back to Public DNS (which resolves the Atlas Wildcard to public IPs)
~~~
```

## 11.3.
`P3†` ≔ 
```		
Часть `P†`, описанная `PD` так:
~~~
Datastream Test: Datastream Connection Profile test fails. Configuring a dummy hostname (...mongodb.net-RESET) proves it resolves to Public IPs, meaning Datastream is not utilizing the Custom Routes exported via Peering.
~~~
```

# 12. Что беспокоит `ꆜ` (анализ выполнен Gemini Deep Think)
https://gemini.google.com/share/231e575dc7eb

## 1. Выявление проблем (`P†`)

На основе анализа описания `PD` в документе `O.md`, можно выделить три составляющие проблемы, диагностированные клиентом `ꆜ`:

1.  **`P1†` (Симптом)**: Datastream пытается подключиться к публичным IP-адресам MongoDB Atlas вместо использования приватных IP-адресов (PSC). Это приводит к ошибкам соединения («Connection Refused» или «Timeout»).
2.  **`P2†` (Диагноз DNS)**: Datastream игнорирует частную зону DNS (`mongo-psc-isolated`), настроенную в VPC клиента (`datastream-net`), и откатывается к использованию публичного DNS. Клиент называет это «Split-Horizon DNS Failure».
3.  **`P3†` (Диагноз маршрутизации)**: Клиент делает вывод, что Datastream не использует кастомные маршруты (Custom Routes), экспортируемые через пиринг, так как тестирование с фиктивным хостнеймом показало разрешение в публичный IP.

## 2. Анализ обоснованности проблемы `P1†`
**Статус:** Обоснована.

Эта проблема является **валидным симптомом**.
В логах действительно зафиксированы попытки подключения к публичным IP-адресам. При использовании публичного DNS (см. анализ `P2†`) хостнеймы MongoDB Atlas разрешаются в публичные IP. Поскольку архитектура безопасности проекта подразумевает приватное соединение, доступ через публичный интернет, вероятно, закрыт фаерволом или настройками Atlas, что и вызывает ошибки подключения.

## 3. Анализ обоснованности проблемы `P2†`
**Статус:** Обоснована (Корневая причина).

Диагноз клиента технически верен: Datastream действительно не использует частную DNS-зону клиента. Однако важно отметить, что это является **документированным архитектурным ограничением**, а не сбоем конфигурации (failure) в привычном понимании.

*   **Техническое обоснование:** Google Cloud Datastream — это управляемый сервис, работающий в отдельной сети производителя (service producer network). При подключении через VPC Peering (Private Service Access) маршруты транслируются, но конфигурация Cloud DNS **не наследуется** автоматически. Сервис не имеет доступа к приватным зонам в проекте потребителя.
*   **Авторитетный источник:** Согласно официальной документации Google Cloud:
    > *"You need to provide the **private IP addresses** when setting up the private connectivity configuration because **Datastream doesn't support Domain Name System (DNS) resolution in private connections**."* (Source: Google Cloud Datastream Documentation).
*   **Вывод:** Поскольку сервис не поддерживает DNS-резолвинг в приватных соединениях, он использует свои локальные (публичные) DNS-резолверы. Это приводит к тому, что адреса Atlas разрешаются в их публичные значения.

## 4. Анализ обоснованности проблемы `P3†`
**Статус:** Необоснована (Ложный вывод).

Заключение клиента о том, что *"Datastream не использует экспортируемые маршруты"* (`Datastream is not utilizing the Custom Routes`), является ошибочной интерпретацией причинно-следственной связи.

*   **Анализ:** Процесс установления соединения происходит в последовательности: `DNS Resolution` -> `Routing`.
    1.  Из-за ограничения `P2†`, DNS возвращает **публичный IP-адрес**.
    2.  Datastream проверяет таблицу маршрутизации для этого *публичного* адреса.
    3.  Пользовательские маршруты (Custom Routes), экспортированные через пиринг, предназначены для **частных диапазонов** (IP-адресов PSC). Они не применимы к публичным адресам.
*   **Вывод:** Трафик направляется в интернет (или блокируется) не потому, что маршруты игнорируются, а потому, что адрес назначения не соответствует этим маршрутам. Если бы в конфигурации использовался корректный приватный IP, маршрутизация через пиринг сработала бы штатно.

# 13. Что беспокоит `ꆜ` (анализ выполнен Gemini Deep Research)
https://gemini.google.com/share/deae4f0355ee

## **1. Введение и контекст исследования**

Настоящий отчет представляет собой исчерпывающий технический анализ инцидента, связанного с невозможностью установления приватного сетевого соединения между сервисом Google Cloud Datastream (Change Data Capture — CDC) и кластером MongoDB Atlas, развернутым с использованием технологии Private Service Connect (PSC). Документ подготовлен в ответ на запрос клиента (ꆜ) и направлен на детальную валидацию выявленных проблем, диагностику корневых причин сбоя на уровне архитектуры облачной сети, а также разработку детерминированных стратегий их устранения.

В современной облачной инженерии задача интеграции управляемых сервисов (Managed Services), таких как Datastream, с базами данных, размещенными в сторонних SaaS-средах (MongoDB Atlas), является критически важной для построения конвейеров данных реального времени. Однако, как показывает практика и текущий инцидент P⁎, данная интеграция сопряжена со значительными архитектурными сложностями, возникающими на стыке технологий виртуализации сетей (SDN), управления доменными именами (DNS) и политик безопасности.

Целью данного документа является не только решение локальной задачи T⁎ (установление соединения), но и предоставление глубокого понимания механики взаимодействия компонентов Google Cloud Networking. Анализ базируется на предоставленных данных об инфраструктуре (O.md), логах ошибок и авторитетной технической документации.

### **1.1. Обзор проблематики проекта P⁎**

Проект P⁎ нацелен на реализацию защищенного канала передачи данных между Google Cloud Datastream и MongoDB Atlas. Ключевым требованием является полное исключение прохождения трафика через публичный интернет ("avoid public internet traversal"). Для реализации этой задачи была выбрана архитектура, включающая:

* **VPC Peering** (через Private Services Access) для связи Datastream с пользовательской сетью (datastream-net).  
* **Private Service Connect (PSC)** для связи пользовательской сети с MongoDB Atlas.  
* **Cloud DNS Private Zone** для разрешения имен хостов Atlas во внутренние IP-адреса.

Несмотря на кажущуюся корректность дизайна, система не функционирует. Сервис Datastream демонстрирует симптомы, указывающие на попытки соединения через публичные IP-адреса, игнорируя настроенную частную зону DNS. Клиент диагностировал проблему как "Split-Horizon DNS Failure", однако, как покажет дальнейший анализ, ситуация осложняется фундаментальными ограничениями транзитивной маршрутизации в Google Cloud, которые не были учтены в исходном дизайне.

### **1.2. Методология анализа**

Анализ проводится методом декомпозиции сетевого стека взаимодействия. Мы последовательно рассмотрим:

1. Уровень DNS: Механизмы разрешения имен в управляемых VPC Google и их ограничения при пиринге.  
2. Уровень IP-маршрутизации: Топологию VPC Peering и правила транзитивности трафика к PSC Endpoint.  
3. Уровень Приложения (Application Layer): Специфику протокола MongoDB, механизмы обнаружения топологии (Service Discovery) и требования TLS/SSL.

Каждая выявленная клиентом проблема (P1†, P2†, P3†) будет подвергнута строгой технической валидации на основе официальной спецификации сервисов.

## **2. Детальный аудит инфраструктуры и валидация симптомов**

Прежде чем переходить к архитектурным решениям, необходимо зафиксировать текущее состояние системы и подтвердить корректность наблюдений, сделанных инженерной командой клиента.

### **2.1. Топология сети и компоненты**

Согласно описанию инфраструктуры, мы имеем следующую цепочку взаимодействия компонентов:

| Компонент | Роль | Сетевой сегмент | Примечание |
| :---- | :---- | :---- | :---- |
| **Datastream Service** | Источник данных (CDC) | Google Managed VPC | Управляется Google, скрыт от пользователя. |
| **PSA Connection** | Канал связи | VPC Peering | Соединяет Managed VPC и datastream-net. |
| **VPC datastream-net** | Транзитная сеть | Project: internal-resources-corp | Контролируется пользователем. |
| **PSC Endpoint** | Точка входа | IP в datastream-net | Forwarding Rule, указывающее на Service Attachment Atlas. |
| **Cloud DNS** | Разрешение имен | Zone: mongo-psc-isolated | Привязана к datastream-net. A-записи ведут на IP PSC. |
| **MongoDB Atlas** | Целевая система | Atlas VPC | Доступ через PSC Service Attachment. |

### **2.2. Анализ диагностированных проблем (P†)**

Клиент выделил три ключевых аспекта проблемы. Проведем их экспертную оценку.

#### **Проблема P1†: Соединение с публичными IP**

*Описание:* "The error logs show Datastream attempting to connect to Atlas Public IPs instead of the PSC Private IPs".

Валидация: Абсолютно подтверждено.  
Логи Datastream, фиксирующие попытки соединения с публичными адресами, являются неопровержимым доказательством того, что разрешение DNS-имен происходит некорректно. MongoDB Atlas, даже при настроенном Private Endpoint, сохраняет публичные DNS-записи для своих кластеров (обычно вида *.mongodb.net). Эти записи являются глобально разрешимыми и указывают на публичные IP-адреса шлюзов Atlas.1 Если клиент (в данном случае Datastream) не видит частную зону DNS, он обращается к публичным рекурсивным резолверам Google (8.8.8.8), которые возвращают публичные адреса.  
Поскольку в инфраструктуре клиента, вероятно, отсутствуют маршруты в интернет для Datastream (или настроены строгие правила Egress), либо IP Access List в Atlas закрыт для публичных IP Datastream, соединение завершается ошибкой Connection Refused или Timeout.

#### **Проблема P2†: Игнорирование Private DNS Zone**

*Описание:* "Datastream is ignoring the Private DNS Zone in the peered VPC and falling back to Public DNS".

Валидация: Абсолютно подтверждено (Архитектурное ограничение).  
Это наблюдение является точным описанием поведения сервиса, однако термин "ignoring" (игнорирует) может создать ложное впечатление, что это ошибка конфигурации или баг. В действительности, это задокументированное ограничение архитектуры Google Cloud Datastream при использовании метода подключения "Private Connectivity" (через VPC Peering).  
Документация Google Cloud прямо утверждает: "Datastream doesn't support Domain Name System (DNS) resolution in private connections".2  
Механизм VPC Peering объединяет пространства IP-адресов двух сетей, но не объединяет пространства имен DNS автоматически. Резолверы, работающие внутри управляемой сети Datastream, не имеют доступа к конфигурации Cloud DNS в пользовательском проекте. Они не знают о существовании зоны mongo-psc-isolated, привязанной к datastream-net, и следовательно, выполняют стандартную рекурсию через публичные корни.

#### **Проблема P3†: Ложноположительный результат верификации**

*Описание:* "Datastream Test fails... Configuring a dummy hostname proves it resolves to Public IPs... VM DNS Test succeeds".

Валидация: Критически важно.  
Клиент провел тестирование с использованием "DNS Verifier VM", размещенной внутри сети datastream-net. Успех этого теста (nslookup вернул частный IP, mongosh подключился) создал ложную уверенность в исправности инфраструктуры.  
Ошибка в рассуждениях заключается в экстраполяции прав доступа VM на сервис Datastream.

* **VM** находится *внутри* datastream-net. Она использует metadata server этой сети для DNS (169.254.169.254) и видит все зоны, привязанные к этой сети.  
* Datastream находится снаружи (в пиринговой сети). Он находится в другой зоне безопасности и административного домена.  
  Успех VM доказывает лишь то, что зона настроена корректно, но не то, что она доступна для пиров.

### **2.3. Скрытая проблема: Транзитивность маршрутизации (The Hidden Blocker)**

Помимо проблем с DNS, выявленных клиентом, анализ инфраструктуры указывает на наличие второго, еще более фундаментального блокирующего фактора, который клиент пока не диагностировал явно, но который неизбежно проявится даже при решении проблемы с именами.

Речь идет о транзитивной маршрутизации к эндпоинтам Private Service Connect.  
Согласно топологии:

1. Datastream (Network A) соединен пирингом с datastream-net (Network B).  
2. PSC Endpoint находится в datastream-net (Network B).

Документация Google Cloud по VPC Peering гласит: "The VPC Network Peering connection... doesn't let Datastream connect to: Private Service Connect endpoints located in your VPC network".3  
Это ограничение обусловлено тем, как реализованы правила пересылки (Forwarding Rules) в SDN Google. Трафик, приходящий из пиринговой сети, не может быть направлен в эндпоинт PSC, если не используются специальные конструкции (например, PSC Interface в той же сети или промежуточный прокси).  
Таким образом, даже если мы "заставим" Datastream разрешить имя в частный IP-адрес PSC (например, 10.0.0.5), пакеты от Datastream, адресованные на 10.0.0.5, будут отброшены на границе пиринга или внутри сети datastream-net из-за невозможности маршрутизации к сервисному эндпоинту.

## **3. Глубокий анализ корневых причин (Root Cause Analysis)**

В этом разделе мы подробно разберем физику процессов, приводящих к сбою, опираясь на теорию облачных сетей.

### **3.1. Механика сбоя DNS Resolution (Split-Horizon)**

Концепция Split-Horizon DNS подразумевает, что ответ на DNS-запрос зависит от источника запроса. В данном сценарии мы имеем две "вселенные":

1. **Public Internet Scope:** Здесь cluster.mongodb.net разрешается в публичные IP AWS/GCP/Azure (где хостится Atlas).  
2. **Private VPC Scope (datastream-net):** Здесь настроена Private Zone, перекрывающая публичную, где cluster.mongodb.net разрешается в локальные IP PSC.

Сервис Datastream, будучи развернутым в тенанте Google, использует свои локальные DNS-серверы. При установлении Private Connectivity через PSA (Private Services Access), Google прокладывает маршруты для трафика данных (Data Plane), но **не синхронизирует** Control Plane, отвечающий за разрешение имен.

Существует механизм "DNS Peering" (не путать с VPC Peering), который позволяет одной VPC пересылать DNS-запросы в другую.4 Однако, этот механизм требует настройки на *обеих* сторонах. Пользователь может настроить DNS Peering в своей сети, но он не имеет административного доступа к сети Datastream, чтобы настроить пересылку запросов *оттуда* в свою сеть. Datastream не предоставляет API для настройки DNS Peering со своей стороны.

Именно поэтому Datastream жестко ограничен использованием IP-адресов при приватном подключении, либо требует наличия механизмов, работающих на уровнях L3/L4, которые не зависят от DNS (что невозможно для MongoDB из-за SSL, о чем ниже).

### **3.2. Несовместимость Peering и PSC (The Transitivity Problem)**

В Google Cloud существует жесткое правило: Peering is non-transitive (Пиринг не транзитивен).  
Обычно это означает, что если Сеть А соединена с Сетью Б, а Сеть Б с Сетью В, то А не может говорить с В.  
В случае с PSC ситуация еще специфичнее. PSC Endpoint — это не просто виртуальная машина с сетевым интерфейсом. Это абстракция Software Defined Network, представляющая собой правило переадресации (Forwarding Rule), которое инкапсулирует трафик и отправляет его через Google Backbone к производителю сервиса (MongoDB Atlas).  
Когда пакет приходит из пиринговой сети (Datastream VPC), маршрутизатор VPC проверяет таблицу маршрутизации. Для обычных VM маршруты распространяются через BGP при включении флагов export-custom-routes / import-custom-routes (что клиент и сделал). Однако PSC Endpoints не являются стандартными подсетями. Они публикуются внутри VPC особым образом.  
До недавнего времени доступ к PSC Endpoint из пиринговой сети был технически невозможен. Хотя Google внедряет улучшения (например, PSC Interface), в классической схеме "PSA Peering -> Customer VPC -> PSC Endpoint" этот путь заблокирован.3  
Это означает, что архитектура клиента, подразумевающая "прозрачный проброс" соединения от Datastream через его VPC к Atlas, нереализуема в текущем виде без посредников.

## **4. Специфика протокола MongoDB и вызовы безопасности**

Понимание того, как работает драйвер MongoDB, критически важно для выбора правильной стратегии исправления. MongoDB — это не просто TCP-сокет (как PostgreSQL или MySQL). Это сложная распределенная система.

### **4.1. Обнаружение топологии (Service Discovery)**

При подключении к кластеру (Replica Set или Sharded Cluster) клиент MongoDB выполняет процедуру "Initial Handshake":

1. Клиент подключается к "Seed List" (адресам, указанным в строке подключения).  
2. Клиент отправляет команду isMaster (или hello в новых версиях).  
3. Сервер отвечает документом, содержащим конфигурацию реплика-сета, включая поле hosts, где перечислены адреса всех членов кластера (Primary и Secondaries).  
4. Клиент **обрывает** текущее соединение и переподключается к адресам, полученным в ответе isMaster, чтобы работать с конкретными нодами напрямую (балансировка чтения, запись в Primary).

Проблема: Сервер MongoDB Atlas сконфигурирован так, что он "знает" о себе только свои канонические публичные DNS-имена (например, atlas-shard-00-00.mongodb.net). В ответе на isMaster он вернет именно их.  
Даже если мы обманем Datastream на первом шаге (через /etc/hosts или прокси), драйвер Datastream получит список публичных имен и на втором шаге попытается соединиться с ними. Это вернет нас к Проблеме P1† (Public IP access).  
**Решение:** Необходимо принудительно заставить драйвер Datastream работать в режиме **Direct Connection**, игнорируя топологию. Параметр directConnection=true в строке подключения (Connection String) указывает драйверу выполнять операции непосредственно на том хосте, к которому он подключился изначально, не пытаясь обнаружить других участников.6

### **4.2. TLS/SSL и SNI (Server Name Indication)**

MongoDB Atlas требует обязательного использования TLS. Сертификаты, выдаваемые Atlas, являются валидными для доменов *.mongodb.net.  
Если Datastream подключается к прокси-серверу по IP-адресу (например, 10.10.10.10), но ожидает защищенного соединения, произойдет сбой валидации сертификата (Hostname Mismatch), так как сертификат сервера выдан на DNS-имя, а не на IP.  
Существует два пути решения:

1. **Отключение валидации:** Использование флагов типа tlsAllowInvalidHostnames или tlsInsecure. Однако, Datastream — это управляемый сервис, и его UI/API не всегда предоставляет гранулярный контроль над опциями TLS драйвера, часто требуя загрузки CA-сертификатов, но не давая кнопки "Ignore Hostname".8  
2. **Прозрачное туннелирование:** Использование механизмов, где "клиент" (Datastream) думает, что подключается к локальному хосту (туннель), или использование корректного DNS-разрешения на стороне проксирующего агента.

## **5. Стратегии решения (Remediation Strategies)**

На основе проведенного анализа мы предлагаем три стратегии решения проблемы, ранжированные по надежности, производительности и сложности реализации.

### **5.1. Стратегия А: Проксирование через VM (Рекомендуемая)**

Это наиболее надежное и архитектурно корректное решение, устраняющее как проблему DNS, так и проблему транзитивности PSC.

Суть решения:  
Внедрение промежуточного звена (Proxy VM) внутри пользовательской сети datastream-net. Datastream подключается к этой VM, а VM пересылает трафик на PSC Endpoint.  
**Архитектура:**

1. **Proxy VM:** Развертывается в VPC datastream-net (зоне доступности, близкой к Datastream). Тип машины: e2-micro или e2-small (достаточно для TCP streaming).  
2. **ПО:** Используется Nginx (модуль stream) или HAProxy.  
3. **Маршрутизация:**  
   * Datastream -> (Peering) -> Proxy VM (Private IP).  
   * Proxy VM -> (Local Network Resolution) -> PSC Endpoint DNS Name -> PSC IP.  
   * Proxy VM -> (Local Network Routing) -> PSC Endpoint.

**Конфигурация (Пример для Nginx):**

| Параметр | Значение | Обоснование |
| :---- | :---- | :---- |
| **Resolver** | 169.254.169.254 | Использование Cloud DNS метадата-сервера для разрешения приватных зон. |
| **Upstream** | atlas-endpoint-address.mongodb.net:27017 | Прокси должен обращаться по имени, чтобы сработал Private DNS. |
| **Proxy Protocol** | TCP (Layer 4) | Nginx не должен расшифровывать SSL (Passthrough), чтобы не управлять сертификатами. |

Решение проблемы MongoDB Discovery:  
В профиле Datastream необходимо:

1. Указать **IP-адрес Proxy VM** в качестве хоста.  
2. Использовать "Standard connection string".  
3. Добавить параметр directConnection=true (если поддерживается полем UI или через API/Terraform в поле аргументов).10  
4. Если Datastream строго требует валидации TLS хостнейма, может потребоваться использование собственного CA или самоподписанного сертификата на прокси, либо использование опции "Skip verification" (если доступна). В некоторых случаях, Nginx настраивается на переписывание SNI, но это сложно в реализации с mTLS Atlas.

### **5.2. Стратегия Б: Datastream Forward SSH Tunnel (Альтернативная)**

Datastream предоставляет встроенный механизм "Forward SSH tunnel".5 Это решение позволяет избежать установки и настройки Nginx, перекладывая задачу проксирования на SSH-демон.

Суть решения:  
Datastream устанавливает SSH-соединение с Bastion Host (VM в datastream-net) и пробрасывает порт до MongoDB.  
**Преимущества:**

* **Решение проблемы DNS:** Когда SSH-клиент (Datastream) просит пробросить порт на hostname:27017, разрешение этого имени выполняет **SSH-сервер** (Bastion) на своей стороне.13 Поскольку Bastion находится в datastream-net, он видит Private DNS зону и разрешает имя в IP PSC.  
* **Безопасность:** Весь трафик между Datastream и VPC шифруется SSH.  
* **Простота:** Не нужно настраивать балансировщики нагрузки или сложные конфиги Nginx. Достаточно Linux VM с публичным ключом Datastream.

**Конфигурация в Datastream:**

1. **Connectivity Method:** Forward SSH tunnel.  
2. **SSH Bastion:** IP-адрес VM в datastream-net.  
3. **Hostname (DB):** Каноническое DNS-имя Atlas (напр. cluster0-pl-0.mongodb.net).  
4. **Port:** 27017.

**Почему это работает:** SSH-туннель делает Bastion Host точкой входа. С точки зрения сети, соединение к Atlas инициирует сама VM, у которой нет проблем с маршрутизацией к PSC.

**Ограничения:**

* Производительность SSH-туннелирования ("TCP over TCP") может быть ниже, чем у чистого TCP-прокси, что критично для высоконагруженных потоков CDC.15  
* Необходимость управления SSH-ключами.

### **5.3. Стратегия В: Использование Private Service Connect Interfaces (Перспективная)**

Недавно Google представил возможность создавать PSC Interface непосредственно для Datastream.2 Это отличается от PSA (Peering).  
В этом сценарии Datastream создает сетевой интерфейс (NIC) внутри пользовательской VPC.  
Анализ:  
Если Datastream имеет "ногу" (интерфейс) в datastream-net, он технически становится локальным ресурсом сети.

* **Плюс:** Исчезает проблема транзитивности пиринга (так как нет пиринга, есть присутствие в сети).  
* **Минус:** Проблема DNS может сохраняться. Документация 2 все еще предупреждает: *"You need to provide the private IP addresses... because Datastream doesn't support DNS resolution"*. Даже имея интерфейс в подсети, Datastream может не использовать Cloud DNS резолвер этой подсети, а продолжать использовать свои внутренние.  
* **Вывод:** Этот метод решает проблему маршрутизации, но, вероятно, все еще потребует использования IP-адресов, что возвращает нас к проблеме TLS сертификатов MongoDB. Поэтому стратегии А и Б остаются предпочтительными для MongoDB.

## **6. План действий (Action Plan)**

Для скорейшего решения инцидента и разблокирования проекта P⁎, рекомендуется выполнить следующие шаги. Мы выбираем **Стратегию Б (SSH Tunnel)** как наиболее быструю для проверки (PoC) и **Стратегию А (Proxy VM)** как целевую для продакшна (из-за производительности).

### **Шаг 1: Подготовка Bastion/Proxy VM**

1. В проекте internal-resources-corp в сети datastream-net создать VM (e.g., datastream-gateway).  
2. Убедиться, что на VM разрешен входящий трафик от диапазонов IP Datastream (или конкретного пиринга).  
3. Проверить, что VM может резолвить имена Atlas в приватные IP: nslookup atlas-xxx.mongodb.net.  
4. Проверить связность с Atlas: telnet atlas-xxx.mongodb.net 27017 или mongosh....

### **Шаг 2: Настройка Datastream (Вариант SSH Tunnel)**

1. В Google Cloud Console перейти в Datastream -> Connection Profiles.  
2. Создать новый профиль MongoDB.  
3. Выбрать метод подключения: **Forward SSH tunnel**.  
4. Ввести детали SSH Bastion (IP, User, загрузить приватный ключ, публичный добавить на VM в ~/.ssh/authorized_keys).  
5. В качестве **Hostname** базы данных указать **DNS-имя Atlas** (не IP!).  
   * *Примечание:* Datastream попросит бастион разрешить это имя. Бастион вернет IP PSC. Соединение пойдет через туннель к PSC.  
6. Ввести учетные данные MongoDB пользователя.  
7. Запустить валидацию.

### **Шаг 3: Настройка Datastream (Вариант Proxy - если SSH не подходит)**

1. Настроить Nginx stream proxy на VM (как описано в п. 5.1).  
2. В профиле Datastream выбрать **Private connectivity (VPC peering)**.  
3. В качестве **Hostname** указать **Internal IP** прокси-VM.  
4. **Критически важно:** Если валидация падает на SSL Handshake (из-за несовпадения IP и имени в сертификате), необходимо рассмотреть возможность использования directConnection=true и, если возможно, загрузки корневого сертификата, либо перехода на SSH Tunnel, который прозрачнее работает с именами.

## **7. Заключение**

Анализ подтвердил, что текущая конфигурация клиента ꆜ является неработоспособной из-за фундаментальных ограничений платформы Google Cloud: отсутствия поддержки DNS-разрешения частных зон в Datastream и отсутствия транзитивной маршрутизации к PSC эндпоинтам через VPC Peering. Диагноз "Split-Horizon DNS Failure" верен, но является лишь частью проблемы.

Решение задачи требует изменения архитектуры подключения. Прямое соединение "Datastream -> Peering -> PSC" невозможно. Необходимо внедрение промежуточного узла в пользовательской VPC, который возьмет на себя функции разрешения имен и маршрутизации трафика. Использование **SSH-туннелирования** через бастион-хост является наиболее рекомендуемым способом, так как оно нативно поддерживается Datastream и элегантно обходит обе выявленные проблемы без сложной настройки прокси-серверов.

---

**Таблица: Сравнительный анализ методов подключения**

| Метод | Решает проблему DNS? | Решает проблему PSC Routing? | Сложность настройки | Примечание |
| :---- | :---- | :---- | :---- | :---- |
| **Direct Peering (Текущий)** | ❌ Нет | ❌ Нет | Низкая | **Неработоспособен** для PSC |
| **Proxy VM (Nginx)** | ✅ Да | ✅ Да | Средняя | Требует управления конфигами Nginx |
| **SSH Tunnel** | ✅ Да (через Remote Resolve) | ✅ Да | Низкая | Встроен в Datastream, рекомендуем |
| **PSC Interface** | ❌ Нет (требует IP) | ✅ Да | Высокая | Новая фича, возможны проблемы с TLS |

### ---

**Библиография и источники данных**

В отчете использованы данные из официальной документации Google Cloud и MongoDB, а также анализ предоставленных сниппетов:

* 2: Ограничения DNS в Datastream Private Connectivity.  
* 3: Ограничения транзитивности VPC Peering для PSC.  
* 5: Механика работы SSH-туннелей и удаленного разрешения DNS.  
* 6: Параметры подключения MongoDB (directConnection).  
* 1: Публичная доступность DNS-записей Atlas.

#### **Works cited**

1. Announcing Google Private Service Connect (PSC) Integration for MongoDB Atlas, accessed December 6, 2025, [https://www.mongodb.com/company/blog/product-release-announcements/announcing-google-private-service-connect-psc-integration-mongodb-atlas](https://www.mongodb.com/company/blog/product-release-announcements/announcing-google-private-service-connect-psc-integration-mongodb-atlas)  
2. Create a private connectivity configuration | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration)  
3. Configure VPC peering | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/vpc-peering](https://docs.cloud.google.com/datastream/docs/vpc-peering)  
4. How to use Cloud DNS peering in a Shared VPC environment | Google Cloud Blog, accessed December 6, 2025, [https://cloud.google.com/blog/products/networking/how-to-use-cloud-dns-peering-in-a-shared-vpc-environment/](https://cloud.google.com/blog/products/networking/how-to-use-cloud-dns-peering-in-a-shared-vpc-environment/)  
5. Create connection profiles | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/create-connection-profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles)  
6. MongoDB Integration - Elastic, accessed December 6, 2025, [https://www.elastic.co/docs/reference/integrations/mongodb](https://www.elastic.co/docs/reference/integrations/mongodb)  
7. Connection String Options - Database Manual - MongoDB Docs, accessed December 6, 2025, [https://www.mongodb.com/docs/manual/reference/connection-string-options/](https://www.mongodb.com/docs/manual/reference/connection-string-options/)  
8. Diagnose issues | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/diagnose-issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues)  
9. TLS/SSL Configuration for Clients - Database Manual - MongoDB Docs, accessed December 6, 2025, [https://www.mongodb.com/docs/manual/tutorial/configure-ssl-clients/](https://www.mongodb.com/docs/manual/tutorial/configure-ssl-clients/)  
10. Manage connection profiles | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/manage-connection-profiles](https://docs.cloud.google.com/datastream/docs/manage-connection-profiles)  
11. REST Resource: projects.locations.connectionProfiles | Datastream, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles)  
12. Forward SSH tunnel | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/ssh-tunnel](https://docs.cloud.google.com/datastream/docs/ssh-tunnel)  
13. When using an SSH tunnel does the server resolve domain names or is it still done via the ISP/DNS server on the router? - Information Security Stack Exchange, accessed December 6, 2025, [https://security.stackexchange.com/questions/144297/when-using-an-ssh-tunnel-does-the-server-resolve-domain-names-or-is-it-still-don](https://security.stackexchange.com/questions/144297/when-using-an-ssh-tunnel-does-the-server-resolve-domain-names-or-is-it-still-don)  
14. How to SSH tunnel to a destination host resolved via internal DNS on the bastion host, accessed December 6, 2025, [https://unix.stackexchange.com/questions/598819/how-to-ssh-tunnel-to-a-destination-host-resolved-via-internal-dns-on-the-bastion](https://unix.stackexchange.com/questions/598819/how-to-ssh-tunnel-to-a-destination-host-resolved-via-internal-dns-on-the-bastion)  
15. Network connectivity methods | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/network-connectivity-options](https://docs.cloud.google.com/datastream/docs/network-connectivity-options)  
16. Configure Private Service Connect interfaces | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/psc-interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces)

# 14.
## 14.1.
`D𐊑⠿` ≔ ⠿~ (Заблуждения `ꆜ` относительно `P⁎`)

## 14.2.
`D𐊑ᵢ` : `D𐊑⠿`

## 14.3.
`Pⰳ(D𐊑ᵢ)` ≔
```
Правдоподобность `D𐊑ᵢ`.
Правдоподобность заблуждения `D𐊑ᵢ` означает оценку того, насколько утверждение `D𐊑ᵢ` действительно является заблуждением `ꆜ`. 
```

# 15. Анализ `D𐊑⠿` (выполнен Gemini Deep Think)
https://gemini.google.com/share/344a43072565

## 1. Идентификация `D𐊑⠿`
На основе анализа описания проблемы `PD` и технической документации Google Cloud (Deep Research), мною идентифицировано множество заблуждений `D𐊑⠿`, которых придерживается клиент `ꆜ`.

*   **`D𐊑₁`**: «Нерешённая проблема с DNS (Split-Horizon DNS Failure) является техническим сбоем конфигурации, который можно исправить настройками внутри VPC».
*   **`D𐊑₂`**: «Datastream пытается соединиться с публичными IP-адресами Atlas, потому что он игнорирует («ignoring» / «not utilizing») экспортируемые пользовательские маршруты (Custom Routes)».
*   **`D𐊑₃`**: «Успешное подключение к MongoDB Atlas с тестовой виртуальной машины (DNS Verifier VM), расположенной внутри сети `datastream-net`, подтверждает корректность настройки всей сетевой инфраструктуры для Datastream».
*   **`D𐊑₄`**: «Архитектура, связывающая Datastream с Private Service Connect (PSC) Endpoint через VPC Peering, технически работоспособна при условии решения проблемы с DNS».

## 2. Анализ `D𐊑⠿`

### 2.1. Анализ `D𐊑₁` (Природа проблемы DNS)
**Суть заблуждения:** Клиент убеждён, что сервис Datastream должен видеть Private DNS Zone его сети, а текущее поведение — это «сбой» («Failure»).

#### 2.1.1. Доводы за `Pⰳ(D𐊑₁)` (Почему это заблуждение)
1.  **Документированное ограничение:** Официальная документация Google Cloud Datastream в разделе Private Connectivity явно гласит: *«Datastream doesn't support Domain Name System (DNS) resolution in private connections»*.
2.  **Архитектурная изоляция:** Datastream работает в отдельном тенанте (сети производителя). Механизм Private Services Access (PSA) объединяет таблицы маршрутизации (IP), но не объединяет пространства имен DNS. Резолверы внутри сети Datastream физически не имеют доступа к конфигурации Cloud DNS в проекте пользователя.
3.  **Вывод:** Это не «сбой», а отсутствие функциональности в текущей версии сервиса.

#### 2.1.2. Доводы против `Pⰳ(D𐊑₁)` (Может ли клиент быть прав?)
*   Отсутствуют. Поведение сервиса строго соответствует документации (fallback на публичный DNS 8.8.8.8 при отсутствии локального разрешения).

#### 2.1.3. Оценка `Pⰳ(D𐊑₁)`
**100**

---

### 2.2. Анализ `D𐊑₂` (Игнорирование маршрутов)
**Суть заблуждения:** Клиент утверждает, что причина ухода трафика в публичную сеть — это игнорирование маршрутов.

#### 2.2.1. Доводы за `Pⰳ(D𐊑₂)` (Почему это заблуждение)
1.  **Нарушение причинно-следственной связи:** Маршрутизация (Layer 3) происходит **после** разрешения имени (DNS).
2.  **Механизм:** Поскольку DNS (из-за ограничения `D𐊑₁`) вернул публичный IP-адрес Atlas (например, AWS Public IP), Datastream ищет маршрут именно к этому публичному адресу.
3.  **Неприменимость:** Экспортированные через пиринг Custom Routes указывают на **приватные** подсети (IP PSC Endpoint). Они не были «проигнорированы» — они были технически неприменимы к целевому публичному IP-адресу.

#### 2.2.2. Доводы против `Pⰳ(D𐊑₂)`
*   Нет. Логика клиента фундаментально ошибочна в понимании порядка сетевых операций.

#### 2.2.3. Оценка `Pⰳ(D𐊑₂)`
**100**

---

### 2.3. Анализ `D𐊑₃` (Валидность теста с VM)
**Суть заблуждения:** Клиент считает, что успешный тест с VM внутри сети («✅ VM Connectivity Test») доказывает, что инфраструктура настроена верно, и проблема только в Datastream.

#### 2.3.1. Доводы за `Pⰳ(D𐊑₃)` (Почему это заблуждение)
1.  **Ложная эквивалентность:**
    *   **VM** находится **внутри** периметра VPC и использует локальный Metadata Server (169.254.169.254) для DNS.
    *   **Datastream** находится **снаружи** (в пиринговой сети) и не имеет доступа к этому серверу.
2.  **Разные пути:** VM имеет прямой доступ к PSC Endpoint (Intra-VPC). Datastream пытается получить доступ через пиринг (Inter-VPC). Успех локального теста никак не подтверждает доступность ресурса через пиринговое соединение.

#### 2.3.2. Доводы против `Pⰳ(D𐊑₃)`
*   Тест полезен только для подтверждения того, что сам кластер MongoDB жив. В остальном он вводит в заблуждение относительно связности.

#### 2.3.3. Оценка `Pⰳ(D𐊑₃)`
**95**

---

### 2.4. Анализ `D𐊑₄` (Работоспособность архитектуры)
**Суть заблуждения:** Скрытое убеждение, что топология `Datastream -> Peering -> PSC Endpoint` валидна.

#### 2.4.1. Доводы за `Pⰳ(D𐊑₄)` (Почему это заблуждение)
1.  **Нетранзитивность пиринга:** В Google Cloud существует жесткое ограничение: *«Consumer endpoints cannot be accessed from peered networks»*. Трафик, приходящий из пиринговой сети (Datastream), не может быть направлен в Private Service Connect Endpoint, расположенный в потребительской сети (`datastream-net`).
2.  **Блокирующий фактор:** Даже если клиент решит проблему с DNS (вписав IP вручную), пакеты будут отброшены SDN-контроллером Google на границе сетей или внутри VPC, так как PSC Endpoint не анонсируется в пиринг.

#### 2.4.2. Доводы против `Pⰳ(D𐊑₄)`
*   Существует новая фича *Datastream Private Service Connect interfaces*, которая позволяет такую связь, но она требует создания интерфейса Datastream внутри VPC, а не использования VPC Peering (Private Services Access), как настроено у клиента. В текущей конфигурации это невозможно.

#### 2.4.3. Оценка `Pⰳ(D𐊑₄)`
**100**

## 3. Вердикт
Клиент `ꆜ` находится в состоянии глубокого технического заблуждения.
Все диагностические выводы клиента («Split-Horizon DNS Failure», «Ignoring Custom Routes») неверны, так как основаны на ложных предпосылках о возможностях платформы.

**Главный вывод:** Задача `T⁎` в текущей архитектурной постановке (прямое соединение Datastream через Peering к PSC Endpoint) **технически нерешаема** из-за ограничений Google Cloud (отсутствие DNS resolution и нетранзитивность пиринга к PSC).
Клиенту необходимо изменить архитектуру: внедрить промежуточный прокси (Proxy VM / SSH Bastion) внутри своей VPC или перейти на использование *Datastream PSC Interfaces*.

# 16. Анализ `D𐊑⠿` (выполнен Gemini Deep Research)
https://gemini.google.com/share/f67772b92f0c


## **1. Введение и Архитектурный Контекст**

В современной экосистеме облачной инженерии данных задача интеграции управляемых сервисов Change Data Capture (CDC) со сторонними платформами баз данных (DBaaS) представляет собой сложный архитектурный вызов. Данный отчет представляет собой исчерпывающий анализ проблемы подключения сервиса Google Cloud Datastream к кластерам MongoDB Atlas, использующим архитектуру Private Service Connect (PSC). Документ подготовлен в ответ на запрос клиента (далее — Клиент ꆜ) и основывается на детальном изучении предоставленных материалов (O.md, T.md, L.md), а также широкого спектра технической документации и исследовательских данных.

Основная цель данного отчета — деконструкция архитектурных заблуждений клиента (обозначенных как D𐊑⠿) относительно возможностей прямой интеграции через PSC и разработка детального плана реализации задачи ᛭T. Задача ᛭T подразумевает создание работоспособной, безопасной и масштабируемой схемы подключения, преодолевающей фундаментальные ограничения сетевого стека Google Cloud Platform (GCP) и сетевой модели MongoDB Atlas.

Сложность ситуации обусловлена столкновением двух изолированных программно-определяемых сетей (SDN): управляемой сети Google (где работает Datastream) и управляемой сети MongoDB (где развернут Atlas). Стремление клиента использовать Private Service Connect продиктовано желанием обеспечить безопасность по модели Zero Trust и избежать сложностей, связанных с VPC Peering (конфликты IP-адресов, проблемы с маршрутизацией). Однако, как показывает глубокий анализ, прямая стыковка этих технологий "из коробки" невозможна без применения промежуточных архитектурных паттернов.

В следующих разделах мы проведем глубокую вивисекцию сетевых протоколов, ограничений DNS и механизмов маршрутизации, чтобы доказать необходимость использования проксирующего слоя и предоставить пошаговое руководство по его внедрению.

## **2. Теоретическая База и Сетевые Примитивы**

Для полноценного понимания выявленных проблем и предлагаемых решений необходимо погрузиться в технические детали функционирования задействованных компонентов. Мы рассматриваем взаимодействие трех сетевых доменов:

1. **Producer Network (Google):** Внутренняя сеть, управляемая Google, в которой разворачиваются воркеры Datastream.  
2. **Consumer VPC (Customer):** Пользовательская виртуальная частная сеть (VPC), в которой клиент разворачивает свои ресурсы и через которую планируется транзит трафика.  
3. **Producer Network (MongoDB Atlas):** Сеть, управляемая MongoDB Inc., содержащая кластеры баз данных.

### **2.1 Механика Private Connectivity в Google Cloud Datastream**

Google Cloud Datastream, являясь бессерверным решением, не находится внутри пользовательской VPC. Для доступа к источникам данных, расположенным в частных сетях (on-premise через VPN/Interconnect или внутри GCP), используется механизм "Private Connectivity Configuration". Согласно документации, существуют два метода реализации этого подключения:

1. **VPC Network Peering:** Традиционный метод, создающий прямой пиринг между сетью Datastream и VPC клиента. Этот метод накладывает жесткие ограничения: IP-адреса не должны пересекаться, и, что критически важно, пиринг не является транзитивным.1  
2. **Private Service Connect (PSC) Interfaces:** Более современный метод, при котором Datastream инициирует соединения *из* своей сети *в* сеть клиента через специальный ресурс — Network Attachment.3

Критически важным аспектом, который часто упускается из виду, является отсутствие поддержки разрешения DNS-имен (DNS Resolution) внутри приватных соединений Datastream. Как указано в 4 и 4, сервис требует указания конкретных приватных IPv4-адресов источника данных. Datastream не имеет доступа к Cloud DNS зонам клиента или публичным DNS серверам при работе через приватный канал. Это ограничение становится фатальным при работе с распределенными системами, полагающимися на служебные записи (SRV) и динамическое обнаружение хостов, такими как MongoDB.

### **2.2 Архитектура Сетевого Воздействия MongoDB Atlas**

MongoDB Atlas предоставляет доступ к своим кластерам через аналогичные механизмы, но с инвертированной логикой "Producer-Consumer":

1. **VPC Peering:** Atlas инициирует пиринг с VPC клиента. Из-за нетранзитивности пиринга в GCP, трафик из Datastream (который также имеет пиринг с VPC клиента) не может "протечь" сквозь VPC клиента в VPC Atlas.2  
2. **Private Service Connect (PSC) Endpoints:** Atlas публикует свои сервисы (Service Attachments), а клиент создает в своей VPC PSC Endpoint (Forwarding Rule).6 Это создает в VPC клиента статический внутренний IP-адрес, который маппится на кластер Atlas.

Особенностью MongoDB является использование архитектуры Replica Set, которая требует от драйвера клиента (в данном случае Datastream) знания топологии кластера. При подключении драйвер получает список узлов (Topology Map). В средах с приватным доступом Atlas использует технологию Split Horizon DNS, возвращая клиенту DNS-имена, которые должны разрешаться во внутренние IP-адреса (в данном случае — адреса PSC Endpoint).8

### **2.3 Фундаментальный Конфликт**

Суть проблемы заключается в несовместимости требований этих двух систем при попытке прямого соединения:

* **Datastream** требует IP-адрес и не умеет разрешать DNS.  
* **MongoDB Atlas** требует использования DNS-имен для корректной работы драйверов и SSL-валидации, а также возвращает имена хостов в ответ на команду isMaster/hello.  
* **Сетевая топология:** Попытка соединить Datastream (через PSC Interface) напрямую с Atlas (через PSC Endpoint) в рамках одной VPC невозможна без маршрутизации, так как PSC Interface предназначен для доставки трафика в подсеть, а PSC Endpoint — это правило переадресации, которое не "слушает" трафик из подсети напрямую без прохождения через стек виртуализации, который Datastream не контролирует.

## **3. Анализ Заблуждений Клиента (D𐊑⠿)**

На основе анализа предоставленных (подразумеваемых) файлов O.md и T.md, а также типичных паттернов поведения, описанных в исследовательских сниппетах, мы выявили три ключевых заблуждения клиента ꆜ. Эти заблуждения (D𐊑⠿) блокируют успешную реализацию задачи и требуют детального опровержения.

### **3.1 D𐊑⠿-1: Иллюзия Транзитивности PSC (The Transitivity Fallacy)**

**Суть заблуждения:** Клиент полагает, что использование Private Service Connect автоматически решает проблему транзитивности, свойственную VPC Peering. Логика клиента такова: "Если я подключу Datastream к моей VPC через PSC, и Atlas к моей VPC через PSC, они смогут обмениваться пакетами, так как находятся в одной 'коммутационной среде'".

Опровержение:  
Глубокий анализ документации Google Cloud 2 показывает, что хотя PSC Interface (используемый Datastream) действительно позволяет "приземлить" трафик в VPC клиента, он не создает полноценного сетевого интерфейса, способного маршрутизировать трафик далее в другие PSC Endpoints.

* **Техническое обоснование:** Трафик, исходящий из Datastream, инкапсулируется и доставляется в Network Attachment. Для того чтобы этот трафик попал в PSC Endpoint (ведущий в Atlas), он должен пройти через стек маршрутизации VPC. Однако, правила Google Cloud явно запрещают прямую маршрутизацию от одной управляемой службы к другой через "пассивный" транзит в клиентской VPC без участия активного компонента (VM или NAT), который бы терминировал сессию.  
* **Следствие:** Прямая связь Datastream -> -> VPC -> -> Atlas невозможна. Пакеты будут отброшены SDN-контроллером Google (Andromeda), так как источник трафика (Datastream) не имеет маршрута к назначению (Atlas Service Attachment).

### **3.2 D𐊑⠿-2: Слепое Пятно DNS (The DNS Resolution Blind Spot)**

**Суть заблуждения:** Клиент рассчитывает передать Datastream стандартную строку подключения MongoDB (Connection String), содержащую доменные имена (например, mongodb+srv://cluster0.example.mongodb.net), ожидая, что сервис самостоятельно разрешит их в IP-адреса PSC Endpoint.

Опровержение:  
Это, пожалуй, наиболее критическое заблуждение. Как подтверждается множественными источниками 4, "Datastream не поддерживает разрешение доменных имен (DNS) в приватных соединениях".

* **Техническое обоснование:** Datastream оперирует на уровне L3/L4 модели OSI при установлении приватного соединения. Он ожидает, что пользователь предоставит конкретный IPv4-адрес. Даже если бы Datastream мог принять доменное имя, он не имеет доступа к приватным зонам Cloud DNS клиента (Private Zones), где прописаны A-записи для mongodb.net.9  
* **Сценарий отказа:** Если клиент укажет IP-адрес одного из узлов Atlas, соединение может быть установлено *первично*. Однако протокол MongoDB подразумевает, что узел ответит картой топологии, содержащей *доменные имена* остальных реплик. Драйвер Datastream попытается переподключиться к этим именам и неминуемо потерпит неудачу с ошибкой разрешения имен или "Connection Refused", так как не сможет сопоставить имена с IP-адресами.13

### **3.3 D𐊑⠿-3: Эквивалентность Интерфейсов и Эндпоинтов**

**Суть заблуждения:** Клиент не различает "PSC Interface" и "PSC Endpoint", считая их взаимозаменяемыми "портами" для подключения.

Опровержение:  
В терминологии GCP PSC это полярные сущности:

* **PSC Interface** — это механизм *исходящего* доступа (Egress) для производителя сервиса (Datastream). Он позволяет продюсеру инициировать соединение *к* потребителю.  
* PSC Endpoint — это механизм входящего доступа (Ingress) для потребителя. Он позволяет потребителю инициировать соединение к продюсеру (Atlas).  
  Попытка соединить "Выход" (Datastream) с "Входом" (Atlas) требует наличия "Провода" между ними. В облачной сети этим "проводом" не может быть просто VPC; требуется активный посредник, который примет запрос от Datastream и перенаправит его в Atlas.10

## **4. Задача ᛭T: Реализация Архитектуры Проксирования**

На основании выявленных ограничений и анализа заблуждений, единственным архитектурно верным решением задачи ᛭T является внедрение **Промежуточного Проксирующего Слоя (Proxy Mediation Layer)**. Это решение не является "костылем", а представляет собой стандартный паттерн "Transitive Bridge" в облачных архитектурах, где требуется связность между изолированными Tenant-сетями.

### **4.1 Архитектурный Дизайн Решения**

Мы предлагаем архитектуру, состоящую из следующих компонентов:

1. **Google Cloud Datastream:** Настроен с использованием Private Connectivity (через PSC Interface).  
2. **Customer VPC:** Центральный узел связности.  
3. **Proxy Virtual Machine (Bastion):** Экземпляр Google Compute Engine (GCE), выполняющий роль транслятора протоколов и DNS-резолвера.  
4. **Network Attachment:** Точка входа для трафика Datastream в VPC клиента.  
5. **PSC Endpoint (Atlas):** Точка выхода трафика из VPC клиента в сеть MongoDB Atlas.  
6. **Cloud DNS:** Приватная зона для разрешения имен Atlas внутри VPC.

#### **Логическая Схема Потока Данных**

Datastream (Producer) -> -> `Network Attachment (Customer VPC)` -> `Proxy VM` -> -> PSC Endpoint (Atlas) -> MongoDB Cluster

### **4.2 Сравнительный Анализ Вариантов Проксирования**

Для реализации проксирующего слоя были рассмотрены два основных подхода. Результаты сравнения представлены в Таблице 1.

| Характеристика | Вариант А: L4 TCP Proxy (HAProxy/Nginx) | Вариант Б: Forward SSH Tunnel |
| :---- | :---- | :---- |
| **Производительность** | **Высокая**. Минимальный оверхед на пересылку пакетов. Подходит для high-throughput CDC. | **Низкая/Средняя**. Двойное шифрование (SSH + TLS Mongo) создает нагрузку на CPU. Ограниченная пропускная способность TCP-over-TCP. |
| **Устойчивость** | **Высокая**. Прокси-сервисы (HAProxy) созданы для долгих соединений. | **Средняя**. SSH-туннели могут разрываться при простоях, требуют механизмов keep-alive. |
| **Сложность настройки** | Средняя. Требует конфигурации конфиг-файлов прокси. | Низкая. Встроена в интерфейс Datastream.16 |
| **DNS Resolution** | **Гибкая**. Прокси использует системный резолвер VM, который видит Cloud DNS. | **Автоматическая**. Резолвинг происходит на стороне SSH-сервера (Bastion). |
| **Совместимость с PSC** | Полная. Трафик приходит на IP VM. | Полная. Требует только доступа по порту 22. |
| **Рекомендация** | **Рекомендуется для Production** | Рекомендуется для PoC / Dev |

**Выбор для задачи ᛭T:** Учитывая требование к надежности и производительности CDC-потоков, мы выбираем **Вариант А (L4 TCP Proxy)**. Использование SSH-туннеля, хоть и поддерживается нативно 17, вводит дополнительную точку отказа и "узкое горлышко" по CPU, что критично при больших объемах репликации данных.

### **4.3 Детальный План Реализации**

Ниже представлен пошаговый алгоритм выполнения задачи ᛭T, интегрирующий все необходимые исправления заблуждений D𐊑⠿.

#### **Шаг 1: Подготовка Сетевой Инфраструктуры (Customer VPC)**

1. **Настройка PSC Endpoint для MongoDB Atlas:**  
   * В консоли MongoDB Atlas создать Private Endpoint для Google Cloud.  
   * В консоли GCP создать PSC Endpoint (Forwarding Rule), указывающий на Service Attachment, предоставленный Atlas.  
   * *Результат:* Получен статический IP-адрес (например, 10.128.0.50), ведущий в Atlas.6  
2. **Настройка Cloud DNS (Split Horizon Simulation):**  
   * Создать Private DNS Zone в GCP для домена mongodb.net (или конкретного поддомена кластера).  
   * Добавить A-записи для всех узлов кластера (Primary, Secondaries), указывающие на **IP-адрес PSC Endpoint** (10.128.0.50).  
   * *Обоснование:* Это позволяет Прокси-VM разрешать имена, возвращаемые Atlas, в локальный IP-адрес Endpoint'а.9

#### **Шаг 2: Развертывание Proxy VM**

1. **Создание VM:**  
   * Развернуть минимальный инстанс Compute Engine (e.g., e2-medium) в той же VPC и регионе.  
   * ОС: Ubuntu 22.04 LTS или Debian 11.  
2. **Установка и Конфигурация ПО (Nginx Stream):**  
   * Установить Nginx с модулем stream.  
   * Конфигурация (nginx.conf):  
     Nginx  
     stream {  
         server {  
             listen 27017;  
             proxy_pass cluster0-shard-00.mongodb.net:27017;  
             proxy_connect_timeout 10s;  
             proxy_timeout 24h;  
         }  
     }

   * *Важно:* Nginx будет использовать системный DNS-резолвер (169.254.169.254), который, благодаря настройке Cloud DNS на Шаге 1, вернет IP-адрес PSC Endpoint'а.15

#### **Шаг 3: Настройка Входящего Соединения от Datastream**

1. **Создание Network Attachment:**  
   * Создать ресурс Network Attachment в подсети, где находится Proxy VM. Выбрать политику "Accept connection automatically".3  
2. **Настройка Firewall Rules:**  
   * Создать правило Firewall, разрешающее входящий трафик на порт 27017 (и 22 для администрирования) для Proxy VM.  
   * *Source:* Диапазон IP-адресов, который будет выделен для Datastream Private Connection (обычно /29).14

#### **Шаг 4: Конфигурация Datastream**

1. **Создание Private Connectivity Configuration:**  
   * Выбрать метод "Private Service Connect Interface".  
   * Указать созданный ранее Network Attachment.  
   * Datastream выделит себе IP-адрес в подсети Network Attachment.  
2. **Создание Connection Profile (MongoDB):**  
   * **Hostname:** Указать **Внутренний IP-адрес Proxy VM** (например, 10.128.0.5). **Не** использовать доменное имя Atlas!.5  
   * **Port:** 27017.  
   * **Authentication:** Стандартные учетные данные Atlas.  
   * **Connection Options:** Критически важно добавить параметр directConnection=true.21

### **4.4 Роль параметра directConnection=true**

Этот аспект требует особого внимания, так как часто становится причиной сбоев даже при корректной сетевой настройке.

По умолчанию драйверы MongoDB при подключении к Replica Set пытаются обнаружить все узлы кластера (Auto-Discovery).

1. Datastream подключается к Proxy VM (10.128.0.5).  
2. Proxy пересылает запрос в Atlas.  
3. Atlas отвечает: "Я Primary узел shard-00-01.mongodb.net. Мои соседи: shard-00-02 и shard-00-03".  
4. Драйвер Datastream, получив этот ответ, пытается закрыть соединение с "неизвестным" хостом 10.128.0.5 и открыть прямые соединения к shard-00-xx.mongodb.net.  
5. **Сбой:** Datastream не может разрешить эти имена (см. D𐊑⠿-2).

**Решение:** Установка флага directConnection=true (или использование "Direct Connection" в настройках профиля Datastream 23) принуждает драйвер работать в режиме "Standalone". Он игнорирует топологию и продолжает работать только через тот хост (Proxy IP), который был указан изначально. Вся маршрутизация к актуальному Primary узлу ложится на плечи PSC Endpoint и внутренней балансировки Atlas.

## **5. Дополнительные Исследовательские Данные и Инсайты**

В ходе выполнения Deep Research были выявлены дополнительные факторы, влияющие на стабильность и стоимость решения.

### **5.1 Стоимость и Оптимизация PSC**

Исследование 25 подчеркивает, что использование PSC может быть дорогим удовольствием. Каждый PSC Endpoint тарифицируется почасово, плюс оплата за обработанный трафик. В сценарии с прокси мы используем один Endpoint для доступа ко всему кластеру (если использовать Connection String уровня кластера), что является оптимальным с точки зрения затрат по сравнению с созданием отдельных Endpoint'ов для каждого шарда.

### **5.2 Проблема "Connection Refused" и ACL**

Сниппеты 13 указывают на распространенную проблему "Connection Refused". В контексте Atlas PSC это часто вызвано не только сетевой недоступностью, но и **IP Access List** в самом Atlas. Даже при использовании Private Endpoint, настройки Network Access в Atlas должны быть корректными. Традиционный "Allowlist" IP-адресов в Atlas обычно не применяется к трафику, приходящему через PrivateLink/PSC, так как доверие устанавливается на уровне идентификатора VPC/Link. Однако, проверка конфигурации Network Peering и отсутствие блокирующих правил — обязательный шаг диагностики.

### **5.3 Альтернатива через SSH Tunneling (детальный взгляд)**

Хотя мы рекомендовали Proxy VM, вариант с SSH туннелем 16 заслуживает внимания для сценариев с низкой пропускной способностью.

* **Механизм:** Datastream действует как SSH-клиент. Вы создаете Bastion Host. В профиле Datastream выбираете "Forward SSH Tunnel".  
* **Преимущество:** Не нужно настраивать Nginx/HAProxy. Не нужно настраивать сложные Network Attachments (достаточно публичного IP на бастионе с ограничением доступа только для IP Datastream, либо также через приватный канал).  
* **Недостаток:** Двойная инкапсуляция. Datastream шифрует трафик SSH, внутри которого идет шифрованный трафик MongoDB. Это создает значительный оверхед. Кроме того, SSH-туннели TCP-over-TCP могут страдать от проблемы "TCP Meltdown" при потере пакетов.

## **6. Операционные Аспекты и Мониторинг**

Для обеспечения промышленной эксплуатации решения необходимо внедрить следующие практики:

### **6.1 Мониторинг Прокси**

Proxy VM становится единой точкой отказа (SPOF). Рекомендуется:

1. Использовать **Managed Instance Group (MIG)** с автовосстановлением для Proxy VM. Если процесс Nginx падает или VM зависает, GCP автоматически пересоздаст инстанс.  
2. Настроить **Internal Load Balancer (ILB)** перед группой Proxy VM, если требуется высокая доступность (HA). Datastream будет подключаться к VIP ILB, который распределит трафик по здоровым нодам прокси.

### **6.2 Логирование**

Необходимо включить логирование соединений в Nginx (log_format stream_routing) и отправлять логи в Cloud Logging. Это позволит отслеживать разрывы соединений, длительность сессий и объемы переданных данных, что критично для диагностики проблем репликации CDC.

## **7. Заключение**

Анализ задачи подключения Google Cloud Datastream к MongoDB Atlas через Private Service Connect показал, что интуитивное ожидание "прямой совместимости" двух технологий PSC является ошибочным (D𐊑⠿). Ограничения транзитивности сетей Google Cloud и отсутствие поддержки DNS в приватных коннекторах Datastream делают невозможным прямое соединение без посредника.

Реализация задачи ᛭T требует внедрения архитектурного паттерна **"Proxy Bridge"**. Предложенное решение, включающее использование Compute Engine VM с TCP-проксированием, Network Attachments и симуляцию Split Horizon DNS, полностью удовлетворяет требованиям безопасности (трафик не покидает приватные сети) и функциональности.

Ключевым фактором успеха является использование параметра directConnection=true в профиле Datastream, что позволяет обойти сложную логику обнаружения узлов MongoDB и делегировать маршрутизацию инфраструктуре Private Service Connect. Предложенная архитектура является надежной, масштабируемой и соответствует лучшим практикам построения гибридных облачных сетей.

### **Резюме по исправлению заблуждений (Remediation Summary)**

| Заблуждение Клиента (D𐊑⠿) | Реальность GCP/MongoDB | Решение в Задаче ᛭T |
| :---- | :---- | :---- |
| **D𐊑⠿-1:** Транзитивность PSC | PSC Interface -> PSC Endpoint не работает напрямую. | Внедрение **Proxy VM** для терминации и пересоздания соединения. |
| **D𐊑⠿-2:** DNS в Datastream | Datastream требует IP, не умеет резолвить имена. | Использование **IP-адреса Прокси** в конфиге Datastream + Cloud DNS на стороне Прокси. |
| **D𐊑⠿-3:** Прямое подключение к Replica Set | Драйвер пытается переключиться на имена узлов. | Принудительное использование **directConnection=true** для фиксации маршрута через прокси. |

---

Автор отчета: Ведущий Архитектор Облачных Решений (Senior Cloud Solutions Architect)  
Дата: 06 декабря 2025 г.  
Версия документа: 1.0 (Final Release)

#### **Works cited**

1. VPC Network Peering | Virtual Private Cloud, accessed December 6, 2025, [https://docs.cloud.google.com/vpc/docs/vpc-peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)  
2. Configure VPC peering | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/vpc-peering](https://docs.cloud.google.com/datastream/docs/vpc-peering)  
3. Configure Private Service Connect interfaces | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/psc-interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces)  
4. Create a private connectivity configuration | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration)  
5. Configuring Google Cloud Datastream private connectivity with cloud sql for postgreSQL | by Hnacino | Medium, accessed December 6, 2025, [https://medium.com/@hnacino/configuring-google-cloud-datastream-private-connectivity-with-cloud-sql-for-postgresql-95272d6c19c2](https://medium.com/@hnacino/configuring-google-cloud-datastream-private-connectivity-with-cloud-sql-for-postgresql-95272d6c19c2)  
6. Example: Private connectivity for a MongoDB Atlas cluster | Integration Connectors, accessed December 6, 2025, [https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb)  
7. Learn About Private Endpoints in Atlas - Atlas - MongoDB Docs, accessed December 6, 2025, [https://www.mongodb.com/docs/atlas/security-private-endpoint/](https://www.mongodb.com/docs/atlas/security-private-endpoint/)  
8. Split-DNS Horizons usage with Percona Server for MongoDB, accessed December 6, 2025, [https://docs.percona.com/percona-server-for-mongodb/7.0/horizon.html](https://docs.percona.com/percona-server-for-mongodb/7.0/horizon.html)  
9. Resolve Split-Horizon DNS on Google Cloud Platform (GCP) - Medium, accessed December 6, 2025, [https://medium.com/google-cloud/resolve-split-horizon-dns-on-google-cloud-platform-gcp-a861d9c0e1d6](https://medium.com/google-cloud/resolve-split-horizon-dns-on-google-cloud-platform-gcp-a861d9c0e1d6)  
10. About Private Service Connect interfaces - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces)  
11. Private Service Connect - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/vpc/docs/private-service-connect](https://docs.cloud.google.com/vpc/docs/private-service-connect)  
12. Database Migration Service (DMS), VPN and private DNS resolution - #2 by greb - Compute Infrastructure - Google Developer forums, accessed December 6, 2025, [https://discuss.google.dev/t/database-migration-service-dms-vpn-and-private-dns-resolution/173970/2](https://discuss.google.dev/t/database-migration-service-dms-vpn-and-private-dns-resolution/173970/2)  
13. Recently Active 'connection-refused' Questions - Page 2 - Stack Overflow, accessed December 6, 2025, [https://stackoverflow.com/questions/tagged/connection-refused?page=2&sort=Active&pageSize=50](https://stackoverflow.com/questions/tagged/connection-refused?page=2&sort=Active&pageSize=50)  
14. Diagnose issues | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/diagnose-issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues)  
15. Connecting Datastream to Cloud SQL postgres over private IP: Do I need a reverse proxy even if they are in the same project? - Stack Overflow, accessed December 6, 2025, [https://stackoverflow.com/questions/77438318/connecting-datastream-to-cloud-sql-postgres-over-private-ip-do-i-need-a-reverse](https://stackoverflow.com/questions/77438318/connecting-datastream-to-cloud-sql-postgres-over-private-ip-do-i-need-a-reverse)  
16. Network connectivity methods | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/network-connectivity-options](https://docs.cloud.google.com/datastream/docs/network-connectivity-options)  
17. Forward SSH tunnel | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/ssh-tunnel](https://docs.cloud.google.com/datastream/docs/ssh-tunnel)  
18. Connect to an instance using Private Service Connect | Cloud SQL for MySQL, accessed December 6, 2025, [https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect)  
19. Introducing Private DNS Zones: resolve to keep internal networks concealed - Google Cloud, accessed December 6, 2025, [https://cloud.google.com/blog/products/networking/introducing-private-dns-zones-resolve-to-keep-internal-networks-concealed](https://cloud.google.com/blog/products/networking/introducing-private-dns-zones-resolve-to-keep-internal-networks-concealed)  
20. google_compute_network_attac, accessed December 6, 2025, [https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_attachment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_attachment)  
21. Connection String Options - Database Manual - MongoDB Docs, accessed December 6, 2025, [https://www.mongodb.com/docs/manual/reference/connection-string-options/](https://www.mongodb.com/docs/manual/reference/connection-string-options/)  
22. gcp.datastream.ConnectionProfile | Pulumi Registry, accessed December 6, 2025, [https://www.pulumi.com/registry/packages/gcp/api-docs/datastream/connectionprofile/](https://www.pulumi.com/registry/packages/gcp/api-docs/datastream/connectionprofile/)  
23. REST Resource: projects.locations.connectionProfiles | Datastream, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles)  
24. Manage connection profiles | Datastream - Google Cloud Documentation, accessed December 6, 2025, [https://docs.cloud.google.com/datastream/docs/manage-connection-profiles](https://docs.cloud.google.com/datastream/docs/manage-connection-profiles)  
25. Atlas Mongo <-> GCP private connectivity using PSC, is this the best option?, accessed December 6, 2025, [https://discuss.google.dev/t/atlas-mongo-gcp-private-connectivity-using-psc-is-this-the-best-option/188902](https://discuss.google.dev/t/atlas-mongo-gcp-private-connectivity-using-psc-is-this-the-best-option/188902)  
26. Configure connectivity using reverse SSH tunnel | Database Migration Service | Google Cloud Documentation, accessed December 6, 2025, [https://cloud.google.com/database-migration/docs/postgres/configure-connectivity-reverse-ssh-tunnel](https://cloud.google.com/database-migration/docs/postgres/configure-connectivity-reverse-ssh-tunnel)

# 17.
## 17.1.
`T༄` ≔ `T⁎`

## 17.2.
`Aᚖ⠿` ≔ ⠿~ (Альтернативные `T༄` способы решения выявленных источников беспокойства `ꆜ` (`O.md::§12`, `O.md::§13`))

## 17.3.
`Aᚖᵢ` : `Aᚖ⠿`

# 18. Анализ `Aᚖ⠿` (выполнен Gemini Deep Think)
https://gemini.google.com/share/1238ab0d795a

## `Aᚖ₁`: SSH-туннелирование (Bastion Host)

### Суть
Данный архитектурный паттерн предполагает использование встроенного в Datastream механизма «Forward SSH tunnel» для инкапсуляции трафика репликации внутрь защищенного соединения.
В качестве точки входа в сеть клиента (`datastream-net`) используется простая виртуальная машина (Bastion Host), доступная по приватному IP-адресу через Private Service Access (PSA).
Сервис Datastream устанавливает SSH-сессию с этим бастионом и запрашивает перенаправление TCP-трафика на доменное имя кластера MongoDB Atlas.
SSH-демон, запущенный на бастионе, выполняет разрешение DNS-имени Atlas, используя локальный резолвер VPC, который имеет доступ к Private DNS Zone и возвращает корректные IP-адреса Private Service Connect (PSC).
После разрешения адреса бастион устанавливает соединение с конечной точкой PSC и транслирует зашифрованный поток данных между Datastream и базой данных.
Такая схема позволяет Datastream обращаться к целевому хосту по имени, что критически важно для корректной валидации TLS-сертификатов MongoDB.

### Оценка
95

### Достоинства
Это решение является нативным для Google Cloud Datastream и официально рекомендуется для сценариев со сложной сетевой топологией.
Архитектура автоматически устраняет проблему `P2†` (DNS Split-Horizon), так как резолвинг имен выполняется внутри периметра VPC, где настроена приватная зона.
Полностью решается проблема `P1†` (Public IP), поскольку бастион направляет трафик строго на приватные IP-адреса PSC Endpoint.
Метод обходит ограничение нетранзитивности VPC Peering, так как соединение терминируется на бастионе и пересоздается внутри целевой сети.
Использование доменных имен при подключении гарантирует успешное прохождение TLS Handshake без ошибок «Hostname Mismatch».
Конфигурация на стороне пользователя минимальна и сводится к развертыванию одной VM с публичным ключом Datastream.

### Недостатки
Инкапсуляция протокола базы данных внутрь SSH (TCP-over-TCP) создает дополнительные накладные расходы на процессор и снижает эффективную пропускную способность (MTU).
В сценариях с экстремально высокой нагрузкой (High Throughput CDC) производительность одного SSH-туннеля может стать узким местом («bottle neck»).
Бастион-хост становится единой точкой отказа (SPOF), что требует настройки механизмов автовосстановления (Managed Instance Group) для обеспечения надежности.

## `Aᚖ₂`: Промежуточный L4 TCP-прокси (Proxy VM)

### Суть
Этот подход подразумевает развертывание в сети клиента (`datastream-net`) выделенной виртуальной машины с программным обеспечением для балансировки нагрузки (Nginx или HAProxy).
Datastream подключается к приватному IP-адресу этой прокси-машины через VPC Peering, используя строку подключения MongoDB с параметром `directConnection=true`.
Прокси-сервер принимает входящие TCP-пакеты на порт 27017, разрешает имя назначения MongoDB Atlas через системный DNS и пересылает трафик на PSC Endpoint.
Для обеспечения работоспособности прокси настраивается в режиме `stream` (Layer 4), прозрачно передавая зашифрованный трафик без терминации SSL.
Драйвер Datastream настраивается принудительно на работу с одним узлом, чтобы избежать попыток автоматического обнаружения топологии кластера и ухода с прокси.

### Оценка
80

### Достоинства
Проксирование на транспортном уровне (L4) обеспечивает высокую производительность и минимальные задержки, превосходя SSH-туннелирование.
Решение предоставляет администраторам полный контроль над параметрами сетевого стека, включая настройки `keepalive`, таймауты и буферы.
Отсутствует двойное шифрование данных, что снижает нагрузку на CPU прокси-сервера по сравнению с SSH-шлюзом.
Архитектура позволяет легко масштабироваться горизонтально, размещая прокси-серверы за внутренним балансировщиком нагрузки (Internal Load Balancer).

### Недостатки
Фундаментальной проблемой является несоответствие имени хоста в TLS-сертификате: Datastream подключается к IP прокси, а получает сертификат для домена `*.mongodb.net`.
Для устранения ошибки валидации сертификата требуется либо отключение проверки подлинности (что небезопасно), либо сложная настройка перешифрования (SSL Re-encryption) с управлением собственным CA.
Внедрение требует глубокой экспертизы в администрировании Nginx/HAProxy и усложняет эксплуатацию инфраструктуры.
Необходимость использования флага `directConnection` ограничивает возможности драйвера по автоматическому переключению (Failover) при сбоях узлов базы данных.

## `Aᚖ₃`: Подключение через публичный интернет (Public Access List)

### Суть
Данный альтернативный сценарий предполагает отказ от использования приватных каналов связи (Private Service Connect и Peering) в пользу публичной маршрутизации.
В настройках сетевого доступа MongoDB Atlas (Network Access) создается правило, разрешающее входящие соединения с публичных статических IP-адресов сервиса Datastream.
Трафик данных передается через публичный интернет, но защищается обязательным шифрованием TLS на уровне протокола MongoDB.
В профиле подключения Datastream используется стандартный метод «Public connectivity» и публичное доменное имя кластера.

### Оценка
30

### Достоинства
Это технически простейшее решение, не требующее настройки DNS, виртуальных машин, пиринга или прокси-серверов.
Полностью исключаются все проблемы, связанные с транзитивной маршрутизацией, Split-Horizon DNS и приватными зонами.
Отсутствуют дополнительные расходы на инфраструктуру Google Cloud (Compute Engine, Network Traffic).

### Недостатки
Решение грубо нарушает исходное требование задачи `T༄` об исключении прохождения трафика через публичный интернет («avoid public internet traversal»).
Использование публичных сетей увеличивает поверхность атаки и может противоречить корпоративным политикам безопасности (Compliance).
Публичные IP-адреса Datastream могут изменяться, что создает необходимость постоянного обслуживания списков доступа (Maintenance Overhead).
Сетевые задержки и стабильность канала через публичный интернет менее предсказуемы по сравнению с выделенным интерконнектом.

## Итоговый вердикт

Исходный план `T༄` технически нереализуем в текущей конфигурации из-за документированных ограничений Google Cloud Platform.
Главные препятствия — это отсутствие DNS-резолвинга в приватных соединениях Datastream и нетранзитивность пиринга для Private Service Connect.
Я рекомендую использовать решение **`Aᚖ₁` (SSH-туннелирование)** в качестве основного и наиболее надежного способа выполнения задачи `T⁎`.
Этот метод получил наивысшую оценку (95), так как он «из коробки» решает проблемы маршрутизации и DNS, корректно обрабатывает TLS-сертификаты и официально поддерживается вендором.
Решение `Aᚖ₂` (Proxy VM) следует рассматривать только в том случае, если производительность SSH-туннеля окажется недостаточной и у команды есть экспертиза для решения проблем с подменой SSL-сертификатов.
Вам необходимо развернуть Bastion Host в сети `datastream-net` и перенастроить профиль соединения Datastream на использование метода «Forward SSH tunnel».

# 19. Анализ `Aᚖ⠿` (выполнен Gemini Deep Research)
https://gemini.google.com/share/78382e3d4701

## **Aᚖ₁: Промежуточный прокси-сервер L4 (TCP Proxy VM)**

### **Суть**

Данная архитектурная альтернатива предполагает развертывание выделенного вычислительного инстанса в пользовательской виртуальной сети для транзита трафика.  
В рамках этой стратегии создается виртуальная машина Google Compute Engine в сети datastream-net, которая выступает в качестве промежуточного шлюза.  
На этом инстансе развертывается программное обеспечение для балансировки нагрузки и проксирования на транспортном уровне модели OSI, например, Nginx с модулем stream или HAProxy.  
Сервис Datastream конфигурируется для установления соединения с приватным IP-адресом этой виртуальной машины через существующий механизм VPC Peering.  
Прокси-сервер принимает входящие TCP-соединения от Datastream на определенном порту и перенаправляет их на адрес Private Service Connect Endpoint, ведущий к MongoDB Atlas.1  
Ключевой особенностью является то, что прокси-сервер находится внутри периметра безопасности пользователя, что дает ему доступ к локальной инфраструктуре DNS.  
Благодаря этому прокси-сервер способен корректно разрешать приватные доменные имена MongoDB Atlas, используя настроенную зону Cloud DNS mongo-psc-isolated.  
Это позволяет обойти ограничение сервиса Datastream, который не поддерживает разрешение имен в приватных соединениях.2  
Трафик передается в режиме TCP Passthrough, что означает отсутствие терминации SSL/TLS на стороне прокси-сервера.  
Шифрованный поток данных передается от Datastream к MongoDB Atlas в неизменном виде, обеспечивая целостность сквозного шифрования.  
Для корректной работы драйвера MongoDB, инициируемого Datastream, необходимо использовать параметр directConnection=true.3  
Это требование обусловлено тем, что стандартный механизм обнаружения топологии кластера MongoDB возвращает список хостов, к которым драйвер пытается переподключиться напрямую.  
В случае использования прокси-сервера драйвер должен оставаться подключенным к единственной точке входа — IP-адресу прокси.  
Таким образом, данное решение создает необходимый мост между изолированными сетевыми сегментами, преодолевая отсутствие транзитивной маршрутизации в VPC Peering.4

### **Оценка**

95

### **Достоинства**

Данное решение обеспечивает полный и гранулярный контроль над процессом маршрутизации трафика данных между изолированными сетями.  
Инженеры получают возможность управлять таймаутами соединений, размерами буферов и поведением при сбоях на уровне конфигурации Nginx или HAProxy.5  
Решение проблемы Split-Horizon DNS реализуется наиболее естественным образом через использование системного резолвера операционной системы виртуальной машины.  
Это устраняет необходимость в сложных манипуляциях с файлами hosts или попытках внедрения DNS-записей в недоступные среды управляемых сервисов.  
Производительность современных прокси-серверов на уровне L4 позволяет обрабатывать гигабитные потоки данных с минимальными накладными расходами процессорного времени.6  
Отсутствие двойной инкапсуляции трафика, характерной для туннельных решений, снижает вероятность фрагментации пакетов и повышает пропускную способность.  
Использование стандартных протоколов TCP/IP гарантирует совместимость с любыми версиями баз данных и клиентов без привязки к проприетарным механизмам облака.  
Решение позволяет реализовать расширенное логирование сетевой активности, фиксируя каждый факт установления и разрыва соединения для аудита безопасности.  
Виртуальная машина прокси-сервера может быть легко интегрирована в существующие системы мониторинга инфраструктуры для отслеживания метрик здоровья.  
Возможность использования внутренних балансировщиков нагрузки Google Cloud перед группой прокси-серверов обеспечивает горизонтальную масштабируемость решения.  
Стоимость эксплуатации данного решения остается низкой, так как для проксирования трафика достаточно вычислительных мощностей базовых типов инстансов, таких как e2-micro.7  
Этот подход является проверенным индустриальным стандартом для организации транзитного доступа в сложных облачных топологиях с нетранзитивным пирингом.  
Конфигурация прокси-сервера может быть полностью описана в коде (Infrastructure as Code) с использованием Terraform или Ansible, что упрощает воспроизводимость среды.  
Решение не требует от сервиса Datastream поддержки специфических функций, полагаясь только на базовую возможность подключения по приватному IP.  
Обеспечивается строгая изоляция контуров, так как прокси-сервер может быть настроен на прием соединений только из диапазона IP-адресов Datastream.

### **Недостатки**

Внедрение промежуточной виртуальной машины неизбежно увеличивает эксплуатационную нагрузку на команду сопровождения инфраструктуры.  
Требуется регулярное обновление операционной системы и программного обеспечения прокси-сервера для устранения уязвимостей безопасности.  
Виртуальная машина становится потенциальной единой точкой отказа в архитектуре, если не приняты меры по обеспечению высокой доступности.  
Для реализации отказоустойчивости необходимо настраивать группы инстансов и механизмы автоматического восстановления, что усложняет архитектуру.  
Использование параметра directConnection=true отключает встроенные в драйвер MongoDB механизмы автоматического переключения на новый мастер-узел при сбоях.8  
Это перекладывает ответственность за обнаружение сбоев и перенаправление трафика на инфраструктуру Private Service Connect и балансировщики нагрузки Atlas.  
Существует риск возникновения сложностей с валидацией SSL-сертификатов, если клиент ожидает совпадения IP-адреса подключения с именем в сертификате.  
Хотя режим TCP Passthrough передает SNI от клиента, несоответствие адреса назначения может вызвать ошибки в некоторых строгих конфигурациях TLS-клиентов.  
Добавление дополнительного сетевого узла (хопа) в путь прохождения пакета теоретически увеличивает задержку передачи данных.  
Необходимость ручного управления правилами брандмауэра для прокси-сервера повышает риск человеческой ошибки при конфигурировании доступа.  
Мониторинг состояния самого процесса проксирования требует настройки специализированных агентов и сбора метрик, отличных от метрик управляемых сервисов.  
В случае масштабных атак или аномальных всплесков трафика прокси-сервер может стать узким местом, исчерпав лимиты сетевой пропускной способности инстанса.  
Расходы на исходящий трафик могут возрасти, если прокси-сервер и целевой эндпоинт находятся в разных зонах доступности, так как трафик проходит через VM.  
Настройка корректного keepalive для долгоживущих соединений CDC требует глубокого понимания параметров ядра Linux и конфигурации прокси.9  
Ошибки в конфигурации прокси-сервера могут быть неочевидны и требовать сложной диагностики с анализом сетевых дампов.

## **Aᚖ₂: SSH-туннелирование через Bastion Host (Native Feature)**

### **Суть**

Данный метод базируется на использовании встроенной функциональности сервиса Datastream для установления защищенных соединений через промежуточный хост.  
В архитектуре развертывается виртуальная машина в сети datastream-net, выполняющая роль SSH-бастиона, к которому Datastream подключается как SSH-клиент.  
Настройка производится непосредственно в интерфейсе создания профиля соединения Datastream, где выбирается метод "Forward SSH tunnel".10  
Datastream устанавливает зашифрованное SSH-соединение с бастионом, используя пару криптографических ключей или пароль для аутентификации.  
В рамках этого SSH-соединения создается туннель, который перенаправляет трафик с локального порта сервиса Datastream на целевой хост и порт MongoDB Atlas.  
Критически важным аспектом является то, что разрешение DNS-имени целевого хоста выполняется на стороне бастиона, а не на стороне Datastream.11  
Когда Datastream запрашивает соединение к доменному имени кластера Atlas, SSH-сервер на бастионе использует локальные настройки DNS для получения IP-адреса.  
Поскольку бастион находится в пользовательской VPC, он имеет доступ к Cloud DNS Private Zone и корректно разрешает имя в приватный IP-адрес PSC Endpoint.  
Трафик базы данных инкапсулируется внутри пакетов SSH и передается через пиринговое соединение или публичную сеть к бастиону.  
Бастион извлекает пакеты базы данных и пересылает их на PSC Endpoint, выступая в роли инициатора соединения внутри сети VPC.  
Этот метод позволяет обойти ограничения нетранзитивной маршрутизации, так как с точки зрения сети соединение исходит от локального ресурса VPC.12  
Datastream автоматически управляет поддержанием SSH-сессии, выполняя переподключение в случае разрыва связи.  
Для реализации требуется добавить публичный ключ Datastream в файл authorized_keys на бастионе и разрешить входящие SSH-соединения на сетевом уровне.  
Использование данного метода официально рекомендовано Google для сценариев подключения к источникам данных, находящимся в защищенных сетях.13  
Конфигурация профиля соединения включает указание адреса бастиона, учетных данных и целевых параметров базы данных MongoDB.

### **Оценка**

85

### **Достоинства**

Этот метод является нативным для сервиса Datastream, что гарантирует полную поддержку и совместимость со стороны облачного провайдера.  
Отсутствует необходимость в установке и сложной настройке дополнительного программного обеспечения, такого как веб-серверы или специализированные прокси.  
Решение проблемы разрешения имен DNS происходит автоматически благодаря архитектуре протокола SSH, поддерживающего удаленный резолвинг.12  
Это устраняет необходимость в настройке локальных резолверов или модификации файлов конфигурации на стороне источника данных.  
Весь трафик данных между Datastream и пользовательской сетью дополнительно шифруется протоколом SSH, обеспечивая высокий уровень защиты.  
Аутентификация с использованием пары ключей SSH (Public/Private Key) является надежным стандартом индустрии для контроля доступа.  
Упрощается процесс прохождения проверок безопасности, так как использование бастион-хостов является общепринятым паттерном в корпоративной среде.  
Datastream берет на себя управление жизненным циклом туннеля, снижая нагрузку на инженеров по написанию скриптов мониторинга и перезапуска.  
Метод позволяет использовать публичные IP-адреса для бастиона, если приватная связность через пиринг затруднена или невозможна.  
Легкость смены целевого хоста базы данных без необходимости переконфигурирования самого бастиона делает решение гибким.  
Журналирование подключений на уровне системных логов SSH (/var/log/auth.log) предоставляет подробную информацию об попытках доступа.14  
Бастион-хост может использоваться для подключения к множеству различных баз данных, выступая универсальным шлюзом.  
Отсутствие необходимости в управлении SSL-сертификатами на промежуточном узле упрощает эксплуатацию по сравнению с TLS-прокси.  
Нативная интеграция в UI/API Datastream позволяет настраивать соединение декларативно через Terraform или другие инструменты IaC.15  
Минимизируются риски ошибок конфигурации сети, так как туннель абстрагирует сложность маршрутизации между сервисом и VPC.

### **Недостатки**

Инкапсуляция протокола TCP внутри другого протокола TCP (SSH) может приводить к проблемам производительности, известным как "TCP Meltdown".16  
При потере пакетов во внешнем соединении внутреннее соединение может испытывать экстремальные задержки из-за конфликта механизмов повторной передачи.  
Пропускная способность SSH-туннеля ограничена производительностью процессора бастиона, затрачиваемой на шифрование и дешифрование потока данных.17  
Это может стать критическим узким местом для высоконагруженных потоков CDC с большими объемами изменений данных.  
Бастион-хост представляет собой единую точку отказа, и организация его кластеризации для SSH-туннелей технически сложна.  
Управление SSH-ключами требует внедрения процессов их ротации и безопасного хранения, чтобы предотвратить компрометацию доступа.  
Если используется подключение по публичному IP, это формально нарушает требование задачи о полном исключении выхода в публичный интернет, даже при наличии шифрования.  
Мониторинг качества соединения внутри туннеля затруднен, так как для внешнего наблюдателя это выглядит как единый зашифрованный поток.  
Ограничения конфигурации демона SSHD (например, MaxStartups) могут неожиданно блокировать новые соединения при масштабировании количества задач репликации.  
Некоторые функции драйверов баз данных, чувствительные к задержкам, могут работать нестабильно из-за накладных расходов туннелирования.  
Отладка проблем с подключением может быть сложной из-за неочевидных сообщений об ошибках, скрывающих реальную причину сбоя внутри туннеля.18  
Зависимость от стабильности SSH-сессии означает, что любые разрывы сетевого соединения требуют полного пересоздания контекста подключения к базе данных.  
Использование SSH-туннеля может не поддерживаться некоторыми корпоративными политиками безопасности, требующими инспекции трафика или использования специфических протоколов VPN.  
При высокой нагрузке возможно исчерпание портов на бастионе или достижение лимитов операционной системы по количеству открытых файлов.  
Двойное шифрование (SSH плюс TLS самой базы данных) создает избыточную вычислительную нагрузку, не повышая существенно уровень безопасности данных.

## **Aᚖ₃: Использование Datastream Private Service Connect Interfaces**

### **Суть**

Эта альтернатива опирается на использование нового механизма подключения, предоставляемого Google Cloud специально для управляемых сервисов.  
Вместо традиционного VPC Peering, Datastream настраивается на использование Private Service Connect Interfaces для исходящих соединений.19  
В пользовательской VPC создается ресурс Network Attachment, который служит точкой терминации для интерфейса Datastream.  
При создании конфигурации приватного подключения в Datastream указывается ссылка на этот Network Attachment.  
Google Cloud автоматически создает сетевой интерфейс в подсети пользователя и привязывает его к инстансу Datastream.  
Этот интерфейс получает внутренний IP-адрес из диапазона подсети пользовательской VPC, становясь локальным ресурсом сети.20  
Сетевой трафик от Datastream теперь исходит непосредственно из пользовательской VPC, что технически устраняет проблему транзитивности пиринга.  
Пакеты данных могут маршрутизироваться к другим ресурсам PSC (Endpoints) внутри той же сети, так как они находятся в одном домене маршрутизации.  
Однако, несмотря на решение проблемы связности L3, данный метод не предоставляет встроенных механизмов разрешения DNS.2  
Datastream по-прежнему требует указания IP-адресов целевых серверов, так как не имеет доступа к инфраструктуре Cloud DNS VPC.  
Для подключения к MongoDB Atlas через PSC Interface необходимо использовать IP-адрес PSC Endpoint Atlas в строке подключения.  
Чтобы обеспечить работоспособность соединения с MongoDB, требующей валидации хостнеймов для SSL, необходимо применять параметры драйвера, отключающие проверки, или использовать directConnection=true.  
Этот метод представляет собой современный, "cloud-native" подход к интеграции сервисов, исключающий сложности управления пиринговыми связями.  
Он обеспечивает строгую изоляцию и контроль над точками входа в сеть через механизм Network Attachments.19  
Конфигурация требует тщательной настройки IAM-ролей для сервисного аккаунта Datastream, чтобы он мог создавать интерфейсы в проекте пользователя.

### **Оценка**

60

### **Достоинства**

Данный метод позволяет полностью отказаться от использования VPC Peering, устраняя риски конфликтов адресного пространства IP.  
Отсутствует необходимость в резервировании больших диапазонов адресов через servicenetworking, что экономит адресное пространство VPC.  
Datastream получает прямое присутствие в пользовательской сети, что упрощает понимание топологии и отладку маршрутизации.  
Трафик между Datastream и базой данных никогда не покидает магистральную сеть Google, обеспечивая максимальную безопасность и низкие задержки.  
Исключается необходимость в развертывании и обслуживании промежуточных виртуальных машин, что снижает операционные расходы (OPEX).  
Решение обладает высокой надежностью, опираясь на программно-определяемую сеть Google Andromeda, а не на отдельные инстансы Compute Engine.  
Позволяет реализовать более гранулярные политики безопасности брандмауэра, применяя правила непосредственно к IP-адресам интерфейсов Datastream.  
Соответствует стратегии Google Cloud по переходу на PSC как основной метод интеграции сервисов, что гарантирует долгосрочную поддержку.  
Упрощает аудит сетевого доступа, так как интерфейсы Datastream видны как обычные ресурсы в консоли управления сетью.  
Обеспечивает лучшую изоляцию между различными средами (dev/prod), так как Network Attachments могут быть созданы в разных подсетях.  
Позволяет избежать проблемы "шумных соседей", характерной для общих каналов пиринга, предоставляя выделенную полосу пропускания.  
Поддерживает транзитивный доступ к ресурсам, подключенным через VPN или Interconnect к пользовательской VPC.21  
Конфигурация через Terraform позволяет полностью автоматизировать развертывание сетевой инфраструктуры для Datastream.15  
Снижает сложность сетевой топологии для организаций, использующих архитектуру Shared VPC, упрощая управление правами доступа.  
Является наиболее перспективным методом подключения, функциональность которого активно развивается со стороны Google Cloud.

### **Недостатки**

Критическим недостатком является отсутствие поддержки разрешения имен DNS в текущей реализации Datastream, даже при использовании PSC Interfaces.2  
Это вынуждает использовать IP-адреса в конфигурации подключения, что делает настройку зависимой от статичности инфраструктуры.  
Необходимость использования IP-адресов создает серьезные проблемы при подключении к MongoDB Atlas, использующей TLS-сертификаты, выданные на доменные имена.  
Отсутствие возможности легко игнорировать ошибки SSL в настройках Datastream может сделать прямое подключение к Atlas невозможным без нарушения безопасности.  
Использование directConnection=true лишает драйвер возможности автоматически реагировать на изменения топологии кластера MongoDB, снижая отказоустойчивость.  
Настройка PSC Interfaces требует более глубокого понимания IAM и сетевых абстракций GCP, чем традиционный пиринг.  
Невозможность миграции существующих конфигураций требует пересоздания профилей подключения с потерей истории или необходимостью полной ресинхронизации данных.13  
В некоторых случаях наблюдаются проблемы с задержкой при создании интерфейсов, когда статус "Creating" зависает на длительное время.22  
Ограниченная документация и примеры сообщества для комбинации Datastream PSC Interface и MongoDB Atlas создают риски при внедрении.  
Стоимость использования PSC Interfaces и обработки данных может быть выше, чем у бесплатного трафика внутри пиринга в рамках одной зоны.  
При изменении IP-адресов PSC Endpoint (например, при пересоздании) потребуется ручное обновление конфигурации Datastream, так как нет DNS-автоматизации.  
Отсутствие возможности внедрения заголовков или модификации трафика ограничивает гибкость решения в сложных сценариях безопасности.  
Не все инструменты мониторинга GCP могут корректно отображать метрики для PSC Interfaces на данный момент.  
Существует риск столкнуться с неочевидными ограничениями платформы, характерными для новых функций, которые еще не прошли проверку временем в масштабных инсталляциях.  
Для реализации полноценного решения с поддержкой DNS все равно может потребоваться внедрение прокси, что нивелирует преимущества отказа от VM.

## **Aᚖ₄: Использование публичного IP Allowlisting (Public Connectivity)**

### **Суть**

Данная альтернатива предполагает отказ от попыток организации приватного сетевого канала в пользу использования публичной сети Интернет.  
Сервис Datastream настраивается на использование метода подключения "IP allowlisting", при котором трафик исходит с набора статических публичных IP-адресов Google.  
В консоли управления MongoDB Atlas создаются правила сетевого доступа (Network Access), разрешающие входящие соединения исключительно с этих IP-адресов Datastream.13  
Маршрутизация трафика осуществляется через публичные шлюзы интернета, однако данные защищаются обязательным для Atlas шифрованием TLS.  
В этом сценарии Datastream использует публичные DNS-серверы (например, Google Public DNS 8.8.8.8) для разрешения имен хостов.  
Публичные DNS-серверы корректно разрешают канонические имена узлов MongoDB Atlas (*.mongodb.net) в их публичные IP-адреса.  
Это автоматически устраняет проблему Split-Horizon DNS (P2†), так как используется глобально доступное пространство имен.  
Также устраняется проблема маршрутизации (P3†), так как публичные IP-адреса Atlas доступны из любой точки сети при наличии соответствующих разрешений брандмауэра.  
Драйвер MongoDB в Datastream работает в штатном режиме, используя строку подключения mongodb+srv://, и корректно обрабатывает обнаружение топологии реплика-сета.  
Метод обеспечивает функциональную работоспособность интеграции "из коробки" с минимальными усилиями по настройке.  
Безопасность обеспечивается комбинацией белых списков IP (Network Level) и аутентификации базы данных с шифрованием (Application Level).  
Данный подход часто используется как временное решение или для сред разработки, где требования к изоляции сети менее строгие.  
Реализация не требует создания и управления ресурсами в Google Cloud VPC, такими как пиринг, DNS-зоны или виртуальные машины.  
Однако этот метод прямо противоречит заявленной цели задачи T⁎ — избегать прохождения трафика через публичный интернет.

### **Оценка**

40

### **Достоинства**

Максимальная простота и скорость внедрения позволяют запустить репликацию данных буквально за несколько минут.  
Гарантированная работоспособность всех механизмов драйвера MongoDB, включая валидацию SSL-сертификатов и автоматическое обнаружение узлов.  
Отсутствие необходимости в развертывании, настройке и обслуживании какой-либо дополнительной инфраструктуры (Zero Ops).  
Нулевые дополнительные расходы на облачные ресурсы, так как не используются виртуальные машины, NAT-шлюзы или платные функции VPC.  
Высокая надежность соединения за счет исключения промежуточных точек отказа, которые могли бы возникнуть при использовании прокси или туннелей.  
Легкость диагностики и отладки проблем подключения, так как доступность публичных эндпоинтов можно проверить с любой рабочей станции.  
Независимость от архитектурных ограничений и лимитов Google Cloud VPC, таких как квоты на маршруты или правила транзитивности.  
Автоматическая адаптация к изменениям в инфраструктуре Atlas, так как DNS-записи обновляются на стороне MongoDB и корректно воспринимаются Datastream.  
Отсутствие риска возникновения проблем с производительностью из-за накладных расходов на инкапсуляцию трафика (как в VPN или SSH).  
Прозрачность для инструментов мониторинга Atlas, которые видят реальные IP-адреса источника подключений.  
Возможность использования стандартной документации и примеров конфигурации без необходимости адаптации под специфику приватных сетей.  
Упрощение схемы взаимодействия между командами, так как не требуется согласование выделения приватных диапазонов IP или настройки пиринга.  
Отсутствие проблем с пересечением адресных пространств (IP Overlap), которые часто возникают при объединении корпоративных сетей.  
Минимальный риск человеческой ошибки при настройке, так как процесс сводится к копированию списка IP-адресов.  
Стабильность работы при обновлении версий сервисов, так как используется наиболее базовый и поддерживаемый метод подключения.

### **Недостатки**

Фундаментальное нарушение требования безопасности о предотвращении выхода трафика в публичный интернет ("avoid public internet traversal").  
Повышенный риск кибератак, таких как DDoS или попытки подбора паролей, так как публичные интерфейсы базы данных теоретически доступны всему интернету.  
Несоответствие многим корпоративным стандартам безопасности и нормативным требованиям (PCI DSS, HIPAA, GDPR), требующим сетевой изоляции баз данных.  
Зависимость от актуальности списков публичных IP-адресов Datastream, которые могут изменяться Google, требуя оперативного обновления правил в Atlas.  
Потенциально более высокая и менее предсказуемая задержка передачи данных по сравнению с выделенными приватными каналами внутри сети Google.  
Отсутствие гарантий качества обслуживания (QoS) для трафика, проходящего через публичные сегменты сети.  
Сложности с прохождением аудита безопасности, требующего доказательства того, что данные не подвергались риску перехвата или манипуляции в публичной сети.  
Невозможность использования механизмов VPC Service Controls для ограничения периметра данных, так как трафик покидает защищенный контур.  
Возможные дополнительные расходы на трафик (Data Transfer Out) со стороны MongoDB Atlas, если публичный трафик тарифицируется выше приватного.  
Психологический дискомфорт для заказчика, который уже инвестировал ресурсы в настройку PSC и ожидает решения уровня Enterprise.  
Риск блокировки трафика промежуточными провайдерами или национальными фаерволами в случае трансграничной передачи данных.  
Отсутствие возможности скрыть факт использования облачных сервисов от внешнего наблюдателя, анализирующего трафик.  
Усложнение архитектуры безопасности в целом, так как приходится поддерживать исключения для публичного доступа в политиках "Deny All".  
Невозможность использования приватных имен хостов и внутренних DNS-зон для управления маршрутизацией трафика.  
Восприятие решения как "непрофессионального" или "временного костыля" в контексте современной облачной архитектуры.

## **Итоговый вердикт**

На основании всестороннего анализа технических ограничений Google Cloud Datastream, специфики работы сетевого стека MongoDB Atlas и требований задачи T⁎ по обеспечению приватности соединения, сформулировано следующее заключение.

Прямая реализация схемы Datastream -> VPC Peering -> PSC Endpoint технически невозможна из-за отсутствия транзитивной маршрутизации в пиринге Google Cloud и неспособности Datastream выполнять разрешение DNS-имен в частных зонах.  
Заблуждения клиента ꆜ относительно "сбоя DNS" и "игнорирования маршрутов" опровергнуты фактами архитектурного дизайна платформы.  
Сравнительный анализ альтернатив показывает, что Стратегия Aᚖ₁ (Промежуточный прокси-сервер L4) является наиболее сбалансированным и надежным решением для промышленной эксплуатации.  
Она обеспечивает полный контроль над маршрутизацией и разрешением имен DNS, устраняя оба корневых блокирующих фактора.  
Использование прокси-сервера позволяет сохранить архитектуру Private Service Connect, обеспечивая безопасность трафика и соответствие требованиям комплаенса, при этом гарантируя высокую производительность и стабильность потока данных.  
Рекомендация: Следует отказаться от текущей стратегии T༄ в пользу внедрения архитектуры Aᚖ₁.  
Это потребует развертывания минимальной инфраструктуры (одной или двух VM с Nginx), но взамен предоставит детерминированное и управляемое решение проблемы связности.  
Использование directConnection=true в профиле Datastream является обязательным условием успеха данной интеграции.

#### **Works cited**

1. Mongo DB behind Nginx as reverse proxy, share your Mongo DB with your friends in LAN network - GitHub Gist, accessed December 6, 2025, [https://gist.github.com/bugb/e08f4edd1d7ba11706469ccd6cce1dfd](https://gist.github.com/bugb/e08f4edd1d7ba11706469ccd6cce1dfd)  
2. Create a private connectivity configuration | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration)  
3. Connection String Options - Database Manual - MongoDB Docs, accessed December 6, 2025, [https://www.mongodb.com/docs/manual/reference/connection-string-options/](https://www.mongodb.com/docs/manual/reference/connection-string-options/)  
4. VPC Network Peering | Virtual Private Cloud, accessed December 7, 2025, [https://docs.cloud.google.com/vpc/docs/vpc-peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)  
5. Module ngx_stream_proxy_module - nginx, accessed December 7, 2025, [https://nginx.org/en/docs/stream/ngx_stream_proxy_module.html](https://nginx.org/en/docs/stream/ngx_stream_proxy_module.html)  
6. How to setup MongoDB behind Nginx Reverse Proxy [closed] - Stack Overflow, accessed December 7, 2025, [https://stackoverflow.com/questions/31853755/how-to-setup-mongodb-behind-nginx-reverse-proxy](https://stackoverflow.com/questions/31853755/how-to-setup-mongodb-behind-nginx-reverse-proxy)  
7. How To Setup Network Connectivity Between VPCs In Google Cloud - Xebia, accessed December 6, 2025, [https://xebia.com/blog/how-to-setup-network-connectivity-between-vpcs-in-google-cloud/](https://xebia.com/blog/how-to-setup-network-connectivity-between-vpcs-in-google-cloud/)  
8. Connect to a Deployment - mongosh - MongoDB Docs, accessed December 6, 2025, [https://www.mongodb.com/docs/mongodb-shell/connect/](https://www.mongodb.com/docs/mongodb-shell/connect/)  
9. MongoDB behind Nginx Reverse Proxy Manager : r/selfhosted - Reddit, accessed December 7, 2025, [https://www.reddit.com/r/selfhosted/comments/1ctr6zx/mongodb_behind_nginx_reverse_proxy_manager/](https://www.reddit.com/r/selfhosted/comments/1ctr6zx/mongodb_behind_nginx_reverse_proxy_manager/)  
10. Create connection profiles | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/create-connection-profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles)  
11. When using an SSH tunnel does the server resolve domain names or is it still done via the ISP/DNS server on the router? - Information Security Stack Exchange, accessed December 7, 2025, [https://security.stackexchange.com/questions/144297/when-using-an-ssh-tunnel-does-the-server-resolve-domain-names-or-is-it-still-don](https://security.stackexchange.com/questions/144297/when-using-an-ssh-tunnel-does-the-server-resolve-domain-names-or-is-it-still-don)  
12. How to SSH tunnel to a destination host resolved via internal DNS on the bastion host, accessed December 7, 2025, [https://unix.stackexchange.com/questions/598819/how-to-ssh-tunnel-to-a-destination-host-resolved-via-internal-dns-on-the-bastion](https://unix.stackexchange.com/questions/598819/how-to-ssh-tunnel-to-a-destination-host-resolved-via-internal-dns-on-the-bastion)  
13. Network connectivity methods | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/network-connectivity-options](https://docs.cloud.google.com/datastream/docs/network-connectivity-options)  
14. how to connect to mongodb server via ssh tunnel, accessed December 7, 2025, [https://serverfault.com/questions/597765/how-to-connect-to-mongodb-server-via-ssh-tunnel](https://serverfault.com/questions/597765/how-to-connect-to-mongodb-server-via-ssh-tunnel)  
15. google_datastream_private_con, accessed December 7, 2025, [https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/datastream_private_connection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/datastream_private_connection)  
16. Are there disadvantages in SSH tunneling? - Unix & Linux Stack Exchange, accessed December 6, 2025, [https://unix.stackexchange.com/questions/34499/are-there-disadvantages-in-ssh-tunneling](https://unix.stackexchange.com/questions/34499/are-there-disadvantages-in-ssh-tunneling)  
17. What limits are there on the number of reverse ssh tunnels? - Server Fault, accessed December 6, 2025, [https://serverfault.com/questions/358088/what-limits-are-there-on-the-number-of-reverse-ssh-tunnels](https://serverfault.com/questions/358088/what-limits-are-there-on-the-number-of-reverse-ssh-tunnels)  
18. Forward-SSH Tunnel Datastream Option Trouble - Google Developer forums, accessed December 7, 2025, [https://discuss.google.dev/t/forward-ssh-tunnel-datastream-option-trouble/143918](https://discuss.google.dev/t/forward-ssh-tunnel-datastream-option-trouble/143918)  
19. Configure Private Service Connect interfaces | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/psc-interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces)  
20. Using PSC interfaces for managed service egress | Google Cloud Blog, accessed December 7, 2025, [https://cloud.google.com/blog/products/networking/using-psc-interfaces-for-managed-service-egress/](https://cloud.google.com/blog/products/networking/using-psc-interfaces-for-managed-service-egress/)  
21. Private Service Connect Interface | Google Codelabs, accessed December 7, 2025, [https://codelabs.developers.google.com/codelabs/psc-interface](https://codelabs.developers.google.com/codelabs/psc-interface)  
22. Unable to connect Datastream via PSC - Data Analytics - Google Developer forums, accessed December 7, 2025, [https://discuss.google.dev/t/unable-to-connect-datastream-via-psc/253612](https://discuss.google.dev/t/unable-to-connect-datastream-via-psc/253612)

# 20.
## 20.1.
`R⬆⠿` ≔ ⠿~ (Рекомендации для моего ответа `ꆜ` на `P⁎`)

## 20.2.
`R⬆ᵢ` : `R⬆⠿`

# 21. Анализ `R⬆⠿` (выполнен Gemini Deep Think)
https://gemini.google.com/share/90e75ec582ea

## R⬆₁: Использование SSH-туннелирования (Bastion Host)

### Суть
Данная рекомендация предполагает изменение метода подключения на «Forward SSH tunnel», который нативно поддерживается сервисом Datastream.
Вам необходимо развернуть одну небольшую виртуальную машину (Bastion Host) внутри вашей сети `datastream-net`.
Сервис Datastream будет устанавливать зашифрованное SSH-соединение с этим бастионом, используя его как шлюз в вашу инфраструктуру.
Ключевым моментом является то, что разрешение DNS-имен MongoDB Atlas будет выполняться процессом SSH на самом бастионе.
Поскольку бастион находится внутри VPC, он имеет доступ к Private DNS Zone и корректно преобразует адреса `*.mongodb.net` в приватные IP-адреса PSC Endpoint.
После разрешения имени трафик будет перенаправлен бастионом на целевой PSC Endpoint, оставаясь внутри приватного контура.
Это архитектурное решение автоматически обходит оба главных препятствия: отсутствие DNS в Datastream и нетранзитивность пиринга.

### Оценка
95

### Достоинства
Метод официально рекомендовав Google Cloud для сценариев со сложной сетевой топологией и приватными источниками данных.
Использование удаленного разрешения DNS (Remote DNS Resolution) через бастион полностью устраняет проблему Split-Horizon DNS.
Соединение инициируется локальным ресурсом (бастионом) внутри VPC, что решает проблему нетранзитивности пиринга для PSC.
Подход гарантирует успешную валидацию TLS-сертификатов, так как позволяет использовать доменные имена в строке подключения.
Конфигурация требует минимальных усилий по настройке инфраструктуры и сводится к управлению одной виртуальной машиной.
Обеспечивается высокий уровень безопасности за счет шифрования трафика внутри SSH-туннеля.

### Недостатки
Инкапсуляция трафика базы данных внутрь протокола SSH создает дополнительные накладные расходы на процессор (проблема TCP-over-TCP).
В сценариях с экстремально высокой пропускной способностью (High Throughput CDC) производительность одного туннеля может стать узким местом.
Бастион-хост становится единой точкой отказа (SPOF), что требует настройки группы инстансов (MIG) для автовосстановления.
Необходимо управлять SSH-ключами доступа и обеспечивать безопасность самой промежуточной виртуальной машины.

## R⬆₂: Внедрение промежуточного L4 TCP-прокси

### Суть
Эта рекомендация заключается в установке выделенного прокси-сервера (например, Nginx или HAProxy) внутри сети `datastream-net`.
Datastream настраивается на подключение к приватному IP-адресу этого прокси-сервера через существующий VPC Peering.
В профиле подключения Datastream необходимо обязательно добавить параметр `directConnection=true` для отключения автообнаружения топологии.
Прокси-сервер принимает входящие пакеты, разрешает имя назначения через системный резолвер VPC и пересылает трафик на PSC Endpoint.
Прокси настраивается в режиме «stream» (Layer 4) для прозрачной передачи зашифрованного трафика без терминации SSL.
Таким образом создается транзитный узел, который соединяет сеть Datastream и PSC Endpoint, преодолевая сетевые ограничения.

### Оценка
85

### Достоинства
Проксирование на транспортном уровне обеспечивает более высокую производительность и меньшие задержки по сравнению с SSH-туннелированием.
Отсутствует двойное шифрование трафика, что снижает нагрузку на вычислительные ресурсы промежуточного узла.
Решение предоставляет администраторам полный контроль над параметрами TCP-стека, таймаутами и буферизацией соединений.
Архитектура позволяет легко масштабироваться горизонтально путем добавления прокси-серверов за внутренним балансировщиком нагрузки.

### Недостатки
Существует высокий риск ошибок валидации TLS-сертификатов, так как Datastream подключается к IP-адресу прокси, а сертификат выдан на доменное имя.
Использование параметра `directConnection` отключает встроенные в драйвер механизмы автоматического переключения при сбоях (Failover).
Решение требует глубокой технической экспертизы для корректной настройки Nginx и отладки возможных проблем с SSL.
Эксплуатационная сложность выше, чем у SSH-туннеля, из-за необходимости администрирования программного обеспечения прокси.

## R⬆₃: Использование Datastream PSC Interfaces

### Суть
Данный подход предполагает отказ от VPC Peering в пользу создания интерфейса Datastream непосредственно в вашей VPC через механизм Network Attachments.
Datastream получает сетевой интерфейс в подсети пользователя, что технически помещает его в одну сеть с PSC Endpoint.
Однако, согласно документации, сервис Datastream даже в этом режиме не поддерживает разрешение DNS-имен в приватных соединениях.
Вам придется указывать IP-адреса узлов MongoDB Atlas в конфигурации подключения вместо их доменных имен.

### Оценка
60

### Достоинства
Метод исключает использование промежуточных виртуальных машин, снижая эксплуатационные расходы и сложность обслуживания.
Трафик остается строго внутри магистральной сети Google и изолирован от других потребителей пиринга.
Решение соответствует современной стратегии Google Cloud по переходу на интеграции через Private Service Connect.

### Недостатки
Критическим недостатком является невозможность разрешения доменных имен, что ломает цепочку доверия TLS в MongoDB Atlas.
Необходимость использования IP-адресов делает конфигурацию хрупкой и зависимой от изменений в инфраструктуре базы данных.
Решение требует отключения проверки SSL или сложной подмены сертификатов, что снижает уровень безопасности.
На текущий момент этот метод создает больше технических проблем для сценария с MongoDB, чем решает.

## Вердикт

Текущая конфигурация с прямым пирингом технически неработоспособна из-за отсутствия DNS-резолвинга в Datastream и нетранзитивности пиринга к PSC.
Диагностированные вами проблемы являются следствием этих архитектурных ограничений платформы, а не ошибками настройки.
Я настоятельно рекомендую выбрать **R⬆₁ (SSH-туннелирование)** в качестве основного решения задачи `T⁎`.
Это единственное решение, которое «из коробки» устраняет проблемы с DNS и маршрутизацией, сохраняя при этом корректную работу TLS и безопасность.
Переход на SSH-туннель через Bastion Host позволит вам немедленно восстановить связность и запустить репликацию данных.

# 22. Анализ `R⬆⠿` (выполнен Gemini Deep Research)
https://gemini.google.com/share/48f5a4673334


## **1. Введение и контекст взаимодействия**

Настоящий отчет представляет собой исчерпывающий технический ответ на запрос клиента (Upwork ID: ꆜ), касающийся интеграции сервиса Google Cloud Datastream с кластером MongoDB Atlas с использованием механизма Private Service Connect (PSC). Целью данного документа является детальный анализ проблемы, оценка предложенных технических решений и формулирование обоснованного вердикта по выбору архитектуры подключения.

В современной облачной экосистеме задачи репликации данных в реальном времени (CDC — Change Data Capture) становятся критически важными для аналитических платформ. Однако интеграция управляемых сервисов (Managed Services) от разных провайдеров — в данном случае Google Cloud Platform (GCP) и MongoDB Atlas — часто сопряжена с нетривиальными сетевыми вызовами. Основной конфликт возникает на стыке политик безопасности, механизмов маршрутизации и протоколов прикладного уровня. В ходе предварительного исследования (файлы B.md, L.md, O.md) была выявлена фундаментальная несовместимость между механизмом разрешения имен (DNS) в приватных контурах Datastream и требованиями протокола TLS/SSL, предъявляемыми MongoDB Atlas.

Данный отчет структурирован таким образом, чтобы последовательно разобрать каждый слой проблемы: от сетевого уровня (L3/L4) до уровня приложений (L7). Мы рассмотрим ограничения, накладываемые квотами Google Cloud 1, специфику работы VPC-пиринга и Private Service Connect 2, а также особенности работы драйверов MongoDB в условиях репликационных наборов (Replica Sets).4 Итогом анализа станет детализированная архитектура решения, обеспечивающая надежность, безопасность и соответствие лучшим практикам эксплуатации облачных систем.

### **1.1 Цели и задачи анализа**

В рамках формализованной задачи перед нами стоят следующие цели:

1. **Декомпозиция проблемы подключения:** Выявить корневые причины сбоев соединения, зафиксированных в логах (L.md), связанных с ошибками SSL Handshake и невозможностью разрешения DNS-имен.  
2. **Анализ ограничений платформы:** Оценить влияние квот и лимитов Google Cloud Datastream и Cloud DNS на выбор архитектурного решения.1  
3. **Оценка стратегических опций:** Провести сравнительный анализ трех основных подходов (прямое подключение, SSH-туннелирование, проксирование) с точки зрения производительности, безопасности и эксплуатационной сложности.  
4. **Разработка целевой архитектуры:** Сформировать детальное техническое задание на реализацию рекомендованного решения, включая конфигурационные параметры и схемы потоков данных.

## **2. Технический бэкграунд и формализация проблемы (Анализ B.md)**

Для понимания сути проблемы необходимо глубоко погрузиться в архитектуру сетевого взаимодействия между Google Cloud и MongoDB Atlas. Ситуация осложняется тем, что мы имеем дело с двумя независимыми облачными средами, соединенными через приватные каналы связи, которые имеют свои строгие правила транзитивности и видимости.

### **2.1 Ландшафт подключения: Datastream и Private Service Connect**

Google Cloud Datastream — это бессерверный сервис, предназначенный для асинхронной репликации данных. Архитектурно он реализован как управляемый сервис, ресурсы которого (воркеры, осуществляющие чтение и передачу данных) разворачиваются в специальном служебном проекте Google (Service Producer Project), скрытом от пользователя. Для того чтобы эти воркеры могли получить доступ к ресурсам в пользовательской сети VPC (Consumer VPC), используется механизм "Private Connectivity".7

Этот механизм базируется на технологии VPC Network Peering. При создании конфигурации частного подключения устанавливается пиринговое соединение между сетью Service Producer и сетью пользователя. Это дает воркерам Datastream возможность отправлять IP-пакеты на внутренние адреса в сети пользователя.2

С другой стороны, MongoDB Atlas предоставляет доступ к своим кластерам через Private Service Connect (PSC). PSC позволяет представить удаленный сервис (в данном случае базу данных Atlas, работающую в собственном VPC MongoDB) как локальный IP-адрес (Endpoint) внутри пользовательской сети Google Cloud VPC.3 Это обеспечивает однонаправленный доступ к базе данных без выхода в публичный интернет, что является стандартом безопасности для корпоративных систем.4

### **2.2 Фундаментальная несовместимость: Проблема "Double Peering" и DNS**

Анализ материалов исследования (B.md) и документации выявляет критический архитектурный конфликт, который делает "наивную" реализацию подключения невозможной.

#### **2.2.1 Нарушение транзитивности маршрутизации**

В Google Cloud пиринг сетей VPC не является транзитивным.9 Это означает, что если сеть A (Datastream Producer) соединена пирингом с сетью B (User Consumer VPC), а сеть B соединена с сетью C (или сервисом через PSC), то сеть A не может автоматически отправлять трафик в сеть C через сеть B.  
Хотя Private Service Connect технически отличается от классического пиринга, маршруты к PSC Endpoints не всегда автоматически экспортируются в пиринговые соединения с сервис-провайдерами, если не используются специальные механизмы, такие как PSC Interfaces.10 В стандартной конфигурации Datastream "видит" только те диапазоны IP-адресов, которые явно анонсируются из пользовательской VPC. Если PSC Endpoint находится в подсети пользовательской VPC, Datastream может иметь техническую возможность отправить пакет на этот IP, но здесь вступает в силу следующая, более серьезная проблема.

#### **2.2.2 "Черная дыра" DNS в приватных подключениях**

Документация Datastream содержит критическое ограничение: "Datastream не поддерживает разрешение доменных имен (DNS) в частных подключениях".7 Это ограничение продиктовано архитектурой изоляции. Воркеры Datastream работают в полностью управляемой среде и используют собственные DNS-резолверы Google. Они не имеют доступа к зонам Cloud DNS, настроенным в пользовательской VPC (Private Zones), так как механизмы DNS Peering между Managed Services и User VPC в данном контексте не реализованы.11

Это означает, что даже если пользователь настроит в своей сети Cloud DNS Private Zone, которая разрешает имя cluster0-shard-00.mongodb.net в IP-адрес PSC Endpoint (например, 10.128.0.5), Datastream не сможет воспользоваться этим разрешением. Сервис требует ввода IP-адреса, а не хостнейма, для установления соединения.

#### **2.2.3 Зависимость MongoDB от хостнеймов**

Протокол MongoDB и архитектура Replica Set жестко завязаны на использование доменных имен.

1. **SSL/TLS Verification:** Кластеры MongoDB Atlas защищены TLS-сертификатами, выписанными на их публичные доменные имена (например, *.mongodb.net). Если клиент (Datastream) подключается к серверу по IP-адресу (10.128.0.5), сервер все равно предъявляет сертификат для *.mongodb.net. Клиент, ожидающий соединения с IP-адресом, обнаруживает несоответствие имени в сертификате (Subject Alternative Name mismatch) и разрывает соединение, если не отключена проверка хостнейма.12  
2. **Topology Discovery:** Даже если удастся установить первичное соединение с одной нодой, драйвер MongoDB запрашивает конфигурацию реплика-сета (команда isMaster или hello). Сервер возвращает список участников кластера. В MongoDB Atlas этот список всегда содержит FQDN-имена нод, а не их IP-адреса.4 Получив этот список, Datastream пытается установить новые соединения с полученными хостнеймами. Поскольку DNS-разрешение отсутствует 7, эти попытки обречены на провал, что приводит к невозможности работы CDC.

Таким образом, мы имеем замкнутый круг: Datastream требует IP-адреса из-за отсутствия DNS, а MongoDB Atlas требует использования хостнеймов для корректной работы SSL и топологии кластера.

## **3. Глубокий анализ ограничений и данных логов (Анализ L.md)**

В данном разделе мы детально разберем конкретные технические ограничения и ошибки, подтверждающие выводы, сделанные на этапе формализации проблемы. Анализ логов (L.md) и сниппетов документации позволяет точно диагностировать причины сбоев.

### **3.1 Ошибка SSL Handshake: Hostname Mismatch**

В предоставленных материалах 13 описывается типичная ошибка: SSLHandshakeFailed: The server certificate does not match the host name.  
Когда Datastream инициирует TLS-соединение, он отправляет пакет ClientHello. Если в конфигурации профиля указан IP-адрес (что неизбежно из-за ограничений DNS), поле SNI (Server Name Indication) в ClientHello либо отсутствует, либо содержит IP-адрес.  
Сервер MongoDB Atlas, получая такой запрос, возвращает свой стандартный сертификат, выданный на доменное имя. Библиотека OpenSSL на стороне Datastream сверяет запрошенный адрес (IP) с именем в сертификате (DNS) и фиксирует ошибку валидации.  
Некоторые пользователи пытаются обойти это, загружая корневые сертификаты (CA) или используя самоподписанные сертификаты. Однако Datastream, как управляемый сервис, имеет ограниченные возможности по настройке параметров верификации. В частности, в API Datastream (v1) параметры ssl_config позволяют загрузить клиентский сертификат и CA, но не предоставляют явного флага tlsAllowInvalidHostnames, который доступен в стандартных драйверах MongoDB.14 Хотя некоторые источники упоминают возможность отключения валидации (verify_server_certificate=false или аналоги), для управляемых сервисов Google эта функциональность часто ограничена политиками безопасности, запрещающими MITM-уязвимые конфигурации.

### **3.2 Ограничения квот и масштабируемость**

При проектировании решения необходимо учитывать жесткие квоты Google Cloud, приведенные в 1 и.6

* **Лимит конфигураций частного подключения:** "Each Google Cloud project can have a maximum of 5 private connectivity configurations".1 Это критически важное ограничение. Оно означает, что мы не можем создавать отдельную сетевую конфигурацию для каждого потока данных, если их планируется много. Архитектура должна быть централизованной: одна конфигурация подключения должна обслуживать множество источников и приемников.  
* **Пропускная способность DNS:** Хотя лимиты на DNS-запросы высоки (100,000 запросов за 10 секунд на зону 6), они касаются Cloud DNS внутри пользовательской VPC. Поскольку Datastream не использует этот DNS, эти лимиты косвенно влияют только на проксирующие решения, которые мы будем рассматривать далее.  
* **Транзитивность пиринга:** Ограничения VPC Peering 2 подтверждают, что прямая маршрутизация трафика "Datastream -> Consumer VPC -> Peered Network" невозможна без промежуточного звена (NAT-шлюза или Прокси).

### **3.3 Специфика MongoDB Atlas Private Endpoint**

Согласно 16 и 4, соединения через Private Endpoint являются однонаправленными: Atlas не может инициировать соединения обратно в VPC клиента. Это упрощает модель угроз (нам не нужно беспокоиться о защите VPC от вредоносного трафика из базы данных), но накладывает ограничения на использование некоторых схем репликации, где инициатором выступает база данных. В случае Datastream инициатором всегда выступает стриминговый сервис (Datastream), поэтому данное ограничение не блокирует работу, но подтверждает необходимость корректной настройки Firewall Rules на входящий трафик в Atlas (через Security Groups в консоли Atlas).

## **4. Оценка стратегических опций (Анализ O.md)**

На основе проведенного анализа и материалов (O.md), мы рассматриваем три основных архитектурных подхода к решению проблемы. Каждый подход оценивается по критериям функциональности, безопасности, производительности и сложности поддержки.

### **4.1 Опция A: Прямое подключение к PSC Endpoint (Direct Connection)**

* **Концепция:** Настроить профиль подключения Datastream, указав IP-адрес PSC Endpoint в качестве хоста.  
* **Анализ:**  
  * *DNS:* Не работает. Datastream не может разрешить имена нод, возвращаемые командой hello.  
  * *SSL:* Не работает. Ошибка Hostname mismatch.  
  * *Workaround:* Теоретически можно попытаться использовать режим "Direct Connection" (подключение к одной ноде, минуя discovery) и отключить SSL-валидацию. Однако, как отмечалось выше, Datastream не позволяет гибко управлять флагами SSL-валидации (в частности, игнорировать hostname mismatch) через стандартный UI/API безопасным образом для управляемых источников.17 Более того, прямое подключение к одной ноде лишает систему отказоустойчивости (High Availability): если Primary-нода сменится, поток данных остановится.  
* **Вердикт:** **Непригодно для промышленной эксплуатации.** Решение слишком хрупкое и нарушает принципы безопасности.

### **4.2 Опция B: SSH-туннелирование через Bastion (Forward SSH Tunnel)**

* **Концепция:** Использовать встроенную функцию Datastream "Forward SSH tunnel".18 Разворачивается промежуточная виртуальная машина (Bastion Host) в Consumer VPC. Datastream устанавливает SSH-соединение с бастионом и пробрасывает через него трафик к MongoDB.  
* **Анализ:**  
  * *DNS:* SSH-туннель (port forwarding) работает на уровне TCP. Обычно клиент (Datastream) сам разрешает DNS-имя перед открытием туннеля. Однако в конфигурации Datastream мы указываем *локальный* порт и хост туннеля. Если Datastream подключается к туннелю, он "думает", что работает с локальным ресурсом. Проблема возникает, когда драйвер MongoDB внутри Datastream получает список хостов реплика-сета. Он попытается открыть *новые* соединения к этим хостам. SSH-туннель в режиме local forwarding (-L) пробрасывает только один конкретный порт на один конкретный хост. Он не обеспечивает прозрачного доступа ко всему кластеру динамически.  
  * *SOCKS Proxy:* Для работы с динамическим набором хостов (реплика-сетом) требуется динамический туннель (SOCKS). Документация Datastream не указывает явной поддержки SOCKS-проксирования для всего трафика драйвера MongoDB, а описывает лишь "Forward SSH tunnel" к конкретному хосту.18  
  * *Производительность:* Инкапсуляция TCP в TCP (туннелирование базы данных через SSH) известна проблемой "TCP Meltdown" при высоких нагрузках и потерях пакетов. Это создает значительные риски для стабильности CDC-потока.  
  * *Безопасность:* Требует управления SSH-ключами и администрирования ОС бастиона.  
* **Вердикт:** **Условно пригодно для простых сценариев (Single Node), но рискованно для Replica Set.** Высокая сложность настройки маршрутизации для всех членов кластера и проблемы с производительностью делают этот вариант нежелательным для высоконагруженных систем.

### **4.3 Опция C: Промежуточный TCP-прокси (Рекомендованное решение)**

* **Концепция:** Развернуть в Consumer VPC группу виртуальных машин с ПО для проксирования TCP-трафика (например, Nginx или HAProxy) за внутренним балансировщиком нагрузки (Internal Load Balancer - ILB).  
* **Механизм работы:**  
  1. Datastream подключается к IP-адресу Прокси (через Private Connectivity).  
  2. Прокси терминирует TCP-соединение.  
  3. Прокси открывает новое соединение к PSC Endpoint (или напрямую к хостнеймам Atlas, используя Cloud DNS пользовательской VPC).  
  4. Прокси передает данные между Datastream и Atlas.  
* **Решение проблемы DNS:** Прокси находится в Consumer VPC и имеет полный доступ к Cloud DNS. Он может разрешать имена *.mongodb.net в IP-адреса PSC.  
* **Решение проблемы SSL:** Nginx поддерживает директиву proxy_ssl_server_name on;.19 Это заставляет Nginx использовать SNI при подключении к Atlas, передавая правильное доменное имя. Таким образом, Atlas видит корректный запрос и возвращает валидный сертификат, который Nginx успешно проверяет.  
  * Со стороны Datastream прокси может выглядеть как конечная точка. Мы можем настроить Nginx на использование собственного сертификата (Self-Signed или от корпоративного CA) для шифрования канала "Datastream -> Proxy". Datastream будет доверять этому CA (загруженному в профиль подключения) и подключаться по IP-адресу прокси без ошибок SNI (так как сертификат прокси можно выписать на IP-адрес или Datastream будет просто доверять CA).  
* **Вердикт:** **Оптимальное архитектурное решение.** Оно полностью устраняет проблемы DNS и SSL, обеспечивает высокую производительность и масштабируемость.

## **5. Детальный анализ рекомендаций (R⬆⠿)**

В данном разделе мы формализуем выбранную стратегию (Опция C) и отбрасываем альтернативы с обоснованием, формируя итоговые рекомендации для клиента.

### **5.1 Отклоненная рекомендация: NAT/Masquerading на шлюзе**

* **Суть:** Настройка iptables NAT на промежуточной VM для перенаправления пакетов.  
* **Причина отказа:** NAT работает на уровне L3/L4 (сетевой/транспортный). Он может решить проблему маршрутизации пакетов, но он абсолютно прозрачен для протоколов SSL и MongoDB. При NAT-инге ClientHello от Datastream останется неизменным (без SNI или с неверным SNI), и SSL-хендшейк с Atlas все равно упадет. NAT не решает проблему прикладного уровня.

### **5.2 Отклоненная рекомендация: DNS Peering с Service Producer**

* **Суть:** Попытка настроить пиринг DNS между проектом Datastream и проектом клиента.  
* **Причина отказа:** Согласно документации Cloud DNS 11, функционал DNS Peering предназначен для пользовательских VPC. Google не предоставляет интерфейса для настройки DNS-пиринга "внутрь" управляемых сервисов типа Datastream (Black Box). Мы не можем повлиять на настройки резолверов внутри воркеров Datastream.

### **5.3 Принятая рекомендация: "Proxy Bridge" с перешифрованием (Re-encryption)**

Это единственное решение, которое покрывает все технические разрывы.

#### **5.3.1 Архитектурная топология**

* **Зона A (Datastream Producer Project):** Воркеры Datastream.  
* **Связь:** VPC Network Peering.  
* **Зона B (Customer Consumer VPC):**  
  * **Компонент:** Internal TCP Proxy (Nginx).  
  * **Роль:** Посредник, "переводчик" протоколов.  
  * **Сетевой доступ:** Имеет доступ к Cloud DNS Private Zone для mongodb.net.  
* **Зона C (MongoDB Atlas VPC):**  
  * **Компонент:** MongoDB Cluster.  
  * **Связь:** Private Service Connect (PSC Endpoint в Зоне B).

#### **5.3.2 Механизм решения проблем**

1. **DNS:** Datastream обращается к Прокси по статическому внутреннему IP (например, 10.128.0.50). DNS-разрешение на стороне Datastream не требуется.  
2. **SSL Identity (Datastream -> Proxy):** Прокси использует самоподписанный сертификат, созданный для IP-адреса 10.128.0.50 (или просто валидный сертификат, которому доверяет Datastream через загруженный Root CA). Это обеспечивает шифрование первого плеча и успешный хендшейк.  
3. **SSL Identity (Proxy -> Atlas):** Прокси инициирует новое TLS-соединение к Atlas. Nginx конфигурируется с proxy_ssl_server_name on, что подставляет правильное имя хоста (например, cluster0-shard-00.mongodb.net) в SNI. Хендшейк с Atlas проходит успешно, так как имя совпадает с сертификатом Atlas.  
4. **Топология кластера:** В конфигурации Nginx upstream мы можем прописать адрес PSC Endpoint. Для обеспечения работы со всеми шардами/репликами может потребоваться несколько блоков server в Nginx, слушающих на разных портах, каждый из которых мапится на соответствующую ноду Atlas (если требуется прямой доступ к конкретным нодам), либо (что предпочтительнее для CDC) использование Connection String, указывающего на прокси как на единую точку входа, при условии, что драйвер Datastream сможет корректно интерпретировать это в контексте CDC.  
   * *Важное уточнение по CDC:* Datastream часто использует протокол репликации MongoDB, читая Oplog. Ему нужен доступ к Primary или Secondary нодам. Если драйвер Datastream получит от Прокси (который перенаправляет трафик от Atlas) список реальных хостнеймов реплик (shard-00.mongodb.net), он снова попытается к ним подключиться и упадет.  
   * *Решение для Discovery:* Самый надежный способ — использовать **Direct Connection** (Single Node) в настройках Datastream, указав IP прокси. Прокси же настраивается на пересылку трафика на *текущий Primary* (через использование SRV-записи в конфигурации Nginx или через механизм Health Checks, который будет определять Primary ноду). Однако Nginx (версия Open Source) имеет ограниченные возможности по активному мониторингу протокола MongoDB.  
   * *Альтернатива:* Использовать stream модуль Nginx для проксирования всего трафика на адрес PSC Endpoint (который обычно является Load Balancer-ом на стороне Atlas или адресом одной из нод). Но наиболее стабильным вариантом является использование режима **"Direct Connection"** в Datastream и указание IP-адреса прокси. Это заставляет Datastream игнорировать топологию кластера и просто читать поток с того хоста, который мы ему подсовываем.

## **6. Безопасность и соответствие стандартам (Security & Compliance)**

Реализация схемы с проксированием вводит дополнительный элемент в цепочку доверия. Критически важно обеспечить, чтобы этот элемент не стал "слабым звеном".

### **6.1 Цепочка доверия SSL (Chain of Trust)**

Схема реализует классическую атаку Man-in-the-Middle (MITM), но в конструктивном, управляемом русле (TLS Termination Proxy).

* **Сегмент 1 (Datastream -> Proxy):** Защищен TLS. Мы генерируем свой CA и сертификат сервера для Прокси. Публичная часть CA загружается в профиль подключения Datastream в поле ca_certificate.17 Это гарантирует, что Datastream "доверяет" Прокси.  
* **Сегмент 2 (Proxy -> Atlas):** Защищен TLS. Прокси использует системное хранилище корневых сертификатов (Root CA store) ОС (Debian/RHEL) для валидации сертификатов Atlas (которые подписаны публичными CA, например Let's Encrypt или DigiCert). Директива proxy_ssl_verify on; в Nginx обязательна для предотвращения реальных MITM-атак на этом участке.

### **6.2 Аутентификация и контроль доступа**

* **Аутентификация в БД:** Прокси работает на уровне TCP (L4) и прозрачно передает пакеты аутентификации MongoDB (SCRAM-SHA-1/256). Учетные данные хранятся только в Datastream и Atlas; на Прокси они не оседают в открытом виде (трафик внутри прокси расшифровывается в памяти, но не логируется).  
* **Сетевой экран (Firewall):**  
  * *Ingress (Proxy):* Разрешить входящий трафик на порт 27017 только из диапазона IP-адресов Datastream Private Connection (отображается в консоли GCP после создания конфигурации).  
  * *Egress (Proxy):* Разрешить исходящий трафик на порт 27017 только в подсеть PSC Endpoint.

## **7. Операционный вердикт и дорожная карта внедрения (Implementation Roadmap)**

### **7.1 Итоговый Вердикт**

На основании всестороннего анализа, мы приходим к заключению, что прямое подключение Google Cloud Datastream к MongoDB Atlas через Private Service Connect технически невозможно без использования промежуточного слоя адаптации.  
Причиной является отсутствие поддержки DNS и механизмов подмены SNI в сервисе Datastream.  
**Рекомендованное решение:** Внедрение архитектуры **"Transparent TCP Proxy Bridge"** на базе Nginx в Consumer VPC. Это решение обеспечивает необходимую гибкость для преодоления ограничений протоколов, сохраняя высокий уровень безопасности и производительности.

### **7.2 План реализации (Technical Specification)**

Ниже представлен пошаговый план настройки, который должен быть выполнен инженерами клиента.

#### **Фаза 1: Подготовка инфраструктуры (Infrastructure Preparation)**

1. **Настройка PSC:** Убедиться, что в проекте GCP (Consumer VPC) создан Private Service Connect Endpoint для сервиса MongoDB Atlas.8 Зафиксировать его IP-адрес (например, 10.0.0.100).  
2. **Настройка DNS:** В Cloud DNS создать Private Zone mongodb.net (или соответствующую зону вашего кластера), настроить A-записи для перенаправления имен нод Atlas на IP-адрес PSC Endpoint. Это необходимо для того, чтобы Прокси мог разрешать имена. Проверить работу DNS с тестовой VM: dig +short cluster0-shard-00.mongodb.net должно возвращать IP PSC.

#### **Фаза 2: Развертывание Прокси (Proxy Deployment)**

1. **Provisioning:** Развернуть VM (e2-medium или выше, в зависимости от нагрузки) в той же VPC и регионе, что и Datastream Connectivity.  
2. **Генерация сертификатов:**  
   Bash  
   # Создать CA  
   openssl req -x509 -sha256 -newkey rsa:2048 -keyout ca.key -out ca.crt -days 3650 -nodes -subj '/CN=MyProxyCA'  
   # Создать сертификат сервера (для IP прокси)  
   openssl req -new -newkey rsa:2048 -keyout proxy.key -out proxy.csr -nodes -subj '/CN=10.128.0.50'  
   openssl x509 -req -CA ca.crt -CAkey ca.key -in proxy.csr -out proxy.crt -days 365 -CAcreateserial

3. Конфигурация Nginx (/etc/nginx/nginx.conf):  
   Использовать модуль stream для TCP-проксирования.  
   Nginx  
   stream {  
       server {  
           listen 27017 ssl; # Слушаем SSL от Datastream  
           proxy_pass atlas_backend;

           # Сертификаты для Datastream  
           ssl_certificate /etc/nginx/certs/proxy.crt;  
           ssl_certificate_key /etc/nginx/certs/proxy.key;

           # Настройки подключения к Atlas (SSL Re-encryption)  
           proxy_ssl on;  
           proxy_ssl_server_name on; # Включает SNI!   
           proxy_ssl_verify on;  
           proxy_ssl_trusted_certificate /etc/ssl/certs/ca-certificates.crt; # Системные руты

           # Опционально: принудительно задать имя для верификации  
           # proxy_ssl_name cluster0-shard-00.mongodb.net;   
       }

       upstream atlas_backend {  
           # Здесь используем DNS-имя Atlas. Nginx разрешит его в IP PSC через системный резолвер.  
           server cluster0-shard-00.mongodb.net:27017;  
       }  
   }

#### **Фаза 3: Настройка Datastream (Configuration)**

1. **Connection Profile:** Создать новый профиль MongoDB.  
   * **Hostname:** Внутренний IP-адрес Прокси VM (например, 10.128.0.50).  
   * **Port:** 27017.  
   * **Connectivity Method:** Private Connectivity.  
   * **Encryption:** Выбрать опцию "Server verification" (или аналогичную). Загрузить файл ca.crt (публичный ключ вашего CA), созданный на Фазе 2. Это критически важно для доверия самоподписанному сертификату прокси.17  
2. **Тестирование:** Запустить проверку соединения. Datastream должен успешно подключиться к Прокси, установить TLS-туннель, а Прокси перенаправит трафик в Atlas.

#### **Фаза 4: Отказоустойчивость (High Availability)**

Для Production-среды одиночная VM является точкой отказа.

* **Рекомендация:** Создать Instance Template с настроенным Nginx.  
* Развернуть Managed Instance Group (MIG) с автоскейлингом (мин. 2 реплики).  
* Создать Internal TCP Load Balancer (L4 ILB) перед группой.  
* В Datastream указывать IP-адрес Load Balancer-а.

### **7.3 Риски и ограничения**

1. **Ротация сертификатов:** Необходимо наладить процесс обновления сертификатов на Прокси и в профиле Datastream до истечения их срока действия.  
2. **Изменение топологии Atlas:** Если в Atlas добавляются новые шарды или меняются доменные имена, может потребоваться обновление конфигурации Nginx (если имена захардкожены) или DNS-зон. Использование динамического DNS-резолвинга в Nginx (resolver 169.254.169.254;) минимизирует этот риск.  
3. **Split-Horizon DNS:** Важно следить, чтобы приватная зона DNS не перекрывала публичную зону mongodb.net таким образом, чтобы нарушить доступ других сервисов, которым нужен публичный доступ (если таковые есть).

## **8. Заключение**

Предложенное архитектурное решение трансформирует несовместимые требования двух облачных платформ в надежную, управляемую систему. Использование TCP-прокси с функцией SNI Injection и перешифрованием трафика полностью устраняет блокирующие факторы (отсутствие DNS, SSL Hostname Mismatch), при этом оставаясь в рамках политик безопасности (все каналы шифруются). Данный подход является стандартом де-факто для интеграции legacy-систем или систем с жесткими сетевыми ограничениями, к классу которых относится текущая реализация приватных подключений в Google Cloud Datastream.

### ---

**Таблицы и Структурированные Данные**

#### **Таблица 1: Сравнительный анализ архитектурных решений**

| Характеристика | Direct PSC (Напрямую) | SSH Tunnel (Бастион) | TCP Proxy (Nginx) |
| :---- | :---- | :---- | :---- |
| **Тип подключения** | Private IP | Инкапсулированный туннель | Private IP (через посредника) |
| **Разрешение DNS** | **Провал** (Datastream не умеет) | Частично (Зависит от клиента) | **Успех** (Прокси разрешает) |
| **Обработка SSL/SNI** | **Провал** (Mismatch) | **Провал** (Туннель прозрачен) | **Успех** (Прокси инжектирует SNI) |
| **Производительность** | Высокая (Теоретически) | Низкая (Оверхед TCP-over-TCP) | Высокая (Потоковое проксирование) |
| **Сложность внедрения** | Низкая | Средняя | Средняя |
| **Безопасность** | Высокая | Высокая | Высокая (Re-encryption) |
| **Вердикт** | **Блокирует работу** | **Не рекомендуется** | **Рекомендуется к внедрению** |

#### **Таблица 2: Влияние квот Google Cloud на решение**

1

| Ресурс / Квота | Лимит | Влияние на архитектуру |
| :---- | :---- | :---- |
| **Max Private Connectivity Configs** | 5 на проект | Необходимо использовать архитектуру "Hub-and-Spoke" или Shared VPC, проксируя несколько стримов через один канал. |
| **Streams per Region** | 50 | Прокси-группа (MIG) должна масштабироваться для обработки параллельных соединений от 50 стримов. |
| **DNS Queries per Zone** | 100,000 / 10s | Настройки кэширования DNS в Nginx критичны для предотвращения троттлинга запросов к Cloud DNS. |
| **Packet Mirroring** | Не поддерживается на PSC | Отладка сети на стыке PSC затруднена; необходимо полагаться на подробные access/error логи Nginx. |

---

*Конец отчета.*

#### **Works cited**

1. Quotas and limits | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/quotas](https://docs.cloud.google.com/datastream/docs/quotas)  
2. Private services access - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/vpc/docs/private-services-access](https://docs.cloud.google.com/vpc/docs/private-services-access)  
3. Private Service Connect - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/vpc/docs/private-service-connect](https://docs.cloud.google.com/vpc/docs/private-service-connect)  
4. Announcing Google Private Service Connect (PSC) Integration for MongoDB Atlas, accessed December 7, 2025, [https://www.mongodb.com/company/blog/product-release-announcements/announcing-google-private-service-connect-psc-integration-mongodb-atlas](https://www.mongodb.com/company/blog/product-release-announcements/announcing-google-private-service-connect-psc-integration-mongodb-atlas)  
5. Configure a MongoDB database for CDC | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/configure-mongodb](https://docs.cloud.google.com/datastream/docs/configure-mongodb)  
6. Quotas and limits | Cloud DNS - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/dns/quotas](https://docs.cloud.google.com/dns/quotas)  
7. Create a private connectivity configuration | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration)  
8. Example: Private connectivity for a MongoDB Atlas cluster | Integration Connectors, accessed December 7, 2025, [https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb)  
9. VPC Network Peering | Virtual Private Cloud, accessed December 7, 2025, [https://docs.cloud.google.com/vpc/docs/vpc-peering](https://docs.cloud.google.com/vpc/docs/vpc-peering)  
10. Configure Private Service Connect interfaces | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/psc-interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces)  
11. Google Cloud networking in-depth: What's new with Cloud DNS, accessed December 7, 2025, [https://cloud.google.com/blog/products/networking/google-cloud-networking-in-depth-whats-new-with-cloud-dns](https://cloud.google.com/blog/products/networking/google-cloud-networking-in-depth-whats-new-with-cloud-dns)  
12. Mongodb SSL connection failing when using SSL certificate issued by Let's encrypt suddenly even though the certificate is not expired - Stack Overflow, accessed December 7, 2025, [https://stackoverflow.com/questions/69481148/mongodb-ssl-connection-failing-when-using-ssl-certificate-issued-by-lets-encryp](https://stackoverflow.com/questions/69481148/mongodb-ssl-connection-failing-when-using-ssl-certificate-issued-by-lets-encryp)  
13. Atlas MongoDB SSH Tunnel hostname mismatch - Stack Overflow, accessed December 7, 2025, [https://stackoverflow.com/questions/73958306/atlas-mongodb-ssh-tunnel-hostname-mismatch](https://stackoverflow.com/questions/73958306/atlas-mongodb-ssh-tunnel-hostname-mismatch)  
14. google_datastream_connection_, accessed December 7, 2025, [https://registry.terraform.io/providers/hashicorp/google/6.11.0/docs/resources/datastream_connection_profile](https://registry.terraform.io/providers/hashicorp/google/6.11.0/docs/resources/datastream_connection_profile)  
15. Elastic MongoDB connector reference, accessed December 7, 2025, [https://www.elastic.co/docs/reference/search-connectors/es-connectors-mongodb](https://www.elastic.co/docs/reference/search-connectors/es-connectors-mongodb)  
16. Learn About Private Endpoints in Atlas - Atlas - MongoDB Docs, accessed December 7, 2025, [https://www.mongodb.com/docs/atlas/security-private-endpoint/](https://www.mongodb.com/docs/atlas/security-private-endpoint/)  
17. API Reference — google_api_datastream v0.10.0 - HexDocs, accessed December 7, 2025, [https://hexdocs.pm/google_api_datastream/](https://hexdocs.pm/google_api_datastream/)  
18. Forward SSH tunnel | Datastream - Google Cloud Documentation, accessed December 7, 2025, [https://docs.cloud.google.com/datastream/docs/ssh-tunnel](https://docs.cloud.google.com/datastream/docs/ssh-tunnel)  
19. Proxy RUM data to Frontend Observability | Grafana Cloud documentation, accessed December 7, 2025, [https://grafana.com/docs/grafana-cloud/monitor-applications/frontend-observability/instrument/data-proxy/](https://grafana.com/docs/grafana-cloud/monitor-applications/frontend-observability/instrument/data-proxy/)

# 23.
## 23.1.
`A1ᨀ` ≔  (мой потенциальный ответ `ꆜ`) 

## 23.3.
Содержание `A1ᨀ`:
```markdown
1) In points 2-5, I outline your misconceptions.
In point 6, I outline the correct method to solve your problem.
2) You mistakenly believe that Google Datastream (hereafter — `Dᨀ`) should have access to the Private DNS Zone of your network, and that the current behavior of `Dᨀ` (hereafter — `B𐏐`) is a failure.
In fact, `B𐏐` is explicitly stated in the official documentation of `Dᨀ` (hereafter — `D⸙`): «Datastream doesn't support Domain Name System (DNS) resolution in private connections»
https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration
3) You mistakenly attribute the routing of traffic destined for public IPs to «ignored» routes.
In fact, routing (Layer 3) occurs after DNS resolution.
Since DNS (due to `B𐏐`) resolved the hostname of Atlas (hereafter — `Aᨀ`) to a public IP, `Dᨀ` directed traffic to that destination.
The VPC Network Peering connection (hereafter — `P`) exchanges routes for the standard subnets containing Private Service Connect endpoints (hereafter — `PSC`).
These routes were not «ignored» but were inapplicable to the public IP.
4) You mistakenly believe that the successful «VM Connectivity Test» proves the infrastructure is configured correctly.
In fact, the VM resides inside the VPC network and queries the local metadata server for DNS.
`Dᨀ` operates in the service producer network and uses independent Google internal DNS resolvers.
These resolvers have no access to your Private DNS Zone because `P` shares IP routes but not DNS records.
The VM has direct intra-VPC access to `PSC`.
Since `Dᨀ` resolves the hostname to a public IP, `Dᨀ` attempts to route traffic via the public internet instead of `P`.
Your test proves backend availability but not reachability via `P`.
5) You mistakenly believe that your «`Dᨀ` → `P` → `PSC`» topology is valid.
In fact, `D⸙` states: «The VPC Network Peering connection between your VPC network and the Datastream VPC network doesn't let Datastream connect to: Private Service Connect endpoints located in your VPC network»:
https://cloud.google.com/datastream/docs/private-connectivity
Traffic from `Dᨀ` cannot reach `PSC` in `datastream-net` because `P` does not support transitive access to `PSC` endpoints.
Even if you bypass the DNS problem by entering the IP manually, the Google SDN controller will drop the packets.
6) `R`: the correct method to solve your task
6.1) Use the native «Forward SSH tunnel» mechanism in `Dᨀ` to encapsulate replication traffic inside a secure connection (hereafter — `C`).
6.2) Deploy a virtual machine (Bastion Host, hereafter — `Hᨀ`) in `datastream-net` accessible via Private Service Access.
6.3) `Dᨀ` tunnels TCP traffic via `Hᨀ` to the `Aᨀ` node hostname.
6.4) `Hᨀ` resolves the hostname via local VPC DNS to the `PSC` IP.
6.5) `R` allows `Dᨀ` to connect to the target host by name, ensuring the validation of `Aᨀ` TLS certificates.
6.6) The connection string used in `C` must include `directConnection=true` to disable topology discovery (otherwise, the driver bypasses the tunnel, causing failure).
6.7) `R` is native to `Dᨀ` and recommended for complex topologies.
6.8) `R` resolves the «DNS Split-Horizon» issue by performing name resolution inside the VPC.
6.9) `Hᨀ` routes traffic strictly to private `PSC` IPs.
6.10) `R` bypasses VPC Peering non-transitivity by initiating the connection inside `datastream-net`.
6.11) Domain-based connection prevents «Hostname Mismatch» errors.
```

# 24.
`R1ᨀ` ≔ (Рекомендуемый способ `R` (§6) из `A1ᨀ`)

# 25.
## 25.1.
`S⌖1` ≔
```
Замечание к `R1ᨀ` 
~~~
В описании метода `R` отсутствует обязательное требование использовать параметр строки подключения `directConnection=true` (или режим «Direct connection» в интерфейсе Datastream).
MongoDB Atlas работает как Replica Set. Без явного указания `directConnection=true` драйвер MongoDB внутри Datastream после первого подключения выполнит процедуру обнаружения топологии (Topology Discovery), получит список адресов всех остальных узлов кластера и попытается установить с ними *новые* прямые соединения. Поскольку SSH-туннель обеспечивает проброс трафика только до одной точки (seed host), соединения с остальными узлами пойдут в обход туннеля и будут заблокированы (так как прямая маршрутизация не работает). Для работы через SSH-бастион необходимо принудительно ограничить драйвер одним соединением.
Степень уверенности: 100 
~~~
```

## 25.2.
`S⌖2` ≔
```
Замечание к `S⌖1` 
~~~
В пункте `S⌖1` содержится фактическая ошибка. Интерфейс настройки профиля подключения MongoDB в Google Cloud Datastream (Console, API, Terraform) предоставляет фиксированный набор полей (`Hostname`, `Port`, `Username`, `Password`) и не содержит поля для ввода произвольной строки подключения (Connection String) или дополнительных параметров драйвера. Следовательно, пользователь технически не может выполнить требование о добавлении параметра `directConnection=true` в конфигурацию профиля.
Степень уверенности: 100
~~~
```

# 26.
## 26.1.
`S⌖3` ≔
```
Замечание к `R1ᨀ` 
~~~
В пункте 6.3 указано, что туннель настраивается до «`Aᨀ` cluster hostname».
В экосистеме MongoDB «cluster hostname» обычно подразумевает SRV-запись (формат `mongodb+srv://`), которая возвращает список хостов. Механизм «Forward SSH tunnel» (TCP Port Forwarding), используемый в Datastream, работает на транспортном уровне и требует указания **конкретного целевого хоста** (FQDN A-записи, например `cluster0-shard-00-00.mongodb.net`) и порта. SSH-демон не умеет разрешать SRV-записи для выбора цели туннеля.
Степень уверенности: 95
~~~
```

## 26.2.
`S⌖4` ≔
```
Замечание к `S⌖3` 
~~~
В пунктах `S⌖3` предлагается настроить туннелирование до хостнейма конкретного узла (`node hostname`). Это архитектурное решение содержит логическую ошибку, так как создает единую точку отказа (Single Point of Failure). Кластер MongoDB Atlas является репликационным набором (Replica Set), и при недоступности выбранного узла или изменении его роли (например, при перевыборах Primary) поток репликации остановится, поскольку статический SSH-туннель, настроенный на один адрес, не поддерживает автоматическое переключение (Failover) на другие узлы кластера.
Степень уверенности: 95
~~~
```