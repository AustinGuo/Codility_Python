def solution(S, P, Q):
    # write your code in Python 3.6
    
    def matAdd(A, B):
        if len(A) != len(B):
            return A
        res = []
        for i in range(len(A)):
            res.append(A[i] + B[i])
        return res
    
    def matDec(A, B):
        if len(A) != len(B):
            return A
        res = []
        for i in range(len(A)):
            res.append(B[i] - A[i])
        return res
        
    def getPrefix(S):
        prefix = [[0, 0, 0, 0]] * (N+1)
        for i, c in enumerate(S):
            if c == 'A':
                prefix[i+1] = matAdd(prefix[i], [1, 0, 0, 0])
            elif c == 'C':
                prefix[i+1] = matAdd(prefix[i], [0, 1, 0, 0])
            elif c == 'G':
                prefix[i+1] = matAdd(prefix[i], [0, 0, 1, 0])
            elif c == 'T':
                prefix[i+1] = matAdd(prefix[i], [0, 0, 0, 1])
        return prefix
        
    def getResult(S, A, B):
        return matDec(S[A], S[B])
    
    N = len(S)
    M = len(P)
    prefixS = getPrefix(S)
    ans = []
    
    for K in range(M):
        res = getResult(prefixS, P[K], Q[K]+1)
        if res[0] > 0:
            ans.append(1)
        elif res[1] > 0:
            ans.append(2)
        elif res[2] > 0:
            ans.append(3)
        else:
            ans.append(4)

    return ans