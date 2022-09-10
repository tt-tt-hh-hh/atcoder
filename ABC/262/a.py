y = int(input())

mod = y % 4

if mod == 0:
    print(y + 2)
elif mod == 1:
    print(y + 1)
elif mod == 2:
    print(y)
elif mod == 3:
    print(y + 3)
    