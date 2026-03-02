# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 
# represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded 
# by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.

def islandPerimeter(grid):
    from collections import deque
    perimeter = 0
    n = len(grid)
    m = len(grid[0])

    start = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                start = (i,j)
                break
        if start:
            break
        
    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]] = True
    dq = deque([start]) # przy czym start na pewno da nam juz perimeter 2
    while dq:
        x,y = dq.popleft()
        
        for dx, dy in moves:
            nx, ny = dx+x, dy+y
            if 0 <= nx < n and 0 <= ny < m:
                # case 1: jest tam woda i peri sie zwieksza
                if grid[nx][ny] == 0:
                    perimeter += 1
                else: # case 2: jest tam wyspa
                    # case 2.1: bylismy juz na niej -> nic nie robimy
                    # case 2.2: nie bylismy
                    if not visited[nx][ny]:
                        dq.append((nx,ny))
                        visited[nx][ny] = True
            else:
                perimeter += 1

    return perimeter


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islandPerimeter(grid))
