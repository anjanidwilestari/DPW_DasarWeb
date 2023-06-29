<html>
<head>
</head>
<body>
    <?php
        $myFile="testFile.txt";
        $fh= fopen($myFile, 'r');
        $theData=fgets($fh);
        fclose($fh);
        echo $theData;
    ?>
</body>
</html>