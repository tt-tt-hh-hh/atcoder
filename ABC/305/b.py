p, q = input().split()

l = {'A':0, 'B':3, 'C':4, 'D':8, 'E':9, 'F':14, 'G':23}

l1 = l[p]
l2 = l[q]
print(abs(l1-l2))