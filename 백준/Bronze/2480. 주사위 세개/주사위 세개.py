one, two, three = map(int, input().split()) # 3개의 주사위 던져서 나온 눈

if one == two == three :
    print(10000+(one*1000))
elif one == two or one == three :
    print(1000+(one*100))
elif two == three :
    print(1000+(two*100))
else :
    if one < two :
        if two < three :
            print(three*100)
        else :
            print(two*100)
    elif one < three :
        if two < three :
            print(three*100)
        else :
            print(two*100)
    else :
        print(one*100)