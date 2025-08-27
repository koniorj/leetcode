# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. 
# You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

def longestIncreasingPath(matrix):
    moves = [(1,0), (0,1), (-1,0),(0,-1)]
    m = len(matrix[0])
    n = len(matrix)

    # czy serio dfs z kazdego!! pola? masakra... trzeba uzyc DP
    dp = [[0 for _ in range(m)] for _ in range(n)] # najdluzsza sciezka zaczynajaca sie tutajS

    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]
        best = 1

        for di, dj in moves:
            if 0 <= i+di < n and 0 <= j+dj < m and matrix[i][j] < matrix[i+di][j+dj]:
                prev = dfs(i+di, j+dj)
                best = max(best, prev+1)

        dp[i][j] = best
        return best
    
    res = 0
    for i in range(n):
        for j in range(m):
            res = max(res, dfs(i,j))

    return res

matrix = [[9,9,4],[6,6,8],[2,1,1]] # 4
print(longestIncreasingPath(matrix))