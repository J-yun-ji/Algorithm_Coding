def bridge(N):
    if N > 1:
        return (N * bridge(N-1))
    else:
        return 1

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    print (bridge(M) //  (bridge(M-N) * bridge(N)))