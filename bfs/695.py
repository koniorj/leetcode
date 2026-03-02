# You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
#  connected 4-directionally (horizontal or vertical.) You may assume all four edges of 
# the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

from collections import deque
def maxAreaOfIsland(grid):
    n = len(grid)
    m = len(grid[0])

    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = grid[0][0]

    # bfsem bedziemy wchodzic do kazdej nieodwiedzonej komorki, ktora nie jest 0.
    def bfs(x, y, visited):
        dq = deque()
        dq.append((x, y))
        visited.add((x,y))
        area = 0

        while dq:
            x, y = dq.popleft()

            # if (x,y) in visited:
            #     continue # bylismy tu wczesniej

            # if grid[x][y] == 0: # nic nie musimy robic. Skipujemy
            #     continue

            area += 1

            for dx, dy in moves:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 1 and (nx, ny) not in visited: # mamy sasiada, ktory nie byl wczesniej policzony
                        visited.add((nx,ny))
                        dq.append((nx,ny))

        return area
    
    ans = 0
    visited = set()
    # kazde wywolanie bfsa znajduje nam wyspe.
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and (i,j) not in visited:
                ans = max(ans, bfs(i,j,visited))

    return ans

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))