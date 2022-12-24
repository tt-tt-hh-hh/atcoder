from itertools import groupby

S = input()
cnt = 0

""" for i in range(len(S)):
    s = S[i]

    if s != '0':
        cnt += 1
    else:
        if S[i-1] != '0' and  """

def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

l = runLengthEncode(S)
for i in l:
    if i[0] != '0':
        cnt += i[1]
    else:
        syou = i[1]//2
        amari = i[1]%2

        cnt += (syou+amari)

print(cnt)