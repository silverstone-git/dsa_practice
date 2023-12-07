# include "../../arrutils.h"

void display_recursively(int* arr, int len) {
	if(len < 1) return;
	printf("%d ", *arr);
	display_recursively(arr + 1, len - 1);
}

void showsubs(int* arr, int len, int* temp, int temp_len, int pos) {
	// base case
	if(pos == len) {
		display_recursively(temp, temp_len);
		printf("\n");
		return;
	}
	
	// not take case
	showsubs(arr, len, temp, temp_len, pos + 1);

	// take case
	temp[temp_len] = arr[pos];
	temp_len ++;

	showsubs(arr, len, temp, temp_len, pos + 1);
}
