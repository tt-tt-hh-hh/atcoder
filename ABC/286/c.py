n, a, b = map(int, input().split())
s = input()

s = s+s
ans = 1<<60

for i in range(n):
    tmp = a*i
    for j in range(n//2):
        if s[i+j] != s[i+n-1-j]:
            tmp += b
    ans = min(tmp, ans)

print(ans)