import math
import numpy as np

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
p = [a,b,c,d,a,b,c,d]

#角度計算開始
def getdig(x0,y0,x1,y1,x2,y2):
    vec1=[x1-x0,y1-y0]
    vec2=[x2-x0,y2-y0]
    absvec1=np.linalg.norm(vec1)
    absvec2=np.linalg.norm(vec2)
    inner=np.inner(vec1,vec2)
    cos_theta=inner/(absvec1*absvec2)
    theta=math.degrees(math.acos(cos_theta))
    return round(theta,2)

for i in range(4):
    x0,y0,x1,y1,x2,y2 = p[i][0],p[i][1],p[i+1][0],p[i+1][1],p[i+2][0],p[i+2][1]
    kakudo = getdig(x0,y0,x1,y1,x2,y2)
    print(kakudo)

    if kakudo < 180.0:
        continue
    else:
        print('No')

print('Yes')
