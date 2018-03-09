# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N < 2:
        return 0
    P = 0
    candP = 0
    Q = 1
    for i in range(1, N):
        if A[i] > A[Q]:
            Q = i
        if A[i] < A[candP]:
            candP = i
        if A[P]-A[candP] > A[Q]-A[i]:
            P = candP
            Q = i
    if A[Q] - A[P] < 0:
        P = Q

    return A[Q] - A[P]