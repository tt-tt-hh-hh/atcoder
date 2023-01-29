a, b = map(int, input().split())
l = [[2,3],[4,5],[6,7],[8,9],[10,11],[12,13],[14,15]]

if a>7 and b>7:
    print('No')
    exit()

if b in l[a-1]:
    print('Yes')
else:
    print('No')