from collections import deque

n = int(input())
a = list(map(int, input().split()))
a.sort()
d = deque(a)
d.appendleft(0)
#book = []

for i in range(1,n+1):
    if i == d[i]:
        #book.append(i)
        continue
    elif i != d[i]:
        if i+2 < len(d):
            d.pop()
            d.pop()
            #book.append(i)
            d.appendleft(0)
            #d.insert(i,i)
        elif i+2 == len(d):
            print(i)
            exit()
        else:
            print(i-1)
            exit()

