def solution(s):
    answer = ''
    num = s.split(" ")
    ss = []
    
    for i in range(len(num)) :
        ss.append(int(num[i]))
        
    mn = min(ss)
    mx = max(ss)
    
    ss = str(mn) + " " + str(mx)
        
    return ss