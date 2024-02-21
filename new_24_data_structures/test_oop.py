# Asta vroiam sa spun.
# Clasa iti permite sa nu scrii
# de fiecare data toate acele date
# pentru fiecare variabila (pisica, catel, catel_2 etc.)
# ci poti folosi clasa ca sablon

class Animal():
    def __init__(self, greutate=20, varsta=90, nume="leopard"):
        self.greutate = greutate
        self.varsta = varsta
        self.nume = nume

    def o_functie(self):
        pass



pisica = Animal()
pisica.greutate = 45

catel = Animal()
catel.nume = "Vasile"

catel_2 = Animal()
catel_2.nume = "Beriliu"
catel_2.greutate = 33

print(pisica.greutate, pisica.varsta, pisica.nume)
print(catel.greutate, catel.varsta, catel.nume)
print(catel_2.greutate, catel_2.varsta, catel_2.nume)

















# cd ..
# mkdir denumire
# code denumire (tab)