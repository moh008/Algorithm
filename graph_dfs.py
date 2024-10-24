"""
# Graph DFS 예시  그래프와 트리의 다른점: 트리는 방향이 잡혀있어서 방문한 노드를 조사할 필요가 없으나 
# 그래프는 방향성이 없기때문에 방문한 노드를 검사하지 않으면 infinite loop에 걸릴 위험이 있음
# dictionary 'G' 생긴 예시  0:[1, 2, 3] 0번노드의 이웃은 1, 2, 3번임 1:[0, 4, 3] 1번 노드의 이웃은 0, 4, 3번임 
"""

#get connected components
def numConnectedComponents(G):
  n = len(G)              # dictionary 'G'는 키가 노드 개수만큼 있으니 노드의 개수를 의미
  vis = n * [False]       # 초기화땐 전부 방문 값을 False로 놔야하니 vis dic을 노드 개수만큼 False로 지정
  res = 0                 
  for node in range(n):
    if not vis[node]:
      vis[node] = True
      dfs(G, node, vis)
      res += 1
  return res

def dfs(G, node, vis):  
  for nbr in G[node]:   # 노드의 이웃들을 모두 traverse
    if not vis[nbr]:    # 그 이웃 노드중에서 방문한 적이 없는 노드라면
      vis[nbr] = True   # 방문했다는 마크 남기고
      dfs(G, node, vis)

"""
dic = {
  'x1': 'x2', 3.0
  'x2': 'x1', 1.0 / 3.0
}
queue = ([(start, 1.0)])
visited = {start}
queries = [['x9', 'x2'], ['x9', 'x9']]

Queries[0] = ['x9', 'x2']
queue = (['x9', 1.0])
visited = {'x9'}
node, cur_val = 'x9', 1.0
node = 'x9' != 'x2' (end)
dic['x9'] not exists
return -1.0

Queries[1] = ['x9', 'x9']
queue = ([('x9', 1.0)])
visited = {'x9'}
'x9' == 'x9'
if 'x9' not in dic
return -1.0
"""