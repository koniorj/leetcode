# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one 
# outgoing edge.

# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a 
# directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

# Return the length of the longest cycle in the graph. If no cycle exists, return -1.

# A cycle is a path that starts and ends at the same node.

# bedziemy po prostu implementowac kosaraju

def longestCycle(edges):
    # DFS, reverse edges, DFS
    from collections import defaultdict
    n = len(edges)
    graph = defaultdict(list)
    transpose = defaultdict(list)

    for u, v in enumerate(edges):
        graph[u].append(v)
        transpose[v].append(u)

    visited = set()
    stack = []
    def dfs1(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs1(v)
        stack.append(u)

    def dfs2(u):
        visited.add(u)
        scc.add(u)
        for v in transpose[u]:
            if v not in visited:
                dfs2(v)
        
    for u in range(n):
        if u not in visited:
            dfs1(u)

    cycle = float('-inf')
    visited = set()
    while stack:
        u = stack.pop()
        if u not in visited:
            scc = set() # kazda nowa SCC
            dfs2(u)
            cycle = max(cycle, len(scc))

    return cycle

edges = [3,3,4,2,3]
print(longestCycle(edges))