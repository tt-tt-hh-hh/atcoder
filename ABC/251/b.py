N, W = list(map(int, input().split()))
A = list(map(int, input().split()))

flag = [0]*(W+1)

for i in range(N):
    n = A[i]
    if n <= W:
        flag[n] = 1

for i in range(N):
    for j in range(i+1, N):
        m = A[i] + A[j]
        if m <= W:
            flag[m] = 1

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            l = A[i] + A[j] + A[k]
            if l <= W:
                flag[l] = 1

print(sum(flag))


