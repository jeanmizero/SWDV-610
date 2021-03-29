mylist = [5, 7, 10, 12, 15, 18, 22, 24, 30, 37, 42, 49, 56, 73]


def findMin(mylist):
    # Base case
    if len(mylist) == 0:
        return
    elif len(mylist) == 1:
        return mylist[0]
    return min(mylist[0], findMin(mylist[1:]))


def findMax(mylist):
    # Base case
    if len(mylist) == 0:
        return
    elif len(mylist) == 1:
        return mylist[0]
    return max(mylist[0], findMax(mylist[1:]))


def reverse(mylist):
  # Base case
    if len(mylist) == 0:
        return
    elif len(mylist) == 1:
        return mylist
    return mylist[len(mylist) - 1:] + reverse(mylist[0:len(mylist) - 1])


print(findMin(mylist))
print(findMax(mylist))
print(reverse(mylist))
