N = int(input())

while True :
    num = True
    for i in str(N) :
        if i != "4" and i != "7" :
            num = False
            N -= 1
    if num :
        print(N)
        break