N = int(input())
S = input()
W = list(map(int, input().split()))

s = []
l = []
ans = []

for i in range(N):
    s.append([S[i], W[i]])

new_s = sorted(s, reverse=False, key=lambda x:x[1])

for i in range(N):
    l.append(new_s[i][0])

for i in range(N):
    if i == 0:
        ans.append(l.count('1'))
    elif i == N-1:
        ans.append(l.count('0'))
    else:
        ch = l[0:i].count('0')
        ad = l[i:N].count('1')
        ans.append(ch+ad)

print(max(ans))