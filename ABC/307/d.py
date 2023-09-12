import re

n = int(input())
S = input()

while True:
    if re.search('\([a-z]*\)', S) == None:
        print(S)
        exit()
    else:
        S = re.sub('\([a-z]*\)', '', S)