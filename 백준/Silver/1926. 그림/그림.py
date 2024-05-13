"""
1. 아이디어 
- 2중 for => 값 1 && 방문x => BFS
- BFS 돌면서 그림 개수 +1, 최대값을 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : n*m = 500 * 500
- E : 4V = 250000
- V+E : 1250000 약 100만 < 2억 => 연산 가능!!

3. 자료구조
- 그래프 전체 구조 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline

from collections import deque


n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y) :
    result = 1
    q = deque()
    q.append([x, y])
    
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if map[nx][ny] == 1 and visited[nx][ny] == False :
                    result += 1
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return result       



drawCnt = 0
maxSize = 0

for i in range(n) :
    for j in range(m) :
        if map[i][j] == 1 and visited[i][j] == False :
            visited[i][j] = True
            drawCnt += 1
            maxSize = max(maxSize, bfs(i, j))

print(drawCnt)
print(maxSize)