# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    def fibonacci(n):
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[2:]

    fib_list = fibonacci(max(A)+1)

    return list(map(lambda x,y: fib_list[x - 1] % 2 ** y, A, B))