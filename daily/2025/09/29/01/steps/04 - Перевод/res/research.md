https://g.co/gemini/share/d72545ea6231

Официальная лицензионная политика Microsoft для шрифтов, поставляемых с продуктами Windows и Office, явным образом разрешает встраивание шрифтов в документы. 
Это разрешение, известное как «document font embedding», является документированным и поддерживаемым сценарием использования, а не непреднамеренной лазейкой в лицензии.
https://learn.microsoft.com/en-us/typography/fonts/font-faq


Although the redistribution of fonts supplied with Windows is generally not allowed, “document font embedding” is a special case which is allowed in some circumstances.
https://learn.microsoft.com/en-us/typography/fonts/font-faq#document-embedding


Шрифт Century Gothic официально поставляется как неотъемлемый компонент программных продуктов Microsoft, в частности, пакета Microsoft Office. 
https://learn.microsoft.com/en-us/typography/font-list/century-gothic



Спецификация формата шрифтов OpenType определяет технический механизм контроля прав на встраивание, известный как флаг fsType, который является частью таблицы OS/2 файла шрифта.

Это разрешение, соответствующее значению флага 8 (или 0x0008), технически и юридически позволяет встраивать шрифт в документ таким образом, чтобы получатель мог не только просматривать, но и редактировать этот документ с использованием встроенного шрифта, даже при его отсутствии на локальной системе.


Для достижения полной уверенности необходимо выполнить простую техническую проверку на том компьютере, где будет создаваться шаблон Word: открыть панель управления «Шрифты», найти файл Gothic.ttf (и его вариации), открыть его свойства и убедиться, что поле «Font embeddability» имеет значение «Editable» или «Installable». 