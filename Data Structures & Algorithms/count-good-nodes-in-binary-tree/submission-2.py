# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res

        def dfs(root, prevMax):
            nonlocal res  # Tells Python to use the 'res' outside the function
            if not root:
                return 
            if prevMax <= root.val:
                res += 1
            if root.right:
                dfs(root.right, max(prevMax, root.val))
            if root.left:
                dfs(root.left, max(prevMax, root.val))

        dfs(root, float('-inf'))
        return res
