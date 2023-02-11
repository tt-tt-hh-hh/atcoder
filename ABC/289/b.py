n, m = map(int, input().split())
a = list(map(int, input().split()))
l = []
num = []
ans = []
for i in range(1,n+1):
    num.append(i)

for i in range(n+1):
    if i not in a:
        l.append(i)


for i in range(len(l)-1):
    ll = num[l[i]:l[i+1]]
    ll.reverse()
    ans += ll

print(*ans)