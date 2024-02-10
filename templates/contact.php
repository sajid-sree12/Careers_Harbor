<?php
if($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $subject = "Contact: Contact Form Submission"
    $message = $_POST['message'];

    $to = "dsajid942@gmail.com";

    $email_body = "Name: $name\nEmail: $email\n\n$message";

    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "CC: $email\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/plain; charset=utf-8\r\n";
    $headers .= "X-Priority: 1\r\n";

    mail($to, $subject, $email_body, $headers);

    header("Location: thank-you.html");
    exit;
}

?>