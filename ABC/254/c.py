N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [[] for _ in range(K)]

for i, x in enumerate(A):
    B[i%K].append(x)

for i in range(K):
    B[i].sort()

SA = [0]*N
for i in range(N):
    SA[i] = B[i % K][i // K]

if SA == sorted(A):
    print("Yes")
else:
    print("No")