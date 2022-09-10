n = int(input())
M = 998244353

r = n%M

for i in range(M):
    if i%M == r:
        print(i)
        exit()