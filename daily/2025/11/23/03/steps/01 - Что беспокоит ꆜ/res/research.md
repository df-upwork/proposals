https://gemini.google.com/share/6ad4ee21264c


## **1. Введение и контекстуальный анализ проекта**

### **1.1. Резюме задачи и профиль клиента**

Настоящий отчет представляет собой экспертный анализ технического задания, инициированного клиентом ꆜ в рамках проекта P⁎, направленного на развертывание 4-узлового кластера Nutanix. Заявленная цель проекта — создание новой площадки ("new site"), которая будет функционировать параллельно с существующим производственным окружением ("production environment") в качестве выделенного сегмента для резервного копирования и аварийного восстановления (Backup/Disaster Recovery — DR).

Анализ профиля клиента ꆜ, базирующийся в Ирвайне (США), и истории его предыдущих технических запросов на платформе Upwork (проекты P1⁎, P2⁎, P3⁎) позволяет сформировать портрет заказчика со зрелой, но гетерогенной ИТ-инфраструктурой. Наличие задач, связанных с Oracle DBA (P3⁎), Cisco DWDM/ONS (P2⁎) и VoIP-системами (P1⁎), указывает на среду с высокими требованиями к доступности данных, чувствительностью к сетевым задержкам и наличием унаследованных систем (Legacy). Это контекстуальное знание критически важно, так как интеграция гиперконвергентной инфраструктуры (HCI) Nutanix в среду, насыщенную классическими оптическими сетями и тяжелыми базами данных, требует особого внимания к вопросам совместимости.

### **1.2. Деконструкция технических требований и зон риска**

В описании задачи (PD) клиент формулирует ряд специфических требований, которые служат индикаторами потенциальных архитектурных конфликтов. Использование терминологии, такой как «AOS Pro», «Prism Leap» и акцент на «architectural caveats» (архитектурные предостережения), свидетельствует о том, что заказчик обладает определенным уровнем технической осведомленности, но оперирует номенклатурой, которая частично устарела или находится в процессе трансформации.

Ключевые зоны риска, выявленные на этапе предварительного анализа, включают:

1. **Аппаратная валидация (Hardware Compatibility):** Строгие требования Nutanix к списку совместимого оборудования (HCL) и риски использования компонентов, вышедших из цикла поддержки (EOSL).  
2. **Лицензионная коллизия:** Несоответствие между функционалом редакции «Pro», запрашиваемой клиентом, и требованиями к современным сценариям катастрофоустойчивости (RPO < 1 часа, автоматизация Runbooks).  
3. **Сетевая интеграция:** Сложности внедрения микросервисной архитектуры (MSP) Nutanix в существующую сетевую топологию, включая конфликты IP-адресации.  
4. **Операционная совместимость:** Риски, связанные с «растягиванием» кластеров (Metro Availability) и смешиванием гипервизоров (Cross-Hypervisor DR).

Цель данного документа — предоставить исчерпывающее техническое обоснование для каждого этапа развертывания, опираясь на официальную документацию Nutanix, матрицы совместимости и лучшие практики индустрии (Nutanix Validated Designs).

---

## **2. Аппаратная архитектура и валидация компонентов (Hardware Compatibility & Lifecycle)**

Подзадача T2⁎ требует валидации аппаратных идентификаторов (PIDs) и компонентов. В экосистеме Nutanix это не формальная процедура, а критический этап, определяющий саму возможность развертывания программного стека. Игнорирование правил HCL (Hardware Compatibility List) является наиболее частой причиной отказов в технической поддержке и сбоев при инсталляции через Nutanix Foundation.

### **2.1. Политика строгой аппаратной совместимости (HCL)**

Программное обеспечение Nutanix AOS (Acropolis Operating System) не является аппаратно-агностичным в широком смысле. Оно проектируется и тестируется для работы на строго определенных конфигурациях. Согласно документации 1, развертывание возможно только на платформах, присутствующих в HCL. Это касается не только серверов (Nodes), но и дисковых контроллеров (HBA), сетевых карт (NIC) и загрузочных устройств.

#### **Риск смешивания вендоров (Vendor Mixing Limitations)**

