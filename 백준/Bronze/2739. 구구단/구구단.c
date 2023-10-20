#include <stdio.h>

int main(void) {

	int A = 0;
	int count = 0;

	scanf("%d", &count);

	for (int i = 0; i < 9; i++) { 
		printf("%d * %d = %d\n", count, i + 1, count * (i + 1));
	}
	
	return 0;
}