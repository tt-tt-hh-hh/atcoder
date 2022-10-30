s = [input() for _ in range(9)]
cnt =0
d = {}

for i in range(9):
    for j in range(9):
        for k in range(9):
            for l in range(9):
                if i==k and j==l:
                    continue
                
                v1 = s[i][j]
                v2 = s[k][l]
                #v3 = s[i-j+l][j+i-k]
                #v4 = s[k-j+l][l+i-k]
                dx, dy = k-i, l-i
                if 0<=k-dy<9 and 0<=l+dx<9 and 0<=i-dy<9 and 0<=l+dx<9:
                    v3 = s[k-dy][l+dx]
                    v4 = s[i-dy][l+dx]
                    if v1=='#' and v2=='#' and v3=='#' and v4=='#':
                        w = str(i)+','+str(j)+','+str(i-dy)+','+str(l+dx)
                        if d.get(w, 'hoge') == 'hoge':
                            cnt += 1
                            d[w] = 1
                            continue
                elif 0<=k+dy<9 and 0<=l-dx<9 and 0<=i+dy<9 and 0<=l-dx<9:
                    v3 = s[k+dy][l-dx]
                    v4 = s[i+dy][l-dx]
                    if v1=='#' and v2=='#' and v3=='#' and v4=='#':
                        w = str(i)+','+str(j)+','+str(i+dy)+','+str(l-dx)
                        if d.get(w, 'hoge') == 'hoge':
                            cnt += 1
                            d[w] = 1
                            continue
print(cnt)
print(d)
