W, H, x, y, r = list(map(int, input().split()))

top = [x, (y+r)]
bottom = [x, (y-r)]
right = [(x+r), y]
left = [(x-r), y]

if top[1] > H:
    print("No")
elif bottom[1] < 0:
    print("No")
elif right[0] > W:
    print("No")
elif left[0] < 0:
    print("No")
else:
    print("Yes")

