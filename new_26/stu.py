class Coada:
    def __init__(self):
        self.elemente = []

    def adauga_element(self, element_de_adaugat):
        #print(f"Elementul de adaugat este {element_de_adaugat}")
        self.elemente.append(element_de_adaugat)

    def elimina_din_coada(self):
        #elementul_eliminat=self.elemente[0]
        #self.elemente.pop(0)
        #return elementul_eliminat
        #if self.elemente!=[]:
            #return self.elemente.pop(0)
        #else:
            #print("Lista este goala")
        if self.elemente:
            self.elemente.pop(0)
        else:
            print("Lista e goala")

    def printeaza_coada(self):
        print(self.elemente)

   

coada_unu = Coada()
coada_unu.adauga_element("Andrei")
coada_unu.adauga_element("Tiberiu")
coada_unu.printeaza_coada()
coada_unu.elimina_din_coada()
coada_unu.printeaza_coada()
coada_unu.elimina_din_coada()
coada_unu.printeaza_coada()
coada_unu.elimina_din_coada()