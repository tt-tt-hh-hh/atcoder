n, p, q = map(int, input().split())
D = list(map(int, input().split()))

d = min(D)
print(min(p, q+d))