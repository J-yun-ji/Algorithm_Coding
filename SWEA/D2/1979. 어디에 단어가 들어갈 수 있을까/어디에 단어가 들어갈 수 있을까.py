T = int(input())

for t in range(T) :

    N, K = map(int, input().split())

    puz = [list(map(int, input().split())) for _ in range(N)]
    new_puz = [[new[i] for new in puz] for i in range(len(puz))]

    def puzzle_find(N, K, puzzle):
        count = 0
        for i in range(N):
            if puzzle[i].count(1) >= K:  # 각 행에 1이 K 이상이라면
                for j in range(N - K + 1):  # 연속된 1인지 확인
                    if puzzle[i][j] == 1:
                        if puzzle[i][j:j + K].count(1) == K:
                            if j == N - K:
                                if puzzle[i][j - 1] == 0:
                                    count += 1
                                    continue
                            elif puzzle[i][j + K] == 0:
                                if j > 0:
                                    if puzzle[i][j - 1] == 0:
                                        count += 1
                                        if K < N - j:
                                            continue
                                        else:
                                            break
                                else:
                                    count += 1
                                    if K < N - j:
                                        continue
                                    else:
                                        break
                            else:
                                if K < N - j:
                                    continue
                                else:
                                    break
        return count


    print("#" + str(t+1), puzzle_find(N, K, puz) + puzzle_find(N, K, new_puz))