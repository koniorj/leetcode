# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at 
# most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has 
# not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, 
# return the largest possible number of stones that can be removed.

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)] 
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False # nie mamy wyspy, naleza do tego samego
        if rx != ry:
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
                self.parent[ry] = rx
            elif self.rank[rx] > self.rank[ry]:
                self.parent[ry] = rx
            else:
                self.parent[rx] = ry
        return True # wyspa byla
            
def removeStones(stones):
    # to jest zadanie na union find, szukamy ilosci wysp tak naprawde. Punkty maja krawedz miedzy
    # soba jesli maja takie same wspolrzedne

    n = len(stones)
    # chcemy zrzutowac jakby wspolrzedne na ilosc punktow bo inaczej to pamieciowo bedzie krucho...
    # co najwyzej n wspolrzednych na x i na y, teoretycznie moze wbic az 2n
    xs = [x for x, _ in stones]
    ys = [y for _, y in stones]
    xmap = {x: i for i, x in enumerate(set(xs))}
    ymap = {y: i for i, y in enumerate(set(ys))}
    uf = DSU(len(xmap) + len(ymap))

    for x, y in stones:
        uf.union(xmap[x], len(xmap) + ymap[y])

    components = set()
    for x, y in stones:
        components.add(uf.find(xmap[x]))
        components.add(uf.find(len(xmap) + ymap[y]))

    islands = len(components)
    return n - islands

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
print(removeStones(stones))