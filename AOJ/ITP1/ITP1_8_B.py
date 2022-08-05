while True:
    x = input()
    cnt = 0

    if len(x) == 1 and int(x) == 0:
        break

    for i in x:
        cnt += int(i)
    
    print(cnt)
