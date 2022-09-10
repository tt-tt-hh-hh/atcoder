x, y, n = list(map(int, input().split()))
ans = []

for i in range(200):
    for j in range(200):
        cnt = i + 3*j
        if cnt == n:
            cost = x*i + y*j
            ans.append(cost)

print(min(ans))
