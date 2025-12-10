var csvLines = [];
csvLines.push('SalesOrderId,TranId,Entity,Total');
orders.forEach(function (order) {
	var line = order.salesOrderId + ',' +
		order.tranId + ',' +
		order.entity + ',' +
		order.total;
	csvLines.push(line);
});
var csvContent = csvLines.join('\n');