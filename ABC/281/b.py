s = input()

if len(s) != 8:
    print('No')
    exit()

s1=ord(s[0])
if s1 >= 65 and s1<=90:
    pass
else:
    print('No')
    exit()

for i in range(1,7):
    if ord(s[i]) >= 48 and ord(s[i]) <= 57:
        pass
    else:
        print('No')
        exit()

ss = int(s[1:7])
if ss>=100000 and ss<= 999999:
    pass
else:
    print('No')
    exit()

s2=ord(s[7])
if s2 >= 65 and s2<=90:
    pass
else:
    print('No')
    exit()

print('Yes')
