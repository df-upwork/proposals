var targetFolderId = 1234;
// 6) Создаём файл внутри NetSuite
// Параметры fileType зависят от формата вашего файла:
// PLAINTEXT, CSV, XMLDOC, JSON, и т.д.
// (см. enum file.Type в документации NetSuite)
var nsFile = file.create({
	name: remoteFile.name,        // Как будет называться файл в File Cabinet
	fileType: file.Type.PLAINTEXT,
	contents: fileContents,
	folder: targetFolderId        // ID папки в File Cabinet
});

// 7) Сохраняем файл и получаем его внутренний ID
var newFileId = nsFile.save();
log.audit({
	title: 'Файл сохранён',
	details: 'File ID: ' + newFileId
});