Критическим аспектом, который необходимо учитывать при планировании новой DR-площадки, является строгий запрет на смешивание узлов от разных OEM-производителей в рамках одного кластера. Документация 3 эксплицитно указывает:

* Недопустимо смешивание узлов Nutanix NX с узлами OEM-партнеров (Dell XC, Lenovo HX, Cisco UCS) в одном кластере.  
* Недопустимо смешивание узлов разных OEM-производителей (например, Cisco и Dell) между собой.

Если существующая производственная среда клиента построена, например, на оборудовании Dell XC, а для новой площадки закуплены серверы Nutanix NX, объединение их в единый физический кластер невозможно. Репликация данных между ними (Remote Replication) поддерживается, но создание единого пула ресурсов — нет. Это фундаментальное ограничение архитектуры, которое должно быть проверено на этапе анализа BOM (Bill of Materials).

### **2.2. Управление жизненным циклом и поколениями оборудования (Generation Mixing)**

Клиент упоминает необходимость валидации PIDs, что особенно актуально в контексте смены поколений оборудования (G6, G7, G8, G9). В текущий момент времени (ноябрь 2025 года, согласно онтологии O.md) этот вопрос приобретает критическую остроту из-за сроков окончания поддержки (End of Support Life — EOSL).

#### **Анализ статуса поколения G6**

Согласно данным о жизненном цикле оборудования 4, многие популярные модели поколения **G6** (например, NX-1065-G6, NX-3060-G6, NX-8035-G6) достигли даты EOSL **30 января 2025 года** или ранее.

| Поколение | Статус на Ноябрь 2025 | Риск использования |
| :---- | :---- | :---- |
| **G6** | **EOSL (End of Support Life)** | **Критический.** Оборудование не поддерживается вендором. Обновления безопасности и прошивок отсутствуют. Развертывание новой площадки на G6 недопустимо. |
| **G7** | Active / End of Sale | Приемлемо, но требует проверки даты окончания продаж. Может быть ограничена доступность запчастей в будущем. |
| **G8/G9** | Active | Рекомендуется для новых инсталляций. |

Если в спецификации (BOM) новой площадки фигурируют PIDs, содержащие идентификатор «G6», проект должен быть немедленно остановлен для пересмотра оборудования. Использование оборудования EOSL для критически важной задачи аварийного восстановления (DR) создает неприемлемые операционные риски.

#### **Правила смешивания поколений (Mixing Rules)**

Даже если оборудование является поддерживаемым (например, смесь G7 и G8), Nutanix накладывает ограничения на физическое размещение узлов. Хотя в одном кластере могут сосуществовать узлы разных поколений, в рамках одного **шасси (Block)** смешивание запрещено.6

* Блок G7 должен содержать только узлы G7.  
* Блок G8 должен содержать только узлы G8.

Нарушение этого правила приведет к невозможности физической установки узлов или сбоям в системе охлаждения и питания шасси, так как разные поколения имеют разные тепловые пакеты и требования к электропитанию.

### **2.3. Валидация сетевых компонентов и трансиверов**

Требование клиента валидировать «optics» и «cabling» (T4⁎) является технически обоснованным. Гиперконвергентная инфраструктура генерирует интенсивный трафик «Восток-Запад» (CVM-to-CVM traffic) для репликации данных и поддержания когерентности кэша.

Использование трансиверов (SFP+/QSFP), не валидированных производителем сетевой карты (NIC), часто приводит к нестабильности физического линка («flapping»). В среде Nutanix это вызывает постоянные перевыборы мастера (Master CVM election) и деградацию производительности дисковой подсистемы. Валидация должна включать сверку Part Number трансивера с HCL конкретной сетевой карты (Mellanox, Intel и т.д.), установленной в сервере.

---

## **3. Лицензионная архитектура: Анализ несоответствий (Pro vs Ultimate)**

Подзадача T3⁎ («Confirm correct AOS Pro and Prism Leap licensing») выявляет одну из наиболее глубоких проблем проекта: несоответствие между запрашиваемым уровнем лицензирования и требуемым функционалом. Современная модель лицензирования Nutanix Cloud Platform (NCP) существенно отличается от устаревшей модели AOS, и понимание этих различий критично для успешной реализации DR.

