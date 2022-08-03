n = int(input())

univ = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]

for _ in range(n):
    b, f, r, v = list(map(int, input().split()))
    univ[b-1][f-1][r-1] += v

for b in range(4):
    for f in range(3):
        print('', *univ[b][f])

    if b != 3:
        print('####################')
    
    