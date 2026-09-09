class BSTree:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


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


def preOrderTraversal(rootNode):
    if not rootNode:
        return

    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return

    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return

    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)


def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    print("The BST has been successfully Deleted")


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


newBST = BSTree(None)

insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 20)
insertNode(newBST, 40)

preOrderTraversal(newBST)

searchNode(newBST, 200)