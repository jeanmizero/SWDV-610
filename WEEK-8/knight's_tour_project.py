import sys


class NodeKnightsTour:
    # Represents a node of array tree with cordinate X and Y
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.board = []
        self.buildBoard()

    # Function to build the full board for two dimension(i,j) board
    def buildBoard(self):
        for i in range(self.y):
            self.board.append([0] * self.x)

    # Minimum steps for a knight from start to the end for an n-by-n board
    def legalMoveToReachTarget(self, currentPosition):
        newMoves = []
        # Eight possible moves where x and y(knigh) can move/left or right
        moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                       (1, -2), (1, 2), (2, -1), (2, 1)]
        # Generates Eight possible
        for move in moveOffsets:
            newX = currentPosition[0] + move[0]
            newY = currentPosition[1] + move[1]

            if (newX >= self.y):
                continue
            elif (newX < 0):
                continue
            elif (newY >= self.x):
                continue
            elif (newY < 0):
                continue
            else:
                newMoves.append((newX, newY))
        return newMoves

    # Makes sure that a particular move that is generated is still on the board.
    def isStillOnBoard(self, x, currentPosition):
        if x >= 0 and x < currentPosition:
            return True
        else:
            return False

    # Display
    def printChessBoard(self):
        print("  ")
        for element in self.board:
            print(element)
        print("********************************")
        print("  ")

    # The Breadth First Search algorithm for solving the knight’s tour problem by explicitly forbidding a node to be visited more than once
    def knightTourBFS(self, n, path, nodeToVisit):
        """n = current depth in the search tree
           path = list of vertices visited up to this point
           nodeToVisit = node to visit"""

        self.board[nodeToVisit[0]][nodeToVisit[1]] = n
        # Add the newest vertex/queue to the path
        path.append(nodeToVisit)
        # Check every square box is filled
        if n == self.x * self.y:
            self.printChessBoard()
            print(path)
            print()
            print("Done!")
            sys.exit(0)

        else:
            sortedCorners = self.knightTourWarnsdorffSort(nodeToVisit)
            for conner in sortedCorners:
                self.knightTourBFS(n + 1, path, conner)

            self.board[nodeToVisit[0]][nodeToVisit[1]] = 0
            try:
                path.pop()  # to backtrack
            except IndexError:
                sys.exit(0)

        # Use Warnsdorff’s algorithm called a heuristic find a solution close to the best one and they find it fast and easily
        # This knight will visit the hard-to-reach corners early and can use the middle squares to hop across the board only when necessary
    def knightTourWarnsdorffSort(self, nodeToVisit):
        connersList = self.legalMoveToReachTarget(nodeToVisit)
        emptyConnerSquares = []

        for conner in connersList:
            getValue = self.board[conner[0]][conner[1]]
            if getValue == 0:
                emptyConnerSquares.append(conner)

        availableMoveList = []
        for empty in emptyConnerSquares:
            availableMove = [empty, 0]
            moves = self.legalMoveToReachTarget(empty)

            for move in moves:
                if self.board[move[0]][move[1]] == 0:
                    availableMove[1] += 1
            availableMoveList.append(availableMove)
         # We select the vertex to go next that has the fewest available moves by using lambda
        availableMoveListSort = sorted(availableMoveList, key=lambda s: s[1])
        sortedCorners = [s[0] for s in availableMoveListSort]
        return sortedCorners


if __name__ == '__main__':

    # Chessboard of 8x8 size
    knightTour = NodeKnightsTour(5, 5)
    #knightTour = NodeKnightsTour(8, 8)
    knightTour.knightTourBFS(1, [], (0, 0))
    knightTour.printChessBoard()
