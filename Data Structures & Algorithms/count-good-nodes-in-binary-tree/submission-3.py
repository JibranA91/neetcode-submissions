# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:        

        good_nodes = 0
        visited = set([root])
        q = collections.deque([(root,float('-Inf'))])
        while q:
            node, max_val = q.popleft()
            if node.val >= max_val:
                good_nodes += 1
            
            max_val = max(max_val, node.val)
            if node.left and node.left not in visited:
                visited.add(node.left)
                q.append((node.left, max_val))
            if node.right and node.right not in visited:
                visited.add(node.right)
                q.append((node.right, max_val))
        
        return good_nodes



