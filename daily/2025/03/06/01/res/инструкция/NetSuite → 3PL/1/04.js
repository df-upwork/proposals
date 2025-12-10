var fileObj = file.create({
	contents: csvContent
	,description: 'Orders export for 3PL'
	,encoding: file.Encoding.UTF_8
	,fileType: file.Type.CSV
	,folder: 123
	,name: 'export_orders.csv'
});