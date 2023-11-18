while (True) :
    engsen = input()
    if engsen == '#' :
        break
    count = 0
    for engmo in engsen :
        if engmo in 'aeiouAEIOU' :
            count += 1
    print(count)