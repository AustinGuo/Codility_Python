# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    R = [0] * N
    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] % A[j] != 0:
                R[i] += 1
            if A[j] % A[i] != 0:
                R[j] += 1
                
    return R
