from collections import defaultdict

S = input()
count01 = defaultdict(int)
S_count = [0 for _ in range(10)]

count01['0000000000'] += 1

for i in range(len(S)):
    S_count[int(S[i])] = (S_count[int(S[i])]+1)%2
    S_count_list = "".join(list(map(str, S_count)))

    count01[S_count_list] += 1

ans = 0

for i in count01:
    ans += count01[i]*(count01[i]-1)//2

print(ans)