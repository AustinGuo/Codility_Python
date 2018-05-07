# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    result = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if i+A[i] >= j-A[j]:
                result += 1
                
    if result > 10000000:
        result = 10000000
                
    return result
