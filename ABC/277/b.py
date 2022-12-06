n = int(input())
mark = ['H', 'D', 'C', 'S']
num = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
card = {}

for i in mark:
    for j in num:
        card[i+j] = False

S = [input() for _ in range(n)]

for i in S:
    s = i
    if card.get(s) == None or card.get(s) == True:
        print('No')
        exit()
    
    card[s] = True

print('Yes')
    
