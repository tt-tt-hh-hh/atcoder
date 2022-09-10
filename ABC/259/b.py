import math

a, b, d = list(map(int, input().split()))

""" r = math.sqrt(pow(a, 2) + pow(b, 2))

#t = math.sqrt(pow(r, 2) + pow(r, 2) - 2*r*r*math.cos(math.radians(d)))

t2 = pow(r, 2) + pow(r, 2) - 2*r*r*math.cos(math.radians(d))
r2 = pow(a, 2) + pow(b, 2) """


ad = a*math.cos(math.radians(d)) - b*math.sin(math.radians(d))
bd = a*math.sin(math.radians(d)) + b*math.cos(math.radians(d))

print(str(ad) + " " + str(bd))