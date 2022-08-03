n = int(input())
a = [input().split() for _ in range(n)]


card = [[0 for _ in range(13)] for _ in range(4)]

for i in range(n):
    egara = a[i][0]
    num = int(a[i][1]) - 1

    if egara == 'S':
        card[0][num] = 1
    elif egara == 'H':
        card[1][num] = 1
    elif egara == 'C':
        card[2][num] = 1
    elif egara == 'D':
        card[3][num] = 1

for i in range(4):
    for j in range(13):
        if card[i][j] == 0:
            if i == 0:
                print('S' + ' ' + str(j+1))
            elif i == 1:
                print('H' + ' ' + str(j+1))
            elif i == 2:
                print('C' + ' ' + str(j+1))
            elif i == 3:
                print('D' + ' ' + str(j+1))
