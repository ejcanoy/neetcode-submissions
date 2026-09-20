# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def ddfs(rootp, rootq):
            if not rootp and not rootq:
                return True
            
            if not rootp or not rootq:
                return False
            
            if rootp.val != rootq.val:
                return False
            
            return ddfs(rootp.left, rootq.left) and ddfs(rootp.right, rootq.right)

        return ddfs(p, q)            