<html>
<head>
    <title>Get Form</title>
</head>
<body>
    <?php
        if(isset($_GET["myname"]) AND isset($_GET["myaddress"]))
        {
            echo "Selamat Datang ".$_GET["myname"] ."!!<br>";
            echo "Dari ".$_GET["myaddress"];
        }
        else{
            echo "Anda harus mengakses halaman ini dari form_1.html";
        }
    ?>
</body>
</html>