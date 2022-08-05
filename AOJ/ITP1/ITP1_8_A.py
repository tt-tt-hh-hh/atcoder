""" input = input()
output = ""

for i in input:
    if i.islower():
        output += i.upper()
    elif i.isupper():
        output += i.lower()
    else:
        output += i

print(output) """

input = input()
output = ""

print(input.swapcase())