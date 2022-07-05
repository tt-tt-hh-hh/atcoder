N = int(input())
A = list(map(int, input().split()))

P = 0
koma = [0, 0, 0, 0]

for i in range(N):
    koma[0] = 1
    for j in reversed(range(4)):
        if koma[j] == 0:
            continue
        r = j + A[i]
        if r >= 4:
            P += 1
            koma[j] = 0
        else:
            koma[r] = 1
            koma[j] = 0

print(P)
