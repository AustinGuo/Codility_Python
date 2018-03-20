# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def getPrimeFactor(n):
    F = [0] * (n+1)
    i = 2
    while (i*i) <= n:
        if F[i] == 0:
            a = i * i
            while a <= n:
                if F[a] == 0:
                    F[a] = i
                a += i
        i += 1
    return F
    
def getNumSemi(n):
    F = getPrimeFactor(n)
    NS = [0] * (n+2)
    c = 0
    for i in range(n+1):
        if F[i] != 0 and F[int(i/F[i])] == 0:
            c += 1
        NS[i+1] = c
    return NS
    
def solution(N, P, Q):
    # write your code in Python 3.6
    M = len(P)
    R = [0] * M
    NS = getNumSemi(N)
    for i in range(M):
        R[i] = NS[Q[i]+1] - NS[P[i]]

    return R
