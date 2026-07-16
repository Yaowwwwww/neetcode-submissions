# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower, upper):
            if not (lower < root.val and root.val < upper):
                return False
            if not root.left and not root.right:
                return True
            left = (False if root.left and not dfs(root.left, lower, root.val) else True)
            right = (False if root.right and not dfs(root.right, root.val, upper) else True)
            return left and right

        return dfs(root, float('-inf'), float('inf'))