n, m = map(int, input().split())
INF = 10**18
ans = INF

for a in range(1,INF):
    b = (m+a-1)//a

    if a > b:
        break
    if b <= n:
        ans = min(ans,a*b)

print(ans if ans < INF else -1)