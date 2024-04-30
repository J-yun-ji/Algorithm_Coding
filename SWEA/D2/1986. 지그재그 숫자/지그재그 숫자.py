T = int(input()) 

for i in range(T) : 
    sum = 0
    num = int(input())
    for j in range(1, num+1) :    
        if j % 2 == 1 :
            sum += j
        else : 
            sum -= j
    print("#" + str(i+1), sum)
    