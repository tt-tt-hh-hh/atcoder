while True:
    a, b = list(map(int, input().split()))
    if a==0 and b==0:
        break

    if a<=b:
        print("{} {}".format(a, b))
    else:
        print("{} {}".format(b, a))