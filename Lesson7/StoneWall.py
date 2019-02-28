# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    stone = [0]*len(H)
    stone_count = 0
    for i, a in enumerate(H):
        if stone[i] == H[i]:
            continue
        stone_height = a
        stone[i] = stone_height
        stone_count += 1
        for j in range(i+1, len(H)):
            if stone_height > H[j]:
                if stone[j] == H[j]:
                    break
                stone_count += 1
                stone_height = H[j]
            stone[j] = stone_height

    return stone_count