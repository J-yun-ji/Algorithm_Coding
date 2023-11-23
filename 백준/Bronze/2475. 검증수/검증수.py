num = list(map(int, input().split()))
sum = 0

for i in range(5) :
    num[i] = num[i] * num[i]
    sum += num[i]
print(sum % 10)