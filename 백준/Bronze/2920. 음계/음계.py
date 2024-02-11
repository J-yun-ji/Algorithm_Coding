N = list(map(int, input().split()))
sum = 0
for i in range(len(N)) : 
    if N[i] == i+1 :
        sum += 1 
    elif N[i] == 8-i :
        sum -= 1 

if sum == 8 :
    print("ascending")
elif  sum == -8 :
    print("descending")
else :
    print("mixed")

