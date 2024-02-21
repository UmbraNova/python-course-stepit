class Car():
    def __init__(self, year, color, manu, price, type) -> None:
        self.year = year
        self.color = color
        self.manu = manu
        self.price = price
        self.type = type

    def presentation(self):
        print("_"*70)
        print(f"This {self.type} made by {self.manu} it's from {self.year}, painted {self.color}, and you can buy it for {self.price} $\n")

    def discount(self, percent):
        self.price -= self.price * (percent / 100)
        print(self.price)


class Sedan(Car):
    def __init__(self, year, color, manu, price) -> None:
        super().__init__(year, color, manu, price, "Sedan")


class SUV(Car):
    def __init__(self, year, color, manu, price) -> None:
        super().__init__(year, color, manu, price, "SUV")


class Sport(Car):
    def __init__(self, year, color, manu, price) -> None:
        super().__init__(year, color, manu, price, "Sport")


# SUV1 = SUV(2016, "blue", "Range Rover", 1000000, "SUV")
SUV1 = SUV(2016, "blue", "Range Rover", 24000)
SUV1.presentation()
# SUV1.discount(10)
# SUV1.presentation()


# Sport1 = Sport(2022, "grey", "Koenigsegg", 2199000, "Sport")
# Sport1.presentation()

