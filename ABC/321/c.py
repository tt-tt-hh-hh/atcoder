k = int(input())

n = [i for i in range(0,10)]
ans = []

for i in range(2**10):
    num = []
    for j in range(10):
        if ((i >> j) & 1):
            num.append(str(n[j]))

    if len(num) == 0:
        continue
    
    #['3','2','1']
    num.sort(reverse=True)

    num_sorted = ''.join(num)

    ans.append(int(num_sorted))

ans.sort()
print(ans[k])