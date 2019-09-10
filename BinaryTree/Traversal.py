#PreOrder traversal of a tree
def preOrder(root):
    if root:
        print(root.val, end= " ")
        preOrder(root.left)
        preOrder(root.right)

#InOrder traversal of a tree
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)

#PostOrder traversal of a tree
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val, end= " ")
    
def traverse(root):

    print("Method is {}".format(traverse.__name__))
    if root is None:
        print("Empty tree!!!")
        return

    # Calling Order methods from Traversal
    print("The InOrder Traversal of the tree: ")
    inOrder(root)
    print("\nThe PreOrder Traversal of the tree: ")
    preOrder(root)
    print("\nThe PostOrder Traversal of the tree: ")
    postOrder(root)
    print()
