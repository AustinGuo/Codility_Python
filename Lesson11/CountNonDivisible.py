# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Get the smallest factor in every number(if not prime number)
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
    C = getNumList(A)
    F = getPrimeFactor(M)
    R = [N] * N
    for i in range(N):
        R[i] -= C[1]
        if A[i] == 1:
            continue
        lastfac = 0
        x = A[i]
        while (F[x] > 0):
            
            # Avoid decrease factor number count repeat
            if F[x] != lastfac:
                R[i] -= C[F[x]]
                lastfac = F[x]
            R[i] -= C[x]
            x = int(x / F[x])
            
        # Check the last prime number if already be deceased.
        if x != lastfac:
            R[i] -= C[x]

    return R
