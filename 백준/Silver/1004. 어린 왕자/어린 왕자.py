T = int(input()) # 테스트케이스 개수

for _ in range(T) :
    x1, y1, x2, y2 = list(map(int, input().split())) # 출발점, 도착점
    n = int(input()) # 행성계의 개수
    count = 0
    for _ in range(n) :
        cx, cy, r = map(int, input().split())
        dist1 = (x1 - cx)**2 + (y1 - cy)**2
        dist2 = (x2 - cx)**2 + (y2 - cy)**2
        crcr = r**2

        if crcr > dist1 and crcr > dist2 :
            pass
        elif crcr > dist1 :
            count += 1
        elif crcr > dist2 :
            count += 1
    print(count)