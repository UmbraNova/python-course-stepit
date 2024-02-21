import random


class Sandwich():
    def __init__(self, bread) -> None:
        self.bread = bread
        self.ingredients = []

    def print_info(self):
        print(f"Este un sandwich cu paine de tip {self.bread} si ingredientele urmatoare {self.ingredients}")
        print("_"*90)


class Sandwich_builder():
    def __init__(self, bread) -> None:
        self.sandwich = Sandwich(bread)

    def add_ingr(self, value):  # adauga ingrediente
        self.sandwich.ingredients.append(value)
        return self  # practica buna
    
    def finalizeaza(self):  # finalizeaza sandwich-ul si atribuie return-ul unei variabile
        return self.sandwich
    


# sandwich_maker = Sandwich_builder("neagra")
# sandwich_maker.add_ingr("Tarhun").add_ingr("Busuioc").add_ingr("Oregano").add_ingr("Lapte").add_ingr("Sos de rosii").add_ingr("Miere")  # adaugare in cascada
# my_sandwich = sandwich_maker.finalizeaza()
# my_sandwich.print_info()


all_ingr = [
    "oregano", 
    "piper", 
    "sare", 
    "tigri", 
    "orez", 
    "branza", 
    "rosii",
    "banane",
    "ananas"
    "si alte chestii..."
    ]

prev_num = ""
sandwich_maker2 = Sandwich_builder("rosie")
for i_ingr in range(len(all_ingr)-1):
    rnd_num = random.randint(0, 6)
    if rnd_num == prev_num:
        prev_num = rnd_num
    else:
        sandwich_maker2.add_ingr(all_ingr[rnd_num])

sandwich_maker2.finalizeaza().print_info()