# Membuat program Kelulusan
# oleh Beni Oktopiansah

nilai_teori = int(input("Berapa nilai ujian teori : "))
nilai_praktek = int(input("Berapa nilai ujian praktek : "))

if nilai_teori >= int(70) and nilai_praktek >= int(70):
    print("Selamat, Anda Lulus")
elif nilai_teori >= int(70) and nilai_praktek < int(70):
    print("Anda harus mengulang ujian praktek")

elif nilai_teori < int(70) and nilai_praktek >= int(70):
    print("Anda harus Mengulang Ujian Teori")    

else:
    print("Anda harus mengulang ujian teori dan praktek")

#Terima kasih