n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.reverse()

taka = 0
ao = 0
j = 0

while n > 0:
    for i in range(k):
        if a[i] <= n:
            toru = a[i]
            break
     
    if j%2 == 0:
        n -= toru
        taka += toru
    else:
        n -= toru
        ao += toru
    
    j += 1

print(taka)