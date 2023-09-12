import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [False]*n
ans = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(city):
    visited[city] = True
    total_distance = 0

    for next_city, distance in graph[city]:
        if visited[next_city]:
            continue

        total_distance = max(total_distance, distance+dfs(next_city))
                             
    visited[city] = False

    return total_distance

for start_city in range(n):
    ans = max(ans, dfs(start_city))

print(ans)

