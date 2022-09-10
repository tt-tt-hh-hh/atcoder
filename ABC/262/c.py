import itertools

N = int(input())
a = list(map(int, input().split()))

cnt = 0

all = itertools.combinations(a, 2)

for x in all:
    

""" for i in range(N):
    for j in range(i+1, N):
        min_num = min(a[i], a[j])
        max_num = max(a[i], a[j])
        
        if min_num == i+1 and max_num == j+1:
            cnt += 1

print(cnt)
 """

        