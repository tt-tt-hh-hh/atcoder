N = int(input())
c = 0

c = c + (N//2+1)
print('? '+ str(c))
s = int(input())


for i in range(19):
    n = N//2

    if n == 0:
        print('! '+ str(c))
        exit()
    if c >= n or c<=0:
        print('! '+ str(c))
        exit()
    
    if s == 0:
        c = c + (n//2+1)
        print('? '+ str(c))
        s = int(input())
    else:
        c = c - (n//2+1)
        print('? '+ str(c))
        s = int(input())