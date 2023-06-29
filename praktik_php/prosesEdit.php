<?php
    include "koneksi.php";
    $id=$_GET['id'];
    $nama=$_GET['name'];
    $harga=$_GET['price'];
    $query="UPDATE product Set product_name='$nama', harga='$harga' where id='$id'";
    $result=mysqli_query($connect,$query);

    if($result){
        echo "Berhasil update data";
?>
    <a href="homeCRUD.php">Lihat data</a>
<?php
    }
    else {
        echo "Gagal update data".mysqli_error($connect);
    }
?>