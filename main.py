from data import lab6

print("PROGRAM MENAMPILKAN DAFATR NILAI MAHASISWA")
while True:
    print("")
    c =input("(L)lihat, (T)ambah, (U)bah, (H)apus, (K)eluar : ")
    if c.lower() == 't':
        lab6.tambah()

    elif c.lower() == 'u':
        lab6.ubah()

    elif c.lower() == 'l':
        lab6.lihat()

    elif c.lower() == 'h':
        lab6.hapus()

    elif c.lower() == 'k':
        print("Keluar")
        break
