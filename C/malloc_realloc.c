#include <stdio.h>
#include <stdlib.h>

int main(){
    int arr_1[10];
    int *arr_2;
    int i;

    for(int i =0; i < 5; i++){
        arr_2[i] = arr_1[i];
        printf("%d", arr_2[i]);
    }

    printf("\n");

    realloc(arr_2, sizeof(int)*10);

    for(int i=0; i < 10; i++){
        arr_2[i] = arr_1[i];
        printf("%d", arr_2[i]);
    }

    free(arr_2);
    return 0;
}