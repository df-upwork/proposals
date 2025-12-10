import file from 'N/file';
import record from 'N/record';
import search from 'N/search';
import sftp from 'N/sftp';
export function execute() {
	var conn = sftp.createConnection({
		hostKey: 'ssh-rsa 2048 AAAAB3NzaC1yc2E<…>'
		,hostKeyType: sftp.HostKeyType.SSH_RSA
		,passwordGuid: '{GUID<…>}'
		,port: 22
		,url: '<…>'
		,username: '<…>'
	});
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
	conn.list({path: '<…>'}).forEach(function (rf) {
		if (rf.name && rf.name.toLowerCase().endsWith('.csv')) {
			var contents = conn.download({directory: '<…>', filename: f.name}).getContents();
			var lines = contents.split(/\r?\n/);
			for (var i = 1; i < lines.length; i++) {
				var line = lines[i].trim();
				if (line) {
					var fields = line.split(',');
					var o = findOrder(fields[0]);
					if (o) {
						o.setValue({fieldId: 'custbody_shipping_status', value: fields[1]});
						o.setValue({fieldId: 'custbody_tracking_number', value: fields[2]});
						o.save();
					}
				}
			}
		}
	});
}