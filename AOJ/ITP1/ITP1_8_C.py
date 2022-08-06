words = []
cnt = [0]*26

while True:
    try:
        str = input()
        words.append(str)
    except EOFError:
        break

for i in range(len(words)):
    word = words[i].lower()
    for j in word:
        num = ord(j) - ord('a')
        if num >= 0 and num <= 25:
            cnt[num] += 1

for i in range(26):
    alp = chr(i + 97)
    print(alp, ':', cnt[i])
