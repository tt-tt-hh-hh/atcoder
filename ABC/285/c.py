S = input()
ans = 0

for i in range(1,len(S)):
    ans += 26**i

for i in range(len(S)):
    n = ord(S[i])-65
    m = 26**(len(S)-i-1)
    ans += n*m

print(ans+1)