n = int(input())
A = list(map(int, input().split()))

ans = []
cnt = 0
buf = 0

for i in range(7*n):
    cnt += 1
    buf += A[i]

    if cnt%7 == 0:
        ans.append(buf)
        buf = 0

    

print(*ans)


        

    

