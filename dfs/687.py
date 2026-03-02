# Given the root of a binary tree, return the length of the longest path, where each node in the 
# path has the same value. This path may or may not pass through the root.

# The length of the path between two nodes is represented by the number of edges between them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longestUnivaluePath(root):
    ans = 0
    def dfs(node):
        nonlocal ans
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        left_path = right_path = 0
        if node.left and node.left.val == node.val:
            left_path = left + 1
        if node.right and node.right.val == node.val:
            right_path = right + 1

        ans = max(ans, left_path + right_path)
        return max(left_path, right_path)

    dfs(root)
    return ans
        