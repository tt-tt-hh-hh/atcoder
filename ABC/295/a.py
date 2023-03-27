n = int(input())
w = list(input().split())

if 'and' in w:
    print('Yes')
elif 'not' in w:
    print('Yes')
elif 'that' in w:
    print('Yes')
elif 'the' in w:
    print('Yes')
elif 'you' in w:
    print('Yes')
else:
    print('No')