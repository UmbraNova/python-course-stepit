class Product():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def presentation(self):
        print(f"Name {self.name} Price {self.price}")
