num = int(input())  # N의 진짜 약수의 개수
divisor = list(map(int, input().split()))

divisor.sort()      # 정렬하기
print(divisor[0] * divisor[-1]) # 약수 구하기기