T = int(input())

for i in range(T) :
    num = list(map(int, input().split()))
    sum = 0
    for j in range(10) :
        if num[j] % 2 == 1 : 
            sum += num[j]
    print("#" + str(i+1), sum)


