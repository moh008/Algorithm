class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list) #adj에 빈 dictionary 선언
        visited, result, start = set(), [], None

        for u, v in adjacentPairs:  #adj dict에 key=u, v=v, key= v, v = u 식으로 저장
            adj[u].append(v)
            adj[v].append(u)
        
        #start 를 지정할 차례, adj에서 value list의 길이가 1인걸 찾음
        for k, v in adj.items():
            if len(v) == 1:
                start = k
                break                   #start는 하나만 알아도 되므로 길이 1짜리 발견시 바로 break

        #adj에서 key를 순차적으로 탐색하며 dfs 진행
        def dfs(key):
            if key in visited: return   #이미 방문했던 node는 dfs진행 불가
                                        #DFS 기본 코딩
            visited.add(key)            #visited에 지금 node를 추가
            result.append(key)          #결과 리스트에 지금 node 추가

            for k in adj[key]:       #어떻게 traverse할지 결정하는 곳 adj에 있는 key들만 traverse
                dfs(k)
        
        dfs(start)
        return result
        
