# include "libsubs.h"
int main() {
	int len;
	int* arr = enter_array(&len);
	display_recursively(arr, len);
	printf("\n");

	int* temp = (int*) malloc(len * sizeof(int));
	showsubs(arr, len, temp, 0, 0);

	free(arr);
	return 0;
}
