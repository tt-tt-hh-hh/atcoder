import itertools

n = int(input())
S = [input() for _ in range(n)]

for hoge in itertools.permutations(S,2):
    buf = list(hoge[0]+hoge[1])
    for i in range(len(buf)):
        if buf[i] == buf[len(buf)-i-1]:
            pass
        else:
            break

        if i == len(buf)-1:
            print('Yes')
            exit()

print('No')



