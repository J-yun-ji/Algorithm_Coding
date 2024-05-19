from collections import deque

N = int(input())
M = int(input())
com = [list(map(int, input().split())) for _ in range(M)]

def bfs(start) :
    visited = [0] * (N+1)
    queue = deque()
    queue.append(start)
    visited[start] = 1
    cnt = 0

    while queue :
        cur = queue.popleft()
        cnt += 1

        for i in range(M) :
            if com[i][0] == cur and not visited[com[i][1]] :
                queue.append(com[i][1])
                visited[com[i][1]] = 1
            elif com[i][1] == cur and not visited[com[i][0]] :
                queue.append(com[i][0])
                visited[com[i][0]] = 1

    return cnt - 1

print(bfs(1))