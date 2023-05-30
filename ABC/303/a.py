n = int(input())
S = input()
T = input()

s = S.replace('1', 'l').replace('0', 'o')
t = T.replace('1', 'l').replace('0', 'o')

for i in range(n):
    if s[i] == t[i]:
        pass
    else:
        print('No')
        exit()

print('Yes')
