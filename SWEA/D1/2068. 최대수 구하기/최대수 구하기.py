T = int(input())

for i in range(T) :
    num = list(map(int, input().split()))
    print("#" + str(i+1), max(num))