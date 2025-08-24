# You are given an integer n and a directed graph with n nodes labeled from 0 to n - 1.
# This is represented by a 2D array edges, where edges[i] = [ui, vi, starti, endi] 
# indicates an edge from node ui to vi that can only be used at any integer time t 
# such that starti <= t <= endi.

# You start at node 0 at time 0.

# In one unit of time, you can either:

# Wait at your current node without moving, or
# Travel along an outgoing edge from your current node if the current time t satisfies starti <= t <= endi.
# Return the minimum time required to reach node n - 1. If it is impossible, return -1.

def minTime(n, edges):
    adj_list = [[] for _ in range(n)]
    times = [float('inf')] * n
    times[0] = 0

    for u,v,s,e in edges:
        adj_list[u].append((v,s,e))

    from heapq import heappop, heappush
    hq = []
    heappush(hq, (0, 0)) # time, node

    while hq:
        du, u = heappop(hq)

        if du > times[u]:
            continue

        for v,s,e in adj_list[u]:
            if du > e:
                continue
            if s <= du <= e:
                if du+1 < times[v]:
                    times[v] = du+1
                    heappush(hq, (du+1, v))
            if du < s:
                if s+1 < times[v]:
                    times[v] = s+1
                    heappush(hq, (s+1, v))

    return times[n-1] if times[n-1] != float('inf') else -1

n = 4
edges = [[0,1,0,3],[1,3,7,8],[0,2,1,5],[2,3,4,7]] # 5
print(minTime(n, edges))

n = 3
edges = [[1,0,1,3],[1,2,3,5]]
print(minTime(n, edges))