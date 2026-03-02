# You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

# 0 means the cell cannot be walked through.
# 1 represents an empty cell that can be walked through.
# A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's 
# height.
# In one step, you can walk in any of the four directions: north, east, south, and west. If you are 
# standing in a cell with a tree, you can choose whether to cut it off.

# You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at
#  its cell becomes 1 (an empty cell).

# Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees.
#  If you cannot cut off all the trees, return -1.

# Note: The input is generated such that no two trees have the same height, and there is at least 
# one tree needs to be cut off.

def cutOffTree(forest):
    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    n = len(forest)
    m = len(forest[0])
    trees = sorted((forest[i][j], i, j) for i in range(n) for j in range(m) if forest[i][j] > 1)

    from collections import deque

    def bfs(sx, sy, tx, ty):
        if sx == tx and sy == ty: 
            return 0
        
        dq = deque()
        dq.append((0, sx, sy))
        visited = {(sx, sy)}

        while dq:
            steps, x, y = dq.popleft()
   
            for dx, dy in moves:
                nx, ny = dx+x, dy+y
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and forest[nx][ny] != 0:
                    if nx == tx and ny == ty:
                        return steps+1
                    visited.add((nx, ny))
                    dq.append((steps+1, nx, ny))

        return -1
    
    sx = 0
    sy = 0
    steps = 0
    for h, x, y in trees:
        dist = bfs(sx, sy, x, y)
        if dist == -1:
            return -1
        steps += dist
        sx = x
        sy = y

    return steps


forest = [[1,2,3],[0,0,4],[7,6,5]]
print(cutOffTree(forest))