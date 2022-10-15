import bisect
import collections

n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)

a_s = sorted(list(set(a)))

for i in range(n):
    cnt = 0
    """ for j in range(n):
        idx = bisect.bisect_right(a_s,a[j])
        if len(a_s)-idx == i:
            cnt +=1 """
    
    num = len(a_s) - i - 1
    if num < 0:
        cnt = 0
    else:
        cnt = c[a_s[num]]


    print(cnt)



