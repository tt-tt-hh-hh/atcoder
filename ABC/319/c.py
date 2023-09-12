#https://qiita.com/hyouchun/items/adeff7e3f6836ca89aa0#%E3%82%B3%E3%83%BC%E3%83%89-2
import math
from itertools import permutations

c = [list(map(int, input().split())) for _ in range(3)]
A = [(0,4,8), (2,4,6)]
for i in range(3):
    tpl = tuple(i*3 + j for j in range(3))
    A.append(tpl)
for j in range(3):
    tpl = tuple(i*3 + j for i in range(3))
    A.append(tpl)

def is_ok_tuple(tpl, perm):
    T = []
    for pos in tpl:
        i, j = divmod(pos,3)
        T.append((perm[pos], c[i][j]))
    T.sort()

    return T[0][1] != T[1][1]

ok_cnt = 0
for perm in permutations(range(9)):
    is_ok = True
    for tpl in A:
        if not is_ok_tuple(tpl, perm):
            is_ok = False
            break
    if is_ok:
        ok_cnt += 1

ans = ok_cnt / math.prod(range(1,10))
print(ans)