# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(a, b):
            if not a and not b:
                return True
            if (not a and b) or (a and not b) or (a.val != b.val):
                return False
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        if not root:
            return False

        if root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    