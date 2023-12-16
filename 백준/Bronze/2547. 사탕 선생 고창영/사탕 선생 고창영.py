T = int(input())
for _ in range(T):
    Q = input()
    N = int(input())
    list = [int(input()) for i in range(N)]
    print("YES" if sum(list) % N == 0 else "NO")