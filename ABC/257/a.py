N, X = list(map(int, input().split()))

""" s = X // N
amari = X % N

if amari == 0:
    print(chr(96+s))
else:
    print(chr(96+s+1)) """

alp = [chr(i) for i in range(65,65+26)]
s = ""
for i in alp:
    s += i * N

print(s[X-1])
