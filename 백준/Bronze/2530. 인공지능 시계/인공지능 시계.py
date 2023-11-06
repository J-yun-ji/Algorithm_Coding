Hour, Minute, Second = map(int, input().split()) # 시간, 분, 초 입력
CookingTime = int(input())                       # 요리 시간 입력력

Second += CookingTime                            # 초에 요리 시간 더하기
Minute += Second // 60                           # 분에 초를 60으로 나눠서 더하기기
Hour += Minute // 60                             # 시간에 분을 60으로 나눠서 더하기기

print(Hour % 24, Minute % 60, Second % 60)       # 시간, 분, 초 전부 60으로 몫 나누기
