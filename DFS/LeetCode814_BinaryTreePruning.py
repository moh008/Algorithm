class Solution:
  def pruneTree(self, root: TreeNode) -> TreeNode:
    if root is None: return None
    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)
    if root.val == 0 and root.left is None and root.right is None: return None
    return root