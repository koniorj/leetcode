# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, 
# one additional edge added. The added edge has two different vertices chosen from 1 to n, 
# and was not an edge that already existed. The graph is represented as an array edges of length 
# n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
# If there are multiple answers, return the answer that occurs last in the input.

# We're trying to find a redunant edge in an almost 'tree' (n edges). Let's use Union Find:
# in a tree, every edge connects two different sets (no cycles)
# if we find an edge, where find(x) = find(y), then we found a redunant edge 

def findRedundantConnection(edges):
    n = len(edges)
    parent = [i for i in range(n+1)] #we're indexing from 1, not from 0

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x] 
        return x
    
    for u, v in edges:
        if find(u) == find(v):
            return [u, v]
        parent[find(v)] = find(u)
    return []

edges = [[1,2],[1,3],[2,3]] # [2,3]
print(findRedundantConnection(edges))

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]] # [1,4]
print(findRedundantConnection(edges))
