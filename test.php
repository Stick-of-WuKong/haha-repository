<?php

$file = "sth -or -exec cat /etc/passwd '; -quit"; #（多个参数）
print_r("find /tmp -iname " . escapeshellarg($file));
?>