class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        # 1. Check if the current tree matches
        if isSameTree(root, subRoot):
            return True

        # 2. Otherwise, check left or right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)