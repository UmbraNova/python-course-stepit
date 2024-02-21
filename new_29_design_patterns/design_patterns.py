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
 
 
 
# Berlina1 = Berlina(2002, "galben", "Mitsubishi", 3000)
# Berlina1.prezentare()
 
SUV1 = SUV(2009, "silver", "Duster", 1000000)
SUV1.prezentare()
# SUV1.reducere(10)
# SUV1.prezentare()
 
 
Sports_Car1 = Sports_Car(2024, "Pink", "Flash", 2)
Sports_Car2 = Sports_Car(1985, "White", "Aventador", 35)
 
# Sports_Car1.prezentare()
# Sports_Car2.prezentare()

class Fabrica_de_Masini():
    @staticmethod  # Ecest decorator este foarte frumos colorat, si este optional.
    # In alte limbaje nu merge fara specificarea "staticmethod". Dar Python e mai entry-level proof

    def produ_masina(an, culoare, producator, pret, tip):
        if tip == "Berlina":
            return Berlina(an, culoare, producator, pret)
        elif tip == "SUV":
            return SUV(an, culoare, producator, pret)
        elif tip == "Sports Car":
            return Sports_Car(an, culoare, producator, pret)
        

# fabrica = Fabrica_de_Masini()
# masina1 = fabrica.produ_masina(1967, "verde", "vaz", 700, "Sports Car")
# masina1.prezentare()
# masina2 = fabrica.produ_masina(1997, "rosu", "tata", 1300, "Berlina")
# masina2.prezentare()

masina_mea = Fabrica_de_Masini.produ_masina(1997, "rosu", "tata", 1300, "Berlina")
masina_mea.prezentare()
        