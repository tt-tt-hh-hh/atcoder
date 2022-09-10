from collections import deque
n = int(input())
p = list(map(int, input().split()))
ans = 0

d = deque()
idx = p.index(0)

for i in p:
    d.append(i)

for i in range(n):
    d.rotate(i)
    #b = (i-1)%n
    #f = (i+1)%n
    buf = 0
    for j in range(n):
        b = (j-1)%n
        f = (j+1)%n
        if d[b] == j or d[f] == j or d[j] == j:
            buf += 1

    ans = max(ans, buf)

print(ans)