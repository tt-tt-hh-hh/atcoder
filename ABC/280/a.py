h, w = map(int, input().split())
s = [input() for _ in range(h)]
ans = 0

for i in range(h):
    for j in s[i]:
        if j == '#':
            ans += 1

print(ans)