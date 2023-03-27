from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
ans = 0

d = defaultdict(int)

for key in a:
    d[key] += 1

for v in d.values():
    ans += v//2

print(ans)
