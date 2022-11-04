n, k, x = map(int, input().split())
a = list(map(int, input().split()))
souwa = sum(a)
syou = 0
amari = []

for i in range(n):
    p = a[i]//x
    q = a[i]%x

    syou += p
    amari.append(q)

amari.sort()

if k<=syou:
    ans = souwa-x*k
    print(ans)
else:
    ans = souwa-x*syou
    for i in range(n-1,max(n-1-(k-syou),-1),-1):
        ans -= amari[i]

    print(ans)

