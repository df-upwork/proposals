<?php

$db = new mysqli();
$db->real_connect(hostname:'localhost',password:null, username: 'test', database:'test');

$s = $db->prepare("DROP TABLE IF EXISTS test"); $s->execute();
$s = $db->prepare("CREATE TABLE `test` ( `id` int NOT NULL, `f` int NOT NULL, PRIMARY KEY (`id`)) ENGINE=MEMORY"); $s->execute();
$s = $db->prepare("INSERT INTO `test` (`id`, `f`) VALUES(1, 1)"); $s->execute();
for($i=0; $i<10; $i++) {
	$startTime = microtime(true)*1000;
	$s = $db->prepare("UPDATE test SET f=1 WHERE id=1"); $s->execute();
	//$s = $db->prepare("SELECT 1"); $s->execute(); $s->free_result();
	$MS = microtime(true)*1000-$startTime;
	echo "$MS\n";
	usleep(250*1000);
}
