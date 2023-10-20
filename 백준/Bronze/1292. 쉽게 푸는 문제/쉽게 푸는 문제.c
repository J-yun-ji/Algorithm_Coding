#include<stdio.h>  

int main(void) {

    int first = 0, last = 0;
    int sum = 0, plus = 1, count = 1;

    scanf("%d %d", &first, &last);

    for (int i = 1; count <= last; i++) {
        for (int j = 1; j <= plus; j++) {
            if (count >= first) {
                sum += plus;
            } 
            count++;
            if (count > last) {
                break;
            }
        }
        plus++;
    }
    
    printf("%d", sum);

    return 0;
}