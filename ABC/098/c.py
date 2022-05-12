N = int(input())
S = input()

SW = [0]*(N+1)
SE = [0]*(N+1)
int_s = [0]*N
ans = [0]*N

for i in range(N):
    if S[i] == "W":
        int_s[i] = 1
    else:
        int_s[i] = 0

    SW[i+1] = SW[i]+int_s[i]

for i in range(N):
    if S[i] == "E":
        int_s[i] = 1
    else:
        int_s[i] = 0

    SE[i+1] = SE[i]+int_s[i]

for i in range(N):
    ans[i] = SW[i] + (SE[N]-SE[i+1])
    
print(min(ans))