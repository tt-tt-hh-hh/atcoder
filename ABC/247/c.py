n = int(input())
l = []

def s(n):
    if n == 1:
        return [1]

    return s(n-1)+[n]+s(n-1)

if n == 1:
    print(1)
    exit()

print(*s(n))
