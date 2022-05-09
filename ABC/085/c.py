N, Y = list(map(int, input().split()))

x, y, z = -1, -1, -1
total = 0

for i in range(0, N+1):
    for j in range(0, N+1 - i):   
        k = N - i - j
        total = 10000*i + 5000*j + 1000*k
        if Y == total and i+j+k == N:
            x = i
            y = j
            z = k
            break

print(x, y, z)