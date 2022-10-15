n = int(input())

def fx(k):
    if k == 0:
        return 1
    else:
        return k*fx(k-1)

print(fx(n))
