# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    def fibonacci(n, m):
        fib = [0] * (n + 2)
        fib[1] = 1
        a = 2 ** m
        for i in range(2, n + 2):
            fib[i] = (fib[i - 1] + fib[i - 2]) % a

        return fib[1:]

    def sqare(n):
        sqr = [1] * (n + 1)
        for i in range(1, n + 1):
            sqr[i] = sqr[i - 1] * 2
        return sqr

    fib_list = fibonacci(max(A), max(B))
    aqr_list = sqare(max(B))

    return list(map(lambda x,y: fib_list[x] % aqr_list[y], A, B))