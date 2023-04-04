n = int(input())
S = input()

prev = 'U'

for s in S:
    if s==prev:
        print('No')
        exit()

    prev = s

print('Yes')