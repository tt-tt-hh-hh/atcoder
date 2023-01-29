n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))

a1 = a[0:p-1]
a2 = a[p-1:q]
a3 = a[q:r-1]
a4 = a[r-1:s]
a5 = a[s:n]

ans = a1+a4+a3+a2+a5

print(*ans)