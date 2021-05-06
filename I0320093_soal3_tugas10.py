print("=======PROGRAM INPUT BIODATA=======")
print("")

Nama = input("Nama : ")
NIM = input("NIM : ")
Usia = input("Usia : ")
Asal = input("Asal : ")
Prodi = input("Program Studi : ")
Angkatan = input("Angkatan : ")

teks = "\n\nNama : {}\nNIM : {}\nUsia : {}\nAsal : {}\nProdi : {}\nAngkatan : {}"\
    .format(Nama,NIM,Usia,Asal,Prodi,Angkatan)

file_biodata = open("inputbiodata.txt","a")

file_biodata.write(teks)

file_biodata.close()
