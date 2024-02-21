class Produs:

    def __init__(self, denumire, pret) -> None:

        self.denumire = denumire

        self.pret = pret



    def prezentare(self):

        print(f"Denumire: {self.denumire}, Pret = {self.pret}")



class Cola(Produs):

    def __init__(self, pret = 8) -> None:

        super().__init__("Coca Cola", pret)



class Fanta(Produs):

    def __init__(self, pret = 7) -> None:

        super().__init__("Fanta", pret)



class Sprite(Produs):

    def __init__(self, pret = 7.50) -> None: # sprite king

        super().__init__("Sprite", pret)





suc1 = Cola()

suc1.prezentare()



suc2 = Fanta()

suc2.prezentare()



suc3 = Sprite()

suc3.prezentare()