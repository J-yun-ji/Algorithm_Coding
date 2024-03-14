N = int(input())

range = [1, ]
i = 0
j = 6
while range[i] < N :
    range.append(range[i]+j)
    i += 1
    j += 6
print(len(range))