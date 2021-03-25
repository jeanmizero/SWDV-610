# Fibonacci sequence up to n-th term using recursive functions
import time


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


nterms = 10
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
for i in range(nterms):
    print(recur_fibo(i))
print()


# Iterative approach

nterm = 10


def fib_iter(nterm):
    a, b = 0, 1
    if nterm == 0:
        print(a)
    else:
        print("Fibonacci iterative sequence:")
        print(a)
        print(b)

        for i in range(2, nterm):
            c = a + b
            a = b
            b = c
            print(c)


fib_iter(nterm)

if __name__ == "__main__":
    init = time.time()
    print(f"It took {time.time() - init} second")
