# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque

        d = deque([(p,q)])

        while d:
            a,b = d.popleft()
            
            if not a and not b: continue

            if a is None or b is None or a.val != b.val:
                return False
            
            d.append((a.left, b.left))
            d.append((a.right, b.right))
        
        return True