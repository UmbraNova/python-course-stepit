# Lista inlantuita
# Primul pas - definim un nod

class Nod:
    # Initializam clasa cu doua proprietati:
    # Ii dam niste informatii (data) de care el sa tina cont, care pot fi orice (str, int, dict, etc)
    # Cea de a doua proprietate (next) care se refera la urmatorul element din lista (spre cine arata nodul nostru) este initial inexistent (nu arata spre nimic)

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


# nodul1 = Nod("Primul nod")
# print(nodul1.data)
# print(nodul1.next)

# nodul2 = Nod(12)
# print(nodul2.data)
# print(nodul2.next)

# nodul3 = Nod(["televizor", "masa", "creion"])
# print(nodul3.data)
# print(nodul3.next)

# Al doilea pas - definim lista

class List:
    def __init__(self) -> None:
        self.head = None #initializam lista si avem o proprietate head care initial nu are nici o valoare

# Adaugam un nod la sfarsit (append)
def append(self, data):

# Verificam daca avem un cap (head)
# Daca nu avem un head, vrem sa il adaugam

    nod_de_adaugare = Nod(data)
    if self.head is None:
        self.head = nod_de_adaugare

# Daca avem deja un head, creem nodul_curent si apoi mergem cu un ciclu prin nodul_curent cat timp
# next nu este egal cu none
    else:
        nodul_curent = self.head
    while nodul_curent.next:
        nodul_curent = nodul_curent.next


# Odata ce next este egal cu none, ciclul se intrerupe si la ultimul nod din lista se adauga noul nod creat mai sus,
# cu noua valoare

    nodul_curent.next = nod_de_adaugare

    def print_info(self):
        nodul_curent = self.head
        while nodul_curent:
            print(nodul_curent.data)
            nodul_curent = nodul_curent.next

    def length(self):
        lungimea_listei = 0
        nodul_curent = self.head

        while nodul_curent:
            lungimea_listei += 1
            nodul_curent = nodul_curent.next

        #print(lungimea_listei)
        return lungimea_listei





lista = List()
lista.append("Mercur")
lista.append("Venus")
lista.append("Terra")
lista.append("Marte")
# print(lista.head.data)
lista.print_info()
superman = lista.length()
print(superman)
variabila = 0
if variabila:
    print("Conditia este adevarata.")
else:
    print("Conditia este falsa.")