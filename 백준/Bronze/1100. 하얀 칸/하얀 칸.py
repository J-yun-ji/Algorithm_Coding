Chess = []
for _ in range(8) :
    Chess.append(list(map(str, list(input()))))

Whorse = 0
for i in range(8) :
    for j in range(8) :
        if (i + j) % 2 == 0 : # 홀수 즉, 하얀칸일 때
            if Chess[i][j] == 'F' :
                Whorse += 1
print(Whorse)
