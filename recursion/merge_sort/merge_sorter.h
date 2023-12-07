# include "../../arrutils.h"

int* mergesort(int* arr, int len) {
	// break into pieces, sort while going back
	if(len == 0) {
		// we have reached the single element
		printf("Empty array, nothing to sort");

	} else if(len == 1) {
		return arr;

	} else if(len == 2){
		//display(arr, len);
		if(arr[0] > arr[1]) {
			// swap
			arr[1] = arr[1] + arr[0];
			arr[0] = arr[1] - arr[0];
			arr[1] = arr[1] - arr[0];
			//printf("sorted subarray: ");
			//display(arr, len);
		}
		return arr;

	} else {

		// split in half and recurse inwards
		//printf("received even length array to split further: ");
		//display(arr, len);
		//printf("making two %d length arrays by malloc\n", len / 2);

		int b_len = len / 2;
		if (len % 2 != 0)
			b_len ++;

		int j = 0;
		int* alist = (int*) malloc((len - b_len) * sizeof(int));
		int* blist = (int*) malloc(b_len * sizeof(int));


		for(j = 0; j < len; j ++) {
			if(j < len - b_len)
				alist[j] = arr[j];
			else
				blist[j - (len - b_len)] = arr[j];
		}

		//printf("a list : ");
		//display(alist, len - b_len);
		//printf("b list : ");
		//display(blist, b_len);

		// sort each
		// at this point the code just keeps on winding
		
		alist = mergesort(alist, len - b_len);
		blist = mergesort(blist, b_len);

		// the unwinding phase
		// now merge the sorted, ie, pick up all the sorted pieces
		
		int* combined_list = (int*) malloc(len * sizeof(int));
		int b_covered = 0;
		j = 0;
		while(j < len) {
			// if b's current is still greater than a's current,
			// or, b is already copied over
			// and a isnt already copied over
			// keep copying a into combined
			
			//printf("comparing: %d and %d\n", alist[j - b_covered], blist[b_covered]);
			if(
				(alist[j - b_covered] < blist[b_covered] || b_covered == b_len) &&
				j - b_covered < len - b_len
			) {
			//printf("copying a into combined list: %d\n", alist[j - b_covered]);
			combined_list[j] = alist[j - b_covered];

			} else {
			// start taking from b-list now
			// first check if already merging is complete, then set it
			// to insert a's thereon
			//printf("inserting b's in combined now: %d\n", blist[b_covered]);
			combined_list[j] = blist[b_covered];
			b_covered ++;

			}
			j ++;
		}

		free(alist);
		free(blist);

		//printf("sorted and merged list is -> ");
		//display(combined_list, len);

		return combined_list;
	}
}

