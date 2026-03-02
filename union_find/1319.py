# There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

# You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

# Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return False
        
        if self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
            self.rank[rooty] += self.rank[rootx]
        elif self.rank[rootx] > self.rank[rooty]:
            self.parent[rooty] = rootx
            self.rank[rootx] += self.rank[rooty]
        else:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1

        self.count -= 1
        return True

def makeConnected(n, connections):
    # chcemy stworzyc kruskalem jedna prowincje
    # bedziemy to robic usuwajac niektore krawedzie
    # najpierw policzymy, ile komputerow musimy
    # dolaczyc do unii. Dodamy miedzy nimi minimalna
    # ilosc kabli, ktore wezmiemy od komputerow,
    # ktore znajdziemy iterujac i sprawdzajac unionfind.
    wires = len(connections)
    if wires < n-1:
        return -1
    
    dsu = DSU(n)

    for v, u in connections:
        dsu.union(v, u)

    if wires >= n-1:
        return dsu.count - 1
    
    return -1

connections = [[0,1],[0,2],[1,2]] # 1
n = 4
print(makeConnected(n, connections))