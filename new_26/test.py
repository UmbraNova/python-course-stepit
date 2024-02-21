# Queue imlpementation
# Defining a class

class Queue():
    def __init__(self):
        self.elements = []

    def add_element(self, added_element):
        print(f"Added element is: {added_element}")
        self.elements.append(added_element)

    def queue_remove(self):
        if self.elements:
            self.elements.pop(0)
        else:
            print("Lista e goala")

    def print_queue(self):
        print(self.elements)

    def is_empty(self):
        if self.elements:
            print(f"Nu este goala, are {len(self.elements)} elemente.")
        else:
            print("Este goala!")





queue_one = Queue()
print(queue_one)
queue_one.add_element("Alexandru")
queue_one.add_element("Tiberiu")
queue_one.add_element("Leopard")
queue_one.add_element("Motor")
queue_one.print_queue()
queue_one.queue_remove()
queue_one.queue_remove()
queue_one.queue_remove()
queue_one.queue_remove()
queue_one.queue_remove()
queue_one.queue_remove()
queue_one.queue_remove()
queue_one.print_queue()
queue_one.is_empty()

