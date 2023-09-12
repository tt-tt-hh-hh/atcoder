import bisect

N = int(input())
A = list(map(int, input().split()))

s = 0
sleeped = [0]

for i in range(1,N):
    if i%2==0:
        sleeped.append(s+A[i]-A[i-1])
        s += A[i] - A[i-1]
    else:
        sleeped.append(s)

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())

    L = bisect.bisect_right(A, l)
    R = bisect.bisect_right(A, r)

    if L%2 == 0:
        ltime = l - A[L-1] + sleeped[L-1]
    else:
        ltime = sleeped[L]

    if R%2 == 0:
        rtime = r- A[R-1]+sleeped[R-1]
    else:
        rtime = sleeped[R-1]
    
    print(rtime-ltime)

