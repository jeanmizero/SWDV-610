
class Node:
    # Constructor to initialize node
    def __init__(self, item):
        self.item = item
        self.next = None


class QueueLinked:
    # Method to initialize top
    def __init__(self):
        self.top = None
        self.bottom = None
    # Method to add an element data in the Queue

    def enqueue(self, item):
        if self.bottom == None:
            self.top = Node(item)
            self.bottom = self.top
        else:
            self.bottom.next = Node(item)
            self.bottom = self.bottom.next

    # Method to remove first element
    def dequeue(self):
        if self.top == None:
            return None
        else:
            newNode = self.top.item
            self.top = self.top.next
            return newNode

    # Method to return top element in the queue

    def first(self):
        return self.top.item

    # Check if queue size
    def size(self):
        newNode = self.top
        count = 0
        while(newNode != None):
            count = count+1
            newNode = newNode.next
        return count

    # Check if queue is empty
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    # Method to print the stack

    def display(self):
        print("Queue elements are:")
        newNode = self.top
        while (newNode != None):
            print(newNode.item, "-", end=" ")
            newNode = newNode.next


queue = QueueLinked()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)
queue.enqueue(25)
queue.enqueue(30)
queue.display()

print("\nFirst element is: ", queue.first())

print("The length of the queue is ", queue.size())
queue.dequeue()
queue.dequeue()

print("\n\nApply Fist In Fist Out")
queue.display()
print("\nThe length of the queue is ", queue.size())
