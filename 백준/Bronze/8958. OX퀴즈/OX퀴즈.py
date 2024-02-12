num = int(input())

for i in range(num) :
    sum = 0
    k = 0
    str = input()
    for j in range(len(str)) :
        if str[j] == "O" :
            k += 1
            sum += k
        elif str[j] == "X" :
            k = 0
    print(sum) 