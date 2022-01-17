# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
murid = 6
nilai = 4
daftar = [
['izza', 90, 85, 75, 80],
['zain', 75, 80, 85, 80],
['za', 80, 90, 85, 70],
['za',85, 70, 90, 90],
['na', 85, 75, 90, 85],
['ni', 70, 85, 80, 75]
]

for i in range(murid):
    print(daftar[i])



tabel = []
nbaris = 5
nkolom = 5
for i in range(100) :
 baris = [i+1] * nkolom
 tabel.append(baris)
print(tabel)

A12={"nama":"ida", 'umur':21}
B12={"nama":"Andi", 'umur':21}
daftar=[A12, B12]

nama_matkul=['Matematika', 'Bahasa Indonesia', 'Bahasa Inggris', 'Ipa']     
nama=input("Masukkan Nama Siswa: ")
data_nilai=[]
data_nilai.append(nama)
for i in nama_matkul:
    nilai=input("Masukkan Nilai "+ i + ": ")
    data_nilai.append(nilai)
print(data_nilai)

nilai_kelas.append(data_nilai)
print(nilai_kelas)
'''

uname="admin"
password="admin"
nilai_kelas=[
['Adi', 90, 85, 75, 80],
['Ida', 75, 80, 85, 80],
['Uda', 80, 90, 85, 70],
['Edi', 85, 70, 90, 90],
['Adu', 85, 75, 90, 85],
['Dau', 70, 85, 80, 75]
    ]
nama_matkul=['Matematika', 'Bahasa Indonesia', 'Bahasa Inggris', 'Ipa']
print("PROGRAM INPUT-TAMPILKAN NILAI")
print("-----------------------------")
print()
print("-----Login Sebelum Melanjutkan-----")
login_uname=input("Masukkan Userame: ")
login_password=input("Masukkan Password: ")

if(uname==login_uname):
    if(password==login_password):

        print("Login Sukses")
        print("SELAMAT DATANG ADMIN")
        print("---------MENU---------")
        print("1. Menampilkan Nilai")
        print("2. Menambahkan Nilai")
        print("3. Cek Tugas")
        menu=input('Pilih Menu yang ingin diakses (masukkan angka): ')
        menu=int(menu)
        if(menu==1):
            print(nilai_kelas)
        elif(menu==2):   
            ask=input("Apakah anda ingin menambah data? (y/n) :")
            if(ask=="y"):
                masukan=1
            else:
                masukan=0
            while(masukan==1):
                
                nama=input("Masukkan Nama Siswa: ")
                data_nilai=[]
                data_nilai.append(nama)
                for i in nama_matkul:
                    nilai=input("Masukkan Nilai "+ i + ": ")
                    data_nilai.append(nilai)
                print('-------')
                
                nilai_kelas.append(data_nilai)
                ask=input("Apakah anda ingin menambah data? (y/n) : ")
                if(ask=="y"):
                    masukan=1
                else:
                   masukan=0
                   
        elif(menu==3):
            nama_file = input('Masukkan Nama File dan ektensi = ')
            file_masukan = open(nama_file, 'r')
            data = file_masukan.read()
            print(data)
        else:
             print("TERIMA KASIH TELAH MENGAKSES")
            
        


    else:
        print("----------PASSWORD SALAH----------")
else:
    print("Username Tidak Terdaftar")







