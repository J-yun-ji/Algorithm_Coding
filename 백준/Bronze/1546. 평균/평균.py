N = int(input())

score = list(map(int, input().split()))

max = max(score)
new = []

for i in range(len(score)) :
    num = score[i]/max*100 
    new.append(num)

sum = sum(new)
avg = sum / len(score)

print(avg)