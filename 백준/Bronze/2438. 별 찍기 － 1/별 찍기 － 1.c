#include <stdio.h>
int main(void)
{
	int i, j, star;
	scanf("%d", &star);

	for (i = 0; i < star; i++)
	{
		for (j = 0; j <= i; j++)
		{
			printf("*");
		}
		printf("\n");
	}
	
	return 0;
} 
