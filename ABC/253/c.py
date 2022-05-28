Q = int(input())
q = [list(map(int, input().split())) for i in range(Q)]

S = []

for i in range(Q):
    if q[i][0] == 1:
        S.append(q[i][1])
    elif q[i][0] == 2:
        numx = S.count(q[i][1])
        delctn = min(q[i][2], numx)
        if delctn == 0:
            continue
        S = [i for i in S if i != q[i][1] ]
        S.append
        
        """ S.sort()
        delstart = S.index(q[i][1])
        
        del S[delstart:delstart+delctn] """
        
        """ for j in range(delctn):
            S.remove(q[i][1]) """
    elif q[i][0] == 3:
        print(max(S) - min(S))