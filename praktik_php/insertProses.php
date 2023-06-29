<?php
    include "koneksi.php";
    $id=$_GET['id'];
    $nama=$_GET['name'];
    $harga=$_GET['price'];

    $sql="INSERT INTO product (id, product_name, harga)
            VALUES('$id','$nama','$harga')";

    if(mysqli_query($connect, $sql)){
        echo "Data berhasil ditambahkan";
    }
    else {
        echo "Data gagal ditambahkan<br>".mysqli_error($connect);
    }
    mysqli_close($connect);
?>