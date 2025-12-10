import record from 'N/record';
import search from 'N/search';
import sftp from 'N/sftp';
export function execute() {
	const conn = sftp.createConnection({
		hostKey: 'AAAAB3NzaC1yc2E<…>'
		,hostKeyType: sftp.HostKeyType.RSA
		,passwordGuid: '<…>'
		,port: 22
		,url: '<…>'
		,username: '<…>'
	});
	const findOrder = id => {
		const s = search.create({
			columns: ['internalid']
			,filters: [['mainline', 'is', 'T'], 'AND', ['tranid', 'is', id]]
			,type: search.Type.SALES_ORDER
		}).run().getRange({end: 1, start: 0});
		return !s || !s.length ? null : record.load({
			id: parseInt(s[0].getValue({name: 'internalid'})), type: record.Type.SALES_ORDER
		});
	};
	const path = '<…>';
	conn.list({path: path}).forEach(rf => {
		if (rf.name && rf.name.toLowerCase().endsWith('.csv')) {
			const contents = conn.download({directory: path, filename: rf.name}).getContents();
			const lines = contents.split(/\r?\n/);
			for (let i = 1; i < lines.length; i++) {
				let line = lines[i].trim();
				if (line) {
					let fields = line.split(',');
					let o = findOrder(fields[0]);
					if (o) {
						o.setValue({fieldId: 'custbody_shipping_status', value: fields[1]});
						o.setValue({fieldId: 'custbody_tracking_number', value: fields[2]});
						o.save();
					}
				}
			}
			conn.remove({directory: '<…>', filename: rf.name});
		}
	});
}