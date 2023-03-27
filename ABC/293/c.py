import itertools

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

ans = 0
alllist = [_ for _ in range(h+w-2)]

for i in itertools.combinations(alllist, h-1):
    passed = set()
    x=0
    y=0

    passed.add(a[x][y])

    for j in range(h+w-2):
        if j in i:
            x += 1
        else:
            y += 1

        passed.add(a[x][y])

    if len(passed) == h+w-1:
        ans += 1

print(ans)

