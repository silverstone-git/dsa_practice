#include <stdio.h>
#include "fact.h"
int main() {
	int inp;
	printf("enter a number please: ");
	scanf("%d", &inp);
	printf("entered inp is: %d", inp);
	int res = fact(inp);
	printf("factorial of %d is: %d\n", inp, res);
}
