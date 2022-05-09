n, a, b = list(map(int, input().split()))

somesums = 0

for i in range(1, n+1):
    x = str(i)
    l = len(x)
    sums = 0
    for j in range(0, l):
        sums += int(x[j])
    if a<= sums and sums <= b:
        somesums += i

print(somesums)
