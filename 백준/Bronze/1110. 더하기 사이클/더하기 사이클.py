N = int(input()) 
num = N 
Cycle = 0    # 사이클 수

while True :
    first = num // 10
    last = num % 10
    sum = (first+last) % 10
    num = (last*10) + sum
    Cycle += 1
    if (num == N) :
        break

print(Cycle)