cards = input().split()

for i in range(5):
    cnt = 0
    cnt = cards.count(cards[i])

    if cnt == 3 or cnt == 2:
        continue
    else:
        print('No')
        exit()

print('Yes')