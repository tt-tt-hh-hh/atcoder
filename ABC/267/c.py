n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

tot = [0]
for i in range(n):
    tot.append(tot[-1]+a[i])

now = 0

for i in range(m):
    now += (i+1)*a[i]

ans = now

for i in range(n-m):
    minus = tot[i+m]-tot[i]
    plus = a[i+m]*m
    now += plus-minus
    ans = max(ans,now)

print(ans)