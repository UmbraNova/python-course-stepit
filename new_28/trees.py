#   ##########
# ########@#####
# ##@###########
# ###########@##
#   ##@#######
#       ||
#       ||
#       ||
#      ````

class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST():  # Binary Search Tree
    def __init__(self) -> None:
        self.root = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            self.append_recursion(self.root, value)

    def append_recursion(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
            else:
                self.append_recursion(node.left, value)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
            else:
                self.append_recursion(node.right, value)
        else:
            print("Error: The values are equal")
    
    def search_node(self, value):
        return self.search_node_recursive(self.root, value)

    def search_node_recursive(self, node, value):
        if node is None:
            return False
        elif node.data > value:
            return self.search_node_recursive(node.left, value)
        elif node.data < value:
            return self.search_node_recursive(node.right, value)
        else:
            return True


binarySearchTree = BST()
binarySearchTree.append(36)
binarySearchTree.append(37)
binarySearchTree.append(11)
binarySearchTree.append(0)
binarySearchTree.append(-41)
print(binarySearchTree.search_node(97))
print(binarySearchTree.search_node(11))
print(binarySearchTree.search_node(36))
print(binarySearchTree.search_node(-41))
