<?php
$sender = "From: support@paypal.com" . "\r\n" . "CC: someoneelse@gmail.com";
$receiver = "mijinyawajunaid@gmail.com";
$head = "Header";
$message = "Content";
if(mail($receiver, $head, $message, $sender))
{
    echo "success";
}else{
    echo "Couldn't complete operation";
}
?>