a, b, x = list(map(int, input().split()))

if a == 0:
    count = (b//x + 1)

count = (b//x + 1) - ((a-1)//x + 1)
print(count)