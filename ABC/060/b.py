A, B, C = list(map(int, input().split()))

i = 1
count = 0

while True:
    sum = i*A

    r = sum%B
    if r == C:
        print("YES")
        break
    else:
        count += 1
        if count == B-1:
            print("NO")
            break
    i += 1
