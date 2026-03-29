# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, min_value=float("-Inf"), max_value=float("+Inf")):
            if not node:
                return True
        
            return (
                (min_value < node.val < max_value) and 
                dfs(node.left, min_value, node.val) and 
                dfs(node.right, node.val, max_value)
                )
        
        return dfs(root)