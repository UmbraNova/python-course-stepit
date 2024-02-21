from abc import ABC, abstractmethod

#exemplu prost

class Masina(ABC):
    @abstractmethod
    def alimenteaza_cu_curent(self):
        pass

    @abstractmethod
    def alimenteaza_cu_benzina(self):
        pass

    @abstractmethod
    def alimenteaza_cu_motorina(self):
        pass


class Tesla(Masina):
    def alimenteaza_cu_curent(self):
        print("BZZZZZZZZZ")

    def alimenteaza_cu_benzina(self):
        print("Nu")

    def alimenteaza_cu_motorina(self):
        print("Tot nu, lol")


#exemplu bun
from abc import ABC, abstractmethod

class Masina_Electrica(ABC):
    @abstractmethod
    def alimenteaza_cu_curent(self):
        pass


class Masina_Normala(ABC):
    @abstractmethod
    def alimenteaza_cu_benzina(self):
        pass


class Masina_Puternica(ABC):
    @abstractmethod
    def alimenteaza_cu_motorina(self):
        pass


class Tesla(Masina_Electrica):
    def alimenteaza_cu_curent(self):
        print("ZZZZZZZZZZZZZB")


class Toyota_Hibrida(Masina_Electrica, Masina_Normala):
    def alimenteaza_cu_curent(self):
        print("ZZZZZZZZZZZZZB")
    def alimenteaza_cu_benzina(self):
        print("glugluglu")