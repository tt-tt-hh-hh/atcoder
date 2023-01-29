n = int(input())
yes = 0
no = 0

for i in range(n):
    s = input()
    if s == 'For':
        yes += 1
    else:
        no += 1

if yes > no:
    print('Yes')
else:
    print('No')