### **3.1. Трансформация лицензирования: От AOS к NCI**

Nutanix перешла от продажи лицензий AOS к модели **Nutanix Cloud Infrastructure (NCI)**. Хотя названия уровней (Starter, Pro, Ultimate) сохранились, их функциональное наполнение изменилось, особенно в части катастрофоустойчивости.7

#### **Недостаточность редакции NCI Pro для DR**

Клиент планирует использовать площадку для DR и упоминает «replication workflows». Анализ функциональной матрицы 8 показывает следующее:

1. **NCI Pro (бывший AOS Pro):** Включает только базовую асинхронную репликацию (Async Replication) с **RPO >= 1 час**. Это подходит для базового резервного копирования, но не соответствует современным стандартам DR для критичных систем.  
2. **Функции, отсутствующие в Pro:**  
   * **NearSync Replication:** Репликация с RPO от 1 до 15 минут.  
   * **Synchronous Replication:** Нулевая потеря данных (RPO = 0).  
   * **Metro Availability:** Растянутый кластер с автоматическим переключением.  
   * **Runbook Automation:** Оркестрация планов восстановления (то, что ранее называлось «Leap»).

**Вывод:** Запрос клиента на «AOS Pro» для полноценного DR является ошибочным. Для реализации сценариев с RPO < 1 часа или автоматизированным восстановлением необходимо либо приобрести редакцию **NCI Ultimate**, либо докупить специальный аддон **Advanced Replication Add-on** к лицензии Pro.10

### **3.2. Эволюция Prism Leap и Nutanix Disaster Recovery**

Термин «Prism Leap», используемый клиентом, является устаревшим. В актуальном портфолио продукт называется **Nutanix Disaster Recovery**.11 Это изменение номенклатуры важно, так как оно влечет за собой и изменения в лицензировании управления.

Для управления DR-процессами используется **Nutanix Cloud Manager (NCM)**, ранее известный как Prism Pro/Ultimate.

* **Prism Central (Starter):** Позволяет управлять базовыми объектами, но не предоставляет функций расширенной оркестрации.10  
* **Runbooks & Automation:** Для создания сложных планов восстановления (Recovery Plans) с настройкой порядка загрузки ВМ, скриптами смены IP-адресов и тестированием в «песочнице» требуются лицензии уровня **NCM Advanced/Ultimate** или соответствующие аддоны в составе пакета NCI Ultimate.12

### **3.3. Лицензирование Nutanix Files и Objects**

Поскольку новая площадка рассматривается как среда резервного копирования, вероятно использование **Nutanix Objects** (S3-совместимое хранилище) в качестве целевой системы для бэкапов. Важно отметить, что Nutanix Objects лицензируется отдельно по объему (per TiB) или требует выделенной лицензии, если разворачивается на выделенном кластере.10

В рамках лицензий NCI Starter/Pro/Ultimate включено **1 TiB** емкости Nutanix Unified Storage (NUS), что может быть достаточно для пилотного проекта, но критически мало для полноценного бэкап-репозитория.9 Для промышленных объемов потребуется закупка дополнительных лицензий NUS.

### **3.4. Матрица функциональных возможностей лицензий DR**

Для наглядности сравнения возможностей различных редакций приведена следующая таблица, составленная на основе 7:

| Функция Disaster Recovery | NCI Starter | NCI Pro | NCI Pro + Adv. Rep. Add-on | NCI Ultimate |
| :---- | :---- | :---- | :---- | :---- |
| **Async Replication** (RPO ≥ 1 час) | Да | Да | Да | Да |
| **NearSync Replication** (RPO 1–15 мин) | Нет | Нет | **Да** | **Да** |
| **Sync Replication** (RPO = 0) | Нет | Нет | **Да** | **Да** |
| **Metro Availability** (RPO = 0, Auto Failover) | Нет | Нет | **Да** | **Да** |
| **Runbook Automation** (Оркестрация) | Нет | Нет | **Да** | **Да** |
| **Multi-site DR** (Many-to-Many) | Нет | Нет | **Да** | **Да** |
| **Cross-Cluster Live Migration** | Нет | Нет | **Да** | **Да** |

