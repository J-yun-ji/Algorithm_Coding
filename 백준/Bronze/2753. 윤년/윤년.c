#include <stdio.h>

int main(void)
{
	int Year;
	scanf("%d", &Year);

	if (Year % 400 == 0)
	{
		printf("1");
	}
	else if ((Year % 4 == 0) && (Year % 100 != 0))
	{
		printf("1");
	}
    else
    {
        printf("0");
    }

	return 0;
}