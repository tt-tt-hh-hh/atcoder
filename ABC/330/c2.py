D = int(input())
x = 0
ans = []

while True:
    xx = x*x
    if D-xx < 0:
        break
    
    d = D-xx
    for y in range(d):
        if y*y >= d:
            ans.append(min(abs(d-y*y), abs(d-(y-1)*(y-1))))
            break
    
    x += 1

print(min(ans))



