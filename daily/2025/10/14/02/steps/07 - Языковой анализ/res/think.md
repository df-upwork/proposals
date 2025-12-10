1.
Пункт: 3.1.
Степень уверенности: 70.
Замечание: Формулировка «when selectively merging contacts into an existing profile is required» грамматически верна, но несколько тяжеловесна. Кроме того, слово «required» (необходимо) может быть слишком сильным; «preferred» (предпочтительно) или изменение структуры предложения лучше отражает ситуацию, когда этот метод выбирается для удобства слияния данных, а не из-за строгой невозможности применения метода 2.
Предложение:
It is used when methods 1 and 2 are not applicable (e.g., data stored locally in «This computer only» folders within an IMAP OST file) or when contacts need to be selectively merged into an existing profile.

2.
Пункт: 3.1.1.
Степень уверенности: 90.
Замечание: Утверждение о том, что для консолидации можно использовать «Copy Folder» или «Import/Export Wizard», является технически неточным, так как не учитывает разницу в их применении. Функция «Copy Folder» требует, чтобы целевой PST-файл уже был подключен к профилю, тогда как «Import/Export Wizard» может создать новый PST-файл в процессе экспорта. Необходимо уточнить это различие.
Предложение:
This can be achieved using the Outlook «Import/Export Wizard» (exporting specifically to an «Outlook Data File (.pst)») or by using the «Copy Folder» function if a destination PST file is already connected to the profile.

3.
Пункт: 3.1.1.
Степень уверенности: 80.
Замечание: Формулировка «Contrary to common belief» может звучать несколько конфронтационно. Учитывая, что клиент явно выразил опасение по поводу экспорта в PST («A standard export/import (CSV or PST) will not work»), лучше использовать более утвердительную формулировку, которая напрямую адресует это опасение.
Предложение:
Contrary to the concern noted in the project description, exporting specifically to a PST file (unlike CSV) fully preserves all custom fields and groups.

4.
Пункт: 3.1.1.
Степень уверенности: 80.
Замечание: Формулировка «the file is used directly» является расплывчатой. Следует уточнить, что файл используется для последующего переноса.
Предложение:
If the data is already in a PST file, this consolidation step is skipped, and the file is used for the transfer.

5.
Пункт: 3.1.2.
Степень уверенности: 70.
Замечание: Термин «opened in» технически корректен, но для описания процесса добавления файла данных в профиль термин «connected to» является более предпочтительным и понятным для пользователя.
Предложение:
The PST file is copied or moved to the new computer and connected to the new Outlook profile.

6.
Пункт: 3.1.2.
Степень уверенности: 95.
Замечание: Слово ``transferred`` является неточным, так как оно может подразумевать перемещение с удалением данных из источника. Поскольку далее явно указывается использование функции «Copy Folder», необходимо использовать глагол ``copied``. Также термин «destination data store» может быть сложен для нетехнического пользователя; лучше использовать более простое описание.
Предложение:
Within Outlook on the new computer, the «Contacts» folder is then copied from this PST file to the main storage location using the «Copy Folder» function.

7.
Пункт: 3.3.
Степень уверенности: 80.
Замечание: Между предпоследним и последним предложениями отсутствует явная логическая связка. Добавление связующего слова (например, ``Therefore``) в начале последнего предложения улучшит логическую структуру и покажет причинно-следственную связь между потерей цветов и необходимостью их отдельной миграции.
Предложение:
Therefore, preserving the original colors requires a separate, specialized migration of the MCL (e.g., using programmatic methods or third-party tools) because Outlook lacks a built-in feature for this.