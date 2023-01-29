n, m = map(int, input().split())
S = [input() for _ in range(n)]
T = [input() for _ in range(m)]

ans = 0

for i in range(n):
    s = S[i][3:]
    
    if s in T:
        ans += 1

print(ans)
