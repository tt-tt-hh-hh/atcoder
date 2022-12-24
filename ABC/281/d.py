import itertools

n, k, d = map(int, input().split())
a = list(map(int, input().split()))

s = set()

for v in itertools.combinations(a,k):
    ss = sum(v)
    if ss%d == 0:
        s.add(ss)

#s.sort(reverse=True)
l = sorted(s,reverse=True)

for i in l:
    if i%d == 0:
        print(i)
        exit()

print(-1)