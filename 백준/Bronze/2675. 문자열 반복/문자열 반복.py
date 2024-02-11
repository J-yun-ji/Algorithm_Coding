N = int(input())

for i in range(N) :
    str = list(input().split())
    for j in range(len(str[1])) :
        print(int(str[0]) * str[1][j], end='')
    print()