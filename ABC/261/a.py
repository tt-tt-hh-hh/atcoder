L1, R1, L2, R2 = list(map(int, input().split()))

l = max(L1, L2)
r = min(R1, R2)

d = r - l

if d > 0:
    print(d)
else:
    print(0)

