"""
2진트리의 유효성을 검사. 왼쪽 자식은 현재 노드값보다 작아야하고, 오른쪽 자식은 현재 노드값보다 커야함.
DFS를 사용하여 탐색진행. Helper function필요.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def isValidBST(self, root:Optional[TreeNode]) -> bool:
    #Helper function
    def isValid(node, low, high):
      #자식노드까지 traverse한 경우 True를 반환. 왜냐면 비교할게 없거든
      if not node:
        return True
      # 현재 노드의 값이 왼쪽 자식의 값이나 오른쪽 자식의 값 범위안에 있지않으면 False
      if not low < node.val < high:
        return False
      # 이부분이 중요. helperfunction을 각각 왼쪽, 오른쪽으로 뻗어나가게 한다.
      return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)
    # 현재 root값으로 시작하여, 범위는 문제에서 -2^31 <= Node.val <= 2^31 - 1이므로 각각 음과 양의 무한대로 설정해준다.
    return isValid(root, float(-inf), float(inf))