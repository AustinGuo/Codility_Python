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
    M = max(A)
    C = getNumList(A)
    F = getPrimeFactor(M)
    
    divisors = {}
    for element in A:
        divisors[element] = [1]
    
    divisor = 2
    while (divisor*divisor) <= M:
        multiple = divisor
        while multiple <= M:
            if C[multiple] != 0 and not divisor in divisors[multiple]:
                divisors[multiple].append(divisor)
            multiple += divisor
        divisor += 1
        
    R = [N] * N
    for i in range(N):
        for div in divisors[A[i]]:
            y = int(A[i]/div)
            if y >= div:
                R[i] -= C[div]
                if y > div:
                    R[i] -= C[y]
    
    return R