Таким образом, для удовлетворения требований клиента по "deployment readiness" и "DR workflows" (T3⁎, T6⁎), инженеру необходимо настоять на пересмотре спецификации в пользу NCI Ultimate или добавления Advanced Replication Add-on.

---

## **4. Архитектура катастрофоустойчивости и репликации данных**

Задача T5⁎ требует валидации совместимости между площадками, включая топологию сети и возможности репликации. Выбор правильного механизма репликации диктует требования к физической инфраструктуре.

### **4.1. Технологические требования к режимам репликации**

#### **NearSync Replication (RPO 1-15 минут)**

Это наиболее сбалансированный режим для большинства бизнес-приложений. Он использует технологию Lightweight Snapshots (LWS), которая работает не с полными метаданными на диске, а с журналом операций (OpLog) в памяти.

* **Требование к SSD:** Для поддержки NearSync каждый SSD в кластере должен иметь объем не менее **1.2 TB**.15 Это часто упускаемый из виду нюанс. Если в BOM заложены диски по 960 GB или 480 GB (что часто встречается в бюджетных конфигурациях для бэкапа), функционал NearSync будет недоступен, и система откатится к асинхронной репликации с часовым RPO.  
* **Требование к версии AOS:** Оба кластера должны поддерживать LWS. Если производственный кластер работает на старой версии AOS (до 5.19), NearSync может быть недоступен или нестабилен.16

#### **Metro Availability (RPO = 0)**

Если клиент стремится к нулевой потере данных (RPO=0), используется синхронная репликация.

* **Лимит задержки (Latency):** Строгое требование — Round Trip Time (RTT) между площадками **менее 5 мс**.17 При превышении этого порога система не позволит активировать Metro Availability или перейдет в асинхронный режим.  
* **Топология сети:** Metro Availability требует растянутого L2-домена (Subnet extension) между площадками, чтобы ВМ могли мигрировать без смены IP-адреса. Это требует сложной сетевой инфраструктуры (VXLAN, OTV или темное волокно).  
* **Ограничение гипервизора:** Metro Availability в классическом понимании Nutanix поддерживается **только на ESXi**. Аналог для AHV (Synchronous Replication с автоматическим переключением) требует наличия **Nutanix Witness**.15

### **4.2. Архитектура «Свидетеля» (Witness) и защита от Split-Brain**

Для предотвращения сценария «Split-Brain» (когда при обрыве связи оба кластера считают себя активными и начинают запись, повреждая данные), Nutanix использует алгоритм консенсуса Paxos.20

В конфигурациях Metro (или Sync Rep с авто-переключением) обязательно наличие компонента **Witness**.

* **Размещение:** Witness VM должна располагаться в **третьем** домене отказа (Fault Domain), независимом от основной и резервной площадок.19  
* **Ошибка архитектуры:** Если клиент планирует развернуть Witness VM внутри того же кластера, который она должна мониторить, или на второй площадке DR, это сделает автоматическое переключение невозможным. При падении площадки вместе со «Свидетелем» система не сможет собрать кворум.

### **4.3. Кросс-гипервизорная репликация (Cross-Hypervisor DR — CHDR)**

Учитывая, что клиент упоминает «validation... including hypervisor» (T5⁎), вероятен сценарий, когда на продакшене используется VMware ESXi, а новая площадка планируется на Nutanix AHV для экономии лицензионных отчислений VMware.

* **Поддержка:** Nutanix поддерживает CHDR (ESXi -> AHV и обратно).  
* **Ограничения шифрования:** Репликация зашифрованных ВМ (Encrypted VMs) между разными гипервизорами имеет серьезные ограничения. ВМ могут быть реплицированы, но не смогут запуститься на целевой стороне без ручного вмешательства или наличия внешней системы управления ключами (KMS), доступной для обеих площадок.22 Встроенное шифрование Nutanix работает прозрачно, но шифрование на уровне гостевой ОС или vSphere Encryption может стать блокирующим фактором.

---

## **5. Сетевая инфраструктура и микросервисы (MSP)**

Внедрение **Microservices Infrastructure (MSP)** в Prism Central начиная с версии pc.2022.x радикально изменило сетевые требования к развертыванию управления Nutanix. Подзадача T2⁎ («Validate... networking requirements») требует глубокого анализа топологии IP-адресации.

