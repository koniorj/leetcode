# You are given two integers, n and threshold, as well as a directed weighted graph of n nodes
#  numbered from 0 to n - 1. The graph is represented by a 2D integer array edges, where 
# edges[i] = [Ai, Bi, Wi] indicates that there is an edge going from node Ai to node Bi with weight Wi.

# You have to remove some edges from this graph (possibly none), so that it satisfies the following conditions:

# Node 0 must be reachable from all other nodes.
# The maximum edge weight in the resulting graph is minimized.
# Each node has at most threshold outgoing edges.
# Return the minimum possible value of the maximum edge weight after removing the necessary edges.
# If it is impossible for all conditions to be satisfied, return -1.

def minMaxWeight(n, edges, threshold):
    # to jest takie MST po prostu. Tne treshold nie ma znaczenia za duzego. Musimy tylko 
    # odwrocic direction krawedzi i sprawdzic czy z 0 da sie wszedzie dojsc i tyle.

    adj_list = [[] for _ in range(n)]
    visited = set()
    max_w = -1

    for u,v,w in edges:
        adj_list[v].append((w,u))

    from heapq import heappop, heappush
    hq = []
    for w,v in adj_list[0]:
        heappush(hq, (w, 0, v))
    visited.add(0)

    while hq:
        w, u, v = heappop(hq)

        if v in visited:
            continue
        visited.add(v)

        max_w = max(max_w, w)
        for w2, v2 in adj_list[v]:
            if v2 not in visited:
                heappush(hq, (w2, v, v2))

    return max_w if len(visited) == n else -1

n = 5
edges = [[1,2,1],[1,3,3],[1,4,5],[2,3,2],[3,4,2],[4,0,1]] # 2
threshold = 1
print(minMaxWeight(n, edges, threshold))