class Solution:
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    return evalDiv(equations, values, queries)

def evalDiv(equations, values, queries):
  def make_graph():
    nonlocal dic
    for (start, end), val in zip(equations, values):
      dic[start].append((end, val))
      dic[end].append((start, 1.0 / val))
  
  def bfs(start, end):
    queue = collections.deque([(start, 1.0)])
    visited = set([start])

    while queue:
      node, cur_val = queue.popleft()

      if start not in dic or node not in dic:
        return -1.0
      else:
        if node == end:
          return cur_val
        
        for nbr, ratio in dic[node]:
          if nbr not in visited:
            visited.add(nbr)
            queue.append([(nbr, cur_val * ratio)])    
    return -1.0
  

  res = []
  dic = defaultdict(list)
  make_graph()
  for start, end in queries:
    res.append(bfs(start, end))
  return res