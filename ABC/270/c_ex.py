from collections import deque #幅優先探索のためのキュー

N, A, B = map(int, input().split())

# 木を表現する
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(A - 1)
upper = [-1] * N
# 頂点Aは根であることを, -2で表現する
upper[A - 1] = -2

def BFS():
    while q:
        now = q.popleft()
        for nxt in g[now]:
            if upper[nxt] == -1:
                upper[nxt] = now
                q.append(nxt)
BFS()
                
ans = []
now = B - 1

# 頂点
while upper[now] != -2:
    ans.append(now)
    now = upper[now]
# 最後に頂点をansに追加する
ans.append(A-1)
# ansにはB=>Aとたどる経路を格納したので, 逆順に出力する
for i in ans[::-1]:
    print(i + 1, end= " ")