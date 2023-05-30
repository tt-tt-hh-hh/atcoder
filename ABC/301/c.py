S = input()
T = input()
atcoder = 'atcoder'

ds = {chr(i): 0 for i in range(97,123)}
ds['@'] = 0

dt = {chr(i): 0 for i in range(97,123)}
dt['@'] = 0

for i in S:
    ds[i] += 1

for i in T:
    dt[i] += 1

for k, s in ds.items():
    t = dt[k]

    if s != t and k not in atcoder:
        print('No')
        exit()

    if s==t:
        continue
    elif s>t:
        diff = s-t
        if dt['@']>=diff:
            dt['@'] -= diff
        else:
            print('No')
            exit()
    elif s<t:
        diff = t-s
        if ds['@']>=diff:
            ds['@'] -= diff
        else:
            print('No')
            exit()
print('Yes')