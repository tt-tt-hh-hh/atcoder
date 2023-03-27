s = input()
ans = ""
S = list(s)

for i in range(len(S)):
    if i == len(S)//2:
        break
    
    S[2*i], S[2*i+1] = S[2*i+1], S[2*i]

result = ''.join(S)
print(result)