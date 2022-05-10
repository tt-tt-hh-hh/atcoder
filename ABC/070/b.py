A, B, C, D = list(map(int, input().split()))

if C < A:
    if D <= A:
        print(0)
    if A < D <= B:
        print(D-A)
    if B < D:
        print(B-A)
if A <= C < B:
    if D <= B:
        print(D-C)
    if B < D:
        print(B-C)
if B <= C:
    print(0)
    

