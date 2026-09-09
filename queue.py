class Queue:
    def __init__(self, queueSize):
        self.queueSize = queueSize
        self.queueList = []

    def isFull(self):
        if len(self.queueList) == self.queueSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.queueList == []:
            return True
        else:
            return False

    def enQueue(self, value):
        if self.isFull():
            print("Queue is Full")
        else:
            self.queueList.append(value)

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.queueList.pop(0))

    def peekFront(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.queueList[0])

    def deleteQueue(self):
        self.queueList = None
        print("Quue has deleted")

    def displayQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.queueList)


size = int(input("enter the size of queue"))
queueObject = Queue(size)

while True:
    print('1. enQueue')
    print('2. deQueue')
    print('3. peekFront')
    print('4. deleteQueue')
    print('5. displayQueue')
    print('6. isEmpty')
    print('7. isFull')
    print('8. Exit')

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        queueObject.enQueue(value)

    elif choice == 2:
        queueObject.deQueue()

    elif choice == 3:
        queueObject.peekFront()

    elif choice == 4:
        queueObject.deleteQueue()

    elif choice == 5:
        queueObject.displayQueue()

    elif choice == 6:
        print(queueObject.isEmpty())

    elif choice == 7:
        print(queueObject.isFull())

    elif choice == 8:
        print("Exiting")
        break

    else:
        print("Invalid choice")
