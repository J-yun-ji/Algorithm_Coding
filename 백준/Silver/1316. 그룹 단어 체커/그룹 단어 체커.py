N = int(input()) 
cnt = 0
count = -1
str = [input() for _ in range(N)]


for i in range(N) : 
    count = 0
    T = []
    for j in range(len(str[i])) :
        if str[i][j] in T :
            if str[i][j] == str[i][j-1] :
                continue
            else :
                count = 0
                break
        else :                                                              
            T.append(str[i][j]) 
            count = 1
    if count == 1 :
        cnt += 1
    

print(cnt)