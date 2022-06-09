N = int(input())

A = []

for i in range(N):
    a = []
    for j in range(i+1):
        if j == 0 or j == i:
            a.append(1)
        else:
            aij = A[i-1][j-1] + A[i-1][j]
            a.append(aij)
    A.append(a)
    print(*a)

