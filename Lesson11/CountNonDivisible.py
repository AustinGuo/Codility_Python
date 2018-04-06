# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Get the smallest factor in every number(if not prime number)
def getPrimeFactor(n):
    F = [True] * (n+1)
    F[0] = F[1] = False
    i = 2
    while (i*i) <= n:
        if F[i]:
            a = i * i
            while a <= n:
                F[a] = False
                a += i
        i += 1
    return F

# Get number count list
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
        Flag = [True] * (M+1)
        R[i] -= C[1]
        if A[i] == 1:
            continue
        R[i] -= C[A[i]]
        if F[A[i]]:
            continue
        x = 2
        while x*x <= A[i]:
            if not F[x] or A[i] % x != 0:
                x += 1
                continue
            y = int(A[i]/x)
            if x >= y:
                if y == x and Flag[y]:
                    R[i] -= C[y]
                    Flag[y] = False
                break
            if Flag[x]:
                R[i] -= C[x]
                Flag[x] = False
            if Flag[y]:
                R[i] -= C[y]
                Flag[y] = False
            z = x * x
            while z <= A[i]:
                if A[i] % z == 0:
                    y = int(A[i]/z)
                    if z >= y:
                        if y == z and Flag[y]:
                            R[i] -= C[y]
                            Flag[y] = False
                        break
                    if Flag[z]:
                        R[i] -= C[z]
                        Flag[z] = False
                    if Flag[y]:
                        R[i] -= C[y]
                        Flag[y] = False
                z += x
            x += 1
       
    return R
