tc = int(input())

sch = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(tc) :
    N, K = map(int, input().split())
    all = []
    more = []

    score = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N) :
        all.append((score[i][0] * 0.35) + (score[i][1] * 0.45) + (score[i][2] * 0.2))

    pick = all[K-1]
    all.sort(reverse=True)
    pick = all.index(pick)

    if N > 10 :
        for j in range(10) :
            for _ in range(int(N/10)) :
                more.append(sch[j])
        print("#" + str(t+1), more[pick])
    else :
        print("#" + str(t+1), sch[pick])