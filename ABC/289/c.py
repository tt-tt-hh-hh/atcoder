import itertools

n, m = map(int, input().split())
c = []
s = []
for i in range(m):
    c.append(int(input()))
    s.append(list(map(int, input().split())))

a = {i for i in range(1,n+1)}

ans = 0

l = (list(itertools.product(range(2), repeat = m)))

for i in range(1,len(l)):
    b = set()
    for j in range(m):
        if l[i][j] == 1:
            b |= set(s[j])
    
    if a == b:
        ans += 1

print(ans)