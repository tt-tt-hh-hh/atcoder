n = int(input())
a = list(map(int, input().split()))

A = sorted(a, reverse=True)
count = 0

alice, bob = 0, 0

for i in A:
    if count % 2 == 0:
        alice += i
    else:
        bob += i
    count += 1

div = alice - bob
print(div)
