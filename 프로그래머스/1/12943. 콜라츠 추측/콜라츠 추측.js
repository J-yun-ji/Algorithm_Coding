function solution(num) {
    let answer = 0;
    
    while (true) { 
        if (num !== 1 && answer < 500) {
            num % 2 == 0 ? num /= 2 :  num = num * 3 + 1;
        } else if (answer >= 500) {
            answer = -1;
            break;
        } else { break;}
        answer++;
    }
    return answer;
}