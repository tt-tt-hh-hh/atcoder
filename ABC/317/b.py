n = int(input())
A = list(map(int, input().split()))

A.sort()

for i in range(n):
    if A[i+1]-A[i] > 1:
        print(A[i]+1)
        exit()