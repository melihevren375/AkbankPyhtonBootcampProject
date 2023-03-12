def readPizzaText():
    try:
        fileOfPizza=open("Pizza.txt","r")
        results=fileOfPizza.read()
    except:
        print("Hata olustu!!")
        exit(0)
    return results

def readSosText():
    try:
        fileOfSos=open("Sos.txt","r")
        results=fileOfSos.read()
    except:
        print("Hata olustu!!")
        exit(0)
    return  results

