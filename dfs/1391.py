# You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

# 1 which means a street connecting the left cell and the right cell.
# 2 which means a street connecting the upper cell and the lower cell.
# 3 which means a street connecting the left cell and the lower cell.
# 4 which means a street connecting the right cell and the lower cell.
# 5 which means a street connecting the left cell and the upper cell.
# 6 which means a street connecting the right cell and the upper cell.

# You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

# Notice that you are not allowed to change any street.

# Return true if there is a valid path in the grid or false otherwise.

def hasValidPath(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    
    dirs = (
        ((0, -1), (0, 1)),   # 1: l, r
        ((-1, 0), (1, 0)),   # 2: u, d
        ((0, -1), (1, 0)),   # 3: l, d
        ((0, 1),  (1, 0)),   # 4: r, d
        ((0, -1), (-1, 0)),  # 5: l, u
        ((0, 1),  (-1, 0)),  # 6: r, u
    )

    def dfs(x, y):
        if x == m-1 and y == n-1:
            return True
        
        visited[x][y] = True

        for dx, dy in dirs[grid[x][y]-1]:
            if 0 <= dx+x < m and 0 <= dy+y < n and not visited[dx+x][dy+y]:
                if (-dx, -dy) in dirs[grid[dx+x][dy+y]-1]:
                    if dfs(dx+x, dy+y):
                        return True
                    
        return False
    
    return dfs(0,0)

def hasValidPath(grid):
    m = len(grid)
    n = len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    from collections import deque
    
    dirs = (
        ((0, -1), (0, 1)),   # 1: l, r
        ((-1, 0), (1, 0)),   # 2: u, d
        ((0, -1), (1, 0)),   # 3: l, d
        ((0, 1),  (1, 0)),   # 4: r, d
        ((0, -1), (-1, 0)),  # 5: l, u
        ((0, 1),  (-1, 0)),  # 6: r, u
    )

    stack = deque()
    stack.append((0,0))
    while stack:
        x, y = stack.pop()
        if x == m-1 and y == n-1:
            return True
        
        visited[x][y] = True

        for dx, dy in dirs[grid[x][y]-1]:
            nx, ny = dx+x, dy+y
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if (-dx, -dy) in dirs[grid[nx][ny]-1]:
                    stack.append((nx,ny))

    return False
    

