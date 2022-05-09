S = input()

l = len(S)
r_S = S[::-1]
step = 1
words = ["dream", "dreamer", "erase", "eraser"]

can = True

i = 0

while i < l:
    can2 = False
    for j in range(0, 4):
        d = words[j][::-1]
        ss = r_S[i:i+len(d)]
        if ss == d:
            can2 = True
            i += len(d)
            break
            
    if can2 == False:
        can = False
        break

if can == True:
    print("YES")
else:
    print("NO")

        


