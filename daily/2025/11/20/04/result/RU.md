1) TLDR: in point 4 I analyze your probable misconception.
In points 7-8 I outline my recommendations.
2) Предлагаемый вами подход (hereafter — `M1`) для вашей задачи (hereafter — `T⁎`): установка вашего приложения (hereafter — `A`) на «on the locally hosted server» (hereafter — `LHS`) «in the title company» (`hereafter` — `C`) office, чтобы позволить `A` «regularly query» (hereafter — `Q`) «the TPS system» (hereafter — `TS`) «SQL database» (hereafter — `D`).
3) На вашем рынке title industry (hereafter — `TI`) доминирующим способом установки `TS` является Hosted (hereafter — `H`), а не On-Premise (hereafter — `OP`).
4) `M1` не будет работать для `TS`, установленной как `H` (hereafter — `TS-H`).
Как вы сами правильно указали, `TS-H` реализуется в виде «virtual desktop environment» (hereafter — `VDE`).
В модели `VDE` у `A` не будет возможности получить доступ к `D`.
`D` расположена не на `LHS`, а на удалённом сервере.
Вендоры `TS` (hereafter — `T`) не предоставляют `C`, использующим `TS-H`,  учетные записи для authentication в `D`: authentication производится через через сервисный аккаунт, вшитый в `TS-H`, пароль от которого `C` неизвестен.
5) Технически, `M1` возможен при установке `TS` в виде `OP` (hereafter — `TS-OP`).
Однако даже в этом случае `C` вряд ли дадут вам доступ к `D`, потому что это наверняка будет регуляторным нарушением NPI/GLBA.
6) Все ведущие `T` разработали для своих `TS` возможности их интеграции для сторонними информационными системами.
Ниже я описываю правильные подходы для интеграции `TS` двух лидеров `TI`: Resware (hereafter — `R`) и SoftPro (hereafter — `S`).
7) Мои рекомендации для `R`
7.1) Rest API.
Так, например, поступает сервис notarize.com: https://www.notarize.com/blog/resware-notarize  
7.2) Action Events.
Так, например, поступает сервис snapdocs.com: https://support.snapdocs.com/action-event-resware 
8) Мои рекомендации для `S` 
8.1) Разработка официального адаптера для SoftPro 360:
https://info.softprocorp.com/get-started-with-softpro-360
SoftPro 360 — это интеграционная платформу класса middleware, разработанная `S` для обеспечения бесшовного, двунаправленного обмена данными между ядром системы управления недвижимостью (SoftPro Select, Standard, Enterprise) и распределенной сетью внешних поставщиков услуг. 
8.2) Task Notification Tool (TNT): 
https://www.softprocorp.com/real-estate-software-solutions
TNT — специализированный модуль расширения (add-on) для платформы SoftPro Select, разработанный для автоматизации исходящих коммуникаций на основе событийного управления. 
Его архитектурная задача заключается в мониторинге состояния системы и выполнении предопределенных действий (преимущественно отправки электронной почты) при наступлении специфических условий.
TNT непрерывно отслеживает изменения в рабочих процессах (workflows), такие как завершение задач, изменение статусов заказов или ввод специфических данных.
TNT применяет сложные фильтры «Если-То» (If-Then), чтобы определить, требует ли конкретное событие реакции.
TNT отправяет персонализированные уведомления, часто сопровождаемых вложениями документов, сгенерированных в процессе производства титула.
