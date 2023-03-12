import SosFile as sf
import PizzaFile as pf
def pizzaSecim():
    try:
        result = int(input(" Istedeginiz pizza tabanini yanindaki numarayi kodlayarak secebilirsiniz.\n"))

    except ValueError:
        print("Hatalı Secim!")
        result = int(input(" Istedeginiz pizza tabanini yanindaki numarayi kodlayarak secebilirsiniz.\n"))

    return  result

def pizzaYaratma():

    array=[1,2,3,4]
    value=pizzaSecim()

    if value not in array:
       value=pizzaSecim()

    match value:
        case 1:
            pizza=pf.Klasik()
            print(pizza)
            return pizza
        case 2:
            pizza=pf.Margarita()
            return pizza
        case 3:
            pizza=pf.TürkPizza()
            return pizza
        case 4:
            pizza=pf.SadePizza()
            return pizza
        case 0:
            print("Cikis yapildi.")
            exit(0)


def sosSecim():
    soses=[]
    while True:
        try:
            result=int(input(" Istedeginiz sosu yanindaki numarayi kodlayarak secebilirsiniz.\n"))
        except ValueError:
            print("Hatalı Secim!")
            result = int(input(" Istedeginiz sosu yanindaki numarayi kodlayarak secebilirsiniz.\n"))

        if result==-1:
            print("Secim yapma islemi sona erdi.")
            return soses
            break
        elif result==0:
            print("Cikis yapildi.")
            exit(0)
        elif result in soses:
            print("Bu sos zaten eklenmistir.")
        else:
            soses.append(result)



def sosYaratma():

    soslar=sosSecim()
    uzunluk=len(soslar)
    soses=[]
    for value in range(uzunluk):

        match soslar[value]:
            case 1:
                zeytin=sf.Zeytin()
                soses.append(zeytin)
            case 2:
                mantar=sf.Mantar()
                soses.append(mantar)
            case 3:
                keciPeyniri=sf.KeciPeyniri()
                soses.append(keciPeyniri)
            case 4:
                et=sf.Et()
                soses.append(et)
            case 5:
                sogan=sf.Sogan()
                soses.append(sogan)
            case 6:
                misir=sf.Misir()
                soses.append(misir)
    return soses