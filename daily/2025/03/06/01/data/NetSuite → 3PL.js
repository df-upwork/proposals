import file from 'N/file';
import search from 'N/search';
import sftp from 'N/sftp';
export function execute() {
	const orders = search.load({id: 'customsearch_export_orders'}).run().map(r => ({
		entity: r.getText({name: 'entity'})
		,salesOrderId: r.getValue({name: 'internalid'})
		,total: r.getValue({name: 'total'})
		,tranId: r.getValue({name: 'tranid'})
	}));
	let csvA = ['SalesOrderId,TranId,Entity,Total'];
	orders.forEach(o => {csvA.push(
		[o.salesOrderId, o.tranId, o.entity, o.total]
			.map(v => `"${v}"`)
			.join(',')
	);});
	const f = file.create({
		contents: csvA.join('\n')
		,description: '<…>'
		,encoding: file.Encoding.UTF_8
		,fileType: file.Type.CSV
		,folder: 123 // The folder ID in NetSuite File Cabinet
		,name: '<…>.csv'
	});
	f.save();
	const conn = sftp.createConnection({
		directory: '<…>'
		,hostKey: 'AAAAB3NzaC1yc2E<…>'
		,hostKeyType: sftp.HostKeyType.RSA
		,passwordGuid: '<…>'
		,port: 22
		,url: '<…>'
		,username: '<…>'
	});
	conn.upload({file: f, replaceExisting: true});
}