h1, h2, h3, w1, w2, w3 = list(map(int, input().split()))
h = [h1, h2, h3]
w = [w1, w2, w3]
a = []
cnt = 0

def check_w(masu):
    if masu[0][0]+masu[1][0]+masu[2][0] != w1:
        return False
    elif masu[0][1]+masu[1][1]+masu[2][1] != w2:
        return False
    elif masu[0][2]+masu[1][2]+masu[2][2] != w3:
        return False
    else:
        return True

for i in range(1, 31):
    for j in range(1, 31):
        k1 = h1 - i - j
        k2 = h2 - i - j
        k3 = h3 - i - j
        if k1 <= 0 or k2 <=0 or k3 <= 0:
            continue
        else:
            masu = [[i, j, k1], [i, j, k2], [i, j, k3]]
            
        if check_w(masu) == True:
            cnt += 1

print(cnt)

