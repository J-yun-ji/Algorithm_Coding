def solution(n):
    answer = 0
    na = str(n)
    sum = 0
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(na)) :
        answer += int(na[i])

    return answer