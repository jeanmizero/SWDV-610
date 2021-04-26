"""Three cannibals and three missionaries are on one side of a river, along with a boat that can hold one or two people"""


class Condition():
    def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
        self.cannibalLeft = cannibalLeft
        self.missionaryLeft = missionaryLeft
        self.boat = boat
        self.cannibalRight = cannibalRight
        self.missionaryRight = missionaryRight
        self.parent = None

      # set final state (0,0)
    def is_goal(self):
        if self.cannibalLeft == 0 and self.missionaryLeft == 0:
            return True
        else:
            return False

    def is_valid(self):
        if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
            return True
        else:
            return False
    # override to compare

    def __eq__(self, other):
        return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
            and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
            and self.missionaryRight == other.missionaryRight

    # Create set or dictionnary/ put elements in set
    def __hash__(self):
        return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))


def move(current_state):
    children = []

    if current_state.boat == 'LEFT BOAT':
        """Possible move of cannibals(C) and missionaries(M) on one trip.
           Move (2, 0)
           Move (1, 0)
           Move (1, 1)
           Move (0, 1)
           Move (0, 2)"""
        new_state = Condition(current_state.cannibalLeft, current_state.missionaryLeft - 2,
                              'RIGHT BOAT', current_state.cannibalRight, current_state.missionaryRight + 2)
        # 2 missionaries left to right.
        if new_state.is_valid():
            new_state.parent = current_state
            children.append(new_state)
        new_state = Condition(current_state.cannibalLeft - 2, current_state.missionaryLeft,
                              'RIGHT BOAT', current_state.cannibalRight + 2, current_state.missionaryRight)

        # 1 missionary and one cannibal left to right.
        if new_state.is_valid():
            new_state.parent = current_state
            children.append(new_state)
        new_state = Condition(current_state.cannibalLeft - 1, current_state.missionaryLeft - 1,
                              'RIGHT BOAT', current_state.cannibalRight + 1, current_state.missionaryRight + 1)

        # 2 cannibals left to right.
        if new_state.is_valid():
            new_state.parent = current_state
            children.append(new_state)
        new_state = Condition(current_state.cannibalLeft, current_state.missionaryLeft - 1,
                              'RIGHT BOAT', current_state.cannibalRight, current_state.missionaryRight + 1)

        # 1 missionary left to right.
        if new_state.is_valid():
            new_state.parent = current_state
            children.append(new_state)
        new_state = Condition(current_state.cannibalLeft - 1, current_state.missionaryLeft,
                              'RIGHT BOAT', current_state.cannibalRight + 1, current_state.missionaryRight)

        if new_state.is_valid():
            new_state.parent = current_state
            children.append(new_state)

    else:
        new_state = Condition(current_state.cannibalLeft, current_state.missionaryLeft + 2,
                              'LEFT BOAT', current_state.cannibalRight, current_state.missionaryRight - 2)
        # 2 missionaries right to left.
        if new_state.is_valid():
            new_state.parent = current_state
            children.append(new_state)
        new_state = Condition(current_state.cannibalLeft + 2, current_state.missionaryLeft,
                              'LEFT BOAT', current_state.cannibalRight - 2, current_state.missionaryRight)

        # 1 missionary and one cannibal right to left.
        if new_state.is_valid():
            new_state.parent = current_state
            children.append(new_state)
        new_state = Condition(current_state.cannibalLeft + 1, current_state.missionaryLeft + 1,
                              'LEFT BOAT', current_state.cannibalRight - 1, current_state.missionaryRight - 1)

        # 1 cannibal cross right to left.
        if new_state.is_valid():
            new_state.parent = current_state
            children.append(new_state)
        new_state = Condition(current_state.cannibalLeft, current_state.missionaryLeft + 1,
                              'LEFT BOAT', current_state.cannibalRight, current_state.missionaryRight - 1)

        #  1 missionary right to left.
        if new_state.is_valid():
            new_state.parent = current_state
            children.append(new_state)
        new_state = Condition(current_state.cannibalLeft + 1, current_state.missionaryLeft,
                              'LEFT BOAT', current_state.cannibalRight - 1, current_state.missionaryRight)

        if new_state.is_valid():
            new_state.parent = current_state
            children.append(new_state)
    return children

#  Using Breadth first and Depth first


def breadth_first_search():
    """A First-In-First-Out Queue."""
    initial_state = Condition(3, 3, 'LEFT BOAT', 0, 0)
    if initial_state.is_goal():
        return initial_state
    start = list()
    visited = set()

    start.append(initial_state)
    # Iterate until the queue become empty
    while start:
        # Remove and return the first item popped using indexing
        state = start.pop(0)
        if state.is_goal():
            return state
        visited.add(state)
        children = move(state)
        # Check node one by one
        for child in children:
            if (child not in visited) or (child not in start):
                start.append(child)
    return None

# Display output


def print_solution(solution):
    path = []
    path.append(solution)
    parent = solution.parent
    steps = 1

    while parent:
        path.append(parent)
        parent = parent.parent

    for index in range(len(path)):
        state = path[len(path) - index - 1]
        print("STEP " + str(steps) + ': ' + "(" + str(state.cannibalLeft) + "C" + "/" + str(state.missionaryLeft)
              + "M" + " " + state.boat + " " + str(state.cannibalRight) + "C" + "/" +
              str(state.missionaryRight) + "M" + ")")
        steps = steps + 1

        print()


def main():
    solution = breadth_first_search()
    print("Solution can be completed in 12 steps")
    print()
    print_solution(solution)


if __name__ == "__main__":
    main()
