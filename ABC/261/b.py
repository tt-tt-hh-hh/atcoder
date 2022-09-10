N = int(input())
A = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        x = A[i][j]
        y = A[j][i]

        if x == '-':
            continue
        elif x == 'W' and y == 'L':
            continue
        elif x == 'L' and y == 'W':
            continue
        elif x == 'D' and y == 'D':
            continue
        else:
            print("incorrect")
            exit()

print("correct")

