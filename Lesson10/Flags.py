# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    dis = []
    count = 0

    for i in range(1, N-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            dis.append(count)
            count = 0
        count += 1

    F = 0
    i = 1
    while ((i-1)*(i-1)) < N:
        Fa = 0
        L = i
        for p in dis:
            L += p
            if L >= i:
                Fa += 1
                L = 0
            if Fa == i:
                break

        if Fa > F:
            F = Fa
        else:
            return F
        i += 1

    return F
