while True :
    num = list(map(int, input().split()))
    if num[0] == 0 and num[1] == 0 and num[2] == 0 :
        break
    mx = max(num)
    num.remove(mx)
    if num[0] * num[0] + num[1] * num[1] == mx * mx :
        print("right")
    else :
        print("wrong")