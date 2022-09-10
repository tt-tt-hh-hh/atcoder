N = int(input())
S = [input() for _ in range(N)]

cnt = {}

for i in range(N):
    file = S[i]
    x = cnt.get(file)
    if x == None:
        print(file)
        cnt[file] = 1
    else:
        print(file + '(' + str(x) + ')')
        cnt[file] += 1
        