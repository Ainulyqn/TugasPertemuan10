# Nama : Ainul Yaqin <br>
# NIM : 312010423 <br>
# Kelas : TI.20.A.1

# **Lab6**

![Gambar](Poto/gambar1.png) <br>
Pada tugas LAB 6, saya diminta untuk membuat sebuah program menambahkan data ke sebuah list dengan sistem library root yang nantinya akan seperti ini. <br>

# Berikut Adalah Inputnya

`from data import data`



`print("PROGRAM MENAMPILKAN DAFATR NILAI MAHASISWA")` <br>
`while True:` <br>
`    print("")` <br>
`    c =input("(L)lihat, (T)ambah, (U)bah, (H)apus, (K)eluar : ")` <br>
`    if c.lower() == 't':` <br>
`        print("=======Tambah Data=======")` <br>
`        nama = input("Nama                :  ")` <br>
`        nim = input("Nim                 :  ")` <br>
`        tugas = int(input("Masukan Nilai Tugas :  "))` <br>
`        uts = int(input("Masukan Nilai UTS   :  "))` <br>
`        uas = int(input("Masukan Nilai UAS   :  "))` <br>
`        akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)` <br>
`        data[nama] = nim, tugas, uts, uas, akhir` <br>
`    elif c.lower() == 'u':` <br>
`        print('=======Ubah Data Mahasiswa=======')` <br>
`        nama = input('Nama                :  ')` <br>
`        if nama in data.keys():` <br>
`            nim = input('Nim                 :  ')` <br>
`            tugas = int(input("Masukan Nilai Tugas :  "))` <br>
`            uts = int(input("Masukan Nilai UTS   :  "))` <br>
`            uas = int(input("Masukan Nilai UAS   :  "))` <br>
`            akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)` <br>
`            data[nama] = nim, tugas, uts, uas, akhir` <br>
`        else:` <br>
`            print("Data Nilai Tidak Ada".format(nama))` <br>

`    elif c.lower() == 'l':` <br>
`        print("=======Daftar Nilai Mahasiswa=======")` <br>
`        print("================================================================================================")` <br>
`        print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")` <br>
`        print("================================================================================================")` <br>
`        i = 0` <br>
`        for x in data.items():` <br>
`            i += 1` <br>
`            print(` <br>
`                " | {6:2}  |  {0:12s} | {1:9s} | {2:11}  | {3:11} | {4:11}  |  {5:11} |".format(x[0], x[1][0], x[1][1],` <br>
`                                                                                                x[1][2], x[1][3],` <br>
`                                                                                                x[1][4], i))` <br>
`            print("============================================================================================")` <br>

`    elif c.lower() == 'h':` <br>
`        print("=======Hapus Data Mahasiswa=======")` <br>
`        nama = input("Nama :  ")` <br>
`        if nama in data.keys():` <br>
`            del data[nama]` <br>
`        else:` <br>
`            print("Data Nilai Tidak Ada".format(nama))` <br>

`    elif c.lower() == 'k':` <br>
`        print("Keluar")` <br>
`        break` <br>

Dan Setelah Kita Menemukan Hasil Nya Mari Saya Jelaskan Perinciannya

* Langkah pertama yang harus kita lakukan adalah membuat variabel lis kosong. <br>
`from data import data`

* Setelah itu kita membuat kondisi perulangan dan statement yang akan dijalankan ketika perulangan terjadi. berikut intputnya: <br>
`print("PROGRAM MENAMPILKAN DAFATR NILAI MAHASISWA")` <br>
`while True:` <br>
`    print("")` <br>
`    c =input("(L)lihat, (T)ambah, (U)bah, (H)apus, (K)eluar : ")`

*  Berikutnya tambahkan inputan Fungsi Tambahkan <br>
`if c.lower() == 't':` <br>
`print("=======Tambah Data=======")` <br>
`        nama = input("Nama                :  ")` <br>
`        nim = input("Nim                 :  ")` <br>
`        tugas = int(input("Masukan Nilai Tugas :  "))` <br>
`        uts = int(input("Masukan Nilai UTS   :  "))` <br>
`        uas = int(input("Masukan Nilai UAS   :  "))` <br>
`        akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)` <br>
`        data[nama] = nim, tugas, uts, uas, akhir`

* Tambahkan inputan Fungsi Ubah <br>
`elif c.lower() == 'u':` <br>
`print('=======Ubah Data Mahasiswa=======')` <br>
`        nama = input('Nama                :  ')` <br>
`        if nama in data.keys():` <br>
`            nim = input('Nim                 :  ')` <br>
`            tugas = int(input("Masukan Nilai Tugas :  "))` <br>
`            uts = int(input("Masukan Nilai UTS   :  "))` <br>
`            uas = int(input("Masukan Nilai UAS   :  "))` <br>
`            akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)` <br>
`            data[nama] = nim, tugas, uts, uas, akhir` <br>
`        else:` <br>
`            print("Data Nilai Tidak Ada".format(nama))` 

* Tambahkan inputan Fungsi Tampilkan <br>
`elif c.lower() == 'l':` <br>
` print("=======Daftar Nilai Mahasiswa=======")` <br>
`        print("================================================================================================")` <br>
`        print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")` <br>
`        print("================================================================================================")` <br>
`        i = 0` <br>
`        for x in data.items():` <br>
`            i += 1` <br>
`            print(` <br>
`                " | {6:2}  |  {0:12s} | {1:9s} | {2:11}  | {3:11} | {4:11}  |  {5:11} |".format(x[0], x[1][0], x[1][1],` <br>
`                                                                                                x[1][2], x[1][3],` <br>
`                                                                                                x[1][4], i))` <br>
`            print("============================================================================================")`

* Tambahkan inputan Fungsi Hapus <br>
`elif c.lower() == 'h':` <br>
`print("=======Hapus Data Mahasiswa=======")` <br>
`        nama = input("Nama :  ")` <br>
`        if nama in data.keys():` <br>
`            del data[nama]` <br>
`        else:` <br>
`            print("Data Nilai Tidak Ada".format(nama))`

* Tambahkan inputan Fungsi Keluar <br>
`elif c.lower() == 'k':` <br>
`print("Keluar")` <br>
`        break`

# Berikut ini adalah Outputnya :
![Gambar](Poto/gambar2.png)