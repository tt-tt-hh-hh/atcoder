n = int(input())

def make_divisors(n):
    lower, upper = [], []
    i = 1
    while i*i <= n:
        if n%i == 0:
            lower.append(i)
            if i != n//i:
                upper.append(n//i)
        i += 1
    
    return lower + upper[::-1]

J = make_divisors(n)

ans = ""

for i in range(n+1):
    s = 10
    for j in J:
        if 1<=j and j<=9:
            if i%(n//j) == 0:
                s = j
                break
    
    if s == 10:
        ans += "-"
    else:
        ans += str(s)

print(ans)
