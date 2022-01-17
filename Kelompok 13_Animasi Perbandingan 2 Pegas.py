from vpython import *
from tkinter.filedialog import asksaveasfilename
print("==========SIMULASI PEGAS==========")
print("..................................\n")
aa=input("Massa Pegas: ")
#Atur massa balok
mblock =float(aa)
single_mblock=float(aa)


#Atur Konstanta pegas
ks =  15 
ks = 2*ks
single_ks=15

#panjang awal pegas dan posisi awal pegas
L0 =       0.3   
Lstarty =  -2.0

#daftar gravitasi planet
planet=["merkurius", "venus", "bumi", "mars","Jupiter", "Saturnus", "Uranus", "Neptunus", "Bulan"]
planet_grav=[3.7, 8.87, 9.8, 3.721, 24.79, 10.44, 8.87, 11.15, 1.62]

print("Nama Planet      Gravitasi \n")
for i in range (9):
  print(i+1, ". %-15s %5.3f" % (planet[i], planet_grav[i]))
inp_planet=input("Pilih gravitasi yang digunakan: ")
inp_planet=int(inp_planet)
if inp_planet==1:
  g=planet_grav[0]
elif inp_planet==2:
  g=planet_grav[1]
elif inp_planet==3:
  g=planet_grav[2]
elif inp_planet==4:
  g=planet_grav[3]
elif inp_planet==5:
  g=planet_grav[4]
elif inp_planet==6:
  g=planet_grav[5]
elif inp_planet==7:
  g=planet_grav[6]
elif inp_planet==8:
  g=planet_grav[7]
elif inp_planet==9:
  g=planet_grav[8]
else:
  print("Pilih sesuai pilihan, Gravitasi yang digunakan Bumi")
  g=planet_grav[2]

#bantuan looping
deltat = 0.01
t = 0

#penggambaran object
#Pegas ganda
ceiling = box(pos=vec(0,0,0), length = 5, height = 0.01, width = 0.2)
block = box(pos = vector(0,Lstarty,0),size = vec(1,0.1,0.1), color = color.red)
spring = helix(pos= vec(-0.3,0,0), axis = block.pos, radius = .03, thickness = 0.008, coils = 30, color = color.yellow)
spring2 = helix(pos= vec(0.3,0,0), axis = block.pos, radius = .03, thickness = 0.008, coils = 30, color = color.yellow)
#Pegas Tunggal
single_block = box(pos = vector(2,Lstarty,0),size = vec(0.5,0.1,0.1), color = color.red)
min=single_block.pos-vec(2,0,0)
single_spring = helix(pos= vec(2,0,0), axis = min, radius = .03, thickness = 0.008, coils = 30, color = color.green)


#menghitung momentum block
pblock = mblock*vector(0,0,0)
psingle_block=single_mblock*vector(0,0,0)
#menghitung gaya gravitasi
Fgrav =  mblock*vector(0,-g,0)
Fgrav2=  mblock*vector(0,-g,0)
deltapanjang=mag(block.pos)-L0

while t < 5:
    rate(20) #jumlah loop yang dilakuakn dalam 1 detik
    L = block.pos
    L2 = min
    Lhat = norm(L) #norm mengubah menjadi vektor satuan, vektornya panjangnya bernilai 1 satuan
    Lhat2=norm(L2)
    s=mag(L)-L0 #mag adalah nilai mutlak, pertambahan panjang, mag l artinya besaran dari vector l dengan rumus akar dari x kuadrat, y kuadrat, z kuadrat
    s2=mag(L2)-L0
    Fspring=-ks*s*Lhat #or Lhat = L/mag(L)
    Fsingle_spring=-single_ks*s2*Lhat2
    Fnet = Fspring + Fgrav         
    Fsingle_net=Fsingle_spring+Fgrav2
    #if t == 0:
    #    print(Fnet)
    
    pblock = pblock + Fnet*deltat  #hitung pbenda
    block.pos = block.pos + (pblock/mblock)*deltat  #perbarui posisi
    spring.axis=block.pos
    spring2.axis=block.pos
    
    
    psingle_block=psingle_block+Fsingle_net*deltat
    single_block.pos=single_block.pos+(psingle_block/single_mblock)*deltat
    min=single_block.pos-vec(2,0,0)    
    single_spring.axis=min
    
    t = t + deltat

gaya=-ks*mblock*deltapanjang
gaya2=-single_ks*mblock*deltapanjang

info_massa= "massa: " + str(mblock)
info_koef="koefisien pegas: " +str(single_ks)
info_pertpanjang="Pertambahan Panjang: "+str(deltapanjang)
info_gaya="gaya pada pegas berganda:" +str(gaya)
info_gaya2="gaya pada pegas tunggal:" +str(gaya2)
information=[info_massa, info_koef, info_pertpanjang, info_gaya, info_gaya2]

tipeFile = [('Text file', '*.txt'), ('All files', '.*')]
out=asksaveasfilename(filetypes=tipeFile)
# buka file untuk ditulis
file_bio = open(out, "w")
# tulis teks ke file
file_bio.write(('\n').join(information))
# tutup file
file_bio.close()


    


#if bisa dimanfaatkan untuk mengukur apakah gaya termasuk besar atau tidak
#luaran terformat dan sttring mengatur posisi anu itu
#tabel coba dimanfaatkan untuk mengukur ketinggian dari pegas itu sendiri

#kurangan: luaran terformat, if, if3, tabel