### **5.1. Конфликт подсетей микросервисов**

При активации Nutanix Disaster Recovery (ранее Leap) или развертывании Nutanix Objects на Prism Central автоматически поднимается кластер Kubernetes для внутренних нужд. По умолчанию он резервирует следующие подсети 23:

* 10.100.0.0/16 — для сети подов (Pod Network).  
* 10.200.32.0/24 — для сети сервисов (Service Network).

**Критический риск:** Если в существующей корпоративной сети клиента эти диапазоны уже используются (что весьма вероятно для частных сетей класса A), попытка развертывания Prism Central или активации DR приведет к конфликту маршрутизации. Управление кластером станет невозможным, или "ляжет" часть корпоративной сети.

* **Решение:** Необходимо изменить дефолтные подсети MSP *до* начала развертывания (во время инсталляции PC) или через специальные процедуры CLI, если конфликт обнаружен постфактум.25

### **5.2. Требования к портам межсетевого экрана**

Для обеспечения репликации и управления между площадками необходимо обеспечить прохождение трафика через брандмауэры (T2⁎). Список критических портов включает 23:

* **TCP 2020 (ранее 2009):** Основной порт репликации данных между CVM (Stargate).  
* **TCP 9440:** HTTPS трафик управления (Prism API).  
* **TCP 3205 / 3260:** iSCSI трафик (необходим для Nutanix Objects и Volumes).  
* **TCP 2074:** Коммуникация с Nutanix Guest Tools (NGT) для создания консистентных снапшотов приложений (Application Consistent Snapshots).27

Отсутствие доступа по порту 2074 сделает невозможным использование VSS (Volume Shadow Copy Service) внутри Windows-машин, что критично для корректного бэкапа баз данных (SQL, Exchange), упомянутых в профиле клиента (P3⁎).

### **5.3. Настройка физической сети и LACP**

Для 4-узлового кластера Nutanix настоятельно рекомендует использование агрегации каналов (LACP) в режиме **Active-Active** (802.3ad). Это обеспечивает балансировку трафика и высокую доступность.

* **Риск:** Если физические коммутаторы настроены на статический EtherChannel или используют "On" mode вместо LACP negotiation, линки могут не подняться или работать с потерей пакетов.  
* **Jumbo Frames:** Для повышения эффективности репликации рекомендуется включение Jumbo Frames (MTU 9000). Однако, это требует настройки MTU 9000 на всем пути следования трафика ("End-to-End"), включая промежуточные маршрутизаторы между площадками. Если хотя бы одно устройство имеет MTU 1500, пакеты будут фрагментироваться или отбрасываться, что приведет к фатальному падению скорости репликации.

---

## **6. Хранилище резервного копирования: Nutanix Objects**

Поскольку проект позиционируется как "Backup Environment", высока вероятность использования **Nutanix Objects** (S3-совместимое объектное хранилище) в качестве таргета для бэкапов (например, для Veeam или HYCU).

### **6.1. Специфика сайзинга для Objects**

Для развертывания Nutanix Objects существуют жесткие минимальные требования к размеру кластера, которые влияют на архитектуру 4-узлового решения.

* **Минимум 4 узла:** Согласно лучшим практикам 28, для Nutanix Objects рекомендуется (а для определенных конфигураций требуется) минимум 4 узла. Это связано с архитектурой развертывания: требуются рабочие ноды (Worker Nodes) и балансировщики нагрузки (Load Balancers).  
* **Erasure Coding (EC-X):** Для эффективного хранения бэкапов (дедупликация и сжатие) критически важно использование Erasure Coding. EC-X требует минимум 4 узла в кластере. Если один узел выйдет из строя или будет переведен в Maintenance Mode, кластер потеряет способность записывать данные в формате EC-X, что приведет к резкому росту потребления дискового пространства (Revert to RF2/RF3).

### **6.2. Сетевая изоляция Objects**

Nutanix Objects требует выделения отдельных VLAN для внутреннего трафика ("Storage Network") и внешнего доступа ("Public Network").28 Смешивание этого трафика с трафиком управления (CVM Management) или трафиком виртуальных машин может привести к насыщению полосы пропускания и деградации производительности всего кластера во время окон резервного копирования.

