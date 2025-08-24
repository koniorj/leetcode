# You are given an m x n binary matrix grid and an integer health.

# You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).
# You can move up, down, left, or right from one cell to another adjacent cell as long 
# as your health remains positive.

# Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

# Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

def findSafeWalk(grid, health):
    m = len(grid)
    n = len(grid[0])
    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    
    start_health = health - grid[0][0]
    if start_health <= 0:
        return False
    
    best = [[-1] * n for _ in range(m)]  
    best[0][0] = start_health
    
    stack = [(start_health, 0, 0)]

    while stack:
        curr, x, y = stack.pop()

        if x == m-1 and y == n-1 and curr > 0:
            return True
        
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n:
                new = curr - grid[nx][ny]
                if new > 0 and best[nx][ny] < new:
                    best[nx][ny] = new
                    stack.append((new, nx, ny))

    return False

grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
health = 1
print(findSafeWalk(grid, health))