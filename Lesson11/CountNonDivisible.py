# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    R = [0] * N
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] != 0:
                R[i] += 1
                
    return R
