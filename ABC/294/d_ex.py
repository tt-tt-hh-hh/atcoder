from collections import deque

n, q = map(int, input().split())
h = [i+1 for i in range(n)]
human = deque(h)
keijiban = set()

minN = 0

for i in range(q):
    event = input().split()
    if event[0]=="1":
        keijiban.add(human.popleft())
    elif event[0]=="2":
        keijiban.remove(int(event[-1]))
    elif event[0]=="3":
        print(min(keijiban))