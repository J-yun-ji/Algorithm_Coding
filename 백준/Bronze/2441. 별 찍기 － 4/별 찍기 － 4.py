N = int(input())
sum = 0

for i in range(N, 0, -1) :
    for k in range(sum) :
        print(' ', end = "")
    for j in range(i) :
        print('*', end = "")
    sum += 1
    print('')
        
