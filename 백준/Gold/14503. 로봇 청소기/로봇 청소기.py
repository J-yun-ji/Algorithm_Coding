N, M = map(int, input().split())

r, c, d = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(N)]
count = 0

# 북, 동, 남, 서 (상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True :
    if space[r][c] == 0 :
        count += 1
        space[r][c] = 2
    sw = False

    for i in range(1, 5) :
        nx = r + dx[d-i]
        ny = c + dy[d-i]
        if 0 <= nx < N and 0 <= ny < M :
            if space[nx][ny] == 0 :
                r = nx
                c = ny
                d = (d-i+4) % 4
                sw = True
                break

    if sw == False :
        nx = r - dx[d]
        ny = c - dy[d]
        if 0 <= nx < N and 0 <= ny < M :
            if space[nx][ny] == 1 :
                break
            else :
                r = nx
                c = ny
        else :
            break

print(count)