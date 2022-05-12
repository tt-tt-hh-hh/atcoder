N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

ans = []

for i in range(N):
    A1_new = A1[0:i+1]
    A2_new = A2[i:N]
    
    drop = sum(A1_new)+sum(A2_new)
    ans.append(drop)

print(max(ans))