# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    # tutaj uzywamy dfsa ktory nie jest iteracyjny
    ans = []

    def dfs(cur_node, cur_sum, cur_path):
        if not cur_node:
            return
        
        cur_sum += cur_node.val
        cur_path.append(cur_node.val)
        if not cur_node.left and not cur_node.right and cur_sum == targetSum:
            ans.append(cur_path[:])
        dfs(cur_node.left, cur_sum, cur_path)
        dfs(cur_node.right, cur_sum, cur_path)
        cur_path.pop()

    dfs(root, 0, [])
    return ans

root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
targetSum = 22
print(pathSum(root, targetSum))