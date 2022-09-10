s = input()

rows = [[0], [0], [0,0], [0,0], [0,0], [0], [0]]
row = {'row0':False, 'row1':False, 'row2':False, 'row3':False, 'row4':False, 'row5':False, 'row6':False}

for i in range(10):
    if i == 6 and s[i] == '1':
        row['row0'] = True
    elif i == 3 and s[i] == '1':
        row['row1'] = True
    elif (i == 7 or i == 1) and s[i] == '1':
        row['row2'] = True
    elif (i == 4 and i == 0) and s[i] == '1':
        row['row3'] = True
    elif (i == 8 or i == 2) and s[i] == '1':
        row['row4'] = True
    elif i == 5 and s[i] == '1':
        row['row5'] = True
    elif i == 9 and s[i] == '1':
        row['row6'] = True

if s[0] == 1:
    print('No')

for i in range(7):
    for j in range(7):
        if j - i >= 2:
            if row['row'+str(i)] == True and row['row'+str(j)]:
                for k in range(i+1, j):
                    if row['row'+str(k)] == False:
                        print('Yes')
                        exit()

print('No')                   





