def getLeader(A):
    size = 0
    count = 0
    leader = -1
    candidate = -1
    for a in A:
        if size == 0:
            candidate = a
            size += 1
        elif a == candidate:
            size += 1
        else:
            size -= 1
    if size == 0:
        return leader
    for a in A:
        if a == candidate:
            count += 1
    if count > len(A)//2:
        leader = candidate
    
    return leader

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    leader = getLeader(A)
    if leader == -1:
        return -1
        
    for i in range(n):
        if A[i] == leader:
            return i
            
    return -1
