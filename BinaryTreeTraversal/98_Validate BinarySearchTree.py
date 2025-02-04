"""
좌측 섭트리로 내려갈때:
    - 하한값: 부모 노드의 하한값 (-무한대)
    - 상한값: 부모 노드의 값
우측 섭트리로 내려갈때:
    - 하한값: 부모 노드의 값
    - 상한값: 부모 노드의 상한값 (무한대)
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode])-> bool:
        if not root:    #root가 없을땐 이진탐색 트리라 판단
            return True
        def dfs(node, low, high):
            if not node:#마찬가지로 탐색중인 노드가 발견되지 않으면 이진탐색 트리라 판단
                return True
            if not (low < node.val < high): #탐색중인 노드의 값이 하한값과 상한값 사이에 있지않다면 false
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)    #왼쪽, 오른쪽 자식노드 탐색하러 내려감 상한값 하한값은
        return dfs(root, float("-inf"), float("inf"))                                   #왼쪽 섭트리냐 오른쪽 섭트리냐에 따라 다름
        #dfs 콜은 root노드로 하는데 상한값 하한값은 root노드에선 정해지지 않았으므로 -무한대, 무한대로 설정함