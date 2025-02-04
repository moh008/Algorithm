"""
leaf 노드에서 시작한다고 생각하면됨, 그럼 기본적으로 depth는 1이 됨
그 부모 노드에서 왼쪽 자식노드와 오른쪽 자식노드중 depth가 더 큰값을 고른다 
부모노드로 올라왔으니 1을 더해서 계속 리턴하면서 root노드까지 도달
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:    #root 노드가 없을때 (edgecase)
            return 0
        return 1 + max( #왼쪽과 오른쪽 자식노드중 가장 큰 depth를 가진 노드를 취하고 1을 더해서 리턴
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )