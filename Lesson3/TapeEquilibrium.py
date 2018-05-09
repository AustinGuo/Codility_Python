# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    P = 1000
    for i in range(1, N):
        P = min(abs(sum(A[:i])-sum(A[i:])), P)
    return P
