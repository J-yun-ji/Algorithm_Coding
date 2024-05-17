N = int(input())

house = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * N for _ in range(N)]
cnt = []

def dfs(x, y) :

    if x < 0 or x >= N or y < 0 or y >= N:
        return 0

    if house[x][y] == 1 and visited[x][y] == False:
        visited[x][y] = True
        n = 1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            n += dfs(nx, ny)
        return n
    return 0


all = 0
for i in range(N) :
    for j in range(N) :
        if house[i][j] == 1 and visited[i][j] == False : # 방문하지 않았다면.
            house_size = dfs(i, j)
            if house_size > 0 :
                cnt.append(house_size)
            all += 1

print(all)
cnt.sort()
print('\n'.join(map(str, cnt)))

