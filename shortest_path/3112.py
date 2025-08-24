# There is an undirected graph of n nodes. You are given a 2D array edges, 
# where edges[i] = [ui, vi, lengthi] describes an edge between node ui and node 
# vi with a traversal time of lengthi units.

# Additionally, you are given an array disappear, where disappear[i] denotes the time when the node 
# i disappears from the graph and you won't be able to visit it.

# Note that the graph might be disconnected and might contain multiple edges.

# Return the array answer, with answer[i] denoting the minimum units of time required to reach node 
# i from node 0. If node i is unreachable from node 0 then answer[i] is -1.

def minimumTime(n, edges, disappear):
    dist = [float('inf')] * n
    dist[0] = 0
    # answer = [-1] * n
    # answer[0] = 0

    adj_list = [[] for _ in range(n)]
    for u, v, w in edges:
        adj_list[u].append((w, v))
        adj_list[v].append((w, u))

    from heapq import heappop, heappush
    hq = []
    heappush(hq, (0, 0)) # time, node

    while hq:
        dv, v = heappop(hq)

        dis = disappear[v]
        if dv >= dis:
            continue

        if dv > dist[v]:
            continue

        for du, u in adj_list[v]:
            if dv+du < dist[u]:
                dist[u] = dv+du
                heappush(hq, (dv+du, u))

    answer = dist
    for i in range(n):
        if dist[i] >= disappear[i]:
            answer[i] = -1

    return answer

n = 3
edges = [[0,1,2],[1,2,1],[0,2,4]]
disappear = [1,3,5]
print(minimumTime(n, edges, disappear)) # 0 2 3

n = 3
edges = [[0,1,2],[1,2,1],[0,2,4]]
disappear = [1,1,5]
print(minimumTime(n, edges, disappear)) # 0 -1 4