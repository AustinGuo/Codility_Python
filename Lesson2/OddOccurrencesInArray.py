# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    preRes = 0
    numCount = 0
    
    # Resort the list of number
    A.sort()

    # Count the same number
    for N in A:
        
        # If same as last number, plus 1
        if preRes == N:
            numCount += 1
        
        # If diffrent as last number, judge compare nubmer if odd count
        elif numCount & 1 == 1:
            return preRes
        
        # Reset compare number and count
        else:
            preRes = N
            numCount = 1
    return preRes
