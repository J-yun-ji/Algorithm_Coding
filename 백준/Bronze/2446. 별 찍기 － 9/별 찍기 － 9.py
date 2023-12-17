N = int(input())

for i in range(N * 2 - 1):
    if i < N:
        print(" " * i + "*" * (2 * (N - i) - 1))
    else:
        print(" " * (2 * N - 2 - i) + "*" * (3 + 2 * (i - N)))
