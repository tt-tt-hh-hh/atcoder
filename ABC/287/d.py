s = list(input())
t = list(input())

def match(a,b):
    if a == '?' or b == '?' or a == b:
        return True
    else:
        return False

pre = [False] * (len(t)+1)
suf = [False] * (len(t)+1)

pre[0] = True

for i in range(len(t)):
    if not match(t[i], s[i]):
        break
    else:
        pre[i+1] = True

s = s[::-1]
t = t[::-1]
suf[0] = True

for i in range(len(t)):
    if not match(t[i], s[i]):
        break
    else:
        suf[i+1] = True

for i in range(len(t)+1):
    if pre[i] and suf[len(t)-i]:
        print('Yes')
    else:
        print('No')