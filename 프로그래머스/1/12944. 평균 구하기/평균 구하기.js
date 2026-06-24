function solution(arr) {
    var answer = 0;

    console.log(arr.length);
    for(let i = 0; i < arr.length; i++) { 
        answer = answer + arr[i];
    } 
    
    return answer / arr.length;
}