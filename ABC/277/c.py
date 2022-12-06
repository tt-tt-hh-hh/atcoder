n = int(input())
g = {}
ans = 1

for i in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if g.get(a) == None:
        g[a] = [b]
    else:
        g[a] += [b]
    
    if g.get(b) == None:
        g[b] = [a]
    else:
        g[b] += [a]

for i in g.items():
    goal = [False] * (len(g)+1)
    dfs(g[i])
    

