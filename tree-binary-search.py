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


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftchild = deleteNode(rootNode.leftchild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightchild = deleteNode(rootNode.rightchild, nodeValue)
    else:
        if rootNode.leftchild is None and rootNode.rightchild is None:
            return None
        elif rootNode.leftchild is None:
            return rootNode.rightchild
        elif rootNode.rightchild is None:
            return rootNode.leftchild
        else:
            successor = rootNode.rightchild
            while successor.leftchild is not None:
                successor = successor.leftchild
            rootNode.data = successor.data
            rootNode.rightchild = deleteNode(
                rootNode.rightchild,
                successor.data
            )

    return rootNode


def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    return "The BST has been successfully Deleted"


newBST = BSTree(None)

insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 20)
insertNode(newBST, 40)

preOrderTraversal(newBST)

print("")

searchNode(newBST, 40)

print("")

newBST = deleteNode(newBST, 30)

preOrderTraversal(newBST)
print(deleteBST(newBST))