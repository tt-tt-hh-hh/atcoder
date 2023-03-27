n = int(input())
a = list(map(int, input().split()))

d = {key: False for key in range(1,n+1)}

for i in range(n):
    if d[i+1] == True:
        pass
    else:
        d[a[i]] = True

num = 0
hum = []

for k, v in d.items():
    if v == False:
        num += 1
        hum.append(k)

print(num)
print(*hum)
