T = int(input())

for i in range(1, T+1) :
    a = str(i)
    count = 0
    result = 2
    for j in range(len(a)) :
        if '3' in a[j] :
            result = 0
            count += 1 
        elif '6' in a[j] :
            result = 0
            count += 1 
        elif '9' in a[j] :
            result = 0
            count += 1 
        elif result != 0 :
            result = 1
    if result == 0 : 
        print("-" * count, "", end="")
    else :
        print(a, "", end="")
