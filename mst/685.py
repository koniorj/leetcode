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
            return False # sa w tej samej union juz
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
        