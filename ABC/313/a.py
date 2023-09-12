n = int(input())
p = list(map(int, input().split()))

if n == 1:
    print(0)
    exit()

p1 = p[0]
p_other = p[1:]
maxp = max(p_other)

if p1 > maxp:
    print(0)
elif p1 == maxp:
    print(1)
else:
    print(maxp-p1+1)
