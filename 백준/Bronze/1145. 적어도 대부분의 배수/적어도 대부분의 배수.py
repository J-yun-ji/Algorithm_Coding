num = list(map(int, input().split()))
min = min(num) # 최솟값 구하기

while True :
    count = 0
    for i in num :
        if min % i == 0 :
            count += 1
    if count > 2 : # 3개를 찾으면 break
        break
    min += 1
print(min)