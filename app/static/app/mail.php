<?php
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];
$formcontent=" From: $name \n subject: $subject \n Message: $message";
$recipient = "alfred.miller@yandex.ru";
$subject = "Add Your Subject Here";
$mailheader = "From: $email \r\n";
mail($recipient, $subject, $formcontent, $mailheader) or die("Error!");
header("location: app/static/app/templates/thank-you.html")
?>
