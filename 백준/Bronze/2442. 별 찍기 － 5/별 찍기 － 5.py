N = int(input())
NN = N - 2
count = 1
for i in range(N) :  
    if NN == -1 :
        print("*" * count)
    else :
        print(" " * NN, "*" * count)
    count += 2
    NN -= 1