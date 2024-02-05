N = int(input())

client = list(map(int, input().split()))

after = set(client)

print(N - len(after))