N = int(input())

house = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

newHouse = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, k) :

    if x < 0 or x >= N or y < 0 or y >= N :
        return 0

    if house[x][y] == 1 and visited[x][y] == False :
        visited[x][y] = True
        newHouse[x][y] = k
        houseCnt = 1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            houseCnt += dfs(nx, ny, k)
        return houseCnt
    return 0


cnt = 0
houseCnt = []
k = 1

for i in range(N) :
    for j in range(N) :
        if house[i][j] == 1 and not visited[i][j]:
            house_size = dfs(i, j, k)
            if house_size > 0 :
                houseCnt.append(house_size)
                k += 1
                cnt += 1

houseCnt.sort()
print(cnt) 
print('\n'.join(map(str, houseCnt)))
