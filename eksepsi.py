try :
    bil1 = int(input("Masukkan bilangan pertama : "))
    bil2 = int(input("Masukkan bilangan kedua : "))
except ValueError :
    print("Nilai harus bertipe number")
else :
    hasil = bil1 + bil2
    print("Hasil Penjumlahan : ", hasil)
finally:
    print("Akhir dari sebuah program penjumlahan")
    print("ini adalah contoh eksepsi")
