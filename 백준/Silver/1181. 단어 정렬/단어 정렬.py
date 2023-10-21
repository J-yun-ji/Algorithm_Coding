apbnum = int(input())
apb = []

for i in range(apbnum) :
    apb.append(input()) ## 리스트에 문자열 추가.

setapb = set(apb)
apb = list(setapb)

apb.sort() ## 알파벳 순서대로 정렬.
apb.sort(key = len) ## 문자열 길이 순으로 정렬


for i in apb :
    print(i)