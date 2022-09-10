N, M, X, T, D = list(map(int, input().split()))

if X <= M:
    print(T)
    exit()

T0 = T - D*X
TM = T0 + D*M

print(TM)