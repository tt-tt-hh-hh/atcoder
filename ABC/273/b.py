from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal

x, k = map(int, input().split())

""" def my_round(val, digit):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p """

def my_round(val, digit):
    return int(Decimal(val).quantize(Decimal('1E'+str(digit+1)), rounding=ROUND_HALF_UP))

for i in range(k):
    #if int(str(x)[-1*(i+1)]) <= 4:
    val = x
    digit = i
    x = int(my_round(val, digit))

print(x)
