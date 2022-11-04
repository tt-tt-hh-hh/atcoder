n = int(input())
st = {}
ori = {}
point = 0
ans = 10**6

for i in range(n):
    s, t = input().split()

    if ori.get(s):
        continue
    else:
        ori[s] = int(t)
        st[s] = i

""" max_kv_list = [kv for kv in ori.items() if kv[1] == max(ori.values())]

for i in range(len(max_kv_list)):
    ans = min(ans, st.index(max_kv_list[i][0])) """

max_p = max(ori.values())

for i in ori:
    if ori[i] == max_p:
        ans =  min(ans,st[i])

print(ans+1)

