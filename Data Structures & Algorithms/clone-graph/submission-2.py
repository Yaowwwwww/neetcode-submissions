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
            return node

        map = {}
        def dfs(old_root):
            if old_root in map:
                return map[old_root]
            map[old_root] = Node(old_root.val)
            for old_neighbor in old_root.neighbors:
                map[old_root].neighbors.append(dfs(old_neighbor))
            return map[old_root]

        return dfs(node)
        