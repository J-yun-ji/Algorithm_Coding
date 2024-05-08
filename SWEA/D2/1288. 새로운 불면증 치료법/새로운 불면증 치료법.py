N = int(input())

for i in range(N) :
    K = input()
    p = 2
    L = K
    nums = set()

    while True :
        num = []
        for j in range(len(L)) :
            num.append(L[j])
            
        nums.update(map(int, num)) 
        if len(nums) == 10 :
            print("#" + str(i+1), L)
            break 
        L = str(int(K) * p) 
        p += 1 