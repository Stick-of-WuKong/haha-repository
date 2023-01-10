<?php
	$xmlDoc = new DOMDocument();
$xmlDoc->load("note.xml");

$x = $xmlDoc->documentElement;
	foreach($x->childNodes AS $item){  //尝试循环$x->childNotes数组
            print($item->nodeName ."=".$item->nodeValue."<br />");
	}
?>