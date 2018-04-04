# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def getPrimeFactor(n):
    F = [True] * (n+1)
    F[0] = F[1] = False
    i = 2
    while (i*i) <= n:
        if F[i] == True:
            a = i * i
            while a <= n:
                F[a] = False
                a += i
        i += 1
    return F

def getNumList(A):
    N = len(A)*2
    F = [0] * (N+1)
    for n in A:
        F[n] += 1
    
    return F

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    M = N*2
    F = getPrimeFactor(M)
    C = getNumList(A)
    R = [N] * N
    for i in range(N):
        num = A[i]
        R[i] -= C[1]
        a = 2
        while (a*a) <= num:
            if num % a == 0:
                R[i] -= C[a]
                b = a * a
                while b <= num:
                    R[i] -= C[b]
                    b += a
            a += 1

    return R
