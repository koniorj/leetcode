# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x): # szukamy parenta jakiegos pola
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry: # juz naleza do tej samej wyspy
            return 
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]

def largestIsland(grid):
    n = len(grid)
    uf = DSU(n*n)
    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            # grid[i][j] = 2 # to znaczy ze juz tu bylismy
            for di, dj in moves:
                ni, nj = di+i, dj+j
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                    uf.union(i*n+j, ni*n+nj)

    ans = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                seen = set()
                size = 1
                for di, dj in moves:
                    ni, nj = di+i, dj+j
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                        root = uf.find(ni*n+nj)
                        if root not in seen:
                            size += uf.size[root]
                            seen.add(root)
                ans = max(ans, size)

    return ans if ans > 0 else n*n



grid = [[1,0],[0,1]]
print(largestIsland(grid))