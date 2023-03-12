import HesapOlustur
import MenuOkuma
import SecimFile
import KullaniciFile
import SiparisFile
import VeritabaniIslemleri


#Pizza Islemleri
MenuOkuma.getPizzaMenu()
pizza=SecimFile.pizzaYaratma()

#Sos Islemleri
MenuOkuma.getSosesMenu()
soses=SecimFile.sosYaratma()

#Hesap Islemleri
siparis=SiparisFile.Siparis(pizza,soses)
hesap=HesapOlustur.hesap(siparis)

#Kullanici Islemleri
kullanici=KullaniciFile.kullaniciBilgiIsteme()

#Veritabani Islemleri
VeritabaniIslemleri.databaseYazdir(kullanici,hesap,siparis)
data=VeritabaniIslemleri.databaseOku("Orders_Database.csv")
last_row = data[-1]
print(last_row)