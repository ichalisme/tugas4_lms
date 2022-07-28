CREATE DATABASE lms_tugas4;
USE lms_tugas4;

CREATE TABLE datauser(
	id_user INT PRIMARY KEY AUTO_INCREMENT,
    nama VARCHAR(50),
    tanggal_lahir DATE,
    pekerjaan VARCHAR(50),
    alamat VARCHAR(50)
);

CREATE TABLE databuku(
	id_buku INT PRIMARY KEY AUTO_INCREMENT,
    judul_buku VARCHAR(50),
    kategori VARCHAR(50),
    stock INT
);

ALTER TABLE databuku AUTO_INCREMENT = 100;

CREATE TABLE datapinjaman(
	id_user INT,
    id_buku INT,
    nama VARCHAR(50),
    judul_buku VARCHAR(50),
    tanggal_pinjam DATE,
    tanggal_kembali DATE,
    FOREIGN KEY (id_user) REFERENCES datauser(id_user),
    FOREIGN KEY (id_buku) REFERENCES databuku(id_buku)
);