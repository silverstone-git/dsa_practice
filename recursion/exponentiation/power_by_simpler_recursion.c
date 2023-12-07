#include <stdio.h>

int power(int base, int exponent) {
	if(exponent == 1) return base;
	return base * power(base, exponent - 1);
}

int main() {
	int base, exponent;
	scanf("%d", &base);
	scanf("%d", &exponent);
	printf("power is: %d\n", power(base, exponent));
}

