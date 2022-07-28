## Tugas 4 - Library Management Sederhana

Tujuan: Membuat library management sederhana dengan beberapa fungsi yang bisa dilakukan yaitu:

1. Pendaftaran User Baru
2. Pendaftaran Buku Baru
3. Peminjaman Buku
4. Pengembalian Buku
5. Melihat User Perpustakaan
6. Melihat Koleksi Buku
7. Melihat Daftar Peminjaman Buku
8. Cari Buku
9. Keluar

Langkah-langkah:
1. Dengan MySQL Workbench, buat database (CREATE DATABASE) dan tabel-tabel yang diperlukan (CREATE TABLE - datauser, databuku, datapinjaman) termasuk kolom-kolom yang sesuai (id_user, id_buku, nama user, judul buku, tanggal pinjam/kembali, dsb). id_user dan id_buku dibuat agar otomatis input value angka (AUTO_INCREMENT)
2. Buat file python (.py) dan import library-library berikut: mysql.connector, pandas, datetime. Hubungkan python dengan MySQL
3. Buat fungsi-fungsi untuk menampilkan menu utama dan fungsi-fungsi program library:
    - Menu utama: while loop yang akan menampilkan menu fungsi-fungsi library dan input dari user untuk memilih fungsi yang akan dijalankan. Jika user memilih fungsi 9 maka program akan selesai
    - Pendaftaran user baru: input identitas user (nama, tanggal lahir, pekerjaan, alamat), buat dan jalankan query INSERT INTO datauser
    - Pendaftaran buku baru: input identitas buku (judul buku, kategori, stock), buat dan jalankan query INSERT INTO databuku
    - Peminjaman buku: input user dan buku yang akan dipinjam, tanggal pinjam (datetime.date.today) dan tanggal kembali (datetime.timedelta) otomatis akan dibuat sesuai dengan tanggal peminjaman dan masa pinjam 4 hari. Buat dan jalankan query INSERT INTO datapinjaman. Buat dan jalankan query UPDATE databuku untuk mengurangi stock buku yang dipinjam
    - Pengembalian buku: input user dan buku yang akan dikembalikan, buat dan jalankan query DELETE FROM datapinjaman sesuai buku yang dikembalikan. Buat dan jalankan query UPDATE databuku untuk menambah stock buku yang dikembalikan
    - Melihat user perpustakaan/koleksi buku/daftar peminjaman buku: buat dan jalankan query SELECT * FROM datauser/databuku/datapinjaman dan tampilkan hasil query dengan fungsi dari pandas
    - Cari buku: input judul buku yang ingin dicari, buat dan jalankan query SELECT * FROM databuku sesuai dengan judul buku yang dicari dan tampilkan hasil query dengan fungsi dari pandas
4. Jalankan fungsi menu utama

Menjalankan program:
1. Gunakan MySQL Workbench dan buat database dan tabel-tabel yang dibutuhkan dengan menjalankan file LMS_SQL.sql
2. Jalankan lms.py (ketik "python ./lms.py") pada terminal (pastikan telah berada di lokasi file yang akan dijalankan) dan tekan Enter
3. Program akan menghubungkan python dengan MySQL dan kemudian menjalankan program library management
4. Silahkan pilih fungsi yang ingin dijalankan. Jika sudah selesai maka dapat memilih fungsi 9 untuk keluar program

Saran perbaikan:
Sebaiknya tugas 4 tidak terlalu signifikan perbedaan kesulitannya dibandingkan tugas-tugas sebelumnya. Berikan penjelasan tugas yang lebih membantu student untuk mendapat gambaran langkah-langkah yang perlu dilakukan dan beberapa hal teknis yang belum dipelajari sebelumnya.
