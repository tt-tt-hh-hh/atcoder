N = int(input())
a = [int(input()) for _ in range(N)]
a.insert(0, 0)

idx = 1
count = 0

while True:
    i = a[idx]
    count += 1
    
    if a[idx] == 2:
        print(count)
        break

    if count > N:
        print(-1)
        break
    idx = i