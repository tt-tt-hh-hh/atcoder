n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
x = int(input())

trap = [False] * (x+1)
for i in b:
    trap[i] = True

dp = [False] * (x+1)
dp[0] = True

for i in range(1, x+1):
    for j in a:
        if i-j>=0 and dp[i-j]==True and trap[i] != True:
            dp[i] = True
            break

print("Yes" if dp[x] else "No")