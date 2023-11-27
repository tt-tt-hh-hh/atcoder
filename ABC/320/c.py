m = int(input())
S1 = input()
S2 = input()
S3 = input()

INF = 1 << 50
ans = INF

for i in range(m):
    for j in range(m):
        for k in range(m):
            if not (S1[i] == S2[j] == S3[k]):
                continue
            now_ans = 0
            counter = [0] * m

            for n in [i, j, k]:
                now_ans = max(now_ans, n+counter[n]*m)
                counter[n] += 1

            ans = min(ans, now_ans)

if ans == INF:
    print(-1)
else:
    print(ans)
