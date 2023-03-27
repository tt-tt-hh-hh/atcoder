n, q = map(int, input().split())
event = [list(map(int, input().split())) for _ in range(q)]

card = [0]*n

for i in range(q):
    p, c = event[i]

    if p == 1:
        card[c-1] += 1
    elif p == 2:
        card[c-1] += 2
    elif p == 3:
        if card[c-1] >= 2:
            print('Yes')
        else:
            print('No')