import itertools

n = int(input())
A = list(map(int, input().split()))
ans = []

for i in range(n):
    if i == n-1:
        ans.append(A[n-1])
        break
    
    a = A[i]
    aa = A[i+1]

    if a-aa > 1:
        ans.append(a)
        diff = a - aa
        l = []
        for i in range(1,diff):
            ans.append(a-i)
    elif a-aa < 1:
        ans.append(a)
        diff = aa - a
        l = []
        for i in range(1,diff):
            ans.append(a+i)
    else:
        ans.append(a)

print(*ans)
