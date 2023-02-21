dataSiswa = []
kondisi = True

while kondisi:
    print(50*"=")
    print("Menu Program Data Siswa")
    print(50*"=")
    print("1. Tambah data siswa")
    print("2. Tampilkan data siswa")
    print("3. Hapus data siswa")
    print("0. Keluar")
    print(50*"=")
    pilihan = int(input("Masukkan Pilihan kamu:"))

    if pilihan == 1:
        nis = str(input("masukkan Nis:"))
        nama = str(input("masukkan nama siswa:"))
        asal = str(input("masukkan asal:"))

        dataSiswa.append({"nis":nis,
                        "nama":nama,
                        "asal":asal})

    elif pilihan == 2:

        for siswa in dataSiswa:
            print(siswa["nis"], '\t', siswa["nama"],'\t', siswa["asal"])
    elif pilihan == 3:
        
        for siswa in dataSiswa:
           del dataSiswa[int(callable(input("\Masukkan NIS")))]
           break
    elif pilihan == 0:
        kondisi:False
        exit()
    else :
        print("pilihan yang anda masukkan salah")



