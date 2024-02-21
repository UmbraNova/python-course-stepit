# Linked List

# Step 1 - define the node

class Node:
    # Create the object with two properties:
    # data = node value(int, string, dict ...)
    # next points towards the  next node. Starts as None
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


#  Step 2 - define the list
class List:
    def __init__(self) -> None:
        self.head = None 

    def append(self, value):
        new_node = Node(value)
        if self.head is None:  # self.head == None || The == operator compares the value or equality of two objects, whereas the Python is operator checks whether two variables point to the same object in memory.
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

    def length(self):
        current_node = self.head
        list_length = 0
        while current_node:
            current_node = current_node.next
            list_length += 1
        return f"{list_length} Test List LEN"
    
    def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        

lst = List()
lst.append("Mercur")
lst.append("Venus")
lst.append("Terra")
# lst.prepend("Mercur")
# lst.prepend("Venus")
# lst.prepend("Terra")

# lst.print_info()
# print(lst.length())

lst.print_info()
lst.reverse()
lst.print_info()

# print(lst.head.data)

#   #########
# #############
# #############
# #############
#   #########
#      ||
#      ||
#      ||
#     ````