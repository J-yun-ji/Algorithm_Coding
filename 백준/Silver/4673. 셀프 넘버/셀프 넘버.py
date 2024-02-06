number = []

for i in range(10000) :       # 1-10,000 값 넣기
    number.append(i)

for i in range(len(number)) :
    num = str(i)
    if i < 10 :
        number.remove(int(num[0]) + int(num[0]))
    elif i < 100 :
        seq = i + int(num[0]) + int(num[1])
        if seq in number :
            number.remove(seq)
    elif i < 1000 :
        seq = i + int(num[0]) + int(num[1]) + int(num[2])
        if seq in number :
            number.remove(seq)
    elif i < 10000 :
        seq = i + int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
        if seq in number :
            number.remove(seq)

for i in range(len(number)) :
    print(number[i])