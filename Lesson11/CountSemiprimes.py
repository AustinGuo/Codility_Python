# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, P, Q):
    # write your code in Python 3.6
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
    
    F = getPrimeFactor(N)
    M = len(P)
    R = [0] * M
    for i in range(M):
        for x in range(P[i], Q[i]+1):
            if F[x] != 0 and F[int(x/F[x])] == 0:
                R[i] += 1
                
    return R
