class node:  # creates on memory
    def __init__(self, value):
        self.data = value  # [10]
        self.next = None  # [10|None] [20|None] [30|None] [40|None]


class linkedlist:
    def __init__(self):
        self.head = None  # 101       102        103        104


linkedobj = linkedlist()
# creating independent nodes
linkedobj.head = node(10)  # 101
second = node(20)  # 102
thrid = node(30)  # 103
fourth = node(40)  # 104

#connecting the nodes
linkedobj.head.next = second
second.next = thrid
thrid.next = fourth 

#display result
while linkedobj.head != None:
    print("[",linkedobj.head.data,"]","|",linkedobj.head.next,"-->")
    linkedobj.head = linkedobj.head.next