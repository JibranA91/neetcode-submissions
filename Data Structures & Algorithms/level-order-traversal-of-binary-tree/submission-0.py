# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque, defaultdict

        d = deque([(root,0)])
        res_dict = defaultdict(list)

        if not root:
            return []

        while d:
            node, level = d.popleft()
            res_dict[level].append(node.val)

            if node.left:
                d.append((node.left, level+1))
            if node.right:
                d.append((node.right, level+1))
        
        return [res_dict[i] for i in range(len(res_dict))]

