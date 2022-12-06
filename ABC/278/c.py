from collections import defaultdict

n, q = map(int, input().split())
g = defaultdict(set)
tab = [list(map(int, input().split())) for _ in range(q)]

def plus(a,b):
    g[a].add(b)

def minus(a,b):
    g[a].discard(b)

for i in range(q):
    #t, a, b = map(int, input().split())
    t, a, b = tab[i]
    if t == 1:
        plus(a,b)
    if t == 2:
        minus(a,b)
    if t == 3:
        f1 = a in g[b]
        f2 = b in g[a]
        if f1 == True and f2 == True:
            print('Yes')
        else:
            print('No')