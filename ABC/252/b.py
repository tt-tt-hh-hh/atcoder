import sys
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_num = max(A)
idx =[]

for i in range(N):
    if max_num == A[i]:
        idx.append(i)

for i in idx:
    if i+1 in B:
        print("Yes")
        sys.exit()

print("No")