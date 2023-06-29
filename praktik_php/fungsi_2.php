<!DOCTYPE html>
<html>
    <head>
        <title>Fungsi_2</title>
    </head>
    <body>
        <h2>Fungsi</h2>
        <?php
            function familyName($fname, $year){
                echo "$fname Refsnes. Born in $year <br>";
            }
            familyName("Hege","1975");
            familyName("Stale","1978");
            familyName("Kai Jim","1983");
        ?>
    </body>
</html>