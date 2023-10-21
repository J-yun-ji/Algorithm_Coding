N = int(input()) ## N번째 영화 입력.
count = 0

endNum = 666 ## 종말번호.

while True : 
    if '666' in str(endNum) :
        count += 1
    if count == N :
        break
    endNum += 1

print(endNum)