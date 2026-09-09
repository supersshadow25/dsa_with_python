class tree:
    def __init__(self, data):
        self.data = data
        self.tree_list = []

    def addChild(self, child):
        self.tree_list.append(child)

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.tree_list:
            ret += child.__str__(level+1)
        return ret


rootobj = tree('N1')

N2 = tree('N2')
N3 = tree('N3')

N4 = tree('N4')
N5 = tree('N5')

N6 = tree('N6')
N7 = tree('N7')

N9 = tree('N9')
N10 = tree('N10')

rootobj.addChild(N2)  # left
rootobj.addChild(N3)  # right

N2.addChild(N4)
N2.addChild(N5)

N3.addChild(N6)
N3.addChild(N7)

N4.addChild(N9)
N4.addChild(N10)

print(rootobj)
