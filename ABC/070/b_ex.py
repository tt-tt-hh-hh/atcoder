A, B, C, D = list(map(int, input().split()))

b_d = min(B, D)
a_c = max(A, C)

print(max(0, b_d - a_c))