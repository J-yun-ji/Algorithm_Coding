nan = []

for i in range(9) :
    nan.append(int(input()))

sum = sum(nan)
result = 0

for i in range(9) :
    for j in range(i+1, 9) :
        if (sum - (nan[i] + nan[j])) == 100 :
            nan.remove(nan[i])
            nan.remove(nan[j-1]) 
            result = 3
            break
    if result == 3 :
        for k in range(len(nan)) :
            print(nan[k])
        break