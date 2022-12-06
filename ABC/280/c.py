s = input()
t = input()
cnt = 0

for i, j in zip(s,t):
    cnt += 1
    if i != j:
        print(cnt)
        exit()

print(cnt+1)
