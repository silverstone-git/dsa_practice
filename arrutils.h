# include <stdio.h>
# include <stdlib.h>

void display(int* arr, int len) {
        int i = 0;
        for(i = 0; i < len; i ++) {
                printf("%d, ", arr[i]);
        }
        printf("\n");

}


int* enter_array(int* len) {

        printf("Enter length of array -> ");
        scanf("%d", len);
        printf("Enter the array -> ");
        int* arr = (int*) malloc(*len * sizeof(int));
        for(int i = 0; i < *len; i ++) {
                scanf("%d", &arr[i]);
        }
        return arr;

}
