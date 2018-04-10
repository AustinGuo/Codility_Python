# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    dis = []
    count = 1

    # Get next peak distance
    for i in range(1, N-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            dis.append(count)
            count = 0
        count += 1

    maxR = len(dis)
    for i in range(maxR, 0, -1):
        if N % i != 0:
            continue
        block = int(N/i)
        posA = 0
        posB = 0
        for num in dis:
            posA += num
            if posB < posA:
                posB += block
                if posB < posA:
                    break
        if posB == N:
            return i

    return 0
