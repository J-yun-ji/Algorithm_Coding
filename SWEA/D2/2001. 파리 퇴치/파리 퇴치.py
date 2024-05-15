t = int(input())

cnt = 0
maxPari = []
k = 0

for m in range(t) :
    N, M = map(int, input().split())
    pari = [list(map(int, input().split())) for _ in range(N)]
    maxPari = []
    # 파리채로 잡을 수 있는 횟수만큼 반복
    for i in range(N - M + 1):  # 영역: 5x5, 파리채: 3x3이면 9까지
        prSum = 0
        # 파리채의 크기 이상으로 넘어가지 않을 때까지
        for j in range(N - M + 1):  # 영역: 5x5, 파리채: 3x3이면 3까지
            newlist = [row[j:M + j] for row in pari[i:i + M]]
            maxPari.append(sum([element for row in newlist for element in row]))

    print("#" + str(m+1), max(maxPari))