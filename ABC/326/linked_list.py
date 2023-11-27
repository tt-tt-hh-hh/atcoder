class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.Head = None

    def printlist(self):
        current = self.Head
        while current is not None:
            print(current.data)
            current = current.next

myLinkedList = LinkedList()
myNode1 = Node(10)
myNode2 = Node(20)

myLinkedList.Head = myNode1
myNode1.next = myNode2

print(myLinkedList.Head.data)
print(myLinkedList.Head.next.data)

myLinkedList.printlist()