# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    P = [0] * N

    if N == 1:
        return 1

    if A[0] > A[1]:
        P[0] = 1
    for i in range(1, N-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            P[i] = 1
    if A[N-1] > A[N-2]:
        P[N-1] = 1

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
