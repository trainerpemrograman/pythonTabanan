# ini adalah contoh list
# warna = ["merah","kuning","hijau"] 
# buah = ["tomat","jeruk","apel"] 
# del warna[1]

# print(warna)

# for i in buah :
#     for j in warna:
#         print("Buah", i, "Berwarna", j)
   
# warna.append("biru")
# warna.insert(1,"pink")
# print(warna)
# print(warna[2])
# print(len(warna))


# ini adalah contoh tuple
# warna_tuple = ("merah","kuning","hijau")
# x = ("biru",)
# warna_tuple += x
# print(warna_tuple)

# ini adalah contoh set
# warna = {"Merah","Kuning","Hijau"}
# warna.add("Biru")
# print(warna)
# warna1 = set(warna)
# warna1.remove("Biru")
# print(warna1)

# ini adlaah contoh dictionary

dataSiswa = {
    "nama":"Gamelab",
    "alamat":"Salatiga",
    # "no_tlp":123456789,
    "kelas":["web","DevOps","Networking"]
}

dataSiswa["jurusan"] = "TKJ"
del dataSiswa["alamat"]
dataSiswa.update({"no_telp": 78797675})
dataSiswa.clear()
print(dataSiswa)


