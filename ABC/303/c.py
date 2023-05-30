n, m, h, k = map(int, input().split())
S = input()
XY = [list(map(int, input().split())) for _ in range(m)]
xy = set()

for hoge in XY:
    xy.add(str(hoge[0])+','+str(hoge[1]))


local = [0,0]
direct = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0,-1]}

for i in range(len(S)):
    local[0] += direct[S[i]][0]
    local[1] += direct[S[i]][1]
    h -= 1

    if h < 0:
        print('No')
        exit()

    fuga = str(local[0])+','+str(local[1])

    if fuga in xy and h < k:
        h = k
        xy.remove(fuga)

print('Yes')
    