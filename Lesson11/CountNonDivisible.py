# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    M = max(A)
    C = [0] * (M+1)

    divisors = {}
    for element in A:
        C[element] += 1         # Get number count list
        divisors[element] = [1] # Create divisor list
    
    # In this for loop, we only find out all the
    # divisors less than sqrt(A_max), with brute
    # force method.
    divisor = 2
    while (divisor*divisor) <= M:
        multiple = divisor
        while multiple <= M:
            if C[multiple] != 0 and not divisor in divisors[multiple]:
                divisors[multiple].append(divisor)
            multiple += divisor
        divisor += 1
    
    
    # In this loop, we compute all the divisors
    # greater than sqrt(A_max), filter out some
    # duplicate ones, and combine them.
    for element in divisors:
        for div in divisors[element]:
            y = int(element/div)
            if not y in divisors[element]:
                divisors[element].append(y)

    # Decrease the number of divisors every element
    R = [N] * N
    for i in range(N):
        for div in divisors[A[i]]:
            R[i] -= C[div]
    
    return R
