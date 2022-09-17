from itertools import product
n = int(input())

n2 = format(n,'b') #str
ans = []
digit = []
digit0 = []

for i, bit in enumerate(n2):
    if bit == '1':
        digit.append(i)
    else:
        digit0.append(i)


for pro in product((0,1), repeat=len(digit)):
    a = [0]*len(n2)
    for i in range(len(digit)):
        a[digit[i]] = pro[i]

    for i in range(len(digit0)):
        a[digit0[i]] = 0
    
    s = ''.join([str(n) for n in a])
    print(int(s,2))

