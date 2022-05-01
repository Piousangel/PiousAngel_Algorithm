#include <stdio.h>



int arr[5];

void maxAndmin(int *arr, int size, int **maxPtr, int **minPtr){
    int *max;
    int *min;

    max = &arr[0];
    min = &arr[1];

    for(int i = 0; i < size; i++){
        if(*max < arr[i]){
            max = &arr[i];
        }
        else if(*min > arr[i]){
            min = &arr[i];
        }
    }

    *maxPtr = max;
    *minPtr = min;
}

int main(){
    int *maxPtr;
    int *minPtr;
    int arr[5];

    for(int i=0; i < 5; i++){
        printf("정수를입력해주세요");
        scanf("%d", &arr[i]);
    }
    
    maxAndmin(arr, sizeof(arr)/sizeof(int), &maxPtr, &minPtr);
    printf("최대값: %d\n 최솟값: %d\n", *maxPtr, *minPtr);

}