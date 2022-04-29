#include <stdio.h>
#include <stdlib.h>

int main(){

    int n;
    int number;
    int temp;
    scanf("%d", &n);

    int* arr = (int*)malloc(sizeof(int) * n);

    for(int i=0; i < n; i++){
        scanf("%d", &number);
        arr[i] = number;

    }

    for(int i=0; i < n; i++){

        for(int j=i+1; j < n ; j++){

            if(arr[i] > arr[j]){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }    
    }

    for(int i=0; i < n; i++){
        printf("%d\n", arr[i]);
    }

    free(arr);

    return 0;
}