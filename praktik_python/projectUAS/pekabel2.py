def turun(b,a,x):
    if(x<=a):
        nilai = 1
    elif(x>=a and x<=b):
        nilai = (b-x)/(b-a)
    elif(x>=b):
        nilai = 0
    return nilai

def sedang(d,c,b,a,x):
    if(x<=a or x>=d):
        nilai = 0
    elif(x>=a and x<=b):
        nilai = (x-a)/(b-a)
    elif(x>=b and x<=c):
        nilai = 1
    elif(x>=c and x<=d):
        nilai = (d-x)/(d-c)
    return nilai

def naik(b,a,x):
    if(x<=a):
        nilai = 0
    elif(x>=a and x<=b):
        nilai = (x-a)/(b-a)
    elif(x>=b):
        nilai = 1
    return nilai

def agregasi_turun(c,b,a,alfa):
    nilai = c - (alfa*(c-b-a))
    return nilai

def agregasi_sedang(c,b,a,alfa):
    nilai = b - (alfa*(c-b-a)) + b
    return nilai

def agregasi_naik(c,b,a,alfa):
    nilai = alfa*(c-b-a) + a
    return nilai

var = 4

nama_var = ['kelembapan','ketebalan','umur','kelayakan']

    
variabel = dict()
for i in 'kelembapan', 'ketebalan', 'umur':
    print(i)
    up = 100
    middle = 70
    down = 45
    variabel.update({i+"_naik":up})
    variabel.update({i+"_sedang":middle})
    variabel.update({i+"_turun":down})
for i in 'kelayakan':
    print(i)
    up = 0
    down = 1
    variabel.update({i+"_naik":up})
    variabel.update({i+"_turun":down})

print(variabel)

soal = dict()

ver = 'kelembapan'
val = int(input("Kelembapan : "))
soal.update({ver:val})

ver = 'ketebalan'
val = int(input("Ketebalan : "))
soal.update({ver:val})

ver = 'umur'
val = int(input("Umur : "))   
soal.update({ver:val})
print(soal)

dit = 'kelayakan'

nk = dict()
for i in soal:
    up = naik(variabel[i+"_naik"],variabel[i+"_turun"],soal[i])
    middle = sedang(variabel[i+"_naik"],variabel[i+"_sedang"],variabel[i+"_sedang"],variabel[i+"_turun"],soal[i])
    down = turun(variabel[i+"_naik"],variabel[i+"_turun"],soal[i])
    nk.update({i+"_naik":up})
    nk.update({i+"_sedang":middle})
    nk.update({i+"_turun":down})

print(nk)

#AGREGASI
alfa = []
z = []
zz=agregasi_turun, agregasi_naik, agregasi_sedang
r = int(input("Masukkan jumlah peraturan : "))

for i in range(r):
    # kondisi1 = 'kelembapan_turun'
    # kondisi2 = 'ketebalan_turun'
    # kondisi3 = 'umur_turun'
    # kesimpulan = 'kelayakan_turun'

    # kondisi1 = 'kelembapan_turun'
    # kondisi2 = 'ketebalan_turun'
    # kondisi3 = 'umur_sedang'
    # kesimpulan = 'kelayakan_turun'

    # kondisi1 = 'kelembapan_turun'
    # kondisi2 = 'ketebalan_turun'
    # kondisi3 = 'umur_naik'
    # kesimpulan = 'kelayakan_turun'

    # kondisi1 = 'kelembapan_turun'
    # kondisi2 = 'ketebalan_sedang'
    # kondisi3 = 'umur_turun'
    # kesimpulan = 'kelayakan_turun'
    kondisi1 = input("Kondisi 1(naik/turun): ")
    kondisi2 = input("Kondisi 2(naik/turun): ")
    kondisi3 = input("Kondisi 3(naik/turun): ")
    kesimpulan = input("Kesimpulan(naik/turun): ")
    
    #Fire Strength INTERSEKSI (AND)
    
    a = min(nk[kondisi1],nk[kondisi2],nk[kondisi3]) 
    alfa.append(a)
    if(kesimpulan == "turun"):
        zz = agregasi_turun(variabel[dit+"_naik"],variabel[dit+"_turun"],a)
    elif(kesimpulan == "naik"):
        zz = agregasi_naik(variabel[dit+"_naik"],variabel[dit+"_turun"],a)        
    z.append(zz)
    
print(alfa)
print(z)

#DEFUZIFIKASI
df = 0

for i in range(len(alfa)):
    df =df + alfa*z

defuz = int(df/sum(alfa))

print("Jadi, nilai ",dit," adalah ",defuz)