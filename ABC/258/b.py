import itertools
from typing import List

N = int(input())
A = [input() for _ in range(N)]

ans = 0

for dr, dc in zip([0, -1, -1, -1, 0, 1, 1, 1], [1, 1, 0, -1, -1, -1, 0, 1]):
    for i, j in itertools.product(range(N), range(N)):
        result = []
        r = i
        c = j

        for _ in range(N):
            result.append(A[r][c])

            r += dr
            if r < 0:
                r += N
            r %= N

            c += dc
            if c < 0:
                c += N
            c %= N

        ans = max(ans, int("".join(reversed(result))))

print(ans)


