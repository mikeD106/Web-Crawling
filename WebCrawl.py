from urllib.request import urlopen as uRequest
from bs4 import BeautifulSoup as Soup

#untuk pindah tabel href Semester & SKS



#module membuat screenshot
import pyautogui
import tkinter as tk

the_url = 'https://forlap.ristekdikti.go.id/mahasiswa/detail/MzM2QUQ5NjQtNzAxQi00QTA4LUEyRkUtNTRBODNBRURCQjg3'

#open connection
uClient = uRequest(the_url)
Tgtpage = uClient.read()
uClient.close()

#html parse
soup_page = Soup(Tgtpage, "html.parser")

#mengambil div pada general information
containers = soup_page.find_all("div",{"class":"main"})

file_name = "profile.csv"
berkas = open(file_name,"w")

#headers = "Nama, Jenis Kelamin, Perguruan Tinggi, Program Studi, Nomor Induk, Semester Awal, Status Awal, Status saat ini\n"

#berkas.write(headers)

for container in containers:
#mengambil jabatan bernama title pada div
    Jabatan_contain = container.find("div",{"class":"title"})
    jabatan = Jabatan_contain.find(text=True)
    # count = 0
    # for count in len(the_url):
    #     if len(count)=='m' and len(count+1)=='a' and len(count+2)=='h' and len(count+3)=='a' and len(count+4)=='s' and len(count+5)=='i' and len(count+6)=='s' and len(count+7)=='s' and len(count+8)=='a':

        #mengambil table data bernama table1 di div
    tabel_contain = container.find("table",{"class":"table1"})
    tabel_row = tabel_contain.find_all("tr")

    if tabel_row[0]:
        cells = tabel_row[0].find_all("td")
        nama = cells[2].find(text=True)
        print('Nama : ' + nama)

    if tabel_row[1]:
        cells = tabel_row[1].find_all("td")
        kelamin = cells[2].find(text=True)
        print('Jenis Kelamin : ' + kelamin)
            
    if tabel_row[3]:
        cells = tabel_row[3].find_all("td")
        univ = cells[2].find(text=True)
        print('Perguruan Tinggi : ' + univ)
            
    if tabel_row[4]:
        cells = tabel_row[4].find_all("td")
        Program = cells[2].find(text=True)
        print('Program Studi : ' + Program)

    if tabel_row[5]:
        cells = tabel_row[5].find_all("td")
        NIM = cells[2].find(text=True)
        print('Nomor Induk : ' + NIM)

    if tabel_row[6]:
        cells = tabel_row[6].find_all("td")
        SemAwal = cells[2].find(text=True)
        print('Semester Awal : ' + SemAwal)

    if tabel_row[7]:
        cells = tabel_row[7].find_all("td")
        statAwal = cells[2].find(text=True)
        print('Status Awal : ' + statAwal)

    if tabel_row[8]:
        cells = tabel_row[8].find_all("td")
        statAkhir = cells[2].find(text=True)
        print('Status Mahasiswa Saat ini : ' + statAkhir)

    berkas.write("Nama : " + nama + "\n")
    berkas.write("Jenis Kelamin : " + kelamin + "\n")
    berkas.write("Nama Universitas : " + univ + "\n")
    berkas.write("Program Studi : " + Program + "\n")
    berkas.write("Nomor Induk Mahasiswa : " + NIM + "\n")
    berkas.write("Semester Awal : " + SemAwal + "\n")
    berkas.write("Status Awal : " + statAwal + "\n")
    berkas.write("Status Akhir : " + statAkhir + "\n\n")
berkas.close()
# menu= tk.Tk()

# canvas1 = tk.Canvas(menu, width = 300, height = 300)
# canvas1.pack()

# def takeScreenshot ():
    
#     myScreenshot = pyautogui.screenshot()
#     myScreenshot.save(r'/root/Documents/screenshot2.png')

# myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green',fg='white',font= 10)
# canvas1.create_window(150, 150, window=myButton)

# menu.mainloop()
