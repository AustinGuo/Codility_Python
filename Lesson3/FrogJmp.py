# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    return (Y-X)//D if (Y-X)%D == 0 else (Y-X)//D+1
