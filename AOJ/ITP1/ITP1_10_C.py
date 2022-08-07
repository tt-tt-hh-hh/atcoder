import math
while True:
    n = int(input())
    if n == 0:
        break

    s = list(map(int, input().split()))
    m = sum(s)/len(s)
    sig = 0

    for i in range(n):
        sig += pow((s[i]-m),2)

    a = math.sqrt(sig/n)
    print(a)