def goldenLeader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in range(n):
        if (A[k] == candidate):
            count += 1
    if (count > n // 2):
        leader = candidate
    return leader

def solution(A):
    # write your code in Python 3.6
    leader = goldenLeader(A)
    leadc = 0
    n = len(A)
    for a in A:
        if a == leader:
            leadc += 1
    unleadc = n - leadc
    count = 0
    stack = 0
    for a in A:
        if a == leader:
            leadc -= 1
            stack += 1
        else:
            unleadc -= 1
            stack -= 1
        if stack > 0 and leadc > unleadc:
            count += 1
            
    return count
