import math

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
p = [a,b,c,d,a,b,c,d]

def dig(Ax,Ay,Bx,By,Cx,Cy):
    ans = (math.atan2(Cy - By, Cx - Bx) - math.atan2(Ay - By, Ax - Bx)) / math.pi * 180
    return abs(ans)

#print(dig(a[0],a[1],b[0],b[1],c[0],c[1]))

for i in range(4):
    kakudo = dig(p[i][0],p[i][1],p[i+1][0],p[i+1][1],p[i+2][0],p[i+2][1])
    #print(kakudo)
    if kakudo < 180.0 or 360-kakudo < 180.0:
        continue
    else:
        print('No')
        exit()

print('Yes')

