n = int(input())

for i in range(0, 101, 5):
    if abs(i - n) < 3:
        print(i)
        exit()
