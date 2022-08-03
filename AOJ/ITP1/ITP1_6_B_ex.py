n = int(input())

all_cards = [(x, y) for x in ['S', 'H', 'C', 'D'] for y in range(1, 14)]
hold_cards = []

for _ in range(n):
    suit, num = input().split()
    num = int(num)
    hold_cards.append((suit, num))

for card in all_cards:
    if card not in hold_cards:
        print(*card)