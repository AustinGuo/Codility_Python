# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    M = max(A)
    L = [0] * (M+1)
    for N in A:
        L[N] += 1
        
    for i in range(M+1):
        if L[i] & 1 == 1:
            return i
            
    return -1
