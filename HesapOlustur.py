
def hesap(siparis):
    pizzaUcret = siparis.pizza.getCost()

    sosucret = 0

    for value in siparis.soses:
        sosucret += value.getCost()

    toplamUcret = sosucret + pizzaUcret

    return toplamUcret