n = int(input())
d = {}

def task(k):
    if k == 0:
        return 1

    val1 = k//2
    val2 = k//3
    
    if d.get(val1):
        p1 = d.get(val1)
    else:
        p1 = task(val1)
        d[val1] = p1

    if d.get(val2):
        p2 = d.get(val2)
    else:
        p2 = task(val2)
        d[val2] = p2

    return p1 + p2

print(task(n))
