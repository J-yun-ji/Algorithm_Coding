#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<string.h>

int main(void) {

    int N, M, countR = 0, countC = 0;
    char castle[50][50] = { 0 };

    scanf("%d %d", &N, &M); // 성의 가로 크기 N, 세로 크기 M 입력 받기. 
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) { // 마지막은 널문자가 들어가기에 1을 더함.
            scanf(" %c", &castle[i][j]); // 성의 상태 입력 받기.
        }
    }

    for (int i = 0; i < N; i++) {  // 행의 개수만큼 for문 반복.
        int emptyCount = 0;
        for (int j = 0; j < M; j++) { // 열의 개수만큼 for문 반복.
            if (castle[i][j] != 'X') { // i행에 X가 들어 있다면 
                emptyCount++; // count 값을 증가 시킨다.
            }
        } 
        if (emptyCount == M) {
            countR++; 
        } 
    }   

    for (int i = 0; i < M; i++) {  // 열의 개수만큼 for문 반복.
        int emptyCount = 0;
        for (int j = 0; j < N; j++) { // 열의 개수만큼 for문 반복.
            if (castle[j][i] != 'X') { // i열에 X가 들어 있다면 
                emptyCount++; // count 값을 증가 시킨다.
            }
            else {
                break;
            }
        }
        if (emptyCount == N) {
            countC++; 
        } 
    }

    if (countR < countC) {
        printf("%d", countC);
    }
    else {
        printf("%d", countR);
    }



    return 0;
}
