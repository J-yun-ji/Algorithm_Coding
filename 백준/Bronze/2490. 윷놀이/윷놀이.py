for i in range(3) :
    game = list(map(int, input().split()))
    if game.count(0) == 1 :
        print("A")
    elif game.count(0) == 2 :
        print("B")
    elif game.count(0) == 3 :
        print("C")   
    elif game.count(0) == 4 :
        print("D")
    else :
        print("E")