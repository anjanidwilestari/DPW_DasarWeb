from tkinter import *
from openpyxl import Workbook
from openpyxl.styles import Font,Alignment,Border,Side
from tkinter import font as tkfont

root = Tk()
root.title("Implementasi Fuzzy")
root.resizable(width=False,height=False)
workbook = Workbook()
sheet = workbook.active

styling = tkfont.Font(family='Helvetica',weight='bold', size=15)
styling2 = tkfont.Font(family='Helvetica', size=9)

font = Font(bold=True)
border = Border(left=Side(border_style='thin',color='00000000'),
                right=Side(border_style='thin',color='00000000'),
                top=Side(border_style='thin',color='00000000'),
                bottom=Side(border_style='thin',color='00000000'))

alignment = Alignment(horizontal='center', vertical='center')

HEIGHT = 650
WIDTH = 700
canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg='lightblue')
canvas.pack()

sheet['A1'] = "Implementasi Fuzzy\t:"
A1 = sheet['A1']
A1.font = font
sheet['A2'] = "Prediksi Jumlah Produk Handsanitizer yang harus di Produksi\t:"
A2 = sheet['A2']
A2.font = font

sheet['A3'] = "No"
A3 = sheet['A3']
A3.font = font
A3.border = border
A3.alignment = alignment

sheet['B3'] = "Ketebalan Minimal"
B3 = sheet['B3']
B3.font = font
B3.border = border
B3.alignment = alignment

sheet['C3'] = "Ketebalan Maksimal"
C3 = sheet['C3']
C3.font = font
C3.border = border
C3.alignment = alignment

sheet['D3'] = "Stok Tersedia (Minimal)"
D3 = sheet['D3']
D3.font = font
D3.border = border
D3.alignment = alignment

sheet['E3'] = "Stok Tersedia (Maksimal)"
D3 = sheet['E3']
D3.font = font
D3.border = border
D3.alignment = alignment

sheet['F3'] = "Produksi (Minimal)"
D3 = sheet['F3']
D3.font = font
D3.border = border
D3.alignment = alignment

sheet['G3'] = "Produksi (Maksimal)"
D3 = sheet['G3']
D3.font = font
D3.border = border
D3.alignment = alignment

sheet['H3'] = "Ketebalan"
D3 = sheet['H3']
D3.font = font
D3.border = border
D3.alignment = alignment

sheet['I3'] = "Stok Tersedia"
D3 = sheet['I3']
D3.font = font
D3.border = border
D3.alignment = alignment

num = 0


def InsertData():
    global num
    num = num + 1
    sheetnum = num + 3

    sheet['A'+str(sheetnum)] = num
    DataNo = sheet['A'+str(sheetnum)]
    DataNo.border = border
    DataNo.alignment = alignment

    sheet['B'+str(sheetnum)] = KetebalanMinEntry.get()
    TebalMin = sheet['B'+str(sheetnum)]
    TebalMin.border = border
    TebalMin.alignment = alignment

    sheet['C' + str(sheetnum)] = KetebalanMaxEntry.get()
    TebalMax = sheet['C' + str(sheetnum)]
    TebalMax.border = border
    TebalMax.alignment = alignment

    sheet['D' + str(sheetnum)] = StokMinEntry.get()
    StokMin = sheet['D' + str(sheetnum)]
    StokMin.border = border
    StokMin.alignment = alignment

    sheet['E' + str(sheetnum)] = StokMaxEntry.get()
    StokMax = sheet['E' + str(sheetnum)]
    StokMax.border = border
    StokMax.alignment = alignment

    sheet['F' + str(sheetnum)] = ProdukMinEntry.get()
    ProduksiMin = sheet['F' + str(sheetnum)]
    ProduksiMin.border = border
    ProduksiMin.alignment = alignment

    sheet['G' + str(sheetnum)] = ProdukMaxEntry.get()
    ProduksiMax = sheet['G' + str(sheetnum)]
    ProduksiMax.border = border
    ProduksiMax.alignment = alignment

    sheet['H' + str(sheetnum)] = JumKetebalanEntry.get()
    JumTebal = sheet['H' + str(sheetnum)]
    JumTebal.border = border
    JumTebal.alignment = alignment

    sheet['I' + str(sheetnum)] = StokTersediaEntry.get()
    Stok = sheet['I' + str(sheetnum)]
    Stok.border = border
    Stok.alignment = alignment

    KetebalanMinEntry.delete(0, END)
    KetebalanMaxEntry.delete(0, END)
    StokMinEntry.delete(0, END)
    StokMaxEntry.delete(0, END)
    ProdukMinEntry.delete(0, END)
    ProdukMaxEntry.delete(0, END)
    JumKetebalanEntry.delete(0, END)
    StokTersediaEntry.delete(0, END)

