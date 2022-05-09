N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

p = [0, 0, 0]

judge = True

for i in P:
    t = i[0]
    x = i[1]
    y = i[2]

    t0 = p[0]
    px = p[1]
    py = p[2]

    div_x = abs(x - px)
    div_y = abs(y - py)
    div_t = abs(t - t0)

    need_time = div_x + div_y

    if need_time > div_t:
        judge = False
        break

    if need_time == div_t:
        p = [t, x, y]
        continue

    if need_time < div_t:
        if (div_t - need_time)%2 == 1:
            judge = False
            break
        else:
            p = [t, x, y]
            continue

if judge:
    print("Yes")
else:
    print("No")



