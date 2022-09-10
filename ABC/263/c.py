import itertools

n, m = list(map(int, input().split()))
l = list(range(1,m+1))

p = itertools.permutations(l,n)

for v in p:
    for i in range(n):
        if i+1 == n:
            print(*v)
        elif v[i] < v[i+1]:
            continue
        else:
            break



