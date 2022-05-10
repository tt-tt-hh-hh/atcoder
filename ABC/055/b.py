import math

N = int(input())


""" power = 1
for i in range(1, N+1):
    power *= i

print(power%(10**9+7)) """

print(math.factorial(N)%(pow(10,9)+7))

