"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
grid를 놓고, visited 와 queue를 선언. visited는 방문한 그리드에 비었는지 0, 신선한지 1, 썩었는지 2를 판단하며 방문함
q에는 썩은 오렌지의 좌표를 append한걸 갖고있음
q의 size에 따라 썩은사과면 신선한 사과 개수를 하나씩 내리고, 해당 턴의 시간을 +1 늘림. 4방의 위치가 grid의 제한을 넘어가면 minute 카운트가 딱 한번만 더 하게 되어있음. 그래서 minutes을 -1로 설정하고 시작함. (이거 만든사람 천재같음)
"""
class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = grid
    countFreshOranges = 0
    q = collections.deque()
    for i in range(m):
      for j in range(n):
        if visited[i][j] == 2:
          q.append((i, j))
        if visited[i][j] == 1:
          countFreshOranges += 1
    
    if countFreshOranges == 0:
      return 0
    if not q:
      return -1
    
    minutes = -1
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
      size = len(q)
      while size > 0:
        x, y = q.popleft()
        size -= 1
        for dx, dy in dirs:
          i, j = x + dx, y + dy
          if 0 <= i < m and 0 <= j < n and visited[i][j] == 1:
            visited[i][j] = 2
            countFreshOranges -= 1
            q.append((i, j))
      minutes += 1
    
    if countFreshOranges == 0:
      return minutes
    return -1