n = int(input())
p = list(map(int, input().split()))

i = n-2

while p[i] < p[i+1]:
    i -= 1

j = n-1
while p[i]<p[j]:
    j -= 1

p[i], p[j] = p[j], p[i]
mae = p[:i+1]
usiro = sorted(p[i+1:], reverse=True)

print(*mae, *usiro)
