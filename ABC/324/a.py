n = int(input())
a = list(map(int, input().split()))

b = set(a)

if len(b) == 1:
    print('Yes')
else:
    print('No')