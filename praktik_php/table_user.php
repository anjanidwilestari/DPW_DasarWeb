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
    $sql="CREATE TABLE user(
        id INT PRIMARY KEY,
        username varchar (50) not null,
        password varchar (50) not null)";

    if(mysqli_query($connect, $sql)){
        echo "Table User berhasil dibuat<br>";
    }
    else {
        echo "Table User gagal dibuat<br>".mysqli_error($connect);
    }
    mysqli_close($connect);
?>