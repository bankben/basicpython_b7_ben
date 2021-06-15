#Tugas 2  Soal 1 "menyimpan kontak dan juga menampilkan kontak-kontak"
# oleh Beni Oktopiansah

print("Selamat Datang")
print("----Menu----")
print("1 Daftar Kontak")
print("2 Tambah Kontak")
print("3 Keluar")

def fungsi_1():
    print("-" * 20)
    print("Daftar Kontak")
    print("-" * 20)
    print("Nama: Farhan")
    print("Telp: 081234567")
    print("-" * 20)
    print("Nama: Giffari")
    print("Telp: 05243128")
    print("-" * 20)

def fungsi_2():
    print("-" * 20)
    print("Tambah Kontak")
    print("-" * 20)
    nama = str(input("Masukkan Nama Kontak : "))
    telp = int(input("Masukkan Nomor Telepon : "))
    print("*" * 30)
    print("Kontak berhasil ditambahkan")
    print("*" * 30)

def fungsi_3():
    print("#" * 30)
    print("Program selesai, sampai jumpa!")
    print("#" * 30)

def fungsi_4():
    print("!" * 20)
    print("Menu tidak tersedia")
    print("!" * 20)


 
pilihan=int(input("Pilih Menu:"))
if pilihan==1:
    fungsi_1 ()
elif pilihan==2:
    fungsi_2 ()
elif pilihan==3:
    fungsi_3 ()
else:
    fungsi_4 ()

#Mohon koreksi jika ada coding yang salah atau kurang effisien
#terima kasih

