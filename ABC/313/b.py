n, m = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]

human = [0]*n

for ab in AB:
    a, b = ab[0], ab[1]

    human[b-1] = 1

if human.count(0) == 1:
    print(human.index(0)+1)
else:
    print(-1)