def SaveData():
    global informasi
    InsertData()
    workbook.save(filename="ImplementasiFuzzy"+".xlsx")
    informasi['text'] = "Data Prediksi Jumlah Produksi Barang telah di save!\nNama file: "+"ImplementasiFuzzy"+".xlsx"

def CreateNewData():
    global informasi, num
    informasi['text'] = 'Klik Insert untuk semua masukan, kemudian klik Kalkulasi & Save jika semua telah selesai'
    KetebalanMinEntry.delete(0, END)
    KetebalanMaxEntry.delete(0, END)
    StokMinEntry.delete(0, END)
    StokMaxEntry.delete(0, END)
    ProdukMinEntry.delete(0, END)
    ProdukMaxEntry.delete(0, END)
    JumKetebalanEntry.delete(0, END)
    StokTersediaEntry.delete(0, END)
    num = 0

def Kalkulasi():
    # Fuzzifikasi Ketebalan
    def Ketebalan():
        global KetebalanMin
        global KetebalanMax
      
        if (int(JumKetebalanEntry.get()) <= int(KetebalanMinEntry.get())):
            KetebalanMin = 1
            KetebalanMax = 0
        elif (int(JumKetebalanEntry.get()) >= int(KetebalanMinEntry.get()) & int(JumKetebalanEntry.get()) <= int(KetebalanMaxEntry.get())):
            KetebalanMin = float((int(KetebalanMaxEntry.get()) - int(JumKetebalanEntry.get())) / (int(KetebalanMaxEntry.get()) - int(KetebalanMinEntry.get())))
            KetebalanMax = float((int(JumKetebalanEntry.get()) - int(KetebalanMinEntry.get())) / (int(KetebalanMaxEntry.get()) - int(KetebalanMinEntry.get())))
        else:
            KetebalanMin = 0
            KetebalanMax = 1

    # Fuzzifikasi Persediaan
    def Persediaan():
        global StokMin
        global StokMax
        if (int(StokTersediaEntry.get()) <= int(StokMinEntry.get())) :
            StokMin = 1
            StokMax = 0
        elif (int(StokTersediaEntry.get()) >= int(StokMinEntry.get()) & int(StokTersediaEntry.get()) <= int(StokMaxEntry.get())):
            StokMin = float((int(StokMaxEntry.get()) - int(StokTersediaEntry.get())) / (int(StokMaxEntry.get()) - int(StokMinEntry.get())))
            StokMax = float((int(StokTersediaEntry.get()) - int(StokMinEntry.get())) / (int(StokMaxEntry.get()) - int(StokMinEntry.get())))
        else:
            StokMin = 0
            StokMax = 1

    # Inferensi Tsukamoto
    Ketebalan()
    Persediaan()
    # IF Ketebalan TURUN dan Persediaan BANYAK then Produksi Barang Berkurang
    a_predikat1 = min(KetebalanMin, StokMax)
    z1 = int(ProdukMaxEntry.get()) - a_predikat1 * (int(ProdukMaxEntry.get()) - int(ProdukMinEntry.get()))

    # IF Ketebalan TURUN dan Persediaan SEDIKIT then Produksi Barang Berkurang  
    a_predikat2 = min(KetebalanMin, StokMin)
    z2 = int(ProdukMaxEntry.get()) - a_predikat2 * (int(ProdukMaxEntry.get()) - int(ProdukMinEntry.get()))

    # IF Ketebalan NAIK dan Persediaan BANYAK then Produksi Barang Bertambah 
    a_predikat3 = min(KetebalanMax, StokMax)
    z3 = int(ProdukMinEntry.get()) - a_predikat3 * (int(ProdukMinEntry.get()) - int(ProdukMaxEntry.get()))

    # IF Ketebalan NAIK dan Persediaan SEDIKIT then Produksi Barang Bertambah
    a_predikat4 = min(KetebalanMax, StokMin)
    z4 = int(ProdukMinEntry.get()) - a_predikat4 * (int(ProdukMinEntry.get()) - int(ProdukMaxEntry.get()))

    # DEFFUZIFIKASI
    a_pred_z = (a_predikat1*z1)+(a_predikat2*z2)+(a_predikat3*z3)+(a_predikat4*z4) 
    z = a_predikat1+a_predikat2+a_predikat3+a_predikat4 
    zTotal = a_pred_z/z

    # Menampilkan Jumlah Produk yang harus diproduksi
    informasi.configure(text=zTotal)

frameJudul = Frame(root, bg='white')
frameJudul.place(rely=0.025,relx=0.5,relheight=0.1,relwidth=0.8,anchor='n')
judul = Label(frameJudul, bg='white', text='Implementasi Fuzzy Prediksi Kelayakan Kayu', font=styling)
judul.place(relheight=1,relwidth=1)

