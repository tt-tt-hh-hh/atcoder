n, m = list(map(int, input().split()))

a = []
b = []

for _ in range(n):
    val = list(map(int, input().split()))
    a.append(val)

for _ in range(m):
    val = int(input())
    b.append(val)

for i in range(n):
    val = 0
    for j in range(m):
        val += a[i][j]*b[j]
    print(val)
