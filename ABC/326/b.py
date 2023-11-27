n = int(input())

while True:
    nn = str(n)
    x = int(nn[0])
    y = int(nn[1])
    z = int(nn[2])

    if x*y == z:
        print(n)
        exit()
    
    n += 1

