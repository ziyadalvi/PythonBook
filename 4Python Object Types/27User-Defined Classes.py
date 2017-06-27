#User-Defined Classes

class Worker:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay *= (1.0 + percent)
        return self.pay

ziyad = Worker('Ziyad Alvi', 35000)
zohair = Worker('Mohammad Zohair', 40000)

print(ziyad.lastName())
print(zohair.lastName())

print(ziyad.giveRaise(0.3))
