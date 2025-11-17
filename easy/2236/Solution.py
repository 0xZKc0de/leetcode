from typing import Optional

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        """
        Check if the root node's value equals the sum of its children's values.
      
        Args:
            root: The root node of a binary tree with exactly 3 nodes (root and 2 children)
      
        Returns:
            bool: True if root.val == root.left.val + root.right.val, False otherwise
        """
        # Check if parent node value equals sum of left and right child values
        return root.val == root.left.val + root.right.val