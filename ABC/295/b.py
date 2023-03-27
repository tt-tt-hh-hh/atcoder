import copy

r, c = map(int, input().split())
sq = [list(input()) for _ in range(r)]
sq_cp = copy.deepcopy(sq)

def length(bomb,x,y):
    for i in range(r):
        for j in range(c):
            kyori = abs(i-x)+abs(j-y)
            if kyori <= bomb:
                sq_cp[i][j] = '.'


for i in range(r):
    for j in range(c):
        if sq[i][j] != '.' and sq[i][j] != '#':
            bomb = int(sq[i][j])
            length(bomb,i,j)


for a in sq_cp:
    print(*a, sep='')

