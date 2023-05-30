import math

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))

ans = combinations_count(n,2)

nakayoshi = set()

for i in range(m):
    for j in range(n-1):
        s = a[i][j]
        t = a[i][j+1]

        if s > t:
            fuga = str(s)+str(t)
        elif t > s:
            fuga = str(t)+str(s)
        else:
            fuga = str(s)+str(t)

        nakayoshi.add(fuga)

print(ans-len(nakayoshi))

