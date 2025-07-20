"""
2진트리 문제
값이 0인 노드의 자식들마저도 값이 0이면 통째로 가지치기 들어가야함
만약 자식이 없는데(leaf) 노드 값이 0이면 셀프 가지치기 들어감

제일 먼저 root 노드를 방문해서 비었는지 확인부터함
Traverse left and right child
방문한 노드의 값이 0이고 왼쪽이나 오른쪽 자식이 없으면(leaf일때) 가지치기 (return None)
마지막에 root를 반환해서 트리 반환
"""
class Solution:
  def pruneTree(self, root: TreeNode) -> TreeNode:
    if root is None: return None
    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)
    if root.val == 0 and root.left is None and root.right is None: return None
    return root