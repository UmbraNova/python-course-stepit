class Masina:
    def __init__(self, an, culoare, producator, pret, tip):
        self.an = an
        self.culoare = culoare
        self.producator = producator
        self.pret = pret
        self.tip = tip

    def prezentare(self):
        print(f"Acest {self.tip} este din anul {self.an}, are culoarea {self.culoare}\nsi poate fi a dumneavoastra pentru doar {self.pret} euro")

    def reducere(self, procent):
        self.pret = self.pret * (100 - procent) // 100
        print(f"Pretul redus este: {self.pret}")

 
class Berlina(Masina):
    def __init__(self, an, culoare, producator, pret):
        super().__init__(an, culoare, producator, pret, "Berlina")

 
 
 
class SUV(Masina):
    def __init__(self, an, culoare, producator, pret):
        super().__init__(an, culoare, producator, pret, "SUV")
 
 
class Sports_Car(Masina):
    def __init__(self, an, culoare, producator, pret,):
        super().__init__(an, culoare, producator, pret, "Sports Car")
        
 
 
 
# Masina1 = Masina(1995, "albastru", "Toyota", 600)
# Masina2 = Masina(2015, "negru", "Dacia", 8000)
# Masina3 = Masina(2022, "alb", "Tesla", 60000)
# Masina3.prezentare()
 
 
 
Berlina1 = Berlina(2002, "galben", "Mitsubishi", 3000)
Berlina1.prezentare()
 
SUV1 = SUV(2009, "silver", "Duster", 1000000)
SUV1.prezentare()
SUV1.reducere(10)
SUV1.prezentare()
 
 
Sports_Car1 = Sports_Car(2024, "Pink", "Flash", 2)
Sports_Car2 = Sports_Car(1985, "White", "Aventador", 35)
 
Sports_Car1.prezentare()
Sports_Car2.prezentare()

