# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    gap = 0
    maxGap = 0
    
    while N > 0 and N & 1 != 1:
        N >>= 1
        
    while N > 0:
        if N & 1 == 1:
            maxGap = max(maxGap, gap)
            gap = 0
        else:
            gap += 1
        N >>= 1
        
    return maxGap
