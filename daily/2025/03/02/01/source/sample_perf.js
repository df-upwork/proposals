import mysql from 'mysql2/promise';

const db = await mysql.createConnection({'host':'127.0.0.1','user':'test','password':'test','database':'test'});

async function test() {
	const startTime = process.hrtime.bigint();
	await db.query('UPDATE test SET f=1 WHERE id=1');
	//await db.query('SELECT 1');
	var MS = Number(process.hrtime.bigint()-startTime)/1000000;
	console.log(MS);
	setTimeout(test, 250);
}
async function go() {
	await db.query('DROP TABLE IF EXISTS test');
	await db.query('CREATE TABLE `test` ( `id` int NOT NULL, `f` int NOT NULL, PRIMARY KEY (`id`)) ENGINE=MEMORY');
	await db.query('INSERT INTO `test` (`id`, `f`) VALUES(1, 1)');
	test();
}
go();
