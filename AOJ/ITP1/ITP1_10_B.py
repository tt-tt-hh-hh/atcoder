import math

a, b, c = list(map(int, input().split()))
c = math.radians(c)

s = a*b*math.sin(c)/2
l = a+b+math.sqrt(pow(a,2)+pow(b,2)-2*a*b*math.cos(c))
h = 2*s/a

print(s)
print(l)
print(h)