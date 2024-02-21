class Animal():
    def __init__(self, greutate=20, varsta=90, nume="leopard"):
        self.greutate = greutate
        self.varsta = varsta
        self.nume = nume


    def printeaza_nume(self):
        print("Aceasta este o metoda a clasei")
        print(self.nume)

    def introducere_politicoasa(self):
        print(f"Buna ziua, numele meu este {self.nume}, si am varsta de {self.varsta} ani.")

    def formula_de_salut(self):
        print("La revedere.")

    def ziua_de_nastere(self):
        print(f"Astazi este ziua mea si am {self.varsta + 1}")
        self.varsta += 1



pisica = Animal(nume = "Luna", varsta = 3)
pisica.greutate = 45
print(pisica.greutate)

#print(pisica.printeaza_nume())

pisica.printeaza_nume()
pisica.introducere_politicoasa()
pisica.formula_de_salut()
pisica.ziua_de_nastere()

catel = Animal(nume="Labrador")