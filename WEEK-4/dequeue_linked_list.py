class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DequeLinked:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

    def addFront(self, element):

        if self.top == None:
            self.top = Node(element)
            self.bottom = self.top
        else:
            newNode = self.top
            self.top = Node(element)
            self.top.next = newNode
            newNode.prev = self.top
        self.size += 1

    def addRear(self, element):
        if self.top == None:
            self.top = Node(element)
            self.bottom = self.top
        else:
            self.bottom.next = Node(element)
            self.bottom.next.prev = self.bottom
            self.bottom = self.bottom.next
        self.size += 1

    def removeFront(self):
        if self.size == 0:
            raise IndexError
        elif self.size == 1:
            newNode = self.top
            self.top = self.bottom = None
            self.size = 0
            return newNode
        else:
            # top point to top
            newNode = self.top
            self.top = self.top.next
            self.top.prev = None
            return newNode

    def removeRear(self):
        if self.size == 0:
            raise IndexError
        elif self.size == 1:
            newNode = self.top
            self.top = self.bottom = None
            self.size = 0
            return newNode
        else:
            # bottom point to bottom
            newNode = self.bottom
            self.bottom = self.bottom.prev
            self.bottom.next = None
            return newNode

    def size(self):
        return self.size

    def __str__(self):
        output = ""
        newNode = self.top
        while newNode:
            output += str(newNode.item) + " "
            newNode = newNode.next
        return output


deque = DequeLinked()
deque.addFront(5)
deque.addFront(10)
deque.addFront(15)
deque.addRear(20)
deque.addRear(25)
deque.addRear(30)
print("Deque elements are :", str(deque))
print()

deque.removeFront()
print("After remove front element are: ")
print(str(deque))

print()
print("After remove rear element are: ")
deque.removeRear()
print(str(deque))
