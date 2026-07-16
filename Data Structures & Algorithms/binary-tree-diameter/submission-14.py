# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        def h(root):
            if not root:
                return 0
            
            heightL = h(root.left)
            heightR = h(root.right)
            self.maxD = max(heightL + heightR, self.maxD)

            return 1 + max(heightL, heightR)

        h(root)
        return self.maxD
