n = int(input())

def prime_fact(n):
    a = []
    while n%2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n%f == 0:
            a.append(f)
            n //= f
        else:
            f += 2

    if n != 1:
        a.append(n)
    
    return a

l = set(prime_fact(n))

if 2 in l:
    l.remove(2)
if 3 in l:
    l.remove(3)

if len(l) == 0:
    print('Yes')
else:
    print('No')
