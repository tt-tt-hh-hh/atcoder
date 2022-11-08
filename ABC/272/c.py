n = int(input())
a = list(map(int, input().split()))

even = []
odd = []

for i in range(n):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])

even.sort(reverse=True)
odd.sort(reverse=True)

if len(even)>=2:
    even_max = even[0]+even[1]
else:
    even_max = -1

if len(odd)>=2:
    odd_max = odd[0]+odd[1]
else:
    odd_max = -1

print(max(even_max,odd_max))

