def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    
    for i in lost[:] :
        if i in reserve :
            reserve.remove(i)
            lost.remove(i)
            
            
    for i in range(len(lost)) : 
        if (lost[i] - 1 in reserve) :
            reserve.remove(lost[i] - 1)
        elif (lost[i] + 1 in reserve) :
            reserve.remove(lost[i] + 1)
        else :
            answer -= 1
        print(answer)
    return answer