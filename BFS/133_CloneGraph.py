"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if not node:  #그래프가 비었으면 아무것도 없는거 리턴
      return None
    
    visited = {}  #dictionary 세팅
    q = collections.deque([node])   #카피가 아닌 원본 노드들을 넣고 조회할 목적으로 queue 생성
    visited[node] = Node(node.val)  #visited 맵에 처음 카피본 노드(그래서 Node(node.val)하는거 만약에 복사본아니면 그냥 visited[node] = node.val하면 됐음)를 삽입

    while q:                        #그래프의 원본 노드가 남아있을 경우
      current = q.popleft()         #그 원본 노드를 꺼내와서
      for neighbor in current.neighbors:          #현재 노드의 이웃한 노드(이미 문제 자체에 내장돼 있는 node의 attribute)를 루프로 하나씩 조회함
        if neighbor not in visited:               #만약 이웃한 노드가 복제본이 아니라면
          visited[neighbor] = Node(neighbor.val)  #visited dictionary에 지금 방문하고있는 이웃노드를 복사해서 넣어주고
          q.append(neighbor)                      #q에 해당 이웃노드를 추가하여 조회할 예정 q에 추가 안하면 이렇게 한번만에 loop가 끝나버리니까
        visited[current].neighbors.append(visited[neighbor])  
        #현재 오픈한 노드의 이웃정보에 지금 방문하는 중인 이웃 노드의 복사본을 추가해줌. 여기서는 원본의 current를 써도 상관없는듯, 어차피 복사본 리턴할 거니까
    return visited[node]            #복사본 노드를 반환함으로써 전체 그래프 리턴
