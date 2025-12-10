var conn = sftp.createConnection({
	hostKey: 'ssh-rsa 2048 AAAAB3NzaC1yc2E<…>'
	,hostKeyType: sftp.HostKeyType.SSH_RSA
	,passwordGuid: '{GUID<…>}'
	,port: 22
	,url: '<…>'
	,username: '<…>'
});
var dir = '<…>';
var ff = conn.list({path: dir});
for (var i = 0; i < ff.length; i++) {
	var f = ff[i];
	if (f.name && f.name.toLowerCase().endsWith('.csv')) {
		var d = conn.download({directory: dir, filename: f.name});
		var contents = d.getContents();
	}
}