n = int(input())
card = [list(input().split()) for _ in range(n)]

taro = 0
hanako = 0

for i in range(n):
    if card[i][0] == card[i][1]:
        taro += 1
        hanako += 1
    elif card[i][0] > card[i][1]:
        taro += 3
    elif card[i][0] < card[i][1]:
        hanako += 3

print(taro, hanako)
