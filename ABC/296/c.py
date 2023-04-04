n, x = map(int, input().split())
a = list(map(int, input().split()))

diff = set(a)

for i in diff:
    target = x+i
    if target in diff:
        print('Yes')
        exit()

print('No')
