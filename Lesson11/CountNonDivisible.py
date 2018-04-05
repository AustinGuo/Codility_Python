# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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
    R = [N] * N
    for i in range(N):
        x = 1
        while True:
            if A[i] % x == 0:
                y = int(A[i]/x)
                if x >= y:
                    if y == x:
                        R[i] -= C[y]
                    break
                R[i] -= C[x]
                R[i] -= C[y]
            x += 1
    return R
