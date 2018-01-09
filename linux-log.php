<?php
// SERVER
$date = date('Y-m-d_H:i:s');

if(getenv('REQUEST_METHOD') == 'POST') {


	$client_data = file_get_contents("php://input");
	// echo "$client_data";
	$client_ip = get_client_ip();

	$push = $client_data . "\n" . $date;
	$log = "linux-log/" . $date . "_" . $client_ip;
	// echo $log;
	// $ret = file_put_contents($log, $push);

	// $my_file = 'file.txt';
	// $data = 'This is the data';
	$handle = fopen($log, 'w') or die('Cannot open file:  '.$log);
	fwrite($handle, $push);

	// $ret = file_put_contents($log, $push, FILE_APPEND | LOCK_EX);
	exit();
}



function get_client_ip() {
    $ipaddress = '';
    if (getenv('HTTP_CLIENT_IP'))
        $ipaddress = getenv('HTTP_CLIENT_IP');
    else if(getenv('HTTP_X_FORWARDED_FOR'))
        $ipaddress = getenv('HTTP_X_FORWARDED_FOR');
    else if(getenv('HTTP_X_FORWARDED'))
        $ipaddress = getenv('HTTP_X_FORWARDED');
    else if(getenv('HTTP_FORWARDED_FOR'))
        $ipaddress = getenv('HTTP_FORWARDED_FOR');
    else if(getenv('HTTP_FORWARDED'))
       $ipaddress = getenv('HTTP_FORWARDED');
    else if(getenv('REMOTE_ADDR'))
        $ipaddress = getenv('REMOTE_ADDR');
    else
        $ipaddress = 'UNKNOWN';
    return $ipaddress;
}

?>

