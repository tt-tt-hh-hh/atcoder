n = int(input())
a = list(map(int, input().split()))
ope = [0] * n


for i in range(0, n):
    x = a[i]
    while x%2 == 0:
        ope[i] += 1
        x = x/2

print(min(ope))