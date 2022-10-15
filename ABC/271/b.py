n, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
st = [list(map(int, input().split())) for _ in range(q)]

for i in range(q):
    s, t = st[i][0], st[i][1]

    print(a[s-1][t])
