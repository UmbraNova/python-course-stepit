from product import Product


class CocaCola(Product):
    def __init__(self, price=8) -> None:
        super().__init__("Coca-Cola", price)


class Fanta(Product):
    def __init__(self, price=4) -> None:
        super().__init__("Fanta", price)


class Sprite(Product):
    def __init__(self, price=9) -> None:
        super().__init__("Sprite", price)


def juice_choice():
    print("Juice options are: ")
    print("1 - Coca-Cola, \n2 - Fanta, \n3 - Sprite")
    juice_option = input("Enter your juice option: ")

    if juice_option == "1":
        return CocaCola()
    elif juice_option == "2":
        return Fanta()
    elif juice_option == "3":
        return Sprite()