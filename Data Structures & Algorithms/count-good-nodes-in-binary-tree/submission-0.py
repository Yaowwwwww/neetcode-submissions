# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGoodNodes(root, currMax):
            if not root:
                return 0
            
            if root.val > currMax:
                currMax = root.val
            res = countGoodNodes(root.left, currMax) + countGoodNodes(root.right, currMax)
            res += (1 if root.val >= currMax else 0)
            return res

        if not root:
            return 0
        currMax = root.val
        return countGoodNodes(root, currMax)
