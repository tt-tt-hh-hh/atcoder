S = list()

H, W = list(map(int, input().split()))
[S.append(list(input())) for _ in range(H)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

for i in range(H):
    for j in range(W):
        bom = 0

        if S[i][j] == "#":
            continue
        else:
            for d in range(8):
                ni = i + dy[d]
                nj = j + dx[d]
                if ni < 0 or H <= ni:
                    continue
                if nj < 0 or W <= nj:
                    continue
                if S[ni][nj] == "#":
                    bom += 1
            S[i][j] = str(bom)

for i in S:
    print("".join(i))

