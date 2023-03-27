h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

for i in range(h):
    ans = ""
    for j in range(w):
        num = a[i][j]
        if num == 0:
            ans += "."
        else:
            ans += chr(a[i][j]+64)
    print(ans)