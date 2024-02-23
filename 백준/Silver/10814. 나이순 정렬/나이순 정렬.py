N = int(input())

user = []

for i in range(N) :
    age, name = input().split()
    user.append([int(age), name]) 

user.sort(key = lambda x : x[0])

for i in range(N) :
    print(user[i][0], user[i][1])