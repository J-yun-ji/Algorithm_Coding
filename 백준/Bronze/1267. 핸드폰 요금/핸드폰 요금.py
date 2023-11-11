N = int(input())
time = list(map(int, input().split()))
Y = M = 0
for N in time :
    Y += (N//30 + 1) * 10
    M += (N//60 + 1) * 15

if M == Y :
    print("Y M", M)
elif M < Y :
    print("M", M)
else :
    print("Y", Y)