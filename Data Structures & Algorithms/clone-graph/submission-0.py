"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        hm = {}

        def dfs(node):
            if node in hm:
                return hm[node]

            cur = Node(node.val)
            hm[node] = cur

            for neighbor in node.neighbors:
                cur.neighbors.append(dfs(neighbor))
            return cur



        return dfs(node)