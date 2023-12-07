#include <stdio.h>
#include "power.h"
int main() {
	int base, exp, res;
	printf("Enter base: ");
	scanf("%d", &base);
	printf("Enter exponent: ");
	scanf("%d", &exp);
	res = power(base, exp);
	printf("result is ---> %d\n", res);
}
