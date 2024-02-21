# aici declaram listele si printam valorile initiale
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1
print(f"lista1 = {lista1} | lista2 = {lista2} | lista3 = {lista3}")
print("-" * 50)  # doar pt separare vizuala


# ====================================================  schimbam prin referinta la locatia in memorie
def bug_change(data):
    data[2] = 1938  # schimbam valoarea
    # return data  # nu facem return... aparent nu ar trebui sa se schimbe listele 1 si 2 dar...

bug_change(lista3)  # aici schimbam lista 1 si 3 prin referire la locatia in memori


# ====================================================  schimbam prin return
def the_change(data):
    data[1] = 48938  # schimbam valoarea
    return data  # trimitem valoarea prin return

lista2 = the_change(lista2)  # aici schimbam lista 2, o primim prin return si o atribuim variabilei


print(f"lista1 = {lista1} | lista2 = {lista2} | lista3 = {lista3}\n")  # aici putem vedea cum lista 1 si 3 au fost
# modificate desi nu am folosit nici return si pe langa asta nici nu ne-am atins de lista1

print(f"ID1 = {id(lista1)} | ID2 {(lista2)} | ID3 {id(lista3)}")  # aici putem vedea ID-ul in memorie
