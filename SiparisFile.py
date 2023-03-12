import PizzaFile
class Siparis:
    def __init__(self,pizza,soses):
        self.pizza=pizza
        self.soses=soses

    def getSoses(self):
        for value in self.soses:
           print(value.getDeScription())
