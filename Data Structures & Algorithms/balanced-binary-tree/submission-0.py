# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(node, h=0):
            if not node:
                return h
            
            lh = h + dfs(node.left)
            rh = h + dfs(node.right)

            if abs(lh - rh) > 1:
                self.balanced=False
                return 0
            
            return 1 + max(lh, rh)
        
        dfs(root)
        return self.balanced
        
