from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방문 유무 확인
visited = [[False]*N for _ in range(N)]

# 이동 방향 (오른쪽, 아래)
directions = [(1, 0), (0, 1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        step = graph[x][y]

        # 끝점이 -1인 경우 성공
        if step == -1:
            return True

        for dx, dy in directions:
            nx = x + dx * step
            ny = y + dy * step
            
            # 주어진 범위를 벗어나지 않으며 방문하지 않은 경우만 큐에 추가
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

    return False

if bfs(0, 0):
    print('HaruHaru')
else:
    print('Hing')
