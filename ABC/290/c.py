from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

#a.sort()
ans = 0
d = defaultdict(int)

for i in range(n):
    d[a[i]] += 1


for i in range(k):
    if d[i]>0:
        pass
    else:
        ans = i
        print(ans)
        exit()

    if i == k-1:
        print(k)