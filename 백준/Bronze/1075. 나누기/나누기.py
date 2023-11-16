N = input()
M = input()

size = len(N) - 1
num = int(N[:-2]) * (100)
while (True) :
    if num % int(M) == 0 :
        break
    num += 1

print(str(num)[-2:])