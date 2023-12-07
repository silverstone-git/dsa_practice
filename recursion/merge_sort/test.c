# include "merge_sorter.h"

int main() {

	int len;
	int* arr = enter_array(&len);

	printf("entered length: ");
	printf("%d\n", len);
	printf("entered array: ");
	display(arr, len);

	// sort this array

	int* sorted = mergesort(arr, len);

	printf("sorted array: ");
	display(sorted, len);

	free(sorted);
	free(arr);
}
