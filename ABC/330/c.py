d = int(input())
n = 0
m = 0

while True:
    if n*n <= d and (n+1)*(n+1) > d:
        d -= n*n
        break
    n += 1

while True:
    if m*m <= d and (m+1)*(m+1) > d:
        d -= m*m
        break
    m += 1

print(d)
