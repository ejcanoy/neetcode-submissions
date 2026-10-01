class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map values to their index in inorder for O(1) lookup
        inorder_idx_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            # Base case: no elements in current subtree
            if in_left > in_right:
                return None

            # 1. Pick current root value from preorder traversal
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # 2. Split inorder traversal into left and right subtrees
            mid = inorder_idx_map[root_val]

            # 3. Build left subtree first, then right subtree
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)