class BSTree:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


# INSERT NODE
def insertNode(rootNode, nodeValue):

    if rootNode.data is None:
        rootNode.data = nodeValue

    elif nodeValue <= rootNode.data:

        if rootNode.leftchild is None:
            rootNode.leftchild = BSTree(nodeValue)
        else:
            insertNode(rootNode.leftchild, nodeValue)

    else:

        if rootNode.rightchild is None:
            rootNode.rightchild = BSTree(nodeValue)
        else:
            insertNode(rootNode.rightchild, nodeValue)


# PREORDER
def preOrderTraversal(rootNode):

    if rootNode is None:
        return

    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)


# INORDER
def inOrderTraversal(rootNode):

    if rootNode is None:
        return

    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)


# POSTORDER
def postOrderTraversal(rootNode):

    if rootNode is None:
        return

    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)


# SEARCH NODE
def searchNode(rootNode, nodeValue):

    if rootNode is None:
        print("The value is not found")
        return

    if rootNode.data == nodeValue:
        print("The value is found")
        return

    elif nodeValue < rootNode.data:
        searchNode(rootNode.leftchild, nodeValue)

    else:
        searchNode(rootNode.rightchild, nodeValue)


# DELETE NODE
def deleteNode(rootNode, nodeValue):

    if rootNode is None:
        return rootNode

    # Search in left subtree
    if nodeValue < rootNode.data:
        rootNode.leftchild = deleteNode(rootNode.leftchild, nodeValue)

    # Search in right subtree
    elif nodeValue > rootNode.data:
        rootNode.rightchild = deleteNode(rootNode.rightchild, nodeValue)

    # Node found
    else:

        # Case 1: Node has no children
        if rootNode.leftchild is None and rootNode.rightchild is None:
            return None

        # Case 2: Node has only right child
        elif rootNode.leftchild is None:
            return rootNode.rightchild

        # Case 2: Node has only left child
        elif rootNode.rightchild is None:
            return rootNode.leftchild

        # Case 3: Node has two children
        else:

            # Find smallest node in right subtree
            successor = rootNode.rightchild

            while successor.leftchild is not None:
                successor = successor.leftchild

            # Replace current node with successor
            rootNode.data = successor.data

            # Delete successor
            rootNode.rightchild = deleteNode(
                rootNode.rightchild,
                successor.data
            )

    return rootNode


# DELETE WHOLE BST
def deleteBST(rootNode):

    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None

    print("The BST has been successfully deleted")


# CREATE BST
newBST = BSTree(None)


# INSERT VALUES
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 20)
insertNode(newBST, 40)


# DISPLAY PREORDER
print("Preorder Traversal:")
preOrderTraversal(newBST)


# DISPLAY INORDER
print("Inorder Traversal:")
inOrderTraversal(newBST)


# DISPLAY POSTORDER
print("Postorder Traversal:")
postOrderTraversal(newBST)


# SEARCH
print("Search:")
searchNode(newBST, 40)


# DELETE NODE
print("Deleting 30...")
newBST = deleteNode(newBST, 30)


# DISPLAY AFTER DELETION
print("Inorder after deleting 30:")
inOrderTraversal(newBST)