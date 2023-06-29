def turun(b,a,x):
    if(x<=a):
        nilai = 1
    elif(x>a and x<b):
        nilai = (b-x)/(b-a)
    elif(x>=b):
        nilai = 0

    return nilai

def naik(b,a,x):
    if(x<=a):
        nilai = 0
    elif(x>a and x<b):
        nilai = (x-a)/(b-a)
    elif(x>=b):
        nilai = 1

    return nilai

def agregasi_turun(b,a,alfa):
    nilai = b - (alfa*(b-a))
    return nilai

def agregasi_naik(b,a,alfa):
    nilai = alfa*(b-a) + a
    return nilai

var = int(input("Jumlah variabel: "))

nama_var = []
for i in range(var):
    nama = input("Sebutkan nama variabel: ")
    nama_var.append(nama)

    
variabel = dict()
for i in nama_var:
    print(i)
    up = int(input("naik : "))
    down = int(input("turun : "))
    variabel.update({i+"_naik":up})
    variabel.update({i+"_turun":down})
    
print(variabel)

soal = dict()

jml = int(input("Jumlah variabel yang diketahui : "))

for i in range(jml):
    ver = input("Nama variabel : ")
    val = int(input("Nilai : "))   
    soal.update({ver:val})
    
print(soal)

dit = input("Variabel yang ditanyakan : ")

nk = dict()
for i in soal:
    up = naik(variabel[i+"_naik"],variabel[i+"_turun"],soal[i])
    down = turun(variabel[i+"_naik"],variabel[i+"_turun"],soal[i])
    nk.update({i+"_naik":up})
    nk.update({i+"_turun":down})

print(nk)

#AGREGASI
alfa = []
z = []
zz= agregasi_naik, agregasi_turun
r = int(input("Masukkan jumlah peraturan : "))

for i in range(r):
    kondisi1 = input("Kondisi 1(naik/turun): ")
    kondisi2 = input("Kondisi 2(naik/turun): ")
    kesimpulan = input("Kesimpulan(naik/turun): ")
    #Fire Strength INTERSEKSI (AND)
    a = min(nk[kondisi1],nk[kondisi2]) 
    alfa.append(a)
    if(kesimpulan == "turun"):
        zz = agregasi_turun(variabel[dit+"_naik"],variabel[dit+"_turun"],a)
    elif(kesimpulan == "naik"):
        zz = agregasi_naik(variabel[dit+"_naik"],variabel[dit+"_turun"],a)        
    z.append(zz)
    
print(alfa)
print(z)
4
#DEFUZIFIKASI
df = 0

for i in range(len(alfa)):
    df += alfa[i]*z[i]

defuz = float(df/sum(alfa))

print("Jadi, nilai ",dit," adalah ",defuz)