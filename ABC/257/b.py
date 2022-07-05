N, K, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
L = list(map(int, input().split()))

masu = [0]*(N)
ans = []

for i in A:
    masu[i-1] = 1

for i in range(Q):
    if A[L[i]-1] == N:
        continue
    elif masu[A[L[i]-1]] == 1:
        continue
    else:
        masu[A[L[i]-1]] = 1
        masu[A[L[i]-1]-1] = 0
        A[L[i]-1] += 1

for i in range(N):
    if masu[i] == 1:
        ans.append(i+1)

print(*ans)
