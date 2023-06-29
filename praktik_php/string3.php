<!DOCTYPE html>
<html>
    <head>
        <title>String_3</title>
    </head>
    <body>
        <?php
            $rawString="Welcome Birmingham Parent. Your replacement is a pleasure to have!";
            
            $malstr=str_replace("replacement", "son",$rawString);
            $femalstr=str_replace("replacement", "daughter",$rawString);

            echo "Son: ".$malstr."<br>";
            echo "Daughter: ".$femalstr."<br>";

        ?>
    </body>
</html>