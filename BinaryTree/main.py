from BinaryTree import Node 

def main():
    n = int(input("Enter the number whose node is to created : "))
    node = Node(n)
    print("data of the node is {}".format(node.val))
    print("left of the node is {}".format(node.left))
    print("right of the node is {}".format(node.right))


if __name__ == "__main__":
    main()
