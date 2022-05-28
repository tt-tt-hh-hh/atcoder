import itertools
N = int(input())
A = list(map(int, input().split()))

count = 0

combi = list(itertools.combinations(A, 3))

for i in combi:
    if i[0] != i[1] and i[1] != i[2] and i[2] != i[0]:
        count += 1

print(count)