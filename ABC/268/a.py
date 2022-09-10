l = list(map(int, input().split()))

d = {}
for i in l:
    d[str(i)] = True

print(len(d))