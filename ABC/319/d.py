#https://qiita.com/hyouchun/items/adeff7e3f6836ca89aa0
N, M = map(int, input().split())
L = list(map(int, input().split()))

max_L = max(L)

def is_ok(m):
    if max_L > m:
        return False
    now_width = 1 << 63
    cnt = 0

    for l in L:
        if now_width + l + 1 > m:
            cnt += 1
            now_width = l
        else:
            now_width += l + 1

    return cnt <= M
    
ok = 1 << 63
ng = 0

def binary_search(ok, ng):
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(binary_search(ok,ng))