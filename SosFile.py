class Sos:

   def __init__(self,cost,deScription):
        self.cost=cost
        self.deScription=deScription

   def getCost(self):
         return self.cost

   def getDeScription(self):
         return self.deScription

class Zeytin(Sos):
    def __init__(self, cost=5, deScription="Zeytin Sosu"):
        super().__init__(cost, deScription)

class Mantar(Sos):
    def __init__(self, cost=6, deScription="Mantar Sosu"):
        super().__init__(cost, deScription)

class KeciPeyniri(Sos):
    def __init__(self, cost=4, deScription="Keci Peyniri Sosu"):
        super().__init__(cost, deScription)

class Et(Sos):
    def __init__(self, cost=10, deScription="Et Sosu"):
        super().__init__(cost, deScription)

class Sogan(Sos):
    def __init__(self, cost=3, deScription="Sogan Sosu"):
        super().__init__(cost, deScription)

class Misir(Sos):
    def __init__(self, cost=5, deScription="Misir Sosu"):
        super().__init__(cost, deScription)

