n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

""" if n == 1:
    print('Yes')
    exit()

if n == 2:
    i = 1
    f1 = False
    f2 = False
    if abs(a[i]-a[i-1])<=k or abs(a[i]-b[i-1])<=k:
        f1 = True
    if abs(b[i]-a[i-1])<=k or abs(b[i]-b[i-1])<=k:
        f2 = True

    if f1 == True or f2 == True:
        pass
    else:
        print('No')
        exit()


for i in range(1,n-1):
    f1 = False
    f2 = False
    if abs(a[i]-a[i-1])<=k or abs(a[i]-b[i-1])<=k:
        if abs(a[i]-a[i+1])<=k or abs(a[i]-b[i+1])<=k:
            f1 = True
    if abs(b[i]-a[i-1])<=k or abs(b[i]-b[i-1])<=k:
        if abs(b[i]-a[i+1])<=k or abs(b[i]-b[i+1])<=k:
            f2 = True

    if f1 == True or f2 == True:
        pass
    else:
        print('No')
        exit()
 """
fa = True
fb = True

for i in range(n-1):
    ta = False
    tb = False
    if fa:
        if abs(a[i]-a[i+1])<=k:
            ta = True
        
        if abs(a[i]-b[i+1])<=k:
            tb = True

    if fb:     
        if abs(b[i]-a[i+1])<=k:
            ta = True
        if abs(b[i]-b[i+1])<=k:
            tb = True
    fa, fb = ta, tb

if fa == True or fb == True:
    print('Yes')
else:
    print('No')
