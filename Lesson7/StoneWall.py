# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    stone_stake = []
    stone_count = 1
    for i in range(1, len(H)):
        if H[i-1] > H[i]:
            while stone_stake:
                if stone_stake[-1] > H[i]:
                    stone_stake.pop()
                    stone_count += 1
                elif stone_stake[-1] < H[i]:
                    stone_count += 1
                    break
                elif stone_stake[-1] == H[i]:
                    stone_stake.pop()
                    stone_count += 1
                    break
            else:
                stone_count += 1
        elif H[i-1] < H[i]:
            stone_stake.append(H[i-1])
    return stone_count + len(stone_stake)

H = [8,8,5,7,9,8,7,4,8]
print(solution(H))