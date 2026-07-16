# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None
        value = preorder[0]
        root = TreeNode(value)

        
        root.left = self.buildTree(preorder.copy()[1:][:inorder.index(value)] ,inorder.copy()[:inorder.index(value)])
        root.right = self.buildTree(preorder.copy()[1:][inorder.index(value):] ,inorder.copy()[inorder.index(value) + 1:])
        return root