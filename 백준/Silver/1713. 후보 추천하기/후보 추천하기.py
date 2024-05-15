N = int(input())

reco = int(input()) 
num = list(map(int, input().split())) 
cnt = 0
 
win = []  
winCnt = [0 for _ in range(N)] 
seq = [0 for _ in range(N)] 
k = 1 
i = 0

while True : 
    if i == len(num) : 
        break 
    if cnt < N : 
        if num[i] not in win :
            win.append(num[i])  
            winCnt[win.index(num[i])] += 1  
            seq[win.index(num[i])] = k  
            k += 1
            cnt += 1 
        else :
            winCnt[win.index(num[i])] += 1 
    else : 
        if num[i] in win :
            winCnt[win.index(num[i])] += 1
            seq[win.index(num[i])] = k
            k += 1 
        else : 
            if winCnt.count(min(winCnt)) > 1 :
                mi = 1001 
                for j in range(winCnt.count(min(winCnt))) :
                    if mi > seq[winCnt.index(min(winCnt), j)]:
                        mi = winCnt.index(min(winCnt), j) 
            else :
                mi = winCnt.index(min(winCnt))

            winCnt[mi] = 0
            winCnt.remove(0)
            winCnt.append(0)
            win.remove(win[mi])
            cnt -= 1
            i -= 1
    i += 1

win.sort()
s = ' '.join(map(str, win))
print(s)
