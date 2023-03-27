n, q = map(int, input().split())
minN = 1

gone = set()

for i in range(q):
    e = list(map(int, input().split()))
    if e[0] == 1:
        continue
    elif e[0] == 3:
        while True:
            if minN not in gone:
                print(minN)
                break
            else:
                minN += 1
    else:
        x = e[1]
        gone.add(x)
