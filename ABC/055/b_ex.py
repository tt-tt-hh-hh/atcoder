N = int(input())

power = 1
const = pow(10,9)+7


for i in range(1, N+1):
    power *= i
    power %= const

print(power)