x, y = map(int, input().split())

z = y - x

if z > 0:
    if z <= 2:
        print("Yes")
    else:
        print('No')
else:
    if z >= -3:
        print("Yes")
    else:
        print("No")