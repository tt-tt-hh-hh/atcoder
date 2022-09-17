s = [input() for _ in range(10)]

for i in range(10):
    if s[i].count('#') == 0:
        continue
    else:
        A = i+1
        B = A-1
        C = s[i].index('#')+1
        D = s[i].count('#')+C-1
        break

for i in range(A-1, 10):
    if s[i].count('#') != 0:
        B += 1


    
print(A, B)
print(C, D)
