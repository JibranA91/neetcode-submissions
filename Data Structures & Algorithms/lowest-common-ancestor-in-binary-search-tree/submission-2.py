# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        pq = []
        def dfs(node=None, anc=[]):
            if not node:
                return
            
            if node.val in [p.val,q.val]:
                pq.append(anc.copy() + [node])
            
            dfs(node.left, anc + [node])
            dfs(node.right, anc + [node])
        
        dfs(root)
        return [a for a,b in zip(pq[0],pq[1]) if a.val==b.val][-1]

