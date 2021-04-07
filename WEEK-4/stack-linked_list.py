class Node:
    # Constructor to initialize node
    def __init__(self, item):
        self.item = item  # node has value
        self.next = None  # has next


"""Stacks are ordered LIFO"""


class StackLinked:
    # Method to initialize top
    def __init__(self):
        self.top = None
        self.size = 0
    # Check if stack size

    def size(self):
        return self.size
    # Check if stack is empty

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    # Add element

    def push(self, item):
        if self.top == None:
            self.top = Node(item)
        else:
            newNode = Node(item)
            newNode.next = self.top
            self.top = newNode
        self.size += 1

    # Remove element
    def pop(self):
        if self.isEmpty():
            return None
        else:
            poppedNode = self.top
            self.top = self.top.next
            poppedNode.next = None
            self.size -= 1
            return poppedNode.item
     # Returns the top node item

    def peek(self):
        if self.isEmpty():
            return None

        else:
            return self.top.item

    def display(self):
        nodeiter = self.top
        if self.isEmpty():

            print("\nStack is empty")

        else:

            while(nodeiter != None):
                print(nodeiter.item, "-", end=" ")
                nodeiter = nodeiter.next
            print("\nThe length of stack is", self.size)


stack = StackLinked()
print("\nTop element is", stack.peek())
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
stack.push(25)
stack.push(30)

print("\n\nTop element is: ", stack.peek())

stack.display()
stack.pop()
print("\nTop element is", stack.peek())
stack.display()
