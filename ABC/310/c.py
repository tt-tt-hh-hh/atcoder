n = int(input())
S = [input() for _ in range(n)]

d = {}

for i in range(n):
    s = S[i]
    if d.get(s) or d.get(s[::-1]):
        pass
    else:
        d[s] = 1

print(len(d))