from itertools import combinations

v = []
cnt = 0

for i in range(9):
    s = input()
    for j in range(9):
        if s[j] == '#':
            v.append([i,j])

for i in combinations(v,4):
    distance = set()
    for j in combinations(i,2):
        d = (j[0][0]-j[1][0])**2+(j[0][1]-j[1][1])**2
        distance.add(d)
    
    if len(distance) == 2:
        cnt += 1

print(cnt)
    

