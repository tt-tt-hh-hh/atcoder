st = input()
q = int(input())
r = [list(input().split()) for _ in range(q)]

for i in range(q):
    cmd = r[i][0]
    a = int(r[i][1])
    b = int(r[i][2])
    
    if cmd == 'replace':
        p = r[i][3]
        st = st[0:a] + p + st[b+1:]
    elif cmd == 'reverse':
        rev = st[a:b+1]
        st = st[0:a] + rev[::-1] + st[b+1:]
    elif cmd == 'print':
        print(st[a:b+1])
    
