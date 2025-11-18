class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _print_parents(self, node, parent):
        if node:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "->", parent.key)

            self._print_parents(node.left, node)
            self._print_parents(node.right, node)

    def print_parents(self):
        print("Parents are:")
        self._print_parents(self.root, None)

    def print_leaf_nodes(self):
        print("Leaf nodes:", end=" ")
        self._print_leaf(self.root)
        print()

    def _print_leaf(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.key, end=" ")
            return

       
        self._print_leaf(node.left)
        self._print_leaf(node.right)

bst = BST()
bst.insert(10)
bst.insert(12)
bst.insert(11)
bst.insert(9)
bst.insert(13)

bst.print_parents()
bst.print_leaf_nodes()
