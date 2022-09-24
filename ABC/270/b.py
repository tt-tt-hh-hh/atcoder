x, y, z = list(map(int, input().split()))

if x > 0:
    if 0 < y and y < x:
        if y < z:
            print(-1)
        elif z > 0 and z < y:
            print(x)
        elif z < 0:
            print(abs(z)*2 + x)
    else:
        print(x)

if x < 0:
    if x < y and y < 0:
        if z < y:
            print(-1)
        elif y < z and z < 0:
            print(abs(x))
        elif z > 0:
            print(abs(z)*2 + abs(x))
    else:
        print(abs(x))
        