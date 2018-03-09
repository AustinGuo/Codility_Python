# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    N = len(A)
    stack = []
    alive = 0
    upstream = -1
    for i in range(N):
        if B[i] == 1:
            if upstream != -1:
                stack.append(upstream)
            upstream = A[i]
        else:
            if upstream == -1:
                alive += 1
            else:
                while A[i] > upstream:
                    if len(stack) == 0:
                        upstream = -1
                        alive += 1
                        break
                    upstream = stack.pop()
                    
    if upstream > -1:
        alive += len(stack)+1
        
    return alive