---

## **7. Операционные процедуры и тестирование (Runbooks & Testing)**

Задача T9⁎ («Support configuration steps... protection domains») подразумевает не только настройку репликации, но и обеспечение возможности восстановления.

### **7.1. Изоляция тестовых переключений (Test Failover)**

Современные стандарты DR требуют возможности регулярного тестирования планов восстановления без влияния на продуктив. Nutanix DR предоставляет возможность запускать ВМ в изолированной тестовой сети ("Test VPC" или VLAN mapping).29

* **Требование:** На сетевом оборудовании резервной площадки должны быть заранее сконфигурированы тестовые VLAN, которые **не маршрутизируются** в основную корпоративную сеть.  
* **Риск:** Если тестовая сеть имеет L3-связность с продакшеном, запуск дубликатов ВМ (с теми же IP-адресами) приведет к конфликту IP (IP Conflict) и падению продуктивных сервисов. Инженер должен валидировать изоляцию на уровне ACL или VRF на коммутаторах.

### **7.2. Проблема «застрявших» снапшотов (Stun/Stuck Snapshots)**

При использовании сторонних систем резервного копирования (Veeam и др.) совместно с нативной репликацией Nutanix возможны конфликты на уровне гипервизора. Если бэкап-софт создает снапшот и не удаляет его корректно, попытка создания снапшота Nutanix Protection Domain может завершиться ошибкой.

* **Рекомендация:** Разнести расписания бэкапов и репликации Nutanix, чтобы они не пересекались во времени. Избегать одновременного использования VSS-провайдеров от разных вендоров внутри одной ВМ.

---

## **8. Выводы и дорожная карта проекта**

Проведенный анализ подтверждает, что проект P⁎ содержит ряд критических архитектурных рисков, требующих немедленного вмешательства на этапе планирования. Опасения клиента относительно совместимости и лицензирования являются полностью обоснованными.

### **8.1. Сводная таблица рисков и рекомендаций**

| Область риска | Уровень | Проблема | Рекомендация / Действие (Action Item) |
| :---- | :---- | :---- | :---- |
| **Лицензирование** | **Критический** | NCI Pro недостаточно для NearSync/Metro DR. | Заменить спецификацию на **NCI Ultimate** или добавить **Advanced Replication Add-on**. |
| **Оборудование (EOSL)** | **Критический** | Риск использования поколения G6 (EOSL Jan 2025). | Исключить любые PIDs с суффиксом **G6**. Использовать G8/G9. |
| **Хранение (SSD)** | **Высокий** | SSD < 1.2 TB не поддерживают NearSync. | Проверить BOM: SSD должны быть **≥ 1.2 TB**. |
| **Сеть (MSP)** | **Высокий** | Конфликт подсетей 10.100.0.0/16. | Провести аудит IP-адресации клиента. Сменить подсети MSP при инсталляции PC. |
| **Архитектура (Witness)** | **Высокий** | Отсутствие 3-й площадки для Witness. | Запланировать развертывание Witness в облаке или на независимой площадке. |
| **Совместимость** | **Средний** | Смешивание вендоров (NX + Dell/Cisco). | Подтвердить, что новые узлы не будут добавляться в существующий кластер другого вендора. |

### **8.2. Заключение**

Успешная реализация проекта зависит от перехода от формального выполнения инструкций к проактивному архитектурному консалтингу. Инженер должен не просто "валидировать BOM", но и выступить в роли эксперта, способного объяснить клиенту, почему экономия на лицензии NCI Ultimate или SSD-накопителях приведет к невозможности реализации заявленных целей катастрофоустойчивости. Следование представленным рекомендациям позволит нивелировать риски, связанные с HCL, лицензированием и сетевой интеграцией, обеспечив надежный фундамент для системы аварийного восстановления.

#### **Works cited**

