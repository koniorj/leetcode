# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

def largestIsland(grid):
    # bedziemy rozwiazywac zadanie BFS-em. Kazda wyspa jest osobnym komponentem i dostanie swoj wlasny kolor.
    # Mozemy zmieniac dane, wiec bedziemy nadpisywac grid ID roznych wysp. Potem poszukamy pola, ktore
    # sprawi ze polaczenie dwoch wysp da nam wynik
    max_size = 0
    n = len(grid)
    grid = grid[:]
    moves = [(1,0), (0,1), (-1,0), (0,-1)]
    from collections import deque

    # w tym bfsie po prostu szukamy rozmiaru danej wyspy
    def bfs(x, y, id): # wyspa zaczynajaca sie w x,y o id rownym id
        dq = deque()
        visited = set()
        visited.add((x,y))
        grid[x][y] = id
        size = 1
        dq.append((x,y))

        while dq:
            x, y = dq.popleft()

            for dx, dy in moves:
                nx, ny = dx+x, dy+y
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and (nx,ny) not in visited:
                    grid[nx][ny] = id
                    size += 1
                    dq.append((nx,ny))

        return size
    
    island_sizes = []
    id = 2
    for i in range(n):
        for j in range(n): # interesuja nas tylko pola oznaczone jako 1! Bo zmieniamy id wszystkie i tak.
            # indeksacja przeusnieta o 2 przy ids
            if grid[i][j] == 1:
                size = bfs(i,j,id)
                max_size = max(max_size, size)
                island_sizes.append(size)
                id += 1

    # teraz probujemy polaczyc dwie wyspy
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                ids = set()
                nsize = 1
                for di, dj in moves:
                    ni, nj = di+i, dj+j
                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] > 1 and grid[ni][nj] not in ids:
                            ids.add(grid[ni][nj])
                for id in ids:
                    nsize += island_sizes[id-2]
                max_size = max(max_size, nsize)

    return max_size

grid = [[1,1],[1,1]]
print(largestIsland(grid))
grid = [[1,0],[0,1]]
print(largestIsland(grid))
grid = [[1,1],[1,0]]
print(largestIsland(grid))