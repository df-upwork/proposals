Правильный способ диагностики сбоев с кодом 500 в Azure App Services:
1) В первую очередь надо ясно понимать смысл кода 500: «a generic error message, given when an unexpected condition was encountered and no more specific message is suitable»
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#500
Поэтому стратегически правильный способ устранения подобных проблем — не строить гипотезы о причинах сбоя, а правильно реализовать систему диагностики сбоя, и эта система диагностики сама в явном виде укажет причину сбоя.
2) В первую очередь надо правильно связать Azure App Service с  Application Insights.
2.1) Надо в разделе «App Service» → «Settings» → «Environment variables» правильно настроить `APPLICATIONINSIGHTS_CONNECTION_STRING`.
2.2) В .NET-приложении должны быть установлены корректные пакеты NuGet для Application Insights SDK (в первую очередь, `Microsoft.ApplicationInsights.AspNetCore`).
2.3) В коде запуска приложения (обычно в файле `Program.cs`) должен содержаться вызов `services.AddApplicationInsightsTelemetry()`.
2.4) Проверить корректность интеграции Azure App Service с Application Insights проще всего посредством «Application Insights» → «Investigate» → «Live Metrics».
2.5) Если Live Metrics не показывает никаких данных для сбойного эндпоинта, это указывает на серьезный сбой при запуске, который мешает инициализации Application Insights SDK или даже не позволяет запросу достичь конвейера ASP.NET Core.
Пример такого сбоя: «500.30 - ANCM In-Process Start Failure». 
В таком случае надо провести диагностику способами пунктов 3-6 ниже. 
3) Надо зайти в раздел «Monitoring» → «App Service logs» и там включить 4 опции: 
3.1) «Application Logging» и «Web server logging».
При этом надо установить для параметра «Level» значение «Verbose».
3.2) «Detailed Error Messages».
Это позволяет сохранить точную HTML-страницу ошибки, которую сгенерировал бы IIS. 
Такая страница часто содержит более конкретные коды ошибок и сообщения, чем общий ответ 500. 
3.3) «Failed Request Tracing».
Это самый мощный инструмент для диагностики проблем в конвейере IIS, который генерирует подробную XML-трассировку активности каждого модуля для неудачного запроса.
4) В разделе «Monitoring» → «Log Stream» можно увидеть логи пункта 2 в реальном времени.
Например, можно вызвать ваш проблемный endpoint `/api/user/roles` и сразу увидеть, что система запишет в логи.
5) Диагностика посредством `stdout`.
5.1) Для захвата вывода `stdout` и `stderr` необходимо модифицировать конфигурацию модуля ANCM. 
Наиболее прямой способ сделать это в среде Azure App Service — использовать консоль Kudu для редактирования файла `web.config`.
Доступа к консоли Kudu: «Development Tools» → «Advanced Tools» → «Go».
Доступ к командной строке из Kudu: «Debug console» → «CMD».
Вся конфигурация, специфичная для модуля ANCM, находится внутри элемента `<aspNetCore>` в файле `web.config`.
Пример настройки `<aspNetCore>`:
```xml
<aspNetCore processPath="dotnet"
	arguments=".\YourApplication.dll"
	stdoutLogEnabled="true"
	stdoutLogFile="\\?\%home%\LogFiles\stdout"
	hostingModel="InProcess">
</aspNetCore>
```
5.2) После перезапуска приложения и воспроизведения ошибки файл журнала должен быть создан в указанной директории.
Содержимое файла журнала `stdout` является ключом к разгадке проблемы. 
Как правило, оно содержит полное сообщение об исключении и стек вызовов, которые указывают на точное место в коде, где произошел сбой. 
6) Самый мощный способ диагностики (когда способы пунктов 2-5 не помогают): «Development Tools» → «Advanced Tools» → «Go» → «Tools» → «Diagnostic dump».
