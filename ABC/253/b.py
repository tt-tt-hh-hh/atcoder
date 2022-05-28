H, W = list(map(int, input().split()))
S = [input() for _ in range(H) ]

koma = []
idx = []
for i in range(H):
    if S[i].count("o") == 2:
        for j in range(W):
            if S[i][j] == "o":
                idx.append(j)
        print(abs(idx[1]-idx[0]))
        exit()
    if "o" in S[i]:
        koma.append([i, S[i].index("o")])
    else:
        continue

dx = abs(koma[0][0]-koma[1][0])
dy = abs(koma[0][1]-koma[1][1])
ans = dx + dy
print(ans)