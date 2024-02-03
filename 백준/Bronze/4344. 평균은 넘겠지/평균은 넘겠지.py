C = int(input())
# 1. 평균값을 구한다.
# 2. 평균값을 넘는 학생의 개수를 구한다.
# 3. 10에서 나누기 전체 학생 수
# 4. 3번에서 곱하기 2번. 

for _ in range(C) : 
    score = list(map(int, input().split()))
    avg = sum(score[1:]) / score[0]
    student = 0
  
    for num in score[1:] :
        if num > avg :
            student += 1
    result = student / score[0] * 100
    print(f'{result: .3f}%') 
