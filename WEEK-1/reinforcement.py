# Exercise 1
n = int(input("Enter an integer: "))
m = int(input("Enter another integer: "))


def is_multiple(n, m):
    """ If n is a multiple of m, that means n is evenly divisible by m. 16 is a multiple of 2"""
    if n % m == 0:
        return True
    else:
        return False


print(is_multiple(n, m))

# Exercise 2
"""range() is a built-in function of Python. It is used when a user needs to perform an action for a specific number of times"""
for i in range(100):
    print("I will never spam my friends again.")
