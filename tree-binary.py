class tree:
    def __init__(self, data):
        self.data = data #drinks hot cold 
        self.tree_list = [] #101 102 103
    def addChild(self,child):
        self.tree_list.append(child)
        
    def __str__(self, level=0):
        ret =" "* level + str(self.data) + "\n"
        for child in self.tree_list:
            ret += child.__str__(level+1)
        return ret
    
rootobj = tree('DRINKS')
hot     = tree('hot')
cold    = tree('cold')
tea     = tree('tea')
coffee  = tree('coffee')
ice_cream = tree('ice_cream')
pastries = tree('pastries')

rootobj.addChild(hot)#leftchild
rootobj.addChild(cold)#rightchild

hot.addChild(tea)#leftchild
hot.addChild(coffee)#rightchild

cold.addChild(ice_cream)#lefchild
cold.addChild(pastries)#rightchild

print(rootobj)
