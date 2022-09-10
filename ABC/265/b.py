n, m, t = list(map(int, input().split()))
A = list(map(int, input().split()))
xy = {}
room = 0

for i in range(m):
    x, y = list(map(int, input().split()))
    xy[x] = y

while room < n-1:
    spend = A[room]
    bonus = xy.get(room+1,0)
    t += bonus

    if t - spend <= 0:
        print('No')
        exit()

    t -= spend
    room += 1

print('Yes')

""" for i in range(n):
    spend = A[i]
    bonus = xy.get(i, 0)

    t -= spend
    if t <= 0:
        print('No')
        exit()
    
    t += bonus """