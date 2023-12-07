int power(int base, int exponent) {
	// exponentiate using recursion
	// 5^6 -> 25^3 -> 25 * 25^2 -> 25 * 25^2
	// 2^7 -> 2 * 2^6 -> 4^3 -> 4 * 4^2
	if(exponent == 0) {
		return 1;
	} else if(exponent == 1) {
		return base;
	} else if(exponent == -1) {
		return 1 / base;
	} else if(exponent == 2) {
		return base * base;
	} else if(exponent % 2 == 0) {
		return power(power(base, 2), exponent  / 2);
	} else {
		return base * power(base, exponent - 1);
	}
}
