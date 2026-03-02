# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally 
# connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

def closedIsland(grid):
    n = len(grid) # rows
    m = len(grid[0]) # cols
    moves = [(1,0),(0,1),(-1,0),(0,-1)]

    def within(x, y):
        return 0 <= x < n and 0 <= y < m

    # bedziemy rozwiazywac DFS-em. Odwiedzone pole oznaczamy jako 1
    def dfs(x,y):
        if not within(x, y):
            return False
        if grid[x][y] == 1:
            return True
        
        grid[x][y] = 1
        
        ans = True
        for dx, dy in moves:
            if not dfs(dx+x, dy+y):
                ans = False
                
        return ans
    
    islands = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                if dfs(i, j):
                    islands += 1

    return islands

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]] # 2
print(closedIsland(grid))            
            