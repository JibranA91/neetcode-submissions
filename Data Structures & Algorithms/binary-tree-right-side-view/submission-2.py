# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        if not root:
            return []
            
        d = deque([(root,0)])
        res = {}

        while d:
            node, level = d.popleft()
            res[level] = node.val
            
            if node.left:
                d.append((node.left, level+1))
            if node.right:
                d.append((node.right, level+1))
            
        
        return [res[i] for i in range(len(res))]