a = int(input()) #500yen
b = int(input()) #100yen
c = int(input()) #50yen
x = int(input())
count = 0

for i in range(0, a+1):
    for j in range(0, b+1):
        for k in range(0, c+1):
            if x == 500*i + 100*j + 50*k:
                count += 1

print(count)

