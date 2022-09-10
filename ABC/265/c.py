h, w = list(map(int, input().split()))
g = [input() for _ in range(h)]

x = 0
y = 0

done = {}

while True:
    val = g[x][y]
    if done.get(str(x)+str(y),0) == 0:
        done[str(x)+str(y)] = 1
    else:
        print(-1)
        exit()
    
    if val == 'U':
        if x != 0:
            x -= 1
        else:
            print(str(x+1)+' '+str(y+1))
            exit()
    elif val == 'D':
        if x != h-1:
            x += 1
        else:
            print(str(x+1)+' '+str(y+1))
            exit()
    elif val == 'L':
        if y != 0:
            y -= 1
        else:
            print(str(x+1)+' '+str(y+1))
            exit()
    elif val == 'R':
        if y != w-1:
            y += 1
        else:
            print(str(x+1)+' '+str(y+1))
            exit()
    