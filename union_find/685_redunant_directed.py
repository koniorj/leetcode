# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) 
# for which all other nodes are descendants of this node, plus every node has exactly one parent, 
# except for the root node which has no parents.
# The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n),
#  with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, 
# and was not an edge that already existed.
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] 
# that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.
# Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. 
# If there are multiple answers, return the answer that occurs last in the given 2D-array.

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_r = self.find(x)
        y_r = self.find(y)

        if x_r == y_r:
            return False
        if x_r != y_r:
            if self.rank[x_r] == self.rank[y_r]:
                self.parent[y_r] = x_r
                self.rank[x_r] += 1
            elif self.rank[x_r] > self.rank[y_r]:
                self.parent[y_r] = x_r
            else:
                self.parent[x_r] = y_r
        return True  

class Solution:
    def findRedundantDirectedConnection(self, edges):
        n = len(edges)
        parents = [0] * (n+1)
        cand1 = cand2 = None

        # case 1: a node v has two nodes pointing to it
        for u, v in edges:
            if parents[v]:
                cand1 = [parents[v],v]
                cand2 = [u,v]
                break
            parents[v] = u

        # case 2: no node has two parents, instead we get a cycle (dsu for better time complexity)
        dsu = DSU(n)
        for u, v in edges:
            if [u, v] == cand2:
                continue
            if not dsu.union(u, v):
                return cand1 if cand1 else [u, v]

        return cand2
        