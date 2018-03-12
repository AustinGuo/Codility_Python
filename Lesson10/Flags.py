# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    P = [0] * N

    for i in range(1, N-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            P[i] = 1

    F = 0
    i = 1
    while (i*i) <= N+1:
        Fa = 0
        L = i
        for p in P:
            if p == 1 and L >= i:
                Fa += 1
                L == 0
            if Fa == i:
                break;
            L += 1

        if Fa > F:
            F = Fa
        i += 1

    return F
