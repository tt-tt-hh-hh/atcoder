n = int(input())

def div(n):
    num = 0
    for i in range(1,n+1):
        if i*i>n:
            break
        if n%i != 0:
            continue

        num += 1
        if n//i != i:
            num += 1
    
    return num

table = [0 for _ in range(n)]

for i in range(1,n):
    table[i] = div(i)

ans = 0

for i in range(1,n):
    ab=i
    cd=n-i
    ans += table[ab]*table[cd]

print(ans)