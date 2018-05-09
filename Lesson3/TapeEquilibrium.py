# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    P = 10000
    prefix = 0
    suffix = sum(A)
    for i in range(len(A)-1):
        prefix += A[i]
        suffix -= A[i]
        P = min(abs(prefix-suffix), P)
    return P
