
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(value)
    
    def print_info(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


linked_list = LinkedList()
linked_list.append("Motor")
linked_list.append("Cutie")
linked_list.append("Vapor")
linked_list.append("Girafa")
linked_list.append("Gamma")
linked_list.print_info()