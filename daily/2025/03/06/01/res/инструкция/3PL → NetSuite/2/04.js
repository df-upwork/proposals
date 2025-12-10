var lines = fileContent.split(/\r?\n/); // учтём и \r\n, и \n
for (var i = 1; i < lines.length; i++) {
	var line = lines[i].trim();
	if (!line) {
		continue;
	}
	var columns = line.split(',');
	var soNumber = columns[0];
	var shippingStatus = columns[1];
	var trackingNumber = columns[2];
	var soInternalId = findSalesOrderByTranId(soNumber);
	if (!soInternalId) {
		log.error('Not Found', 'Sales Order с номером ' + soNumber + ' не найден');
		continue;
	}
	var soRecord = record.load({
		type: record.Type.SALES_ORDER,
		id: soInternalId
	});
	soRecord.setValue({
		fieldId: 'custbody_shipping_status',
		value: shippingStatus
	});
	soRecord.setValue({
		fieldId: 'custbody_tracking_number',
		value: trackingNumber
	});
	soRecord.save();
}

var findOrder = function(id) {
	var s = search.create({
		columns: ['internalid']
		,filters: [['mainline', 'is', 'T'], 'AND', ['tranid', 'is', id]]
		,type: search.Type.SALES_ORDER
	}).run().getRange({end: 1, start: 0});
	return !s || !s.length ? null : record.load({
		id: s[0].getValue({name: 'internalid'}), type: record.Type.SALES_ORDER
	});
};