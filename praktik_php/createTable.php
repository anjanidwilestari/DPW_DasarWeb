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
    $sql="CREATE TABLE product(
        id INT PRIMARY KEY,
        product_name varchar (30) not null,
        harga int not null)";

    if(mysqli_query($connect, $sql)){
        echo "Table Product berhasil dibuat<br>";
    }
    else {
        echo "Table Product gagal dibuat<br>".mysqli_error($connect);
    }
    mysqli_close($connect);
?>