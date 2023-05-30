S = input()
N = bin(int(input()))

NN = str(N[2:])
SS = S[-len(NN):]

status = False

ans = ""

if len(NN) > len(SS):
    print(int(S.replace('?','1'),2))
    exit()

for i in range(len(NN)):
    s = SS[i]
    n = NN[i]

    if status:
        if s == '?':
            ans += '1'
        else:
            ans += s
    else:
        if n == '0' and s == '0':
            ans += '0'
        elif n == '0' and s == '1':
            print(-1)
            exit()
        elif n == '0' and s == '?':
            ans += '0'
        elif n == '1' and s == '0':
            ans += '0'
            status = True
        elif n == '1' and s == '1':
            ans += '1'
        elif n == '1' and s == '?':
            ans += '0'
            status = True

print(int(ans,2))



