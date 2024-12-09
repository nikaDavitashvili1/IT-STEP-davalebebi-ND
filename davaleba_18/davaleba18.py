import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)


    def printLeafNodes(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.data, end=' ')
            return

        if node.left:
            self.printLeafNodes(node.left)
        if node.right:
            self.printLeafNodes(node.right)

    def countEdges(self, node):
        if node is None:
            return 0

        leftEdges = self.countEdges(node.left)
        rightEdges = self.countEdges(node.right)

        return leftEdges + rightEdges + (1 if node.left or node.right else 0)


bt = BinaryTree()

for _ in range(50):
    bt.insert(random.randint(1, 100))


print("Leaf Nodes:")
bt.printLeafNodes(bt.root)

print("\nNumber of Edges:")
print(bt.countEdges(bt.root))
