import mysql.connector
from mysql.connector import Error
import pandas as pd
import datetime

host_name = "localhost"
user = "root"
password = "root"
db = "lms_tugas4"
myconn = mysql.connector.connect(host = host_name, user = user, passwd = password)
mydb = mysql.connector.connect(host=host_name, user=user, passwd=password, database=db)
mycursor = mydb.cursor(buffered=True)

if mydb:
    print("Berhasil terhubung dengan database "+db+"!")


def main_menu():
    finished = False
    while not finished:
        menu = """
        ..........Perpustakaan Pacmann..........

        Pilih menu:
            1. Pendaftaran User Baru
            2. Pendaftaran Buku Baru
            3. Peminjaman Buku
            4. Pengembalian Buku
            5. Melihat User Perpustakaan
            6. Melihat Koleksi Buku
            7. Melihat Daftar Peminjaman Buku
            8. Cari Buku
            9. Keluar
        """
        print(menu)

        menu_choice = int(input("Silahkan pilih menu: "))
        if menu_choice == 1:
            pendaftaran_user_baru()

        elif menu_choice == 2:
            pendaftaran_buku_baru()

        elif menu_choice == 3:
            peminjaman_buku()

        elif menu_choice == 4:
            pengembalian_buku()

        elif menu_choice == 5:
            melihat_user_perpustakaan()

        elif menu_choice == 6:
            melihat_koleksi_buku()

        elif menu_choice == 7:
            melihat_daftar_peminjaman_buku()

        elif menu_choice == 8:
            cari_buku()

        elif menu_choice == 9:
            finished = True
            print("Terima kasih!")


def pendaftaran_user_baru(): # menu 1
    print("..............................")
    nama = input("Masukkan nama: ")
    tanggal_lahir = input("Masukkan tanggal lahir (YYYY-MM-DD): ")
    pekerjaan = input("Masukkan pekerjaan: ")
    alamat = input("Masukkan alamat: ")

    query_pendaftaran_user_baru = "INSERT INTO datauser VALUES (NULL, %s, %s, %s, %s)"
    mycursor.execute(query_pendaftaran_user_baru, (nama, tanggal_lahir, pekerjaan, alamat))
    mydb.commit()
    print(nama + " berhasil didaftarkan!")
    print("..............................")


def pendaftaran_buku_baru(): # menu 2
    print("..............................")
    judul_buku = input("Masukkan judul buku: ")
    kategori = input("Masukkan kategori: ")
    stock = input("Masukkan stock: ")

    query_pendaftaran_buku_baru = "INSERT INTO databuku VALUES (NULL, %s, %s, %s)"
    mycursor.execute(query_pendaftaran_buku_baru, (judul_buku, kategori, stock))
    mydb.commit()
    print(judul_buku + " berhasil didaftarkan!")
    print("..............................")


def peminjaman_buku(): # menu 3
    print("..............................")
    id_user = input("Masukkan id user: ")
    id_buku = input("Masukkan id buku: ")
    nama = input("Masukkan nama: ")
    judul_buku = input("Masukkan judul buku: ")
    tanggal_pinjam = datetime.date.today()
    tanggal_kembali = tanggal_pinjam + datetime.timedelta(days=4)

    query_peminjaman_buku = "INSERT INTO datapinjaman VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(query_peminjaman_buku, (id_user, id_buku, nama, judul_buku, tanggal_pinjam, tanggal_kembali))

    query_pengurangan_stock = "UPDATE databuku SET stock = stock - 1  WHERE id_buku = (%s)"
    mycursor.execute(query_pengurangan_stock, ([id_buku]))

    mydb.commit()

    print(judul_buku + " dipinjamkan ke " + nama)
    print("..............................")


def pengembalian_buku(): # menu 4
    print("..............................")
    id_user = input("Masukkan id user: ")
    id_buku = input("Masukkan id buku: ")

    query_pengembalian_buku = "DELETE FROM datapinjaman WHERE id_buku = (%s)"
    mycursor.execute(query_pengembalian_buku, ([id_buku]))

    query_penambahan_stock = "UPDATE databuku SET stock = stock + 1  WHERE id_buku = (%s)"
    mycursor.execute(query_penambahan_stock, ([id_buku]))

    mydb.commit()

    print("Buku telah dikembalikan")
    print("..............................")


def melihat_user_perpustakaan(): # menu 5
    print("..............................")
    query_melihat_user_perpustakaan = "SELECT * FROM datauser"
    mycursor.execute(query_melihat_user_perpustakaan)
    columns = [description[0] for description in mycursor.description]

    result = mycursor.fetchall()
    df = pd.DataFrame(result)
    df.columns = columns
    print(df)
    print("..............................")


def melihat_koleksi_buku(): # menu 6
    print("..............................")
    query_melihat_koleksi_buku = "SELECT * FROM databuku"
    mycursor.execute(query_melihat_koleksi_buku)
    columns = [description[0] for description in mycursor.description]

    result = mycursor.fetchall()
    df = pd.DataFrame(result)
    df.columns = columns
    print(df)
    print("..............................")


def melihat_daftar_peminjaman_buku(): # menu 7
    print("..............................")
    query_melihat_daftar_peminjaman_buku = "SELECT * FROM datapinjaman"
    mycursor.execute(query_melihat_daftar_peminjaman_buku)
    columns = [description[0] for description in mycursor.description]

    result = mycursor.fetchall()
    df = pd.DataFrame(result)
    df.columns = columns
    print(df)
    print("..............................")


def cari_buku(): # menu 8
    print("..............................")
    judul_buku = input("Masukkan judul buku: ")

    query_cari_buku = "SELECT * FROM databuku WHERE judul_buku = (%s)"
    mycursor.execute(query_cari_buku, [judul_buku])
    columns = [description[0] for description in mycursor.description]

    result = mycursor.fetchall()
    df = pd.DataFrame(result)
    df.columns = columns
    print(df)
    print("..............................")


main_menu()