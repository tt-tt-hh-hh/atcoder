from collections import deque

n, x, y = list(map(int, input().split()))
g = [[] for _ in range(n)]

for _ in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

q = deque()
q.append
