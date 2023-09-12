n = int(input())
S = input()

t = []
a = []

for i in range(len(S)):
    s = S[i]

    if s != '(' and s != ')':
        t.append(s)
    elif s == '(':
        a.append(i)
        t.append(s)
    elif s == ')':
        if a != []:
            x = a.pop(-1)
            while True:
                r = t.pop(-1)
                if r == '(':
                    break
        else:
            t.append(s)

print(*t, sep='')
