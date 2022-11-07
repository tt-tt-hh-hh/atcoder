from collections import defaultdict

INF = (1<<62)-1

def solve():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]
    S = input()
    l_max = defaultdict(lambda: -INF)
    r_min = defaultdict(lambda: INF)

    for s, (x,y) in zip(S, XY):
        if s == 'L':
            l_max[y] = max(l_max[y], x)
        else:
            r_min[y] = min(r_min[y], x)

    for y in l_max.keys():
        if r_min[y] < l_max[y]:
            return True
    return False

print('Yes' if solve() else 'No')

    
