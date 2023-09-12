from collections import deque

n = int(input())
A = list(map(int, input().split()))
A.sort()
a = deque(A)

ans = 0

if len(a)%2 == 1:
    center = len(a)//2
    c = a[center]

    while True:
        if len(a) <= 1:
            print(ans)
            exit()

        l = a.popleft()
        r = a.pop()

        ans += max(c-l, r-c)

else:
    c1, c2 = a[len(a)//2], a[len(a)//2 - 1]
    c = [(c1+c2)//2, (c1+c2)//2+1] 

    while True:
        if len(a) == 0:
            print(ans)
            exit()
        l = a.popleft()
        r = a.pop()

        ans += max(c[0]-l,r - c[1])
