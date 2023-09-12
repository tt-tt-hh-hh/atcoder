n, m = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    for j in range(n):        
        if i == j:
            continue

        if P[i][0] < P[j][0]:
            continue

        if P[i][1] > P[j][1]:
            continue

        if set(P[i][2:]).issubset(P[j][2:]):
            if P[i][0] > P[j][0] or P[i][1] < P[j][1]:
                print('Yes')
                exit()
print('No')



