number = []

for i in range(10000) :       # 1-10,000 값 넣기
    number.append(i)

for i in range(len(number)) :
  if i < 10 :
    seq = i + i
    number.remove(seq)
  elif i < 100 :
    seq = i + ((i - (i % 10)) / 10) + (i % 10)
    if seq in number :
        number.remove(seq)
  elif i < 1000 :
    seq = i + ((i - (i % 100)) / 100) + (((i % 100) - (i % 10)) / 10) + (i % 10)
    if seq in number :
        number.remove(seq)
  elif i < 10000 :
    seq = i + ((i - (i % 1000)) / 1000) + (((i % 1000) - (i % 100)) / 100) + (((i % 100) - (i % 10)) / 10) + (i % 10)
    if seq in number :
        number.remove(seq)


for i in range(len(number)) : # 셀프 넘버 출력
    print(number[i])