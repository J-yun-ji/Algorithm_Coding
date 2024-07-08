size = int(input())
numList = list(map(int, input().split()))


for i in range(size-1, 0, -1): 
    if numList[i-1] < numList[i]:
        for j in range(size-1, 0, -1): 
            if numList[i-1] < numList[j]: 
                numList[i-1], numList[j] = numList[j], numList[i-1] 
                numList = numList[:i] + sorted(numList[i:])
                print(" ".join(map(str, numList)))
                exit()

print(-1)