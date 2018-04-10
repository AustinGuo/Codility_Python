# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    dis = []
    count = 0

    # Get next peak distance
    for i in range(1, N-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            dis.append(count)
            count = 0
        count += 1

    maxR = len(dis)
    for i in range(maxR, 1, -1):
        posA = 0
        posB = 0
        for num in dis:
            posA += num
            if posB < posA:
                posB += i
                if posB < posA:
                    break
        else:
            return i

    return 0
