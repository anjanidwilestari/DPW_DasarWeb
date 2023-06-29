<?php
    $hostname="localhost";
    $surename="root";
    $password="";
    $connect=mysqli_connect($hostname,$surename,$password);
    
    if($connect){
        echo "Koneksi ke MySQL berhasil<br>";
    }
    else {
        echo "Koneksi ke MySQL gagal<br>".mysqli_connect(error);
    }
    $sql="CREATE DATABASE prakwebdb";
    if(mysqli_query($connect, $sql)){
        echo "Databse berhasil dibuat";
    }
    else {
        echo "Database gagal dibuat".mysqli_error($connect);
    }
    mysqli_close($connect);
?>