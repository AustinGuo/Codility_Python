# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    P = [0] * N

    if A[0] > A[1]:
        P[0] = 1
    for i in range(1, N-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            P[i] = 1
    if A[N-1] > A[N-2]:
        A[N-1] = 1

    F = 0
    i = 2
    while (i*i) < N:
        Fa = L = 0
        for p in P:
            if p == 1 and L >= i:
                Fa += 1
                L == 0
                
            L += 1
            
        if Fa > F:
            F = Fa
        i += 1
            
    return F