frameKetebalanMin = Frame(root, bg='white')
frameKetebalanMin.place(rely=0.2,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
KetebalanMininfo = Label(frameKetebalanMin, bg='white', text='Ketebalan Minimal', font=styling2)
KetebalanMininfo.place(relwidth=0.4,relheight=1)
KetebalanMinEntry = Entry(frameKetebalanMin)
KetebalanMinEntry.place(relx=0.4,relheight=1,relwidth=0.6)

frameKetebalanMax = Frame(root, bg='white')
frameKetebalanMax.place(rely=0.27,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
KetebalanMaxinfo = Label(frameKetebalanMax, bg='white', text='Ketebalan Maksimal', font=styling2)
KetebalanMaxinfo.place(relwidth=0.4,relheight=1)
KetebalanMaxEntry = Entry(frameKetebalanMax)
KetebalanMaxEntry.place(relx=0.4,relheight=1,relwidth=0.6)

frameStokMin = Frame(root, bg='white')
frameStokMin.place(rely=0.34,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
StokMininfo = Label(frameStokMin, bg='white', text='Stok Tersedia Perhari (Minimal) ', font=styling2)
StokMininfo.place(relwidth=0.4,relheight=1)
StokMinEntry = Entry(frameStokMin)
StokMinEntry.place(relx=0.4,relheight=1,relwidth=0.6)

frameStokMax = Frame(root, bg='white')
frameStokMax.place(rely=0.41,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
StokMaxinfo = Label(frameStokMax, bg='white', text='Stok Tersedia Perhari (Maksimal)', font=styling2)
StokMaxinfo.place(relwidth=0.4,relheight=1)
StokMaxEntry = Entry(frameStokMax)
StokMaxEntry.place(relx=0.4,relheight=1,relwidth=0.6)

frameProdukMin = Frame(root, bg='white')
frameProdukMin.place(rely=0.48,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
ProdukMininfo = Label(frameProdukMin, bg='white', text='Produksi Perhari (Minimal)', font=styling2)
ProdukMininfo.place(relwidth=0.4,relheight=1)
ProdukMinEntry = Entry(frameProdukMin)
ProdukMinEntry.place(relx=0.4,relheight=1,relwidth=0.6)

frameProdukMax = Frame(root, bg='white')
frameProdukMax.place(rely=0.55,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
ProdukMaxinfo = Label(frameProdukMax, bg='white', text='Produksi Perhari (Maksimal)', font=styling2)
ProdukMaxinfo.place(relwidth=0.4,relheight=1)
ProdukMaxEntry = Entry(frameProdukMax)
ProdukMaxEntry.place(relx=0.4,relheight=1,relwidth=0.6)

frameJumKetebalan = Frame(root, bg='white')
frameJumKetebalan.place(rely=0.62,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
JumKetebalaninfo = Label(frameJumKetebalan, bg='white', text='Masukkan Jumlah Ketebalan', font=styling2)
JumKetebalaninfo.place(relwidth=0.4,relheight=1)
JumKetebalanEntry = Entry(frameJumKetebalan)
JumKetebalanEntry.place(relx=0.4,relheight=1,relwidth=0.6)

frameStokTersedia = Frame(root, bg='white')
frameStokTersedia.place(rely=0.69,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')
StokTersediainfo = Label(frameStokTersedia, bg='white', text='Masukkan Stok Tersedia', font=styling2)
StokTersediainfo.place(relwidth=0.4,relheight=1)
StokTersediaEntry = Entry(frameStokTersedia)
StokTersediaEntry.place(relx=0.4,relheight=1,relwidth=0.6)

# BUTTON
frameInsertData = Button(root, bg='lightgrey', text='INSERT DATA', command=InsertData)
frameInsertData.place(rely=0.77,relx=0.5,relheight=0.04,relwidth=0.2,anchor='n')

frameKalkulasi = Button(root, bg='lightgrey', text='KALKULASI', command=Kalkulasi)
frameKalkulasi.place(rely=0.83,relx=0.5,relheight=0.04,relwidth=0.2,anchor='e')

frameSave = Button(root, bg='lightgrey', text='SAVE', command=SaveData)
frameSave.place(rely=0.83,relx=0.5,relheight=0.04,relwidth=0.2,anchor='w')

informasi = Label(root, bg='white', font=styling2, text='Klik Save jika telah melakukan kalkulasi!')
informasi.place(rely=0.86,relx=0.5,relheight=0.06,relwidth=0.8,anchor='n')

createNewData = Button(root, bg='lightgrey', text='CREATE NEW', command=CreateNewData)
createNewData.place(rely=0.96,relx=0.5,relheight=0.04,relwidth=0.2,anchor='e')

Exit = Button(root, bg='lightgrey', text='EXIT', command=root.quit)
Exit.place(rely=0.96,relx=0.5,relheight=0.04,relwidth=0.2,anchor='w')

root.mainloop()