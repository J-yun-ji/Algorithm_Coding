S = input()

apb = [-1 for i in range(26)]

for i in range(len(S)) :
    if apb[ord(S[i]) - 97] != -1 :
        continue
    else :
        apb[ord(S[i]) - 97] += i+1

for i in range(len(apb)) :
    print(apb[i], end=" ")