# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    result = 0
    i = 1
    while (i * i < N):
        if N % i == 0:
            result += 2
            
        i += 1
        
    if (i*i) == N:
        result += 1
        
    return result
