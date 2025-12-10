import file from 'N/file';
import record from 'N/record';
import search from 'N/search';
import sftp from 'N/sftp';
export function execute() {
	var s = search.load({id: 'customsearch_export_orders'});
	var orders = [];
	s.run().each(function(r) {
		orders.push({
			entity: r.getText({name: 'entity'})
			,salesOrderId: r.getValue({name: 'internalid'})
			,total: r.getValue({name: 'total'})
			,tranId: r.getValue({name: 'tranid'})
		});
		return true;
	});
	var csvA = [];
	csvA.push('SalesOrderId,TranId,Entity,Total');
	orders.forEach(function (o) {
		csvA.push([o.salesOrderId, o.tranId, o.entity, o.total].join(','));
	});
	var csv = csvA.join('\n');
	var f = file.create({
		contents: csv
		,description: 'Orders export for 3PL'
		,encoding: file.Encoding.UTF_8
		,fileType: file.Type.CSV
		,folder: 123  // The folder ID in NetSuite File Cabinet
		,name: 'export_orders.csv'
	});
	var conn = sftp.createConnection({
		directory: '<…>'
		,hostKey: 'ssh-rsa 2048 AAAAB3NzaC1yc2E<…>'
		,passwordGuid: '{GUID<…>}'
		,port: 22
		,url: '<…>'
		,username: '<…>'
	});
	conn.upload({file: f});
}
