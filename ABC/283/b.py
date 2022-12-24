n = int(input())
a = list(map(int, input().split()))
q = int(input())

for i in range(q):
    query = input().split()
    
    if query[0] == '1':
        k, x = int(query[1]), int(query[2])
        a[k-1] = x
    else:
        k = int(query[1])
        print(a[k-1])
