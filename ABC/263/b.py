n = int(input())
p = list(map(int, input().split()))
l = [0, 0]
p = l + p
cnt = 0
i = n

while i > 1:
    oya = p[i]

    if i != 0:
        cnt += 1
        i = oya
        continue
    else:
        break

print(cnt)