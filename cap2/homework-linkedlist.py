class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


class List:
    def __init__(self) -> None:
        self.head = None 

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_info(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


my_lst = List()
my_lst.append("Meow")
my_lst.prepend("Owl")
my_lst.print_info()