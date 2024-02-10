A = int(input())
B = int(input())
C = int(input())

num = str(A * B * C)
count = [0 for i in range(10)]

for i in range(len(num)) :
    count[int(num[i])] += 1

for i in range(len(count)) :
    print(count[i])