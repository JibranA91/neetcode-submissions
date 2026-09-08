# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        dfs = lambda node: (1 + max(dfs(node.left), dfs(node.right))) if node else 0

        return dfs(root)