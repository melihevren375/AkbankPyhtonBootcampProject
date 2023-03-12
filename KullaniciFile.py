
class Kullanici:
    def __init__(self,isim,TC,krediKartNumarasi,krediKartSifresi):
        self.TC=TC
        self.krediKartNumarasi=krediKartNumarasi
        self.isim=isim
        self.krediKartSifresi=krediKartSifresi


def kullaniciBilgiIsteme():

    try:
        isim = str(input("Lütfen isminizi giriniz.\n"))
    except ValueError:
        print("Yanlış ifade girdiniz")
        isim = str(input("Lütfen isminizi giriniz.\n"))

    try:
        TC = int(input("Lütfen TC kimlik numaranizi giriniz.\n"))
    except ValueError:
        print("Yanlış ifade girdiniz")
        TC = int(input("Lütfen TC kimlik numaranizi giriniz.\n"))

    try:
        krediKartNumarasi = int(input("Lütfen kredikart numaranizi giriniz.\n"))
    except ValueError:
        print("Yanlış ifade girdiniz")
        krediKartNumarasi = int(input("Lütfen kredikart numaranizi giriniz.\n"))

    try:
        krediKartSifresi = int(input("Lütfen kredikart sifrenizi giriniz.\n"))
    except ValueError:
        print("Yanlış ifade girdiniz")
        krediKartSifresi = int(input("Lütfen kredikart sifrenizi giriniz.\n"))

    kullanici=Kullanici(isim,TC,krediKartNumarasi,krediKartSifresi)
    return kullanici