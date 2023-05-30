n = int(input())
S = input()

taka = 0
ao = 0

for i in range(n):
    if S[i] == 'T':
        taka += 1
        if taka >= n//2:
            print('T')
            exit()
    else:
        ao += 1
        if ao >= n//2:
            print('A')
            exit()

if taka > ao:
    print('T')
else:
    print('A')

    