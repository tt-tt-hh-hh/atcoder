N, T = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)
t = T%s

for i in range(N):
    if t > a[i]:
        t -= a[i]
    else:
        print(i+1,t)
        exit()

