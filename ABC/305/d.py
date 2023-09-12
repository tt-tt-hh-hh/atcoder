n = int(input())
A = list(map(int, input().split()))
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

S = [0]

slp = [[0 for _ in range(2)] for _ in range(len(A))]

for i in range(1,len(A)):
    if i%2 == 0:
        slp[i][0] = A[i]
        slp[i][1] = A[i] - A[i-1] + slp[i-1][1]
    else:
        slp[i][0] = A[i]
        slp[i][1] = slp[i-1][1]

for i in range(q):
    l, r = lr[i][0], lr[i][1]
    
