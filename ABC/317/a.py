n, h, x = map(int, input().split())
P = list(map(int, input().split()))

for i in range(n):
    p = P[i]
    if p+h >= x:
        print(i+1)
        exit()