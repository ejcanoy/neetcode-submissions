# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        def validate(lb, root, rb):
            if not root:
                return True
            if not (lb < root.val < rb):
                return False
            return validate(lb, root.left, root.val) and validate(root.val, root.right, rb)
        
        return validate(float("-inf"), root, float("inf"))