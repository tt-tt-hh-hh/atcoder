N = int(input())
l = -1
r = N-1

judge = (r-l)//2
mid = 1 + judge

print('? '+str(mid+1))
s = int(input())

for _ in range(19):
    judge = (r-l)//2

    if judge == 0:
        print('! '+str(mid+1))
        exit()
    
    if s == 0:
        mid = 1 + judge
        print('? '+str(mid+1))
        s = int(input())
    else:
        mid = 1 - judge
        print('? '+str(mid+1))
        s = int(input())


    

