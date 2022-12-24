S = input()
box = {chr(i): False for i in range(97,123)}

def isvalid(p):
    score = 0
    for i in p:
        if i == '(':
            score += 1
        else:
            score -= 1

        if score < 0:
            return False
    
    if score == 0:
        return True

def back(p):
    for i in p:
        if i.isalpha():
            box[i] = False

for i in range(len(S)):
    s = S[i]
    if s.isalpha():
        if box[s] == False:
            box[s] = True
        else:
            print('No')
            exit()
    elif s == '(':
        pass
    elif s == ')':
        j = 10**9
        for k in range(i-1,-1,-1):
            if isvalid(S[k:i]):
                j = k
                break
        back(S[j:i+1])

print('Yes')
        
        
