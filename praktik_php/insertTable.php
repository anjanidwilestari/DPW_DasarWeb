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
    //values (3,'bolpoin', 1000), values (4,'penghapus', 2000) "

    $sql="insert into product (id, product_name, harga)
            values (4,'penghapus', 2000)";  

    if(mysqli_query($connect, $sql)){
        echo "Data berhasil ditambahkan";
    }
    else {
        echo "Data gagal ditambahkan<br>".mysqli_error($connect);
    }
    mysqli_close($connect);
?>