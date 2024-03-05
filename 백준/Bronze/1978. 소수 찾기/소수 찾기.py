N = int(input())

num = list(map(int, input().split())) 

sum = 0
for i in range(N) :
    result = 0 
    if num[i] == 1:
        result = 2
    else :
        for j in range(2, num[i]) :
            if num[i] % j == 0 :
                result = 1
                break
    if result == 0 :
        sum += 1
print(sum)
