# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    L = []
    for N in A:
        if N in L:
            L.remove(N)
        else:
            L.append(N)
    return L[0]
