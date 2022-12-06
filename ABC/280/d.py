k = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

X = factorization(k)
ans = 0

for x, num in X:
    rem=num

    for Nx in range(x,x*(num+1),x):
        j = Nx
        while j%x==0:
            j//=x
            rem-=1
            if rem<=0:
                break
        if rem<=0:
            break
    ans=max(Nx,ans)

print(ans)