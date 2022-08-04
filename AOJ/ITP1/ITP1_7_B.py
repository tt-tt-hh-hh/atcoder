while True:
    cnt = 0
    n, x = list(map(int, input().split()))
    
    if n == 0 and x == 0:
        break

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if j < x-i-j <= n:
                cnt += 1

    print(cnt)