w = input().lower()
t = []
cnt = 0

while True:
    str = input()
    if str == 'END_OF_TEXT':
        break
    t.append(str)

for i in range(len(t)):
    buf = t[i].lower().split()
    cnt += buf.count(w)

print(cnt)

