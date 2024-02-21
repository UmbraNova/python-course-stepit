import produs

 

program_activ = True

lista_produse = []

 

 

while program_activ:

    print("Bine ai venit la Python Kebab")

    print("1.Kebab\n2.Suc\n3.Cartofi\n4.Meniu")

    comanda = input ("Ce ati dori sa comandati?")

 

    if comanda == 'q':

        print("La revedere")

        program_activ = False

    elif comanda == "1":

        print("Optiunea selectata este 1")    

        pass

    elif comanda == "2": # Selectare suc

        print("Doriti sa comandati un suc.")

        print("1.Cola 2.Fanta 3.Sprite")

        comanda_suc = input ("Ce suc doriti?")

        if comanda_suc == "1":

            lista_produse.append(produs.Cola())

        elif comanda_suc == "2":

            lista_produse.append(produs.Fanta())

        elif comanda_suc == "3":

            lista_produse.append(produs.Sprite())  

    elif comanda == "3":

        pass

    elif comanda == "4":

        pass

    else:

        print(f"Optiunea selectata este : {comanda}")