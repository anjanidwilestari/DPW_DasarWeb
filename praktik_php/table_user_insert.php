<?php
    $hostname="localhost";
    $surename="root";
    $password="";
    $database="prakwebdb";
    $connect=mysqli_connect($hostname,$surename,$password,$database);
    
    if($connect){
        echo "Koneksi ke MySQL berhasil<br>";
    }
    else {
        echo "Koneksi ke MySQL gagal<br>".mysqli_connect_error();
    }

    $sql="insert into user (id, username, password)
            values (1,'admin', md5(123))"; 


    if(mysqli_query($connect, $sql)){
        echo "Data berhasil ditambahkan";
    }
    else {
        echo "Data gagal ditambahkan<br>".mysqli_error($connect);
    }
    mysqli_close($connect);
?>