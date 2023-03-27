n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.append(10**10)
B.append(10**10)

ans_a = []
ans_b = []

i, j, cnt = 0, 0, 1

while cnt < n+m+1:
    if A[i] < B[j]:
        ans_a.append(cnt)
        cnt += 1
        if i <= n-1:
            i += 1
    else:
        ans_b.append(cnt)
        cnt += 1
        if j <= m-1:
            j += 1

print(*ans_a)
print(*ans_b)