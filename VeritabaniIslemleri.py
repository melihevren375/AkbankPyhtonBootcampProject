import datetime
import csv

def databaseYazdir(kullanici,hesap,siparis):

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")

    soses=[]
    for value in siparis.soses:
        soses.append(value.getDeScription())


    veriler = [{'Ad': kullanici.isim,
                'TC': kullanici.TC,
                'KrediKartNumarasi': kullanici.krediKartNumarasi,
                'KrediKartSifresi': kullanici.krediKartSifresi,
                'Gun': now,
                'Saat':current_time,
                'Hesap Toplam':hesap,
                'Pizza':siparis.pizza.getDeScription(),
                'Soslar':soses
                }]

    with open("Orders_Database.csv", "a",encoding="utf-8") as dosyam:
        yazici = csv.DictWriter(dosyam, fieldnames=['Ad', 'TC', 'KrediKartNumarasi', 'KrediKartSifresi','Gun','Saat','Hesap Toplam','Pizza','Soslar'])
        yazici.writerows(veriler)

def databaseOku(csvfilename):
    data = []
    with open(csvfilename, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        row_index = 0
        for row in reader:
            if row: 
                row_index += 1
                columns = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],row[8]]
                data.append(columns)
    return data