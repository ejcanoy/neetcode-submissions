# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def bfs(root):
            nonlocal res
            if not root:
                return 0
            
            left = bfs(root.left)
            right = bfs(root.right)
            res = max(res, 1 + left + right)
            return 1 + max(left, right)
        
        bfs(root)
        return res - 1