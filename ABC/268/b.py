s = input()
t = input()

if len(s) > len(t):
    print('No')
    exit()

for i in range(len(s)):
    if s[i] == t[i]:
        continue
    else:
        print('No')
        exit()

print('Yes')
