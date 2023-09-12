N, T, M = map(int, input().split())
NG = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    NG[A].append(B)
    NG[B].append(A)

def is_NG(player, team):
    for member in team:
        if member in NG[player]:
            return True
    
    return False

def rec(player, teams):
    ans = 0

    if player == N:
        if len(teams) != T:
            return 0
        
        return 1
    
    for i in range(len(teams)):
        if is_NG(player, teams[i]):
            continue

        teams[i].append(player)
        ans += rec(player+1, teams)
        teams[i].pop()

    teams.append([player])
    ans += rec(player+1, teams)
    teams.pop()

    return ans

print(rec(0,[]))
