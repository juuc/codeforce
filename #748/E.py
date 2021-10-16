# E. Gardener and Tree
from collections import deque
def bfs(leavenode):
    q = deque()
    q.append((leavenode,0))
    visited = [False] * (n+1)
    visited[leavenode] = True
    levels[leavenode].append(0)
    while q:
        cur, lvl = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                levels[next].append(lvl + 1)
                q.append((next,lvl+1))

for step in range(int(input())):
    input()
    n, k = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    origin_leaves = []
    for idx in range(1,n+1):
        if len(graph[idx]) == 1:
            origin_leaves.append(idx)
    levels = [[] for _ in range(n+1)]
    for leavenode in origin_leaves:
        bfs(leavenode)

    for i in range(n+1):
        if not levels[i]: levels[i].append(0)
        levels[i] = min(levels[i])
    print(levels)
    print(len(tuple(filter(lambda x : x>=k, levels))))