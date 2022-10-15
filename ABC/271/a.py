n = int(input())
#n16 = int(str(n),16)
#n16 = hex(n)

n16 = format(n,'X')

if len(n16) == 1:
    ans = '0'+n16
else:
    ans = n16

print(ans)
