# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        paths = []
        def dfs(node, d=0):
            if not node:
                return d

            d += 1
            return max(dfs(node.left, d), dfs(node.right, d))
        
        return dfs(root)

