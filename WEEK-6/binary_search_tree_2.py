# Create Tree class
class TreeNode:

    def __init__(self, key, left=None, right=None, parent=None):

        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    # Check to see if the tree already has a root

    def findRoot(self, key):
        if self.root:
            self.insertNode(key, self.root)
        else:
            self.root = TreeNode(key)
        self.size = self.size + 1

    def insertNode(self, key, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self.insertNode(key, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self.insertNode(key, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, parent=currentNode)

    def preorderPrint(self, currentNode, level):
        """Root -> Left ->Right"""
        if currentNode.hasLeftChild() and currentNode.hasRightChild():
            print(str(currentNode.key), end=" ")
            self.preorderPrint(currentNode.hasLeftChild(), level + 1)
            self.preorderPrint(currentNode.hasRightChild(), level + 1)

        elif currentNode.hasLeftChild() and (not currentNode.hasRightChild()):
            print(str(currentNode.key), end=" ")
            self.preorderPrint(currentNode.hasLeftChild(), level + 1)

        elif (not currentNode.hasLeftChild()) and currentNode.hasRightChild():
            print(str(currentNode.key), end=" ")
            self.preorderPrint(currentNode.hasRightChild(), level + 1)

        else:
            print(str(currentNode.key), end=" ")

    def inorderPrint(self, currentNode, level):
        """Left -> Root ->Right"""
        if currentNode.hasLeftChild() and currentNode.hasRightChild():
            self.inorderPrint(currentNode.hasLeftChild(), level + 1)
            print(str(currentNode.key), end=" ")
            self.inorderPrint(currentNode.hasRightChild(), level + 1)

        elif currentNode.hasLeftChild() and (not currentNode.hasRightChild()):
            self.inorderPrint(currentNode.hasLeftChild(), level + 1)
            print(str(currentNode.key), end=" ")

        elif (not currentNode.hasLeftChild()) and currentNode.hasRightChild():
            print(str(currentNode.key), end=" ")
            self.inorderPrint(currentNode.hasRightChild(), level + 1)

        else:
            print(str(currentNode.key), end=" ")

    def postorderPrint(self, currentNode, level):
        """Left->Right->Root"""
        if currentNode.hasLeftChild() and currentNode.hasRightChild():
            self.postorderPrint(currentNode.hasLeftChild(), level + 1)
            self.postorderPrint(currentNode.hasRightChild(), level + 1)
            print(str(currentNode.key), end=" ")

        elif currentNode.hasLeftChild() and (not currentNode.hasRightChild()):
            self.postorderPrint(currentNode.hasLeftChild(), level + 1)
            print(str(currentNode.key), end=" ")

        elif (not currentNode.hasLeftChild()) and currentNode.hasRightChild():
            self.postorderPrint(currentNode.hasRightChild(), level + 1)
            print(str(currentNode.key), end=" ")

        else:
            print(str(currentNode.key), end=" ")

    def printtree(self):
        self.preorderPrint(self.root, 0)
        print()
        self.inorderPrint(self.root, 0)
        print()
        self.postorderPrint(self.root, 0)
        print()


def main():

    stru = BinarySearchTree()
    L = [50, 30, 23, 11, 25, 35, 31, 42, 70, 80, 73, 85]

    for i in range(len(L)):

        stru.findRoot(L[i])

    stru.printtree()


if __name__ == "__main__":
    main()
