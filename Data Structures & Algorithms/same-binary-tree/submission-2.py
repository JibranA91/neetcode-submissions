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
            p_node, q_node = d.popleft()

            if not p_node and not q_node: continue

            if p_node is None or q_node is None or p_node.val != q_node.val: 
                return False

            d.append((p_node.left, q_node.left))
            d.append((p_node.right, q_node.right))
            
            
            
        return True
