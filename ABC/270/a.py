a, b = list(map(int, input().split()))

def judge(n):
    if n == 1:
        p = [1,0,0]
    elif n == 2:
        p = [0,1,0]
    elif n == 3:
        p = [1,1,0]
    elif n == 4:
        p = [0,0,1]
    elif n == 5:
        p = [1,0,1]
    elif n == 6:
        p = [0,1,1]
    elif n == 7:
        p = [1,1,1]
    else:
        p = [0,0,0]
    
    return p

ja = judge(a)
jb = judge(b)

ans = 0

if ja[0] == 1 or jb[0] == 1:
    ans += 1
if ja[1] == 1 or jb[1] == 1:
    ans += 2
if ja[2] == 1 or jb[2] == 1:
    ans += 4

print(ans)

