class Node:
    # __init__ method of class Node
    def __init__ (self, key):
        self.left = None
        self.right = None
        self.val = key

    # PreOrder traversal of a tree
    def preOrder(self, node):
        if node:
            print(node.val, end= " ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    # InOrder traversal of a tree
    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print(node.val, end=" ")
            self.inOrder(node.right)

    # PostOrder traversal of a tree
    def postOrder(self, node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.val, end= " ")

    # Insert value into the tree by level-order traversal
    def insert (self, node, value):
        if node is None:
           node = __init__(self, value)
           return node
        # Queue to hold nodes of the tree
        q = []
        q.append(node)
        while q:
            popped = q.pop(0)
            if popped.left:
                q.append(popped.left)
            else:
                popped.left = Node(value)
                break

            if popped.right:
                q.append(popped.right)
            else:
                popped.right = Node(value)
                break

