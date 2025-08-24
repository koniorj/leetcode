class DSU:
    def __init__(self, n):
        self.size = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        uroot = self.find(u)
        vroot = self.find(v)

        if uroot == vroot:
            return False # nie mozemy dodac krawedzi!
        if self.rank[uroot] > self.rank[vroot]:
            self.parent[vroot] = uroot
        elif self.rank[uroot] < self.rank[vroot]:
            self.parent[uroot] = vroot
        else:
            self.parent[vroot] = uroot
            self.rank[uroot] += 1
        return True

def canBuild(n, edges, k, min_strength):
    dsu = DSU(n)
    upgrades = 0
    cnt_edges = 0

    other = []
    for u, v, s, m in edges:
        if m == 1:
            if s < min_strength:
                return False
            if dsu.union(u, v): # upewniamy sie, czy nie stworzyly cyklu te krawedzie
                cnt_edges += 1
            else:
                return False
        else:
            if s >= min_strength:
                other.append((0, s, u, v)) # bez upgrade
            if 2 * s >= min_strength:
                other.append((1, s, u, v))

    other.sort() # najpierw te, ktore nie wymagaja upgrade'u
    for upgrade, s, u, v in other:
        if dsu.union(u, v):
            cnt += 1
            upgrades += upgrade
            if upgrades > k:
                return False
            
    return cnt_edges == n-1


def maxStability(n, edges, k):
    left = 1
    right = max(s for _, _, s, _ in edges) * 2
    res = -1

    while left <= right:
        mid = (left+right)//2
        if canBuild(n, edges, k, mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1

    return res