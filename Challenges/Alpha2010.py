def solution(A):
    N = len(A)
    P = 0
    numList = [0] * (N+1)

    for i in range(N):
        if numList[A[i]] == 0:
            P = i
            numList[A[i]] = 1

    return P
