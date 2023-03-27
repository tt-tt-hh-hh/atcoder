n, k = map(int, input().split())
S = input()
ans = ""

for i in range(len(S)):
    s = S[i]
    if k == 0:
        ans += 'x'   
    elif s == 'o' and k>=1:
        k -= 1
        ans += 'o'
    else:
        ans += 'x'

print(ans)