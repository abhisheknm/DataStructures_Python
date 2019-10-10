#!/usr/bin/python3

from BinaryTree import Node 
from Traversal import traverse, inOrder, preOrder, postOrder

# Return a sample tree with 5 nodes
def createTree():
    print("Method is {}".format(createTree.__name__))
    root = Node(1) 
    root.left      = Node(2) 
    root.right     = Node(3) 
    root.left.left  = Node(4) 
    root.left.right  = Node(5) 
    return root

# Return a sample tree with 5 nodes
def createTree2():
    print("Method is {}".format(createTree2.__name__))
    root = Node(10) 
    root.left      = Node(11) 
    root.right     = Node(9) 
    root.left.left  = Node(7) 
    root.right.left = Node(15)
    root.right.right = Node(8)
    return root
  
# Method to print inorder, postorder and preorder traversals
def printOrders (root = None):

    print("Method is {}".format(printOrders.__name__))

    if isinstance (root, Node):
        # Will call order class methods of class Node
        print("The InOrder Traversal of the tree: ")
        root.inOrder(root)
        print("\nThe PreOrder Traversal of the tree: ")
        root.preOrder(root)
        print("\nThe PostOrder Traversal of the tree: ")
        root.postOrder(root)
        print()
       
    if root is None:
        root = createTree()
        traverse(root)
   
def main():
    print("Method is {}".format(main.__name__))
    #root = createTree()
    #root = createTree2()
    root = Node(1)
    input_list = input("Enter the list of numbers whose node is to created : ")
    for val in input_list.split():
        root.insert (root, val)
    printOrders(root)
#    printOrders(createTree())
#    printOrders()

if __name__ == "__main__":
    main()
