# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    # write your code in Python 3.6
    def getPrefix(S):
        N = len(S)
        prefix = [0] * (N+1)
        for i in range(N):
            prefix[i +1] = prefix[i] + S[i]
            return prefix

    def preSlice(S, A, B):
            return S[B] - S[A]

    N = len(A)
    minN = 10000
    minPos = 0
    prefixA = getPrefix(A)
    for i in range(N-2):
        sliceTwo = preSlice(prefixA, i, i+2)/2
        if minN > sliceTwo:
            minPos = sliceTwo
            mPos = i
        sliceThree = preSlice(prefixA, i, i+3)/3
        if minN > sliceThree:
            minN = sliceThree
            minPos = i

    # The last one "TwoSlice"
    sliceTwo = preSlice(prefixA, N-2, N)/2
    if minN > sliceTwo:
        minN = sliceTwo
        minPos = N-2

    return minPos
