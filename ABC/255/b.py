import math

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(N)]

R = []

""" for xy in XY:
    r = []
    for a in A:
        dx = abs(XY[a-1][0] - xy[0])
        dy = abs(XY[a-1][1] - xy[1])
        buf = math.sqrt(pow(dx,2)+ pow(dy,2))
        if buf != 0:
            r.append(buf)

    if not r:
        continue
    else:
        R.append(min(r))

print(max(R)) """

for i in range(N):
    r = []
    for j in range(K):
        if i == A[j]-1:
            continue
        dx = abs(XY[i][0] - XY[A[j]-1][0])
        dy = abs(XY[i][1] - XY[A[j]-1][1])
        buf = math.sqrt(pow(dx,2)+ pow(dy,2))
        r.append(buf)
    R.append(min(r))

print(max(R))