S = [list(input()) for _ in range(8)]

for i in range(8):
    for j in range(8):
        if S[i][j] == '*':
            l = chr(j+97)
            r = 8-i
            print(str(l)+str(r))
            exit()