n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b+1)
    g[b].append(a+1)

""" for i in range(n):
    l = len(g[i])
   
    g[i].sort()
    
    print(l, *g[i]) """

for i in g:
    l = len(i)
   
    i.sort()
    
    print(l, *i)
