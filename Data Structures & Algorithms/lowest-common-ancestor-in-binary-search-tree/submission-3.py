# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        p_parents = []
        q_parents = []

        def dfs(node, parents=[]):
            nonlocal p_parents, q_parents
            if not node:
                return
            
            path = parents+[node]
            if node.val == p.val:
                p_parents = path
            
            if node.val == q.val:
                q_parents = path

            dfs(node.left, path)
            dfs(node.right, path)
        

        dfs(root)

        print([a.val for a in p_parents])
        print([a.val for a in q_parents])

        res = None
        for a,b in zip(p_parents, q_parents):
            if a.val==b.val:
                res = a
        
        return res

