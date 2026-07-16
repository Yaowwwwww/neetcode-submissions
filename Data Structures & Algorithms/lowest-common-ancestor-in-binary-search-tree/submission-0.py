# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(root, node):
            if not root:
                return False
            if root.val == node.val:
                return True
            left = search(root.left, node)
            right = search(root.right, node)
            return left or right
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if p.val == root.val:
            foundp = True
        elif p.val < root.val:
            foundp = search(root.left, p)
        else:
            foundp = search(root.right, p)

        if q.val == root.val:
            foundq = True
        elif q.val < root.val:
            foundq = search(root.left, q)
        else:
            foundq = search(root.right, q)

        if foundp and foundq:
            return root
        else:
            return min(self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q))




