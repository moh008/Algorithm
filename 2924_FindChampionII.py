"""
그래프 문제처럼 보이나, 한방향으로만 순회하는 DAG(Directed Acyclic Graph)이기 때문에 Graph Traverse 문제가 아님
누가졌는지 list를 선언, 모두 false로 초기화 해놓고, for loop로 edge를 돌면서 누가 졌는지 표시하고
isChampion 값을 -1로, championCount를 0으로 초기화. 진적 없는팀이 나올때마다 isChampion을 해당 team으로 업데이트하며
championCount를 1씩 더함. championCount가 1일때만 isChampion을 리턴하고 나머지는 -1로 리턴
"""
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        isDefeated = [False] * n
        for winner, loser in edges:
            isDefeated[loser] = True
        isChampion, championCount = -1, 0
        for team in range(n):
            if not isDefeated[team]:
                isChampion = team
                championCount += 1
        
        if championCount == 1:
            return isChampion
        else:
            return -1