x, y, z = map(int, input().split())
s = input()

dp = [[0 for _ in range(2)] for _ in range(len(s)+1)]
dp[0][1] = z

for i in range(1,len(s)+1):
    if s[i-1]=='a':
        dp[i][0]=min(dp[i-1][0]+x, dp[i-1][1]+z+x)
        dp[i][1]=min(dp[i-1][0]+z+y, dp[i-1][1]+y)
    else:
        dp[i][0]=min(dp[i-1][0]+y, dp[i-1][1]+z+y)
        dp[i][1]=min(dp[i-1][0]+z+x, dp[i-1][1]+x)

print(min(dp[-1]))