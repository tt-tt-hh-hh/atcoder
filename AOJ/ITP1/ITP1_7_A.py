l = []

while True:
    result = list(map(int, input().split()))
    if result.count(-1) == 3:
        break
    l.append(result)

for i in range(len(l)):
    m = l[i][0]
    f = l[i][1]
    r = l[i][2]

    score = m + f
    
    if m == -1 or f == -1 or score < 30:
        print('F')
    elif score >= 80:
        print('A')
    elif score >= 65 and score < 80:
        print('B')
    elif score >= 50 and score < 65:
        print('C')
    elif score >= 30:
        if r >= 50:
            print('C')
        else:
            print('D')


