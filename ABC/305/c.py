h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]

ck_num = []
for i in S:
    ck_num.append(i.count('#'))

normal_row = ck_num.index(max(ck_num))
lr = [i for i, x in enumerate(S[normal_row]) if x == '#']
l = min(lr)
r = max(lr)


target = ck_num.index(max(ck_num)-1)

for i in range(l, r+1):
    s = S[target][i]
    if s == '.':
        print(target+1, i+1)
        exit()