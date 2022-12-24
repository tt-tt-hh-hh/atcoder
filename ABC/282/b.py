n,m = map(int, input().split())
s = [input() for _ in range(n)]
ans = 0

for i in range(0,n):
    for j in range(i+1,n):
        for k in range(0,m):
            a = s[i][k]
            b = s[j][k]
            if s[i][k] == 'o' or s[j][k] == 'o':
                if k == m-1:
                    ans += 1
                pass
            else:
                break
                
print(ans)