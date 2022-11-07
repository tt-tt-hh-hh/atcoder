from collections import deque

n = int(input())
l = [n for n in range(1,2*n+2)]
d = deque(l)

while True:
    print(d.pop())
    aoki = int(input())
    if aoki == 0:
        exit()
    else:
        d.remove(aoki)

    
