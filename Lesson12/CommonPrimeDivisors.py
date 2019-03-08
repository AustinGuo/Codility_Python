# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    def gcd(a, b):
        return b if a % b == 0 else gcd(b, a % b)

    def gce(num_gcd, y):
        x = gcd(num_gcd, y)
        if x == y:
            return True
        elif x == 1:
            return False

        return gce(num_gcd, y // x)

    ans = 0

    for i in range(len(A)):
        gcd_num = gcd(A[i], B[i])
        if gce(gcd_num, A[i]) and gce(gcd_num, B[i]):
            ans += 1

    return ans