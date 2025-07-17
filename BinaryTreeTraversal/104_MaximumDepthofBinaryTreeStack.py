"""
stack으로 각 노드와 깊이를 쌓고, pop하여 가장 끝 element를 꺼내 그 노드의 자식노드(왼쪽, 오른쪽)를 파악하고 
깊이를 +1하여 max로 최대깊이를 갱신함
자식노드가 없을때까지 계속 pop을 진행
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: #root node가 없을시 edge case
            return 0
        stack = [(root, 1)]
        maxDepth = 0

        while stack:
            node, depth = stack.pop()
            maxDepth = max(depth, maxDepth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return maxDepth


