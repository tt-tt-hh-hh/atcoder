n = int(input())
a = list(map(int, input().split()))

lx = []
ly = []
lz = []
cnt = 0
for i in range(n):
    ai = a[i]
    x, y = 0, 0
    
    while ai%2==0:
        x += 1
        ai //= 2
    
    while ai%3==0:
        y += 1
        ai //= 3
    
    lx.append(x)
    ly.append(y)
    lz.append(ai)

if len(set(lz)) != 1:
    print(-1)
    exit()

x_min = min(lx)
y_min = min(ly)

for i in range(n):
    cnt += lx[i]-x_min
    cnt += ly[i]-y_min


print(cnt)