1. Nutanix Hardware Platforms: Specs for Nutanix, OEM & Partner Platforms, accessed November 23, 2025, [https://www.nutanix.com/products/hardware-platforms](https://www.nutanix.com/products/hardware-platforms)  
2. Support Policies and FAQs - Nutanix, accessed November 23, 2025, [https://www.nutanix.com/support-services/support-policies-and-faqs](https://www.nutanix.com/support-services/support-policies-and-faqs)  
3. Hardware - Product intermixing restrictions in Nutanix Clusters, accessed November 23, 2025, [https://portal.nutanix.com/kb/10240](https://portal.nutanix.com/kb/10240)  
4. Nutanix End of Life List - EOSL & EOL Dates - Park Place Technologies, accessed November 23, 2025, [https://www.parkplacetechnologies.com/eosl/nutanix/](https://www.parkplacetechnologies.com/eosl/nutanix/)  
5. Nutanix Models Approaching EOSL: What's Next? - Pre Rack IT, accessed November 23, 2025, [https://prerackit.com/nutanix-models-approaching-eosl-whats-next/](https://prerackit.com/nutanix-models-approaching-eosl-whats-next/)  
6. Product mixing restrictions - Nutanix Community, accessed November 23, 2025, [https://next.nutanix.com/installation-configuration-23/product-mixing-restrictions-37231](https://next.nutanix.com/installation-configuration-23/product-mixing-restrictions-37231)  
7. Nutanix Cloud Platform, accessed November 23, 2025, [https://www.nutanix.com/library/datasheets/nutanix-cloud-platform](https://www.nutanix.com/library/datasheets/nutanix-cloud-platform)  
8. Nutanix Licensing and Cloud Platform Software Options, accessed November 23, 2025, [https://www.nutanix.com/products/cloud-platform/software-options](https://www.nutanix.com/products/cloud-platform/software-options)  
9. Nutanix Cloud Infrastructure (NCI), accessed November 23, 2025, [https://www.nutanix.com/library/datasheets/nci](https://www.nutanix.com/library/datasheets/nci)  
10. Software Options - Nutanix, accessed November 23, 2025, [https://www.nutanix.com/products/legacy/software-options](https://www.nutanix.com/products/legacy/software-options)  
11. Nutanix Disaster Recovery pc.7.3 - Requirements for DR Configuration between On-Prem AZs, accessed November 23, 2025, [https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-requirements-pc-r.html](https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-requirements-pc-r.html)  
12. Prism Pro Vs Ultimate | PDF - Scribd, accessed November 23, 2025, [https://www.scribd.com/document/854631482/Prism-Pro-vs-Ultimate](https://www.scribd.com/document/854631482/Prism-Pro-vs-Ultimate)  
13. Nutanix Cloud Manager (NCM), accessed November 23, 2025, [https://www.nutanix.com/library/datasheets/ncm](https://www.nutanix.com/library/datasheets/ncm)  
14. Nutanix Licensing Quick Reference Guide, accessed November 23, 2025, [https://www.adn.de/fileadmin/user_upload/Hersteller/Nutanix/Datenblaetter/Nutanix_Licensing_Quick_Reference_Guide2.pdf](https://www.adn.de/fileadmin/user_upload/Hersteller/Nutanix/Datenblaetter/Nutanix_Licensing_Quick_Reference_Guide2.pdf)  
15. Nutanix Business Continuity and Disaster Recovery Solutions, accessed November 23, 2025, [https://portal.nutanix.com/page/documents/solutions/details?targetId=RA-2147-Nutanix-for-Enterprise-Edge:nutanix-business-continuity-and-disaster-recovery-solutions.html](https://portal.nutanix.com/page/documents/solutions/details?targetId=RA-2147-Nutanix-for-Enterprise-Edge:nutanix-business-continuity-and-disaster-recovery-solutions.html)  
16. Nutanix Disaster Recovery pc.7.3 - Conditions and Limitations for Multi-site Configurations, accessed November 23, 2025, [https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-considerations-multisite-pc-r.html](https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-considerations-multisite-pc-r.html)  
17. High network latency between Metro Availability Protection Domains (also known as stretched clusters) - Nutanix Support Portal, accessed November 23, 2025, [https://portal.nutanix.com/kb/4309](https://portal.nutanix.com/kb/4309)  
18. Announcing Nutanix Metro Availability, accessed November 23, 2025, [https://www.nutanix.com/blog/announcing-nutanix-metro-availability](https://www.nutanix.com/blog/announcing-nutanix-metro-availability)  
19. Nutanix Disaster Recovery pc.7.3 - AHV Metro Availability for Volume Groups, accessed November 23, 2025, [https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-ahv-metro-introduction-c.html](https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-ahv-metro-introduction-c.html)  
20. Prevent Network Partition Errors - Nutanix Support Portal, accessed November 23, 2025, [https://portal.nutanix.com/page/documents/solutions/details?targetId=TN-2028-Nutanix-Cloud-Clusters-on-AWS:prevent-network-partition-errors.html](https://portal.nutanix.com/page/documents/solutions/details?targetId=TN-2028-Nutanix-Cloud-Clusters-on-AWS:prevent-network-partition-errors.html)  
21. Disaster Recovery Environment and Protection Setup - Nutanix Support Portal, accessed November 23, 2025, [https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-dr-environment-and-protection-setup-c.html](https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-dr-environment-and-protection-setup-c.html)  
22. Nutanix Disaster Recovery pc.7.3 - Limitations of DR Configuration between On-Prem AZs, accessed November 23, 2025, [https://portal.nutanix.com/page/documents/details?targetId=Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-limitations-pc-r.html](https://portal.nutanix.com/page/documents/details?targetId=Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-limitations-pc-r.html)  
23. Prism - Microservices Infrastructure - The Nutanix Cloud Bible, accessed November 23, 2025, [https://www.nutanixbible.com/pdf/3d-book-of-prism-microservices-infrastructure.pdf](https://www.nutanixbible.com/pdf/3d-book-of-prism-microservices-infrastructure.pdf)  
24. Prism pc.7.3 - Additional Operations, accessed November 23, 2025, [https://portal.nutanix.com/docs/Prism-Central-Guide-vpc_7_3:mul-pc-management-c.html](https://portal.nutanix.com/docs/Prism-Central-Guide-vpc_7_3:mul-pc-management-c.html)  
25. Modifying the networks used by Objects internal services to avoid conflicts with existing networks - Nutanix Support Portal, accessed November 23, 2025, [https://portal.nutanix.com/kb/12606](https://portal.nutanix.com/kb/12606)  
26. Prism pc.7.3 - Microservices Infrastructure Prerequisites and Considerations, accessed November 23, 2025, [https://portal.nutanix.com/docs/Prism-Central-Guide-vpc_7_3:mul-cmsp-req-and-limitations-pc-r.html](https://portal.nutanix.com/docs/Prism-Central-Guide-vpc_7_3:mul-cmsp-req-and-limitations-pc-r.html)  
27. Data Protection and Disaster Recovery Best Practices - Nutanix Support Portal, accessed November 23, 2025, [https://portal.nutanix.com/page/documents/solutions/details?targetId=BP-2005-Data-Protection:BP-2005-Data-Protection](https://portal.nutanix.com/page/documents/solutions/details?targetId=BP-2005-Data-Protection:BP-2005-Data-Protection)  
28. Nutanix Objects Best Practices, accessed November 23, 2025, [https://portal.nutanix.com/page/documents/solutions/details?targetId=TN-2093-NDB-Integration-Nutanix-Objects:nutanix-objects-best-practices.html](https://portal.nutanix.com/page/documents/solutions/details?targetId=TN-2093-NDB-Integration-Nutanix-Objects:nutanix-objects-best-practices.html)  
29. Nutanix Recovery Plans: Orchestrating DR Failover | Mike Dent - eGroup, accessed November 23, 2025, [https://www.egroup-us.com/news/nutanix-recovery-plans-orchestrating-dr-failover/](https://www.egroup-us.com/news/nutanix-recovery-plans-orchestrating-dr-failover/)  
30. Nutanix Disaster Recovery pc.7.3 - Failover Scenarios, accessed November 23, 2025, [https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-scenarios-failover-recoveryplan-pc-c.html](https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-scenarios-failover-recoveryplan-pc-c.html)  
31. Disaster Recovery Configuration Specifications - Nutanix Support Portal, accessed November 23, 2025, [https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-dr-configuration-specifications-c.html](https://portal.nutanix.com/docs/Disaster-Recovery-DRaaS-Guide-vpc_7_3:ecd-ecdr-dr-configuration-specifications-c.html)