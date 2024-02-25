T = int(input())

for i in range(T) :
    VPS = input()
    count1 = 0
    count2 = 0
    result = 0

    for i in range(len(VPS)) :
        if VPS[i] == '(' :
            count1 += 1
        elif VPS[i] == ')' :
            count2 += 1

    if len(VPS) % 2 == 1 or VPS[0] == ')' or count1 != count2 :
        print("NO")
    else :
        for i in range(len(VPS)) :
            if VPS[i] == '(' :
                result += 1 
            elif VPS[i] == ')' :
                if result == 0 :
                    print("NO")
                    result = -1
                    break     
                result -= 1 
        if result == 0 :
            print("YES") 