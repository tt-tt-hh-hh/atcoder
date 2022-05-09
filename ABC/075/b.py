S = list()

H, W = list(map(int, input().split()))
[S.append(list(input())) for _ in range(H)]

for i in range(H):
    for j in range(W):
        bom = 0
        if S[i][j] == "#":
            continue
        else:
            if 0<i and 0<j and S[i-1][j-1] == "#":
                bom += 1
            if 0<j and S[i][j-1] == "#":
                bom += 1
            if 0<j and i<H-1 and S[i+1][j-1] == "#":
                bom += 1
            if 0<i and S[i-1][j] == "#":
                bom += 1
            if i<H-1 and S[i+1][j] == "#":
                bom += 1
            if 0<i and j<W-1  and S[i-1][j+1] == "#":
                bom += 1
            if j<W-1 and S[i][j+1] == "#":
                bom += 1
            if i<H-1 and j<W-1 and S[i+1][j+1] == "#":
                bom += 1
            S[i][j] = str(bom)

for i in S:
    print("".join(i))




