n = int(input())
S = input()

mode = False
ans = []

for i in range(n):
    s = S[i]
    if s == '"':
        mode = not mode
    elif s == ',':
        if mode == False:
            s = '.'
    
    ans.append(s)
    
print("".join(ans))
