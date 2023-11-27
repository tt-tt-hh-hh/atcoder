n, x = map(int, input().split())
A = list(map(int, input().split()))

ans = 300

for i in range(0,101):
    B = A.copy()
    B.append(i)

    B.remove(min(B))
    B.remove(max(B))

    if sum(B) - x >= 0:
        ans = min(ans, i)

if ans == 300:
    print(-1)
else:
    print(ans)