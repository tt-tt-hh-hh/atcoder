from bisect import bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = 0

for left_idx, el in enumerate(a):
    right_idx = bisect_left(a, el+m)
    ans = max(ans, right_idx-left_idx)

print(ans)