# you can write to stdout for debugging purposes, e.g.# print("this is a debug message")
def solution(A):
    # write your code in Python 3.6
    N = len(A)
    maxEnd = maxSlice = A[0]
    for i in range(1, N):
        if maxSlice > 0:
            maxEnd = max(0, maxEnd + A[i])
            maxSlice = max(maxSlice, maxEnd)
        elif A[i] > maxSlice:
            maxEnd = maxSlice = A[i]
    
    return maxSlice
