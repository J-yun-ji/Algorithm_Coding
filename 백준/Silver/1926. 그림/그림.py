import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y) :
    result = 1
    q = deque()
    q.append([x, y])
    while q :
        ex, ey = q.popleft()
        for k in range(4) :
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0 <= nx < n and 0 <= ny < m :
                if map[nx][ny] == 1 and chk[nx][ny] == False :
                    result += 1
                    chk[nx][ny] = True
                    q.append([nx, ny])
    return result

    
drawCnt = 0
maxSize = 0

for i in range(n) :
    for j in range(m) :
        if map[i][j] == 1 and chk[i][j] == False :
            chk[i][j] = True
            drawCnt += 1
            maxSize = max(maxSize, bfs(i, j))

print(drawCnt)
print(maxSize)