class Pizza:
    def __init__(self,cost,deScription):
        self.cost=cost
        self.deScription=deScription

    def getCost(self):
        return self.cost


    def getDeScription(self):
        return self.deScription

class Klasik(Pizza):
    def __init__(self, cost=50, deScription="Klasik pizza"):
        super().__init__(cost, deScription)

class Margarita(Pizza):
    def __init__(self, cost=60, deScription="Margarita pizza"):
        super().__init__(cost, deScription)

class TürkPizza(Pizza):
    def __init__(self, cost=40, deScription="Türk pizza"):
        super().__init__(cost, deScription)

class SadePizza(Pizza):
    def __init__(self, cost=30, deScription="Sade pizza"):
        super().__init__(cost, deScription)