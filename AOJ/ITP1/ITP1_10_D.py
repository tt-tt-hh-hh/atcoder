import math
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
xy = []
d = 0

for i in range(n):
    xy.append(abs(x[i]-y[i]))

for i in range(1, 4):
    d = 0
    for j in range(n):
        d += pow(xy[j],i)
    
    print(d**(1/i))

print(max(xy))

