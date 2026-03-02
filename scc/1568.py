# You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is
# a maximal 4-directionally (horizontal or vertical) connected group of 1's.

# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

# In one day, we are allowed to change any single land cell (1) into a water cell (0).

# Return the minimum number of days to disconnect the grid.

def minDays(grid):
    # probujemy rozwiazac tarjanem. Jesli znajdziemy punkt artykulacji, to wystarczy usunac 1.
    # jesli nie znajdziemy a jest jakas wyspa to 2.
    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    m = len(grid)
    n = len(grid[0])
    tin = [[-1 for _ in range(n)] for _ in range(m)]
    low = [[-1 for _ in range(n)] for _ in range(m)]
    time = 0
    visited = [[0 for _ in range(n)] for _ in range(m)]
    vis_count = 0
    art = []

    def dfs(node, parent): # bo nie mozemy sie wracac do parenta
        nonlocal time, vis_count
        x, y = node
        xp, yp = parent
        visited[x][y] = 1 # odwiedzone
        tin[x][y] = low[x][y] = time
        time += 1
        vis_count += 1
        child = 0

        for dx, dy in moves:
            nx, ny= dx+x, dy+y
            if nx == xp and ny == yp:
                continue
            if not 0 <= nx < m and 0 <= ny < n:
                continue
            if grid[nx][ny] == 0:
                continue

            if visited[nx][ny] == 0:
                child += 1
                dfs((nx,ny), (x,y))
                low[x][y] = min(low[x][y], low[nx][ny])
                if low[nx][ny] >= tin[x][y] and xp != -1 and yp != -1:
                    art.append((x, y))
            else:
                low[x][y] = min(low[x][y], tin[nx][ny])

        if xp == -1 and yp == -1 and child > 1:
            art.append((x, y))

    found = False
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                if found: 
                    return True
                found = True
                dfs((i, j), (-1, -1))

    if art:
        return 1
        # If no articulation point, check if there is at least one land cell
    total_land = sum(sum(row) for row in grid)
    if total_land == 0:
        return 0
    if total_land == 1:
        return 1
    return 2