#https://qiita.com/hyouchun/items/465d437d69ab18d7412d#d---president
INF = 1 << 60

N = int(input())
takahashi, aoki = 0, 0
P = []
for _ in range(N):
    x, y, z = map(int, input().split())
    if x < y:
        mid = (x+y)//2 + 1
        P.append((mid-x, z*2))
        aoki += z
    else:
        takahashi += z

dist = aoki - takahashi

if dist < 0:
    print(0)
    exit()

#dp[i][score]左からi個まで見てsocreを獲得するのに必要なコストの最小値
dp = [[INF]*(dist+1) for _ in range(len(P)+1)]
dp[0][0] = 0

for i in range(len(P)):
    cost, score = P[i]
    for j in range(dist+1):
        #コストを支払わない場合
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

        #コストを支払ってスコアを得る場合
        nj = j + score
        if nj > dist:
            nj = dist

        dp[i+1][nj] = min(dp[i+1][nj], dp[i][j]+cost)

print(dp[len(P)][dist])