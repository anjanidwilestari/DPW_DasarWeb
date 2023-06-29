<?php
    $hostname="localhost";
    $surename="root";
    $password="";
    $connect=mysqli_connect($hostname,$surename,$password);
    
    if($connect){
        echo "Koneksi ke MySQL berhasil";
    }
    else {
        echo "Koneksi ke MySQL gagal".mysqli_connect(error);
    }
?>