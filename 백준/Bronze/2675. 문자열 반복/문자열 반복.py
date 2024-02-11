N = int(input())

for i in range(N) :
    str = list(input().split())
    for j in str[1] :
        print(int(str[0]) * j, end="")
    print()