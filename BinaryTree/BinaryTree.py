class Node:
    def __init__ (self, key):
        self.left = None
        self.right = None
        self.val = key

    #PreOrder traversal of a tree
    def preOrder(self, node):
        if node:
            print(node.val, end= " ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    #InOrder traversal of a tree
    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print(node.val, end=" ")
            self.inOrder(node.right)

    #PostOrder traversal of a tree
    def postOrder(self, node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.val, end= " ")
