n = int(input())
S = input()

status = False
cnt = 0
ans = -1

for i in range(n):
    s = S[i]
    if s == 'o':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans,cnt)

if len(set(S)) == 1:
    print(-1)
else:
    print(ans)
