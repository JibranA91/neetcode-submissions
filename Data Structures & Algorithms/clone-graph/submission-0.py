"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        node_dict = {}
        def dfs(n):

            if n in node_dict:
                return node_dict[n]
            
            new_node = Node(n.val)
            node_dict[n] = new_node
            new_node.neighbors = [dfs(nb) for nb in n.neighbors]
        
            return new_node        

        return dfs(node) if node else None

