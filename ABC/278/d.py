n = int(input())
a = list(map(int, input().split()))
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]

for i in range(q):
    t = query[i][0]
    if t == 1:
        x = query[i][1]
        a = list(map(lambda val: 1, a))
    if t == 2:
        j = query[i][1]
        x = query[i][2]
        a[j-1] += x
    if t == 3:
        j = query[i][1]
        print(a[j-1])