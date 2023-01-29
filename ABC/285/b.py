n = int(input())
s = input()

for i in range(1,n):
    #l = 0
    for j in range(n):
        if j>n-1 or i+j>n-1:
            break        
        if s[j] == s[i+j]:
            #print(j-1)
            break
        else:
            pass
    print(j)