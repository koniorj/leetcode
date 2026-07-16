# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
# horizontally or vertically neighboring. The same letter cell may not be used more than once.

# It's as if we were looking for a path that consists of given weights. DFS. 
    
class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        rows = len(board)
        cols = len(board[0])
        word_len = len(word)

        def within_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def backtrack(r, c, index):
            if index == word_len:
                return True
            
            if not within_bounds(r, c) or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            for dr, dc in dirs:
                if backtrack(r + dr, c + dc, index + 1):
                    return True
            
            board[r][c] = temp
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
sol = Solution()
print(sol.exist(board, word))