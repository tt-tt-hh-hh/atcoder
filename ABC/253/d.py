import math
N, A, B = list(map(int, input().split()))

sum_n = N*(N+1)//2

sum_a = A*(N//A)*(N//A + 1)//2
sum_b = B*(N//B)*(N//B + 1)//2

lcm = int(A*B // math.gcd(A, B))

sum_ab = lcm*(N//lcm)*(N//lcm + 1)//2

print(int(sum_n - sum_a - sum_b + sum_ab))