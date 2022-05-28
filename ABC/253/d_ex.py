import math
N, A, B = map(int, input().split())

def sowa(x):
    ans = x*(x+1)//2
    return ans

LCM = A*B // math.gcd(A,B)
a = N // A
b = N // B
lcm = N // LCM

ctn = sowa(N) - A*sowa(a) - B*sowa(b) + LCM*sowa(lcm)

print(ctn)